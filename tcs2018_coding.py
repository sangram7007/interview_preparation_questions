words = input('enter the words')


words_split = words.split()
word1 = words_split[0]
word2 = words_split[1]
word3 = words_split[2]
changed1 = ''.join((char, "$")[char.lower() in 'aeiou'] for char in word1)
changed2 = ''.join((char, "&")[char.lower() not in 'aeiou'] for char in word2)
changed3 = ''.join((char, char.upper())[char  in char.lower()] for char in word3)
print(f"{changed1} {changed2} {changed3}")



------------------------------------------------------------------------or--------------------------------------------------------------

words = input('enter the words')


words_split = words.split()
word1 = words_split[0]
word2 = words_split[1]
word3 = words_split[2]

for char in word1:
    if char in 'aeiou':
        word1 = word1.replace(char, '$')

print(word1)

for char in word2:
    if char not in 'aeiou':
        word2 = word2.replace(char, '#')

print(word2)


for char in word3:
    if char in char.lower():
        word3 = word3.replace(char, char.upper())

print(word3)



print(f"{word1} {word2} {word3} ")