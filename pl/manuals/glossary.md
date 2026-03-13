---
brief: Ten słowniczek zawiera terminy Defold z krótkimi objaśnieniami.
github: https://github.com/defold/doc
language: pl
layout: manual
title: Słowniczek Defold
toc:
- Słowniczek Defold
- Animation set (Zestaw do animowania)
- Atlas (Galeria obrazów)
- Builtins (Wbudowane elementy)
- Camera (Kamera)
- Collision object (Obiekt kolizji)
- Component (Komponent)
- Collection (Kolekcja)
- Collection factory (Fabryka kolekcji)
- Collection proxy (Pełnomocnik kolekcji)
- Cubemap (Tekstura sześcienna)
- Debugging (Debugowanie)
- Display profiles (Profile wyświetlania)
- Factory (Fabryka)
- Font (Czcionka)
- Fragment shader (Shader fragmentu)
- Gamepads (Kontrolery)
- Game object (Obiekt gry)
- GUI (Interfejs graficzny użytkownika)
- GUI script (Skrypt GUI)
- Hot reload (Szybkie przeładowanie)
- Input binding (Wiązania wejść)
- Label (Etykieta)
- Library (Biblioteka)
- Lua language (Język Lua)
- Lua module (Moduł Lua)
- Material (Materiał)
- Message (Wiadomość)
- Model (Model)
- ParticleFX (Efekt cząsteczkowy)
- Profiling (Profilowanie)
- Render (Render)
- Render script (Skrypt do renderowania)
- Script (Skrypt)
- Sound (Dźwięk)
- Sprite (Obraz)
- Texture profiles (Profile teksturowania)
- Tile map (Mapa kafelków)
- Tile source (Źródło kafelków)
- Vertex shader (Shader wierzchołków)
---

# Słowniczek Defold

Ten słowniczek udziela krótkich wyjaśnień dla terminów, które napotkasz podczas pracy z silnikiem Defold. W większości przypadków zamieszczamy też odnośniki do obszerniejszych opisów.

## Animation set (Zestaw do animowania)

![Animation set](/manuals/images/icons/animationset.png) Zestaw do animowania zawiera listę plików `.dae` lub innych plików `.animationset`, z których odczytywane są animacje. Dodawanie jednego pliku `.animationset` do drugiego jest przydatne, gdy chcesz udostępnić fragmenty animacji kilku modelom. Szczegóły znajdziesz w [instrukcji do animacji modeli 3D](/pl/manuals/model-animation/).

## Atlas (Galeria obrazów)

![Atlas](/manuals/images/icons/atlas.png) Atlas to zbiór osobnych obrazów skompilowanych w większy arkusz, co poprawia wydajność i oszczędza pamięć. Atlasy mogą zawierać statyczne grafiki lub zestawy klatek animacji poklatkowej. Różne komponenty korzystają z atlasów, aby współdzielić zasoby graficzne. Więcej w [dokumentacji do Atlasów](/pl/manuals/atlas).

## Builtins (Wbudowane elementy)

![Builtins](/manuals/images/icons/builtins.png) Folder `builtins` w projekcie zawiera domyślne, tylko do odczytu zasoby. Znajdziesz tam domyślny renderer, skrypt renderujący, materiały i inne elementy. Jeśli potrzebujesz zmodyfikować któryś z tych zasobów, skopiuj go do projektu i edytuj według potrzeb.

## Camera (Kamera)

![Camera](/manuals/images/icons/camera.png) Komponent kamery decyduje, która część świata gry ma być widoczna i jak ma być rzutowana. Powszechną praktyką jest przypinać kamerę do obiektu gracza albo tworzyć osobny obiekt, który podąża za graczem z dodatkowym wygładzaniem. Więcej w [dokumentacji do Kamery](/pl/manuals/camera).

## Collision object (Obiekt kolizji)

![Collision object](/manuals/images/icons/collision-object.png) Obiekty kolizji rozszerzają obiekty gry o właściwości fizyczne, takie jak kształt przestrzenny, masa, tarcie i tłumienie. To one decydują, jak dany obiekt reaguje na kontakt z innymi. Najczęściej spotykane typy to obiekty kinematyczne, dynamiczne i wyzwalacze. Kinematyczny obiekt dostarcza szczegółowe informacje o kolizji, które możesz obsłużyć ręcznie, dynamiczny obiekt jest symulowany przez silnik fizyki zgodnie z prawami Newtona, a wyzwalacze wykrywają tylko wejście lub wyjście innych kształtów. Szczegóły w [dokumentacji do Fizyki](/pl/manuals/physics).

