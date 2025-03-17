import os

messages = []

name = input("Name: ")

while True:
    os.system("cls") #clear terminal

    if len(messages) > 0:
        for m in messages:
            print(m['name'], "-", m['messages'])

    print("____________")

    text = input("Massage: ")
    if text == "stop" or text == "exit" or text =="quit" or text == "end":
        break

    messages.append({
        "name": name,
        "messages": text
    })