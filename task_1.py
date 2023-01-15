#Напишите программу, удаляющую из текста все слова, содержащие "абв".

text=input()
print('исходный текст:', text)
find_sample='абв'
text_correction = [i for i in text.split() if find_sample not in i ]
print('исправленный текст:', ' '.join(text_correction))