## Component (Komponent)

Komponenty nadają obiektom gry konkretną ekspresję lub funkcjonalność, na przykład grafikę, animację, zachowanie zdefiniowane skryptem czy dźwięk. Nie żyją osobno — muszą należeć do obiektów gry. W silniku Defold dostępnych jest wiele rodzajów komponentów, opisanych w [instrukcji o blokach budujących](/pl/manuals/building-blocks).

## Collection (Kolekcja)

![Collection](/manuals/images/icons/collection.png) Kolekcje to mechanizm pozwalający tworzyć szablony (prefaby) zawierające hierarchie obiektów gry. Są strukturami drzewa przechowującymi obiekty gry i inne kolekcje. Kolekcje przechowywane są jako pliki i wprowadza się je do gry statycznie przez edytor lub dynamicznie przez generowanie. Więcej w [instrukcji o blokach budujących](/pl/manuals/building-blocks).

## Collection factory (Fabryka kolekcji)

![Collection factory](/manuals/images/icons/collection-factory.png) Fabryka kolekcji pozwala dynamicznie tworzyć hierarchie obiektów gry zgodne z opisem w kolekcji. Szczegóły w [instrukcji do Fabryki kolekcji](/pl/manuals/collection-factory).

## Collection proxy (Pełnomocnik kolekcji)

![Collection](/manuals/images/icons/collection.png) Pełnomocnik kolekcji służy do ładowania i aktywowania kolekcji w trakcie działania aplikacji. Najczęściej używa się go do wczytywania kolejnych poziomów. Zobacz [dokumentację do Pełnomocników kolekcji](/pl/manuals/collection-proxy).

## Cubemap (Tekstura sześcienna)

![Cubemap](/manuals/images/icons/cubemap.png) Tekstura sześcienna (cubemap) to specjalny typ tekstury złożony z sześciu osobnych obrazów mapowanych na ściany sześcianu. Przydatna do renderowania skyboxów oraz map odbić i oświetlenia.

## Debugging (Debugowanie)

Kiedy gra zaczyna zachowywać się nieoczekiwanie, musisz odnaleźć przyczynę. Nauka debugowania jest sztuką, a Defold oferuje wbudowany debugger, który ułatwia to zadanie. Więcej w [instrukcji do Debugowania](/manuals/debugging).

## Display profiles (Profile wyświetlania)

![Display profiles](/manuals/images/icons/display-profiles.png) Plik profilu wyświetlania pozwala określić układy GUI zależne od orientacji, proporcji obrazu lub modelu urządzenia. Dzięki temu można dostosować interfejs do różnorodnych ekranów. Więcej w [instrukcji do Układów](/pl/manuals/gui-layouts).

## Factory (Fabryka)

![Factory](/manuals/images/icons/factory.png) Czasem nie chcesz tworzyć wszystkich obiektów gry ręcznie w kolekcji — potrzebujesz ich w czasie działania gry. Fabryka umożliwia dynamiczne tworzenie takich obiektów z wcześniej przygotowanej puli. Zobacz [instrukcję do Fabryki](/pl/manuals/factory).

## Font (Czcionka)

![Font file](/manuals/images/icons/font.png) Zasób typu Font powstaje na podstawie pliku TrueType lub OpenType i określa rozmiar oraz dekoracje (np. obrys, cień) renderowanej czcionki. Fonty wykorzystują komponenty GUI i Label. Więcej w [instrukcji do Fontów](/pl/manuals/font/).

## Fragment shader (Shader fragmentu)

![Fragment shader](/manuals/images/icons/fragment-shader.png) Shader fragmentu to program uruchamiany na procesorze graficznym dla każdego piksela (fragmentu) rysowanego wielokąta. Określa kolor wynikowego fragmentu, wykonując obliczenia, odczyty tekstur lub ich kombinacje. Szczegóły w [instrukcji do Shaderów](/manuals/shader).

## Gamepads (Kontrolery)

![Gamepads](/manuals/images/icons/gamepad.png) Plik Gamepads definiuje sposób mapowania wejść ze konkretnych kontrolerów na wyzwalacze wejścia dostępne dla danej platformy. Więcej w [instrukcji do Wejść](/pl/manuals/input).

## Game object (Obiekt gry)

