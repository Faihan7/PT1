"""
Example: Managing a plant tissue culture experiment.

To run this example:
    cd /path/to/PT1
    export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
    python examples/culture_example.py
"""

from datetime import datetime, timedelta
from pt1 import Culture

# Create a new culture
culture = Culture(
    culture_id="AT-001",
    plant_species="Arabidopsis thaliana",
    protocol_name="Arabidopsis Callus Induction"
)

print(f"Started: {culture}")

# Add observations over time
culture.add_observation("Initial plating completed. Explants appear healthy.")

# Simulate time passing
print(f"\nAge: {culture.get_age_days()} days")

culture.add_observation("Day 7: No contamination observed. Explants show slight swelling.")
culture.add_observation("Day 14: Clear callus formation visible on several explants.")
culture.add_observation("Day 21: Robust callus growth. Ready for subculture.")

# Display all observations
print(f"\nObservations for {culture.culture_id}:")
for i, obs in enumerate(culture.observations, 1):
    print(f"{i}. {obs['observation']}")

# Mark as complete
culture.mark_complete()
print(f"\nFinal status: {culture}")
