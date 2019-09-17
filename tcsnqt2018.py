# write a program to input the three words and showing the first word's consonant replaced with '#'
# second word's all vowel replaced with '@' and the third word's all letter should be in capital
# ex: input = 'how are you' output= 'h#w @r@ YOU'.

text = input("enter your desired string")
splitted_string = text.split(' ')
first_word = splitted_string[0]
second_word = splitted_string[1]
third_word = splitted_string[2]
counter = 0
i = 0
# while len(first_word) >= counter :
#     print(first_word[i])
#     i+=1
#     counter+=1

# for i in range(len(first_word)):
ch = ' '.join(char.replace(char, '$') for char in first_word if char not in ('aeiouAEIOU'))
print(ch)