![Game object](/manuals/images/icons/game-object.png) Obiekty gry to kontenery ze swoim cyklem życia podczas działania gry. Zazwyczaj zawierają komponenty wizualne albo dźwiękowe oraz mogą mieć zachowanie opisane skryptem. Tworzy się je w edytorze, umieszczając w kolekcjach, albo dynamicznie przez fabryki. Szczegóły w [instrukcji o blokach budujących](/pl/manuals/building-blocks).

## GUI (Interfejs graficzny użytkownika)

![GUI component](/manuals/images/icons/gui.png) Komponent GUI zawiera elementy interfejsu: tekst, kolorowe lub teksturowane bloki. Elementy można organizować hierarchicznie, skryptować i animować. GUI służy do HUD, menu i powiadomień. Steruje nim skrypt GUI, który opisuje zachowanie i interakcje użytkownika. Więcej w [dokumentacji do GUI](/pl/manuals/gui).

## GUI script (Skrypt GUI)

![GUI script](/manuals/images/icons/script.png) Skrypty GUI kontrolują zachowanie komponentów GUI — animacje, reakcje na wejścia i inne interakcje. Zobacz [instrukcję o Lua w silniku Defold](/pl/manuals/lua), aby dowiedzieć się, jak są wykorzystywane.

## Hot reload (Szybkie przeładowanie)

Edytor Defold pozwala aktualizować zawartość w uruchomionym programie na desktopie i urządzeniach mobilnych. Ta funkcja przyspiesza pracę przy rozwoju gry. Więcej w [instrukcji do Hot reload](/manuals/hot-reload).

## Input binding (Wiązania wejść)

![Input binding](/manuals/images/icons/input-binding.png) Pliki wiązań wejść określają, jak interpretować sygnały z myszy, klawiatury, ekranu dotykowego czy gamepada. Wiążą sprzętowe wejścia z wysokopoziomowymi akcjami, takimi jak `jump` czy `move_forward`. Skrypty nasłuchujące wejść reagują na te akcje w sposób określony przez twórcę. Więcej w [instrukcji do Wejść](/pl/manuals/input).

## Label (Etykieta)

![Label](/manuals/images/icons/label.png) Komponent Label umożliwia przypisanie tekstu do obiektu gry. Renderuje go przy użyciu wybranego fontu, w przestrzeni gry (nie GUI). Więcej w [instrukcji do Etykiet](/pl/manuals/label).

## Library (Biblioteka)

![Game object](/manuals/images/icons/builtins.png) Defold pozwala współdzielić dane między projektami za pomocą bibliotek. Możesz z nich korzystać w wielu projektach, dla siebie lub zespołu. Szczegóły w [dokumentacji do Bibliotek](/pl/manuals/libraries).

## Lua language (Język Lua)

Lua to język skryptowy wykorzystywany do tworzenia logiki gry w silniku Defold. Jest mały, wydajny i wspiera programowanie proceduralne, obiektowe, funkcyjne oraz data-driven. Więcej na oficjalnej stronie https://www.lua.org/ oraz w [instrukcji do Lua](/pl/manuals/lua).

## Lua module (Moduł Lua)

![Lua module](/manuals/images/icons/lua-module.png) Moduły Lua pozwalają tworzyć struktury wielokrotnego użytku i czytelnie organizować kod. Więcej w [instrukcji do modułów Lua](/pl/manuals/modules/).

## Material (Materiał)

![Material](/manuals/images/icons/material.png) Materiały opisują sposób renderowania obiektów przez przypisanie shaderów i ich właściwości. Więcej w [instrukcji do Materiałów](/manuals/material).

## Message (Wiadomość)

Komponenty komunikują się poprzez przesyłanie wiadomości silnika Defold. Mogą też automatycznie reagować na określone wiadomości, np. włączać/wyłączać grafikę, kolizje, animacje, efekty cząsteczkowe lub dźwięk. Silnik używa wiadomości do informowania o zdarzeniach, jak kolizje. System wiadomości potrzebuje odbiorcy, więc wszystko w grze ma unikalny adres. Aby ułatwić komunikację, Defold rozszerza Lua o mechanizm przechwytywania i wysyłania wiadomości oraz dostarcza przydatne funkcje.

Przykładowo, aby ukryć sprite `weapon`, wystarczy:

```lua
msg.post("#weapon", "disable")
```

`"#weapon"` to adres komponentu, z którego wysyłana jest wiadomość, a `"disable"` to nazwa wiadomości, na którą reaguje sprite. Więcej w [dokumentacji do przesyłania wiadomości](/pl/manuals/message-passing).

## Model (Model)

