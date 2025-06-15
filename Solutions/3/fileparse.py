# fileparse.py

import csv
from typing import Any, List, Dict, Tuple, Type, Union

def parse_csv(lines: Any, select: List[str] = None, types: List[Type] = None, has_headers: bool = True, delimiter: str = ',', silence_errors: bool = False) -> List[Union[Dict[str, Any], Tuple]]:
    '''
    Parse a CSV file into a list of records with type conversion.

    Args:
        lines (Any): The lines of the CSV file to process.
        select (List[str], optional): A list of column names to include. If None, all columns are included.
        types (List[Type], optional): A list of type conversion functions (e.g., [int, float]) applied to each column.
        has_headers (bool): Whether the CSV file includes a header row. Defaults to True.
        delimiter (str): Column delimiter used in the file. Defaults to ','.
        silence_errors (bool): Whether to silence the errors raised during the operation.

    Returns:
        List[Union[Dict[str, Any], Tuple]]: A list of records as dictionaries if headers are present, or as tuples if not.
    '''
    records = []

    # Check the arguments given
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    # Parse the file
    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    for row_num, row in enumerate(rows, 1):
        
        # Skip rows with no data
        if not row:
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {row_num}: Couldn't convert {row}")
                    print(f"Row {row_num}: Reason {e}")
                continue

        # Create the dict ot the tuple
        record = tuple(row) if not has_headers else dict(zip(headers, row))
        records.append(record)

    return records
