Val1= int(input("Primo valore"))
Val2= int(input("Secondo valore"))
Val3= int(input("Terzo valore"))
if Val1>Val2 and Val1>Val3 and Val3>Val2:
    print(Val1,Val3, Val2)
if Val2>Val1 and Val2>Val3 and Val1>Val3:
    print (Val2, Val1, Val3)
if Val3>Val1 and Val3>Val2 and Val1>Val2:
    print (Val3, Val1, Val2)
if Val1>Val2 and Val1>Val3 and Val2>Val3:
    print (Val1, Val2, Val3)
if Val2>Val3 and Val2>Val1 and Val3>Val1:
    print (Val2, Val3, Val1)
if Val3<Val2 and Val3>Val1 and Val2>Val1:
    print (Val3, Val2, Val1)