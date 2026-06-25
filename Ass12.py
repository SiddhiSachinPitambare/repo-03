def palindrome(x):
    if str(x) == str(x)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome(123)
palindrome("madam")