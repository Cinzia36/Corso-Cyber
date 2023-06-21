val1= int(input("Primo valore"))
val2= int(input("Secondo valore"))
print ("Scegli il tipo di operazione da svolgere: 1 add, 2 sottr, 3 molt, 4 div")
cal= int(input("Operazione"))
if cal==1:
    print ("La somma è:", (val1+val2))
elif cal==2:
    print ("La differenza è:", (val1-val2))
elif cal==3:
    print ("Il prodotto è:", (val1*val2))
elif cal==4:
    print ("Il quoziente è:", (val1/val2))