import time


def string_match(subStr,str):
    #To check that substring is present in the string
    #input-> A string and a substring which we have to search
    #Output -> Print the substring is present or not
    
    
    for i in range(len(str)):
        for j in range(len(subStr)):
            if subStr[j]==str[i]:
                match=True
                