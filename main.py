from studente import Studente 
from rettangolo import Rettangolo

# Esercizio 1
p1 = Studente("Simone", "3f")

p1.aggiungi_voto(5)
p1.media_voti()
p1.stampa_info()

# Esercizio 2
r1 = Rettangolo(4, 5, "rosso")
r2 = Rettangolo(3, 7, "blu")
r3 = Rettangolo(6, 2, "verde")

r1.stampa_info()
r2.stampa_info()
r3.stampa_info()

area_media = (r1.area() + r2.area() + r3.area()) / 3
print("Media delle aree:", area_media)