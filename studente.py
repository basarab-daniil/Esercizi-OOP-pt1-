class Studente:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.voti = []

    def aggiungi_voto(self, voto): 
        if 0 <= voto <= 10:
            self.voti.append(voto)
        else:
            print("voto non valido")

    def media_voti(self):
        if len(self.voti) == 0:
            return 0
        media_voti = sum(self.voti) / len(self.voti)
        return media_voti

    def stampa_info(self): 
        print(self.nome)
        print(self.classe)
        print(len(self.voti))
        print(self.media_voti())
        
        