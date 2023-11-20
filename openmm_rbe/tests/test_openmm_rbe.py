"""
Unit and regression test for the openmm_rbe package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import openmm_rbe


def test_openmm_rbe_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "openmm_rbe" in sys.modules
