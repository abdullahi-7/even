import time
def even():
    vari = []
    number = int(input("pick a number"))
    if number % 5 == 0:
        vari.append(number)
    else:
        print(f"not even{var}")

    
    vari = []
    var = int(input("pick a number"))
    if var % 1 == 0:
        vari.append(var)
    else:
        print(f"not even{var}")
     
     
    vari = []
    var = int(input("pick a number"))
    if var % 3 == 0:
        vari.append(var)
    else:
        print(f"not even{var}")
        
    vari = []
    var = int(input("pick a number"))
    if var % 4 == 0:
        vari.append(var)
    else:
        print(f"not even{var}")
        
    vari = []
    var = int(input("pick a number"))
    if var % 2 == 0:
        vari.append(var)
    else:
        print(f"not even{var}")
    return vari
print(even())