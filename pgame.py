import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Pygame")
# određujemo dimenzije prozora
(sirina, visina) = (400, 400)
# prikazujemo prozor tih dimenzija
prozor = pg.display.set_mode((sirina, visina))

# bojimo pozadinu prozora u belo
prozor.fill([255, 128, 0])

# crtamo crnu duž od tačke (100, 100) do tačke (300, 300)
# debljine 5
pg.draw.line(prozor, pg.Color([0, 128, 255]), (100, 100), (300, 300), 5)

# osvežavamo sadržaj prozora i tako prikazujemo ono što smo nacrtali
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
   pass

# isključivanje rada biblioteke PyGame
pg.quit()
