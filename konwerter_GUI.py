#  -*- coding: utf-8 -*-
# Konwerter notacji Infix/Postfix GUI

import tkinter as tk
# Do uruchomienia programu wymagana jest biblioteka tkinter
import konwerter


class KonwerterGUI(tk.Tk):
	"""Interfejs graficzny konwertera notacji infix w postfix."""

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_geometry(self, '500x200')
		tk.Tk.wm_title(self ,"Konwerter Infix/Postfix")

		label_witamy = tk.Label(self, text = "Konwerter notacji Infix/Postfix", font=("Arial Bold", 15))

		entry_infix = LabeledEntry(self, label = "Wyrażenie w notacji Infix")
		entry_postfix = LabeledEntry(self, label = "Wyrażenie w notacji Postfix")

		text_wynik = tk.Text(self)
		text_wynik.insert("1.0", "Wynik")


		button_przeksztalc = tk.Button(self, text = "Przekształć na Postfix",
		command = lambda: self.przeksztalc_infix_postfix(entry_infix.get(), entry_postfix))

		button_oblicz_postfix = tk.Button(self, text = "Oblicz Postfix",
		command = lambda: self.oblicz_postfix(entry_postfix.get(), text_wynik))

		entry_infix.bind("<Return>", lambda event = None: button_przeksztalc.invoke())
		entry_postfix.bind("<Return>", lambda event = None: button_oblicz_postfix.invoke())

		label_witamy.pack()
		entry_infix.pack(fill = tk.X)
		button_przeksztalc.pack()
		entry_postfix.pack(fill = tk.X)
		button_oblicz_postfix.pack()
		text_wynik.pack(fill = tk.X)

	def przeksztalc_infix_postfix(self, wejscie, entry_postfix):
		if wejscie != "Wyrażenie w notacji Infix":
			postfix = konwerter.infix_do_postfix(wejscie)
			entry_postfix.delete(0, tk.END)
			entry_postfix.insert(0, postfix)

	def oblicz_postfix(self, wejscie, text_wynik):
		if wejscie != "Wyrażenie w notacji Postfix":
			try:		
				wynik = konwerter.oblicz_postfix(wejscie)
				text_wynik.delete("1.0", tk.END)
				text_wynik.insert("1.0", wynik)
			except:
				text_wynik.delete("1.0", tk.END)


class LabeledEntry(tk.Entry):
	"""Klasa formularza ze znikającym tekstem po naciśnieciu"""
	def __init__(self, master=None, label="Search", **kwargs):
		tk.Entry.__init__(self, master, **kwargs)
		self.label = label
		self.on_exit()
		self.bind('<FocusIn>', self.on_entry)
		self.bind('<FocusOut>', self.on_exit)

	def on_entry(self, event=None):
		if self.get() == self.label:
			self.delete(0, tk.END)

	def on_exit(self, event=None):
		if not self.get():
			self.insert(0, self.label)



app = KonwerterGUI()
app.mainloop()