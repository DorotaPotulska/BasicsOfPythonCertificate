# Zadanie6.  
# Odczytaj liczbę i wypisz na ekran 10*liczba. 
# Uwzględnij niepoprawne dane. 
# Przykład 
# dla danych 20 
# Wynik: 200 
# Dla danych Aaa 
# Wynik: To nie jest poprawna liczba 

try:
    number= int(input('Give me anumber\n'))
    print(10*number)
except:
    print('This is not a number')    