
my_string = 'Hello'
my_num = 3

print(my_string[4:2:-1])

print(my_string[2])

print(my_string[::-1])

words = ["hello", "world"]

print(words[0])
print(["hello", "world"][0])
print("hello")


print("--------------------")

for word in words:
    print(word)
    print(word.capitalize())
    print(word[::-1])
    print()

my_words = ["the", "frankenstein", "monster"]

print(my_words)
my_words[1] = "frankenstein's"
print(my_words)

my_words.append("sighed")
print(my_words)

print(my_string)
# my_string[0] = 'h'
print(my_string)
my_string = my_string + " Hello again"
print(my_string)
my_string = "Hello %s" % "Sam"
print(my_string)




# End code
# raise SystemExit(0)





program_output = '''
Enter however many words you want:
word
hi
there

Word
Hi
There
'''




advice = '''
Steps:
- print out the prompt
    - print statement or input statement
- Collecting input
    - input
    - while
    - 
- Print it all back to them


'''

print("Enter however many words you want:")
user_entered_word = "PLACEHOLDER"
user_entered_words = []

while user_entered_word != "":
    user_entered_word = input()
    if user_entered_word != "":
        user_entered_words.append(user_entered_word)


for word in user_entered_words:
    print(word.capitalize())










