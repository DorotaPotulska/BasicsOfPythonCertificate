# Zadanie11.  Napisz program, który odczytuje wyraz i sprawdza czy pierwsza litera to M. 

word = input('Give me a word\n')

#print(word.lower())

if word[0]=='m' or word[0]=='M':
    print('Yes')
else:
    print('No')