
def greet_user():
    print("hi There!")
    print("welcome")

print('start')
greet_user() 
print("finish")


def greet_user(name):
    print(f"hi {name}")
    print("welcome")

print('start')
greet_user("bharath")  
greet_user("baba")
print("finish")


def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome")

print('start')
greet_user("bharath", last_name="S J")  
print("finish")


def square(number):
    return number * number

print(square(5))



def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output  

message = input('>')
print(emoji_converter(message)) 