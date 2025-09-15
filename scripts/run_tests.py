#!/usr/bin/env python3
"""
Test execution script with pytestomatio integration
"""

import os
import sys
import argparse
from dotenv import load_dotenv

def main():
    """Main function to run tests with different configurations"""
    load_dotenv()

    parser = argparse.ArgumentParser(description='Run tests with pytestomatio integration')
    parser.add_argument('--suite', choices=['api', 'ui', 'all'], default='all', help='Test suite to run')
    parser.add_argument('--marker', help='Pytest marker to filter tests (e.g., smoke, regression)')
    parser.add_argument('--sync', action='store_true', help='Sync tests to Testomatio')
    parser.add_argument('--report', action='store_true', help='Report results to Testomatio')
    parser.add_argument('--remove-ids', action='store_true', help='Remove Testomatio IDs from tests')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    args = parser.parse_args()

    # Base pytest command
    cmd_parts = ['pytest', '-v']

    # Add test path based on suite
    if args.suite == 'api':
        cmd_parts.append('tests/api/')
    elif args.suite == 'ui':
        cmd_parts.append('tests/ui/')
    else:
        cmd_parts.append('tests/')

    # Add marker filter
    if args.marker:
        cmd_parts.extend(['-m', args.marker])

    # Add Testomatio options
    testomatio_options = []
    if args.sync:
        testomatio_options.append('sync')
    if args.report:
        testomatio_options.append('report')
    if args.remove_ids:
        testomatio_options.append('remove')
    if args.debug:
        testomatio_options.append('debug')

    if testomatio_options:
        cmd_parts.extend(['--testomatio', ' '.join(testomatio_options)])

    # Add HTML report
    cmd_parts.extend(['--html=reports/report.html', '--self-contained-html'])

    # Execute command
    cmd = ' '.join(cmd_parts)
    print(f"Executing: {cmd}")
    os.system(cmd)

if __name__ == '__main__':
    main()