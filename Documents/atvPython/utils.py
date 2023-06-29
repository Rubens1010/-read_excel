import re

def row_id_validator(document):
    invalid_cells = []
    for index, row in document.iterrows():
        try:
            int(row['Row ID'])
        except ValueError:
            invalid_cells.append({
                'row': index + 1,
                'column': 'A',
                'value': row['Row ID']
            })
    return invalid_cells

def email_validator(document):
    invalid_cells = []
    for index, row in document.iterrows():
        if not re.match(r"[^@]+@[^@]+\.[^@]+", row['email']):
            invalid_cells.append({
                'row': index + 1,
                'column': 'G',
                'value': row['email']
            })
    return invalid_cells

def sales_validator(document):
    invalid_cells = []
    for index, row in document.iterrows():
        try:
            float(row['Sales'])
        except ValueError:
            invalid_cells.append({
                'row': index + 1,
                'column': 'H',
                'value': row['Sales']
            })
    return invalid_cells
