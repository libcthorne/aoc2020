valid_count = 0

def is_entry_valid(entry):
    for required_field, validator in (
            ('byr', lambda x: int(x) >= 1920 and int(x) <= 2002),
            ('iyr', lambda x: int(x) >= 2010 and int(x) <= 2020),
            ('eyr', lambda x: int(x) >= 2020 and int(x) <= 2030),
            ('hgt', lambda x: (
                x.endswith('cm') and len(x) == 5 and int(x[:3]) in range(150, 194)
            ) or (
                x.endswith('in') and len(x) == 4 and int(x[:2]) in range(59, 77)
            )),
            ('hcl', lambda x: len(x) == 7 and x[0] == '#' and int(x[1:], base=16) >= 0),
            ('ecl', lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}),
            ('pid', lambda x: len(x) == 9 and int(x) >= 0),
    ):
        if required_field not in entry:
            return False
        value = entry[required_field]
        if not validator(value):
            return False
    return True

with open('input.txt') as f:
    entry = {}
    consumed_final_line = False
    while not consumed_final_line:
        line = f.readline()
        if line != '':
            line = line.rstrip()
        else:
            # '' without rstrip -> EOF
            consumed_final_line = True
        if line == '':
            if is_entry_valid(entry):
                valid_count += 1
            entry = {}
            continue
        for field in line.split(' '):
            field_name, field_value = field.split(':')
            entry[field_name] = field_value
print(valid_count)
