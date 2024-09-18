# TRAMNET

## Dane autora

### Imie i nazwisko *Jakub Antas*
### Uczelnia *Politechnika Warszawska*
### Kierunek *Informatyka*
### Ulubiony przedmiot *PIPR*

## Cel i opis projektu


Celem stworzenia tego projektu było uzyskanie symulacji, która ukazuje jazdę tramwaji po liniach tramwajowych. Użytkownik programu poprzez interfejs w terminalu może stworzyć dowolną ilość linii(conajmniej 1), a w każdej z nich dowolną liczbę przystanków tramwajowych (conajmniej 2 aby linia miała sens). Rozmieszczenie przystanków jest również zależne od korzystającej z programu osoby. Dokonuje się go poprzez podanie koordynatów każdego z przystanków. Zakres koordynatów zależy zaś od ustawionej rozdzielczości programu. Po stworzeniu przez użytkownika żądanej liczby linii i przystanków, może on wyświetlić symulację poprzez wskazanie odpowiedniej opcji w Menu. Jego oczom powinno ukazać się okienko, w którym rozmieszczone będą grafiki przystanków położone na poprzednio wybranych koordynatach i będą one odpowiednio połączone(zgodnie z przynależnością do linii) odcinkami reprezentującymi tory tramwajowe. Grafika przystanku znajduje się w pliku `tram_stop.png`. Na początku działania programu na każdym z przystanków pojawi się tramwaj, który następnie rozpocznie swoją podróż dookoła linii. Natrafiąjąc na przystanek zatrzyma się (w celu zabrania pasażerów) i po chwili ruszy dalej. Tramwaj reprezentowany jest przez grafikę tramwaju znajdującą się w pliku `tram.png`.

## Klasy

#### Line

Klasa reprezentująca linie tramwajową. Głownym zadaniem instacji tej klasy jest ,,przetrzymywanie" przystanków należących do niej. Dzięki temu możliwe jest wskazanie, które przystanki powinny zostać ze sobą połączone, a które nie.

#### Stop

Klasa reprezentująca przystanek tramwajowy. ,,Przetrzymuje" informacje na temat położenia graficznej reprezentacji instacji(czyli jej koordynaty).


#### Tram

Klasa reprezentująca tramwaj. Jest to najbardziej rozbudowana klasa w tym projekcie. Przetrzymuje ona informacje na temat położenia tramwaju, przystanku na którym tramwaj został stworzony, linii po której tramwaj podróżuje, ostatniego przystanku na którym tramwaj był i przystanku do którego tramwaj obecnie zmierza. Do tego klasa posiada metody, które pozwalają wyznaczyć kolejny cel tramwaju, czyli przystanek do którego tramwaj ma podążać(wykorzystywana jest gdy tramwaj znajdować się będzie na jakimkolwiek z przystanków), poruszać tramwajem czy stwierdzić czy tramwaj dojechał do przystanku docelowego(czyli czy trzeba wyznaczyć nowy przystanek docelowy).

## Ustawienia

Jeśli chodzi o zmiany w działaniu programu przewidziana została zmiana rozdzielczości wyświetlanego okienka symulacji. Można ją zmienić wpisując odpowiednie wartości w pliku `settings.txt`. Można również zmienić czas przebywania tramwaju na przystanku. Więcej o tym w pliku `README.md`.

## Część refleksyjna

Bardzo dużo czasu poświęciłem na metodę move() z klasy Tram. Czytałem o tym wiele poradników i dokumentacje pygame, ale nie potrafiłem znaleźć metody która pozwoli przemieścić mi obiekt z jednego punktu do drugiego w prostej linii... Na początku próbowałem działać na wektorach, ale trawmaj wciąż zbaczał z kursu i nie jechał prosto. Problem z tą kluczową dla sensu całego programu metodą zatrzymał postęp moich prac na dość długo, ale na szczęście wpadłem na pomysł jak to rozwiązać - po prostu matematycznie. Skorzystałem ze wzoru na wzór funkcji liniowej przechodzącej przez 2 punkty na płaszczyźnie i dzięki temu mogłem przesuwać poziomo(po x-ach) mój obiekt tramwaju, a metoda move() znajdywała położenie w pionie(y) poprzez podłożenie do wzoru funkcji liniowej.