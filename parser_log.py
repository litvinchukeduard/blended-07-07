import re

final_values = {"INFO": 4, "DEBUG": 3, "ERROR": 2, "WARNING": 1}

def print_levels_table(final_values: dict[str, int]) -> None:
    base_format = '{:<17}|{:>10}'
    header = base_format.format('Рівень логування', 'Кількість')
    divider = '-----------------|----------'

    print(f'\n{header}')
    print(divider)

    for level, quantity in final_values.items():
        print(base_format.format(level, quantity))

    print()

print_levels_table(final_values)

# General
log = '2024-01-22 08:45:23 DEBUG Attempting to connect to the database.'

pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>[A-Z]+)'
print(re.match(pattern, log).groupdict())

# By Level
log = '2024-01-22 08:45:23 ERROR Attempting to connect to the database.'

level = 'error'
pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})' + rf' (?P<level>{level})'
pattern_match = re.match(pattern, log, flags=re.IGNORECASE)
if pattern_match is not None:
    print(pattern_match.groupdict())
else:
    print('Not equal')


# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# python3 parser_log.py /Users/eddielitvinchuk/Documents/Repositories/code
# python3 parser_log.py /Users/eddielitvinchuk/Documents/Repositories/blended-07-07/my_log.log
# python3 parser_log.py /Users/eddielitvinchuk/Documents/Repositories/blended-07-07/my_log.log error
import sys

print(sys.argv)
if len(sys.argv) > 2:
    level = sys.argv[2]
    print(level)

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        # print(file.read())
        for line in file:
            print(line)


# Filter by level
level = 'error'
pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})' + rf' (?P<level>{level})'
logs_list = ['2024-01-22 08:30:01 INFO User logged in successfully.', '2024-01-22 08:45:23 DEBUG Attempting to connect to the database.', '2024-01-22 09:00:45 ERROR Database connection failed.']
for log in logs_list:  
    pattern_match = re.match(pattern, log, flags=re.IGNORECASE)
    if pattern_match is not None:
        print(log)