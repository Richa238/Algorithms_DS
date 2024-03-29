def palindrome_test(s):
    i, j=0, len(s)-1

    while i<j:
        while not s[i].isalnum() and i<j:
            i+=1
        while not s[j].isalnum() and i < j:
            j-=1
        if s[i].lower() != s[j].lower():
            # print("Not a Palindrome")
            return False
        i, j = i+1, j-1
    # print("Palindrome")
    return True


text = "Able was I, ere I saw Elba!"
print(text, palindrome_test(text))