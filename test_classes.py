from classes import Line, Stop, Tram


def test_Line_stops():
    przystanek1 = Stop((40, 150))
    przystanek2 = Stop((80, 210))
    linia = Line([przystanek1, przystanek2])
    assert linia.stops == [przystanek1, przystanek2]


def test_Stop_coordinates():
    przystanek = Stop((40, 150))
    assert przystanek.coordinates == (40, 150)


def test_Tram_line():
    przystanek1 = Stop((40, 150))
    przystanek2 = Stop((80, 210))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    assert tramwaj.line == linia


def test_Tram_graphic():
    przystanek1 = Stop((40, 150))
    przystanek2 = Stop((80, 210))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    assert tramwaj.graphic.x == 40
    assert tramwaj.graphic.y == 150


def test_Tram_present_coordinates():
    przystanek1 = Stop((40, 150))
    przystanek2 = Stop((80, 210))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    assert tramwaj.present_coordinates == (40, 150)


def test_Tram_set_target():
    przystanek1 = Stop((40, 150))
    przystanek2 = Stop((80, 210))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    tramwaj.set_target()
    assert tramwaj.current_target == przystanek2
    tramwaj.set_target()
    assert tramwaj.current_target == przystanek1


def test_Tram_find_y():
    przystanek1 = Stop((5, 5))
    przystanek2 = Stop((10, 10))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    tramwaj.start_stop = przystanek1
    tramwaj.current_target = przystanek2
    assert tramwaj.find_y(1) == 1
    assert tramwaj.find_y(100) == 100


def test_Tram_move():
    przystanek1 = Stop((5, 5))
    przystanek2 = Stop((10, 10))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    tramwaj.start_stop = przystanek1
    tramwaj.current_target = przystanek2
    tramwaj.move()
    assert tramwaj._graphic.x == 6
    assert tramwaj._graphic.y == 6


def test_Tram_is_at_target_stop_beggining():
    przystanek1 = Stop((5, 5))
    przystanek2 = Stop((10, 10))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    assert tramwaj.is_at_target_stop()


def test_Tram_is_at_target_stop_positive():
    przystanek1 = Stop((5, 5))
    przystanek2 = Stop((7, 7))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    tramwaj._graphic.x = 7
    tramwaj._graphic.y = 7
    tramwaj.current_target = przystanek2
    assert tramwaj.is_at_target_stop()


def test_Tram_is_at_target_stop_negative():
    przystanek1 = Stop((5, 5))
    przystanek2 = Stop((7, 7))
    linia = Line([przystanek1, przystanek2])
    tramwaj = Tram(linia, przystanek1)
    tramwaj.current_target = przystanek2
    assert not tramwaj.is_at_target_stop()
