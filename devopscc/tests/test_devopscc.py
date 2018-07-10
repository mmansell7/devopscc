"""
Unit and regression test for the devopscc package.
"""

# Import package, test suite, and other packages as needed
import devopscc
import pytest
import sys

def test_devopscc_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "devopscc" in sys.modules
