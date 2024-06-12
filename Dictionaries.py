customer = {
    "name": "Arman Wali",
    "age": 18,
    "is_verified": True
}

customer["name"] = "Sinan khan"
print(customer.get("name"))

# Exercise Question (Taking value in digits and return in english alphabets)

digits = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

Phone = input("\nPlease enter your Phone number : ")
string_digits = ''
for ch in Phone:
    string_digits += digits.get(ch) + " "

print(string_digits)
