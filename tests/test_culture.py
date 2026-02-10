"""
Unit tests for the Culture class.
"""

import unittest
from datetime import datetime, timedelta
from src.pt1.culture import Culture


class TestCulture(unittest.TestCase):
    """Test cases for Culture class."""
    
    def setUp(self):
        """Set up test culture."""
        self.culture = Culture(
            culture_id="TEST-001",
            plant_species="Test plant",
            protocol_name="Test Protocol"
        )
    
    def test_culture_creation(self):
        """Test that a culture can be created with correct attributes."""
        self.assertEqual(self.culture.culture_id, "TEST-001")
        self.assertEqual(self.culture.plant_species, "Test plant")
        self.assertEqual(self.culture.protocol_name, "Test Protocol")
        self.assertEqual(self.culture.status, "active")
        self.assertEqual(len(self.culture.observations), 0)
    
    def test_add_observation(self):
        """Test adding observations to a culture."""
        self.culture.add_observation("First observation")
        self.culture.add_observation("Second observation")
        
        self.assertEqual(len(self.culture.observations), 2)
        self.assertEqual(self.culture.observations[0]["observation"], "First observation")
    
    def test_get_age_days(self):
        """Test calculating culture age."""
        # Culture just created should be 0 days old
        age = self.culture.get_age_days()
        self.assertGreaterEqual(age, 0)
        self.assertLessEqual(age, 1)
    
    def test_mark_complete(self):
        """Test marking a culture as complete."""
        self.culture.mark_complete()
        self.assertEqual(self.culture.status, "complete")
    
    def test_mark_contaminated(self):
        """Test marking a culture as contaminated."""
        self.culture.mark_contaminated()
        self.assertEqual(self.culture.status, "contaminated")
    
    def test_str_representation(self):
        """Test string representation."""
        result = str(self.culture)
        self.assertIn("TEST-001", result)
        self.assertIn("Test plant", result)
        self.assertIn("active", result)


if __name__ == "__main__":
    unittest.main()
