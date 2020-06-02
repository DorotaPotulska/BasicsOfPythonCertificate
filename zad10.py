# Zadanie10.  Odczytaj liczbę i sprawdź czy dana liczba jest podzielna przez 8. 

number=int(input('Give me a number\n'))
divisor=8

if number%divisor==0:
    print('Number divisible by',divisor)
else:
    print('Number not divisible by',divisor)