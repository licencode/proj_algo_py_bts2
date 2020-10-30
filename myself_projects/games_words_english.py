qestion = ("Who like milk?")
words = ["dog", "kate", "elefant"]

print(qestion)

#  Pour aficher chaîn de caractère de liste sans crochets besion faire comme ça print(', '.join(words))
print(', '.join(words))

answer = input("Your answer: ")

if answer == words[1]:
    print("Your answer is correct")
else:
    print("Your answer is not correct")


