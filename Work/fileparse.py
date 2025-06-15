# fileparse.py

import csv
from pathlib import Path
from typing import List, Dict

def parse_csv(filename: Path) -> List[Dict[str, str]]:
    """
    Parse a CSV file into a list of records as dictionaries.

    Args:
        filename (Path): Path to the CSV file to parse.

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing the CSV rows.
    """
    records = []

    # Open the file
    with filename.open("r") as f:

        # Parse the file
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # Read all row
        for row in rows:
            
            # Skip empty rows
            if not row:
                continue
            
            # Create the record and add it to the list
            record = dict(zip(headers, row))
            records.append(record)

    return records
