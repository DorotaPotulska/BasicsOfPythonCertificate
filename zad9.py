# Zadanie9.  
# Odczytaj wiek danej osoby i sprawdź czy osoba jest nastolatkiem. 
# Zakładamy, że osoba jest nastolatkiem jeśli ma od 13 do 17 lat. 

age=int(input('Enter age\n'))
if age>12 and age<18:
    print('You are a teenager')
else:
    print('You are not a teenager')