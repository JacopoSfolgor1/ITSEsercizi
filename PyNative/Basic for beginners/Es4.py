'''Exercise 4: Remove first n characters from a string

Write a Python code to remove characters from a string from 0 to n and return a new string.

For Example:

    remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
    remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
Note: n must be less than the length of the string
'''

def remove_chars(a:str = "", b:int=0)-> list[str,int]:
    c = str(b)
    i2:list = []
    
    if b < len(a):
        for i in range(b+1, len(a)+1):
            str(i)
            i2.append(i)
    else:
        print("numero più grande della parola")
    
    for i in i2:
        print(a[i-1], end = "")

remove_chars("ciao",2)



