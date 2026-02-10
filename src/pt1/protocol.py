"""
Protocol management for plant tissue culture.
"""

from datetime import datetime
from typing import Dict, List, Optional


class Protocol:
    """
    Represents a plant tissue culture protocol.
    
    A protocol defines the steps and conditions for growing plant tissue cultures.
    """
    
    def __init__(
        self,
        name: str,
        description: str,
        medium: str,
        temperature: float,
        light_hours: float
    ):
        """
        Initialize a new protocol.
        
        Args:
            name: Name of the protocol
            description: Detailed description of the protocol
            medium: Growth medium composition (e.g., "MS medium")
            temperature: Incubation temperature in Celsius
            light_hours: Hours of light per day
        """
        self.name = name
        self.description = description
        self.medium = medium
        self.temperature = temperature
        self.light_hours = light_hours
        self.created_at = datetime.now()
        self.steps: List[Dict[str, str]] = []
    
    def add_step(self, step_number: int, description: str, duration_days: int) -> None:
        """
        Add a step to the protocol.
        
        Args:
            step_number: Sequential step number
            description: Description of what to do in this step
            duration_days: Duration of this step in days
        """
        self.steps.append({
            "step_number": step_number,
            "description": description,
            "duration_days": duration_days
        })
    
    def get_total_duration(self) -> int:
        """
        Calculate total duration of the protocol.
        
        Returns:
            Total duration in days
        """
        return sum(step["duration_days"] for step in self.steps)
    
    def __str__(self) -> str:
        """String representation of the protocol."""
        return f"Protocol: {self.name} ({len(self.steps)} steps, {self.get_total_duration()} days)"
    
    def __repr__(self) -> str:
        """Developer representation of the protocol."""
        return f"Protocol(name='{self.name}', steps={len(self.steps)})"
