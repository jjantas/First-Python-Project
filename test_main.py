import pytest
from classes import Tram, Stop, Line
from main import CreateTramWeb



przystanek1 = Stop((30, 50))
przystanek2 = Stop((80, 150))
przystanek3 = Stop((500, 460))
przystanek4 = Stop((10, 800))
przystanek5 = Stop((400, 800))
przystanek6 = Stop((700, 800))
przystanek7 = Stop((1200, 800))



linia1 = Line([przystanek1, przystanek2, przystanek3])
linia2 = Line([przystanek4, przystanek5, przystanek6, przystanek7])



siec = CreateTramWeb([linia1, linia2])

