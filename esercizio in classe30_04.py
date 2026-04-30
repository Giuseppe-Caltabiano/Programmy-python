class Notifiche:
    def __init__(self):
        # Inizializziamo una lista vuota che fungerà da pila
        self.pila = []

    def arriva(self, messaggio):
        # Aggiunge la notifica in fondo alla lista (che consideriamo la "cima")
        self.pila.append(messaggio)

    def leggi(self):
        # Rimuove e restituisce l'ultimo elemento se la pila non è vuota
        if not self.pila:
            print("Nessuna notifica.")
        else:
            notifica = self.pila.pop()
            print(f"Letta: {notifica}")

    def prossima(self):
        # Mostra l'ultimo elemento senza rimuoverlo
        if not self.pila:
            print("Nessuna notifica in attesa.")
        else:
            print(f"In cima: {self.pila[-1]}")

# --- Test del comportamento ---

n = Notifiche()

n.arriva("WhatsApp: Ciao!")
n.arriva("Gmail: Hai un nuovo messaggio")
n.arriva("Instagram: Ti hanno taggato")

n.prossima()  # Output: In cima: Instagram: Ti hanno taggato

n.leggi()     # Output: Letta: Instagram: Ti hanno taggato
n.leggi()     # Output: Letta: Gmail: Hai un nuovo messaggio
n.leggi()     # Output: Letta: WhatsApp: Ciao!
n.leggi()     # Output: Nessuna notifica.