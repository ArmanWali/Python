
def is_palindrome(s):        
    s2 = s[::-1]     # for reversing the string s
    if s == s2:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


string = input("Please enter a word or sentence : ")
strings = string.replace(" ", "")
is_palindrome(strings)