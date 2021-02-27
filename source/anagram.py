"""
   A function  that check if two strings are anagram 
   It return true or false
"""


def anagram(str1, str2):
    if (sorted(str1.lower()) == sorted(str2.lower())):
        return True
    else:
        return False


"""
print(anagram('army', 'Mary'))
print(anagram('TestOne', 'testTwo'))
"""
