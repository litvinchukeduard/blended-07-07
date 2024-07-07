import sys
import re

def read_command_line_arguments() -> tuple[str, str]:
    file_path = None
    level = None

    if len(sys.argv) > 2:
        level = sys.argv[2]

    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    return (file_path, level)

arguments = read_command_line_arguments()
if arguments[0] is None:
    print('Please provide path to the file')
    sys.exit()

print('Here!')

def parse_log_line(line: str) -> dict:
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>[A-Z]+)'
    return re.match(pattern, line).groupdict()
