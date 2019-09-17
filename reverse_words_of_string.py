input_string = input("enter your string")
splitted_string = input_string.split(" ")
new_list = []
new_list = splitted_string[::-1]
print(new_list)
sentence = ' '.join(new_list)
print(sentence)
