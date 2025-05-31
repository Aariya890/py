def pelindromChecker(w):
    n = ''
    for i in w:
        n = i + n 
    if n == w:
        print(w,"is a pelindrom word.")
    else:    
        print(w,"is not a pelindrom word.")

word = str(input("Enter any word:")).lower()

pelindromChecker(word)