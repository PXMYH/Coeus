# Python program that can be executed to report whether particular
# python packages are available on the system.

import os
import math
import sys

def test_numpy():
    try:
        import numpy as np
    except ImportError:
        print("Could not import numpy -> numpy failed")
        return None
    # Simple test
    a = np.arange(0, 100, 1)
    assert np.sum(a) == sum(a)
    
    print "numpy version:" + str(np.__version__)
    print("-> numpy OK")

def test_pandas():
    try:
        import pandas as pd
    except ImportError:
        print("Could not import pandas -> pandas failed")
        return None
    
    print "pandas version:" + str(pd.__version__)  
    print("-> pandas OK")

def test_scipy():
    try:
        import scipy
    except ImportError:
        print("Could not import 'scipy' -> scipy failed")
        return None
    # Simple test
    import scipy.integrate
    assert abs(scipy.integrate.quad(lambda x: x * x, 0, 6)[0] - 72.0) < 1e-6
    
    print "scipy version:" + str(scipy.__version__)  
    print("-> scipy OK")


def test_pylab():
    """Actually testing matplotlib, as pylab is part of matplotlib."""
    try:
        import pylab
    except ImportError:
            print("Could not import 'matplotlib/pylab' -> failed")
            return None
    # Creata plot for testing purposes
    xvalues = [i * 0.1 for i in range(100)]
    yvalues = [math.sin(x) for x in xvalues]
    pylab.plot(xvalues, yvalues, "-o", label="sin(x)")
    pylab.legend()
    pylab.xlabel('x')
    testfilename='pylab-testfigure.png'

    # check that file does not exist yet:
    if os.path.exists(testfilename):
        print("Skipping plotting to file as file {} exists already."\
            .format(testfilename))
    else:
        # Write plot to file
        pylab.savefig(testfilename)
        # Then check that file exists
        assert os.path.exists(testfilename)
        print("-> pylab OK")
        os.remove(testfilename)

def test_quandl():
    try:
        import Quandl as qd
    except ImportError:
            print("Could not import 'quandl' -> fail")
            return None
    
    print "quandl version:" + str(qd.__version__)
    print("-> quandl OK")

def test_sympy():
    try:
        import sympy
    except ImportError:
            print("Could not import 'sympy' -> fail")
            return None
    # simple test
    x = sympy.Symbol('x')
    my_f = x ** 2
    assert sympy.diff(my_f,x) == 2 * x
    
    print "sympy version:" + str(sympy.__version__)  
    print("-> sympy OK")


def test_pytest():
    try:
        import pytest
    except ImportError:
            print("Could not import 'pytest' -> fail")
            return None
            
    print "pytest version:" + str(pytest.__version__)  
    print("-> pytest OK")
    
def test_SEC():
    try:
        import SECEdgar
    except ImportError:
        print("Could not import 'SECEdgar' -> fail")
        return None
    
    print "SECEdgar version:" + str(SECEdgar.__version__)  
    print("-> SECEdgar OK")


# TODO: add commnad to install in case env sanity check failed
if __name__ == "__main__":
    print("Running using Python {}".format(sys.version))

    print("Testing numpy...     "),
    test_numpy()
    
    print("Testing pandas...    "),
    test_pandas()

    print("Testing scipy...     "),
    test_scipy()

    print("Testing matplotlib..."),
    test_pylab()
    
    print("Testing quandl...    "),
    test_quandl()

    print("Testing sympy...     "),
    test_sympy()

    print("Testing pytest...    "),
    test_pytest()
