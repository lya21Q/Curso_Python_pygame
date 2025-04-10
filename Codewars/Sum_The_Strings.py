a=input("Ingresa el valor de a:")
b=input("Ingresa el valor de b:")
def sum_str(a, b):
    if a == "":
        a=0
    else:
        a=int(a)
    if b == "":
        b=0
    else:
        b=int(b)

    return a + b
print(sum_str(a,b))