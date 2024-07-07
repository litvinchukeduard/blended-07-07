'''
В нас є два файли, в яких записані числа. Потрібно прочитати числа з першого файлу та числа 
з другого файлу. В кінці вивести числа, яке є і в тому і в тому файлі
'''

# 1. Потрібно прочитати інформацію з двох файлів
# 2. Записати числа з файлів у два різні списки
# 3. Порівняти ці два списки та вивести числа які є і там і там


# 1. Потрібно прочитати інформацію з двох файлів
# 2. Записати числа з файлів у два різні списки

file_one_numbers = []
file_two_numbers = []

with open('/Users/eddielitvinchuk/Documents/Repositories/blended-07-07/tasks/2/file_one.txt') as file_one:
    for line in file_one.readlines():
        # print(line.strip().split(' ')) # '   hello   ' -> 'hello' 
                                       # '   hello world     ' -> 'hello world'
        file_one_numbers += line.strip().split(' ') # file_one_numbers = file_one_numbers + line.strip().split(' ')

with open('./tasks/2/file_two.txt') as file_two:
    for line in file_two:
        # print(line.strip().split(' '))
        file_two_numbers += line.strip().split(' ')

# 3. Порівняти ці два списки та вивести числа які є і там і там
print(file_one_numbers, file_two_numbers)
for number in file_one_numbers:
    if number in file_two_numbers:
        print(number)
