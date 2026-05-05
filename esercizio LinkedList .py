from collections import deque

class LinkedList:
    def __init__(self):
        self.modifiche = deque()

    def aggiungi_iniziali(self, utenti):
        self.modifiche.extend(utenti)

    def inserisci_dopo(self, riferimento, nuovo):
        idx = self.modifiche.index(riferimento)
        self.modifiche.insert(idx + 1, nuovo)

    def inserisci_prima(self, riferimento, nuovo):
        idx = self.modifiche.index(riferimento)
        self.modifiche.insert(idx, nuovo)

    def inserisci_in_testa(self, utente):
        self.modifiche.appendleft(utente)

    def rimuovi_vecchia(self):
        self.modifiche.popleft()

    def annulla_ultima(self):
        self.modifiche.pop()

    def stampa(self, punto):
        print(f"{punto}. {list(self.modifiche)}")

    def conta(self):
        print(f"13. {len(self.modifiche)}")

    def ultima_recente(self):
        print(f"14. {self.modifiche[-1]}")

gestore = LinkedList()

gestore.aggiungi_iniziali(["admin", "mario", "sara"])
gestore.stampa(2)

gestore.inserisci_dopo("mario", "guest")
gestore.stampa(4)

gestore.inserisci_in_testa("root")
gestore.stampa(6)

gestore.inserisci_prima("sara", "luca")
gestore.stampa(8)

gestore.rimuovi_vecchia()
gestore.stampa(10)

gestore.annulla_ultima()
gestore.stampa(12)

gestore.conta()
gestore.ultima_recente()