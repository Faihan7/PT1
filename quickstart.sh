#!/bin/bash
# Quick Start Script for PT1
# This script sets up the environment and runs examples

echo "Setting up PT1 environment..."

# Add src to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

echo "Running tests..."
python -m unittest discover tests -v

echo ""
echo "Running protocol example..."
python examples/protocol_example.py

echo ""
echo "Running culture example..."
python examples/culture_example.py

echo ""
echo "Setup complete! You can now use PT1."
echo "To run examples, make sure to set PYTHONPATH:"
echo '  export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"'
