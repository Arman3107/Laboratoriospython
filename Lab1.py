num = int(input("Ingrese el ultimo digito de su carnet: "))

for i in range (num):
    if num % 2 == 0:
        print (''*(num -i -1)+"*" *(2 * i + 1))
    
    else:
        print (''*(2 - i - 1)+"*"*(num -i+1))

