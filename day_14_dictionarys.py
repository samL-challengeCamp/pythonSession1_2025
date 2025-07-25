
last_names = {
    "camper1_redacted": "[REDACTED]",
    "camper2_redacted": '[REDACTED]',
    "camper3_redacted": '[REDACTED]'
}

my_list = [1, 3, 4]

print(my_list[2])

print(last_names['jeffrey'])

users = {
    ';lasdkj;dsakjfa': '[REDACTED]',
    'asdf': 'Keith'
}

print('Enter id')
guess = input()
# print("You are " + users[guess])

letters = {
    'a': 'm',
    'b': 'n',
    'c': 'o',
    'd': 'p'
}


message = input('Enter message: ')

encrypted_message = ''
for letter in message:
    encrypted_message += letters[letter]

print(encrypted_message)







