#!/bin/bash

# Testomatio synchronization script

set -e

echo "=== Testomatio Test Sync Script ==="

# Check if TESTOMATIO token is set
if [ -z "$TESTOMATIO" ]; then
    echo "Error: TESTOMATIO environment variable is not set"
    echo "Please set your Testomatio token in .env file or environment"
    exit 1
fi

echo "Testomatio token found"

# Sync tests to Testomatio
echo "Syncing tests to Testomatio..."
pytest --testomatio sync

echo "✅ Tests synchronized successfully with Testomatio"

# Optional: Show current test status
echo "Current test structure:"
pytest --collect-only --quiet