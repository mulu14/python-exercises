def anagram(str1, str2):
    if (sorted(str1.lower()) == sorted(str2.lower())):
        print(True)
    else:
        print(False); 


anagram('Test1', 'test1'); 