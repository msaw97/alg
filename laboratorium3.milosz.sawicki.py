#POLITECHNIKA GDANSKA WFTIMS
#MATEMATYKA SEMESTR IV
#ALGORYTMY I STRUKTURY DANYCH
#LABORATORIUM 2: STOS I NOTACJA POSTFIX
#MILOSZ SAWICKI
#03.04.2019


class Stack:
    def __init__(S):
        S.Stack = []

    def push(S, s):      # Dodawanie elementow
        S.Stack.append(s)

    def peek(S):          # Zwraca ostatni element
        return S.Stack[ len(S.Stack)-1 ]

    def isEmpty(S):        # Sprawdza czy stos jest pusty
        if len(S.Stack) == 0:
            return True
        else:
            return False

    def size(S):         # Ilosc elementow na stosie
            return len(S.Stack)

    def pop(S):     #usuwanie gornego elementu stosu, zwraca ten element
        pom = S.Stack[len(S.Stack)-1]
        del S.Stack[len(S.Stack)-1]
        return pom


def odczyt(pliktxt):    #funkcja odczytujaca z pliku
    f = open(pliktxt, 'r')
    return f.read()


def InfixPostfix(input):
    input_l=input.split()   #zamienia wejsciowy ciag znakow na liste

    stos = Stack()  #definiuje stos i liste z wynikiem
    wynik = []
    prec={}    #tworzy pomocniczy slownik zawierajacy pierwszenstwo wykonywania operatorow
    prec['/']=3
    prec['*']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    prec[')']=1

    for i in input_l:
        if i in "ABCDEFGHIJKLMNOPRSTUWXZ" or i.isdigit():     #szuka czy element z listy wejsciowej jest znakiem lub liczba
            wynik.append(i)     #jesli tak to dodaje go do wyniku
        elif i in "(":  #prawe nawiasy
            stos.push(i)
        elif i in ")":  #lewe nawiasy
            gora=stos.pop()
            while gora != "(":  #usuwa wszystkie elementy ze stosu az do znalezienia nawiasu prawego i dodaje je do wyniku
                wynik.append(gora)
                gora=stos.pop()
        else:   #operatory dzialania
            while (False == stos.isEmpty()) and (prec[stos.peek()] >= prec[i]):     #uwzglednia pierwszenstwo operacji
                wynik.append(stos.pop())
            stos.push(i)    #dodaje operator do stosu

    while False == stos.isEmpty():      #po skonczeniu petli for oproznia stos, dodajac wszystkie elementy do listy wynikowej
        wynik.append(stos.pop())
    return " ".join(wynik)      #laczy osobne ciagi znakow rozdzielajac spacja

#print(InfixPostfix("A * ( B + C ) - D / ( E - F )"))

def Oblicz(input):
    stos = Stack()
    input_l=input.split()

    for i in input_l:   #liczby dodaje na stos
        if i.isdigit():
            stos.push(i)

        if i in "/*+-":
            l1=stos.pop()   #usuwa i zapisuje w pamieci dwie gorne liczby ze stosu
            l2=stos.pop()
            stos.push(str(eval(l2 + i + l1)))   #wykonuje dzialanie i dodaje do stosu

    return round(float(stos.peek()))     #zwraca gorny element stosu czyli wynik

#print(Oblicz("6 5 - 8 4 - * 4 3 - /"))



print("1 - Konwersja notacji infix do postfix")
print("2 - Obliczanie wyrazenia w notacji postfix")
wybor = int(input())

plik=input("Prosze wprowadzic nazwe pliku z danymi(np. plik1.txt / plik2.txt):  ")

dane=odczyt(plik)
print("\nOdczytane dane: %s" %(dane))

if wybor == 1:
    out=InfixPostfix(dane)
    print("Konwersja do postfix: %s" %out)
if wybor == 2:
    out=Oblicz(dane)
    print("Wynik: %i" %out)
