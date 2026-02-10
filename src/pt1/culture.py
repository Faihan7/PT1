"""
Culture management for plant tissue culture experiments.
"""

from datetime import datetime, timedelta
from typing import Optional


class Culture:
    """
    Represents an individual plant tissue culture experiment.
    
    Tracks the status and observations of a culture over time.
    """
    
    def __init__(
        self,
        culture_id: str,
        plant_species: str,
        protocol_name: str,
        start_date: Optional[datetime] = None
    ):
        """
        Initialize a new culture.
        
        Args:
            culture_id: Unique identifier for the culture
            plant_species: Scientific or common name of the plant
            protocol_name: Name of the protocol being followed
            start_date: Start date of the culture (defaults to now)
        """
        self.culture_id = culture_id
        self.plant_species = plant_species
        self.protocol_name = protocol_name
        self.start_date = start_date or datetime.now()
        self.status = "active"
        self.observations = []
    
    def add_observation(self, observation: str) -> None:
        """
        Add an observation about the culture.
        
        Args:
            observation: Description of what was observed
        """
        self.observations.append({
            "date": datetime.now(),
            "observation": observation
        })
    
    def get_age_days(self) -> int:
        """
        Calculate the age of the culture in days.
        
        Returns:
            Age in days since start_date
        """
        return (datetime.now() - self.start_date).days
    
    def mark_complete(self) -> None:
        """Mark the culture as complete."""
        self.status = "complete"
    
    def mark_contaminated(self) -> None:
        """Mark the culture as contaminated."""
        self.status = "contaminated"
    
    def __str__(self) -> str:
        """String representation of the culture."""
        age = self.get_age_days()
        day_word = "day" if age == 1 else "days"
        return f"Culture {self.culture_id}: {self.plant_species} ({self.status}, {age} {day_word})"
    
    def __repr__(self) -> str:
        """Developer representation of the culture."""
        return f"Culture(id='{self.culture_id}', species='{self.plant_species}', status='{self.status}')"
