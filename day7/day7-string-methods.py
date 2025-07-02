name = input("Enter your nickname: ")
#phone_number = input("Enter your phone number: ")

#result = name.find(" ")
#result = name.rfind("a")
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#result = phone_number.replace("-", "/")


if len(name) >= 12:
    print("Please input nickname below 12 characters only")
elif not name.find(" ") == -1:
    print("Nickname should not have spaces")
elif not name.isalpha():
    print("Nickname should not have numbers")

print(name)
