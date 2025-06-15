# tableformat.py

from typing import List

class TableFormatter:
    def headings(self, headers: List[str]) -> None:
        '''
        Emit the table headings.

        Args: 
            headers (List[str]): A list of all the table headers.
        '''
        raise NotImplementedError()

    def row(self, rowdata: List[str])  -> None:
        '''
        Emit a single row of table data.

        Args:
            rowdata (List[str]): The data of a single table row.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers: List[str]) -> None:
        print(' '.join([f'{header:>10s}' for header in headers]))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata: List[str])  -> None:
        print(' '.join([f'{data:>10s}' for data in rowdata]))

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects: List[object], columns: List[str], formatter: TableFormatter) -> None:
    """
    Print a formatted table from a list of objects using the specified formatter.

    Args:
        objects (List[object]): A list of objects to be displayed in the table.
        columns (List[str]): A list of attribute names to extract from each object.
        formatter (TableFormatter): An instance of a TableFormatter subclass to control output format.
    """
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)

