"""
Unit tests for the Protocol class.
"""

import unittest
from src.pt1.protocol import Protocol


class TestProtocol(unittest.TestCase):
    """Test cases for Protocol class."""
    
    def setUp(self):
        """Set up test protocol."""
        self.protocol = Protocol(
            name="Test Protocol",
            description="A test protocol",
            medium="MS medium",
            temperature=25.0,
            light_hours=16.0
        )
    
    def test_protocol_creation(self):
        """Test that a protocol can be created with correct attributes."""
        self.assertEqual(self.protocol.name, "Test Protocol")
        self.assertEqual(self.protocol.description, "A test protocol")
        self.assertEqual(self.protocol.medium, "MS medium")
        self.assertEqual(self.protocol.temperature, 25.0)
        self.assertEqual(self.protocol.light_hours, 16.0)
        self.assertEqual(len(self.protocol.steps), 0)
    
    def test_add_step(self):
        """Test adding steps to a protocol."""
        self.protocol.add_step(1, "Step 1 description", 7)
        self.protocol.add_step(2, "Step 2 description", 14)
        
        self.assertEqual(len(self.protocol.steps), 2)
        self.assertEqual(self.protocol.steps[0]["step_number"], 1)
        self.assertEqual(self.protocol.steps[1]["duration_days"], 14)
    
    def test_get_total_duration(self):
        """Test calculating total duration."""
        self.protocol.add_step(1, "Step 1", 7)
        self.protocol.add_step(2, "Step 2", 14)
        self.protocol.add_step(3, "Step 3", 10)
        
        self.assertEqual(self.protocol.get_total_duration(), 31)
    
    def test_empty_protocol_duration(self):
        """Test that an empty protocol has zero duration."""
        self.assertEqual(self.protocol.get_total_duration(), 0)
    
    def test_str_representation(self):
        """Test string representation."""
        self.protocol.add_step(1, "Step 1", 7)
        result = str(self.protocol)
        self.assertIn("Test Protocol", result)
        self.assertIn("1 step", result)  # Singular form
        self.assertIn("7 days", result)
    
    def test_str_representation_plural(self):
        """Test string representation with plural forms."""
        self.protocol.add_step(1, "Step 1", 5)
        self.protocol.add_step(2, "Step 2", 10)
        result = str(self.protocol)
        self.assertIn("Test Protocol", result)
        self.assertIn("2 steps", result)  # Plural form
        self.assertIn("15 days", result)
    
    def test_str_representation_singular_day(self):
        """Test string representation with singular day."""
        self.protocol.add_step(1, "Step 1", 1)
        result = str(self.protocol)
        self.assertIn("1 step", result)
        self.assertIn("1 day", result)  # Singular day


if __name__ == "__main__":
    unittest.main()
