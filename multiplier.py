def multiplier(string, val):
    new_string = ''
    for char in range(len(string)):
        multiplied_char = string[char] * val
        new_string += multiplied_char
    print(new_string)

text = input("Word: ")
val = int(input("Number: "))
multiplier(text, val)

