#  -*- coding: utf-8 -*-
# Konwerter notacji Infix/Postfix
#
# Błędy do naprawienia:
# 	-0.0 nie jest liczba

alfabet_duze = "ABCDEFGHIJKLMNOPRSTUWXZ"
alfabet_male = "abcdefghijklmnoprstuwxz"

# Słownik zawierajacy przypisane pierwszeństwa wykonywania operatorów
operatory = {} 
operatory['/'] = 3
operatory['*'] = 3
operatory['+'] = 2
operatory['-'] = 2
operatory['('] = 1
operatory[')'] = 1


class Stos:
	"""Struktura danych stosu."""

	def __init__(self):
		"""Konstruktor stosu."""
		self.Stos = []

	def push(self, x):
		"""Dodawanie elementu na wierzch stosu."""
		self.Stos = [x] + self.Stos

	def pop(self):
		"""Zdejmowanie elementu z wierzchu stosu."""
		return self.Stos.pop(0)

	def peek(self):
		"""Sprawdzanie pierwszego elementu na stosie."""
		if not self.is_empty():
			return self.Stos[0]

	def is_empty(self):
		"""Sprawdzanie, czy stos jest pusty."""
		if len(self.Stos) == 0:
			return True
		else:
			return False



def infix_do_postfix(wejscie):
	"""Konwerter wyrażeń w notacji infix do postfix."""

	# Usuwanie białych znaków
	wejscie = wejscie.replace(" ", "")

	# Przekształcanie wejściowego ciągu znaków na listę liczb i operatorów
	wejscie_list = []
	liczba = []

	for j, i in enumerate(wejscie):

		if i in operatory:

			if len(liczba) != 0:
				liczba = "".join([str(i) for i in liczba])
				wejscie_list.append(liczba)
				liczba = []

			# rozpoznawanie liczb ujemnych
			if i == "-" and ( wejscie[j-1] in "(" or j == 0):
				liczba.append("-")

			else:
				wejscie_list.append(i)

		else:
			liczba.append(i)

	if len(liczba) != 0:
		wejscie_list.append("".join([str(i) for i in liczba]))

	
	# Tworzenie pustego stosu i listy wynikowej
	wynik = []
	S = Stos()

	for n in wejscie_list:

		# Dopisywanie liczb w postaci int i float do stosu
		try:
			float(n)	
			wynik.append(n)

		except:

			# Dopisywanie symboli liczb do stosu
			if n in alfabet_male + alfabet_duze:
				wynik.append(n)

			# Dopisywanie nawiasów
			elif n == "(":
				S.push(n)

			elif n == ")":
				m = S.pop() 

				while m != "(":
					wynik.append(m)
					m = S.pop() 

			# Dopisywanie operatorów
			elif n in "*+-/:":
				while not S.is_empty() and operatory[S.peek()] >= operatory[n]:
					wynik.append(S.pop())

				S.push(n)

	# Opróżnianie stosu. Obiekty na stosie dopisywane są do wyniku.
	while not S.is_empty():
		wynik.append(S.pop())

	# Wyświetlanie wyniku w postaci elementów wyrażenia rodzielonego przecinkami
	return ",".join([str(i) for i in wynik])


def oblicz_postfix(wejscie):
	"""Obliczanie wyrażenia zapisanego w notacji postfix."""

	# Usuwanie białych znaków i połączenie elementów wyrażenia w listę
	wejscie = wejscie.replace(" ", "")
	wejscie = wejscie.split(",")

	S = Stos()

	for i in wejscie:

		if i in "/*+-":
			# Usuwanie i zapisywanie w pamieci dwóch górych liczb na stosie
			l1 = S.pop()
			l2 = S.pop()

			# Wykonywanie działania i dodawanie wyniku do stosu
			try:
				float(l1)
				float(l2)
				wynik = str(eval(l2 + i + l1))
				S.push(wynik)

			except:
				#print("liczba_2:",l2, "liczba_1:", l1)
				return "Składniki wyrażenia nie są liczbami."

		# Dodawanie elementów liczbowych do stosu
		else:
			S.push(i)
				
	# Zwracanie górnego elementu stosu - wyniku
	return S.peek()


if __name__ == '__main__':
	# Przykłady działania programu

	przyklad1 = "A*(B + C) − D/(E − F)"
	przyklad2 = "a + (-2)*(6/D) "
	przyklad3 = "(0.20 + (-3.20))/(6-2)"
	przyklad4 = "-3*(2/4) + 1*0 + 10/4"

	przyklad3_postfix = infix_do_postfix(przyklad3)
	przyklad4_postfix = infix_do_postfix(przyklad4)


	print("Infix: ", przyklad1, "\nPostfix: ", infix_do_postfix(przyklad1))
	print("Infix: ", przyklad2, "\nPostfix: ", infix_do_postfix(przyklad2))
	print("Infix: ", przyklad3, "\nPostfix: ", przyklad3_postfix)

	print("Oblicz wyrażenie", przyklad3_postfix, "w notacji Postfix: \nWynik:", oblicz_postfix(przyklad3_postfix))
	print("Oblicz wyrażenie", przyklad4_postfix, "w notacji Postfix: \nWynik:", oblicz_postfix(przyklad4_postfix))
