customer = {
    "name": "bharath",
    "age": 22,
    "is_verified": True
}

print(customer['name'])


print(customer.get("dj", "jan 22 2001"))

customer['birthdate'] = 'oct 22 2001'


print(customer['birthdate'])



phone = input("Phone: ")
output = ""
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)


print("emojis replacing")
message = input(">")
words = message.split(' ')

emojis = {
    ":)": "😊",
    ":(": "😒"
}

output = ""

for word in words:
    output += emojis.get(word, word) + ' '

print(output)