# test_testutility.py
"""
Tests for TestUtility module.
"""

import unittest
from testutility import TestUtility

class TestTestUtility(unittest.TestCase):
    """Test cases for TestUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TestUtility()
        self.assertIsInstance(instance, TestUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TestUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
