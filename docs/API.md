# PT1 - Plant Tissue Culture Package

## Overview

This package provides tools for managing plant tissue culture protocols and experiments.

## Modules

### protocol.py

The `Protocol` class manages tissue culture protocols, including:
- Protocol metadata (name, description, growth conditions)
- Step-by-step procedures
- Duration calculations

### culture.py

The `Culture` class tracks individual culture experiments, including:
- Culture identification and metadata
- Observation logging
- Status tracking (active, complete, contaminated)
- Age calculations

## Usage

See the `examples/` directory for usage examples:
- `protocol_example.py`: Creating and managing protocols
- `culture_example.py`: Tracking culture experiments

## Testing

Run tests using:
```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python tests/test_protocol.py
python tests/test_culture.py
```
