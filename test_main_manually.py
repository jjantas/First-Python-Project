from classes import Stop, Line
from main import CreateTramWeb

"Testing code by manually inserting values of Stops and Lines(not by UI)"

t1 = Stop((200, 800))
t2 = Stop((200, 300))
t3 = Stop((100, 300))
t4 = Stop((100, 200))
t5 = Stop((500, 200))
t6 = Stop((500, 300))
t7 = Stop((300, 300))
t8 = Stop((300, 800))
r1 = Stop((550, 200))
r2 = Stop((900, 200))
r3 = Stop((900, 450))
r4 = Stop((800, 450))
r5 = Stop((1000, 800))
r6 = Stop((850, 800))
r7 = Stop((650, 400))
r8 = Stop((850, 400))
r9 = Stop((850, 250))
r10 = Stop((600, 250))
r11 = Stop((600, 800))
r12 = Stop((550, 800))
a1 = Stop((1050, 800))
a2 = Stop((1200, 200))
a3 = Stop((1350, 800))
a4 = Stop((1300, 800))
a5 = Stop((1200, 400))
a6 = Stop((1100, 800))
m1 = Stop((1400, 800))
m2 = Stop((1400, 200))
m3 = Stop((1650, 450))
m4 = Stop((1900, 200))
m5 = Stop((1900, 800))
m6 = Stop((1850, 800))
m7 = Stop((1850, 300))
m8 = Stop((1650, 550))
m9 = Stop((1450, 300))
m10 = Stop((1450, 800))


linia1 = Line([t1, t2, t3, t4, t5, t6, t7, t8])
linia2 = Line([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12])
linia3 = Line([a1, a2, a3, a4, a5, a6])
linia4 = Line([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10])

if __name__ == '__main__':
    CreateTramWeb([linia1, linia2, linia3, linia4])