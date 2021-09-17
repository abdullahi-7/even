import time
def even():
    vari = []
    var = int(input("pick a number"))
    if var // 2 == 0:
        vari.append(var)
        print("yes even")
    else:
        print(f"not even{var}")

even()