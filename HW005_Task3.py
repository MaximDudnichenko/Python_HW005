# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.git

text = input('Введите текст: ')
archive = []
count = 0
for i in range(len(text)):
    count += 1
    if i == (len(text) - 1) or text[i] != text[i + 1]:
        archive.append((count, text[i]))
        count = 0
print(archive)

restore_text = ''
for item in archive:
    restore_text = restore_text + item[0] * item[1]
print(restore_text)
