def are_anagrams(str1, str2):
    s1 = (str1.replace(" ","")).lower()   # it will remove spaces and lowercase the string
    s2 = (str2.replace(" ","")).lower()
    if sorted(s1) == sorted(s2):          
        print("They are anagrams of each other")
    else: 
        print("They are not anagrams of each other")


string1 = input("Please enter the first string : ")
string2 = input("Please enter the second string : ")

are_anagrams(string1, string2)
