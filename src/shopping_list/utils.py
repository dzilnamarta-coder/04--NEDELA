def calc_line_total(item):
    """Atgriež qty × price"""
    return item['qty'] * item['price']

def calc_grand_total(items):
    """Summē visus line totals"""
    return sum(calc_line_total(item) for item in items)

def count_units(items):
    """Saskaita kopējo vienību skaitu"""
    return sum(item['qty'] for item in items)
