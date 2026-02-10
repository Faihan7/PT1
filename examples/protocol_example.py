"""
Example: Creating and using a plant tissue culture protocol.

To run this example:
    cd /path/to/PT1
    export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
    python examples/protocol_example.py
"""

from pt1 import Protocol

# Create a new protocol for arabidopsis tissue culture
protocol = Protocol(
    name="Arabidopsis Callus Induction",
    description="Protocol for inducing callus formation in Arabidopsis thaliana",
    medium="MS medium with 2,4-D and kinetin",
    temperature=22.0,
    light_hours=16.0
)

# Add steps to the protocol
protocol.add_step(
    step_number=1,
    description="Surface sterilize seeds with 70% ethanol for 1 minute",
    duration_days=1
)

protocol.add_step(
    step_number=2,
    description="Treat with 10% bleach solution for 10 minutes",
    duration_days=1
)

protocol.add_step(
    step_number=3,
    description="Rinse with sterile distilled water 3-5 times",
    duration_days=1
)

protocol.add_step(
    step_number=4,
    description="Place explants on callus induction medium",
    duration_days=21
)

protocol.add_step(
    step_number=5,
    description="Transfer to fresh medium and observe callus formation",
    duration_days=14
)

# Display protocol information
print(protocol)
print(f"Total duration: {protocol.get_total_duration()} days")
print(f"\nProtocol details:")
print(f"  Medium: {protocol.medium}")
print(f"  Temperature: {protocol.temperature}°C")
print(f"  Light: {protocol.light_hours} hours/day")
print(f"\nSteps:")
for step in protocol.steps:
    print(f"  {step['step_number']}. {step['description']} ({step['duration_days']} days)")
