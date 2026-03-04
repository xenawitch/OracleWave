# test_oraclewave.py
"""
Tests for OracleWave module.
"""

import unittest
from oraclewave import OracleWave

class TestOracleWave(unittest.TestCase):
    """Test cases for OracleWave class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleWave()
        self.assertIsInstance(instance, OracleWave)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleWave()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
