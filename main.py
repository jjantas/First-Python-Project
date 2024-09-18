import pygame
import sys
from classes import Line, Stop, Tram


def CreateTramWeb(list_of_lines) -> None:

    list_of_trams = []

    # Initialization
    pygame.init()

    # Setting screen
    try:
        width, height = screen_width, screen_height
    except NameError:
        width, height = (1920, 1080)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Symulacja Tramwajowa')

    # Create Trams
    for line in list_of_lines:
        lista_przystankow = line.stops
        for stop in lista_przystankow:
            nowy_tramwaj = Tram(line, stop)
            list_of_trams.append(nowy_tramwaj)

    # Loading tram image
    tram_pic = pygame.image.load('tram.png')
    tram_stop_pic = pygame.image.load('tram_stop.png')

    # Program
    while True:
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                sys.exit()

            # Drawing
        screen.fill((0, 0, 0))
        for line in list_of_lines:
            last_stop = line.stops[len(line.stops) - 1]
            for stop in line.stops:
                x_stop, y_stop = stop.coordinates
                last_stop_coordinates = last_stop.coordinates
                box = pygame.Rect(x_stop, y_stop, 10, 10)
                pygame.draw.rect(screen, (255, 255, 255), box)
                screen.blit(tram_stop_pic, (x_stop, y_stop))
                pygame.draw.line(screen, (255, 255, 255),
                                 last_stop_coordinates, (x_stop, y_stop))
                last_stop = stop

        for tram in list_of_trams:
            info = tram.is_at_target_stop()
            if info:
                tram.start_stop = tram.current_target
                tram.set_target()
                try:
                    tram.waiting = ticks_for_stop
                except NameError:
                    tram.waiting = 100
            else:
                if tram.waiting == 0:
                    tram.move()
                else:
                    tram.waiting -= 1
            screen.blit(tram_pic, (tram._graphic.x, tram._graphic.y))

        pygame.display.flip()


if __name__ == '__main__':

    # Loading screen resolution

    with open('settings.txt') as file:
        screen_width = int(file.readline().strip().split('=')[1])
        screen_height = int(file.readline().strip().split('=')[1])
        ticks_for_stop = int(file.readline().strip().split('=')[1])

    # Menu input

    linie = []

    inputting = True
    while inputting:
        print('---------------------------------------')
        print('Witamy w kreatorze symulacji tramwajowych.\nWybierz opcje z\
 menu wpisując w terminalu odpowiadającą jej cyfrę:\n\n1.Dodaj linie i\
 przystanki\n2.Wyświetl symulacje\n---------------------------------------')

        menu_choice = input('Wprowadź numer opcji: ')

        if menu_choice == '1':
            przystanki_linii = []
            adding_stops = True
            print('Tworzysz linie. Pamiętaj, że linia powinna mieć co najmniej\
 2 przystanki\n')

            while adding_stops:
                print('Wprowadz w terminal cyfrę odpowiadającą opcji z której\
 chcesz skorzystać:\n\n1.Dodaj przystanek do linii\n2.Zakończ tworzenie\
 linii\n')
                add_stop_choice = input('Wprowadź numer opcji: ')

                if add_stop_choice == '1':
                    x = int(input(f'Podaj x-ową współrzędną przystanku(zakres\
 od 0 do {screen_width}): '))
                    y = int(input(f'Podaj y-ową współrzędną przystanku(zakres\
 od 0 do {screen_height}): '))
                    if x >= 0 and x <= screen_width and y >= 0\
                            and y <= screen_height:
                        przystanki_linii.append(Stop(((x, y))))
                        print('Dodano przystanek\n')
                    else:
                        print('Niepoprawna wartość współrzędnych')
                elif add_stop_choice == '2' and len(przystanki_linii) > 1:
                    adding_stops = False
                    linie.append(Line(przystanki_linii))
                    print('Prawidłowo stworzono linię\n')

                elif add_stop_choice == '2' and len(przystanki_linii) < 2:
                    adding_stops = False
                    print('Usunięto linie. Niewystarczająca liczba\
 przystanków(wymagane conajmniej 2)\n')

                else:
                    print('Nieprawidłowy wybór opcji\n')

        elif menu_choice == '2' and linie:
            inputting = False

        elif menu_choice == '2' and not linie:
            print('Należy dodać co najmniej jedną linię\n')

        else:
            print('Nieprawidłowy wybór opcji.\n')

    CreateTramWeb(linie)