![Model](/manuals/images/icons/model.png) Komponent Model umożliwia import siatek, szkielety i animacje z formatu glTF do gry. Więcej w [instrukcji do Modeli](/pl/manuals/model/).

## ParticleFX (Efekt cząsteczkowy)

![ParticleFX](/manuals/images/icons/particlefx.png) Efekty cząsteczkowe pomagają tworzyć wizualne efekty, takie jak mgła, ogień, deszcz czy spadające liście. Defold wyposażono w edytor ParticleFX, który pozwala budować i dopasowywać efekty w czasie rzeczywistym. Więcej w [dokumentacji do ParticleFX](/pl/manuals/particlefx).

## Profiling (Profilowanie)

Dobra wydajność jest kluczowa, dlatego warto mierzyć wydajność i pamięć gry, aby wykryć wąskie gardła. Defold udostępnia narzędzia do profilowania. Szczegóły w [instrukcji do Profilowania](/manuals/profiling).

## Render (Render)

![Render](/manuals/images/icons/render.png) Pliki Render zawierają ustawienia używane podczas renderowania gry — określają, który render script i materiały mają być użyte. Więcej w [instrukcji do Renderowania](/manuals/render/).

## Render script (Skrypt do renderowania)

![Render script](/manuals/images/icons/script.png) Skrypt do renderowania to skrypt Lua sterujący tym, jak gra jest renderowana na ekranie. Domyślny skrypt pokrywa większość scenariuszy, ale możesz napisać własny, jeśli potrzebujesz niestandardowych efektów lub oświetlenia. Więcej w [instrukcji do Renderowania](/manuals/render/) oraz w [instrukcji do Lua](/pl/manuals/lua).

## Script (Skrypt)

![Script](/manuals/images/icons/script.png) Skrypt to komponent zawierający kod, który definiuje zachowanie obiektu gry. Dzięki skryptom ustalasz reguły gry, reagujesz na interakcje i aktualizujesz stan świata. Wszystkie skrypty pisze się w Lua — aby pracować z silnikiem Defold, ty lub ktoś z zespołu musi poznać ten język. Więcej w [instrukcji do Lua](/pl/manuals/lua).

## Sound (Dźwięk)

![Sound](/manuals/images/icons/sound.png) Komponent dźwiękowy odtwarza określony plik audio. Defold wspiera formaty WAV i Ogg Vorbis. Więcej w [instrukcji do Dźwięków](/pl/manuals/sound).

## Sprite (Obraz)

![Sprite](/manuals/images/icons/sprite.png) Sprite to komponent graficzny, który wyświetla obraz z Tile source lub Atlasu. Obsługuje animacje poklatkowe i oparte na kościach. Sprite’y najczęściej reprezentują postacie i przedmioty w grach 2D.

## Texture profiles (Profile teksturowania)

![Texture profiles](/manuals/images/icons/texture-profiles.png) Profile teksturowania używane są podczas bundlingu, aby automatycznie przetwarzać i kompresować dane obrazowe (w atlasach, Tile sources, cubemapach i osobnych teksturach używanych w modelach czy GUI). Więcej w [instrukcji do Profili teksturowania](/pl/manuals/texture-profiles).

## Tile map (Mapa kafelków)

![Tile map](/manuals/images/icons/tilemap.png) Mapa kafelków wyświetla obrazy z Tile source na jednej lub kilku warstwach siatki. Można używać jej do tworzenia poziomów, ścian, budynków, przeszkód czy jaskiń. Obsługuje wiele warstw w różnych trybach mieszania i pozwala na dynamiczną podmianę pojedynczych kafelków (np. żeby zniszczyć most i zmienić kolizje). Więcej w [dokumentacji do Tile map](/pl/manuals/tilemap).

## Tile source (Źródło kafelków)

![Tile source](/manuals/images/icons/tilesource.png) Tile source to tekstura składająca się z wielu mniejszych obrazów tej samej wielkości, czyli kafelków. Można z niej tworzyć animacje poklatkowe, a także automatycznie generować kształty kolizji. Tile source używa się w Tile mapach, ale też jako teksturę do sprite’ów i efektów cząsteczkowych. Więcej w [dokumentacji do Tile map](/pl/manuals/tilemap).

## Vertex shader (Shader wierzchołków)

![Vertex shader](/manuals/images/icons/vertex-shader.png) Shader wierzchołków to program uruchamiany na GPU, który przetwarza geometrię siatek (wielokąty) i oblicza końcowe pozycje wierzchołków na ekranie. Więcej w [instrukcji do Shaderów](/manuals/shader).