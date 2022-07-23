# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

input_text = 'абв абвгдейка, абвгдейка - это и учёба, и игра.'

print(input_text)


def delete_words(text):
    words = text.split()
    fragment = 'абв'
    new_words = []
    for word in words:
        if fragment not in word:
            new_words.append(word)
    new_words = ' '.join(new_words)
    return new_words


result_text = delete_words(input_text)
print(result_text)
