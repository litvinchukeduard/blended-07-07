'''
Написати функцію, яка буде приймати текст і приймати список спам-слів. 
Яка буде ці спам-слова прибирати з тексту, замінюючи на *
'''
import re

text = """
PyThoNe is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[33]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[34][35]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[37]

Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.
"""

def censor_spam_words(text: str, spam_words: list[str]) -> str:
    for word in spam_words:
        pattern = fr'{word}'
        censor_string = len(word) * '*'
        text = re.sub(pattern, censor_string, text, flags=re.IGNORECASE)
    return text

print(censor_spam_words(text, ['Python', 'Guido', 'and']))
print('___' * 3)