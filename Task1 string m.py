def task ( s,  pos,  c): #function for replacing a letter by its possition
    s = s[:pos] + c + s[pos+1:] #concatnation between s[0:pos] and char c and s[pos+1:end]
    return s
print(task("abracadabra",2,"d")) #print the result after returning the function 

    