'''
Написати функцію, яка буде отриувати адресу email та перевіряти чи вона валідна
'''
import re

# example_my_mail2@gmail.com
email = "example_my_mail2@gmail.com"
pattern = r'\w+@\w+.\w+'

# print(re.fullmatch(pattern, email).group())

# example_my_mail2@gmail.com
email = "example_my_mail2@gmail.com"
pattern = r'(\w+)@(\w+).(\w+)'

# print(re.fullmatch(pattern, email).groups())

# example_my_mail2@gmail.com
email = "example_my_mail2@gmail.com"
pattern = r'(?P<username>\w+)@(?P<domain>\w+).(?P<top_level_domain>\w+)'

print(re.fullmatch(pattern, email).groupdict())