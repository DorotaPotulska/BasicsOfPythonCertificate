# Zadanie3.  
# Ania chce urządzić przyjęcie urodzinowe. 
# Chce podzielić cukierki równo dla gości, a dla siebie zostawić resztę. 
# Powiedz Ani ile zostanie dla niej cukierków. 
# Przykład: Podaj liczbę gości: 10 
# Podaj liczbę cukierków. 32 Dla Justyny zostaną 2 cukierki. 


# calkowite dzielenie
print(10//3)
#zmiennoprzecinkowe dzielenie
print(10/4)
# potęgowanie
print(2**5)
# reszta z dzielenia
print(32%10)

number_of_visitors= int(input('Enter the number of guests\n'))
number_of_sweets=int(input('Enter the number of sweets\n'))
number_of_rest= number_of_sweets%number_of_visitors
print('There are',number_of_rest,'sweets left for Ania.')