Read the README.md in English <a href="./additional-media/README-en.md">here</a>

# Wirtualny Spacer - I LO im. Stanisława Staszica w Chrzanowie

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Static Badge](https://img.shields.io/badge/Panellum.js-%23ffa321?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/AndreansxTech/Staszic360?style=for-the-badge&logo=github)
![GitHub License](https://img.shields.io/github/license/AndreansxTech/Staszic360?style=for-the-badge)
[![Kontakt](https://img.shields.io/badge/Kontakt-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Andrtexh)


Interaktywny wirtualny spacer po I Liceum Ogólnokształcącym im. Stanisława Staszica w Chrzanowie. </br>
Cały projekt jest realizowany przez grupę trzech uczniów szkoły, w pełni bez żadnych korzyści finansowych. Wszystkie zdjęcia wykonane w szkole są dostępne w nieruszonej jakości w folderze <a href="./media/">media</a>.

## 🌐 Demo na żywo

Odwiedź wirtualny spacer na stronie: [Staszic360](https://staszic-virtual-walk.pages.dev) !

## 📝 Opis

Ten projekt zapewnia immersyjne doświadczenie wirtualnego spaceru po korytarzach i salach I LO im. Stanisława Staszica w Chrzanowie. Użytkownicy mogą nawigować po różnych częściach budynku szkoły, odwiedzając sale lekcyjne, korytarze i między innymi sale gimnastyczne jak również gabinety i pomieszczenia nie dostępne typowo dla uczniów szkoły. Strona internetowa jest w pełni dostosowana do standardów dostępności W3C tak aby każdy mógł w pełni.

## 🖼️ Podgląd

![Podgląd Wirtualnego Spaceru](./additional-media/preview-gif2.gif)

## 🚀 Funkcje

- Interaktywny widok w 360 stopniach
- Płynna nawigacja między różnymi lokalizacjami
- Wysokiej jakości zdjęcia panoramiczne
- Funkcjonalność szybkiego dostępu do sal lekcyjnych
- Piękny styl glassmorphism
- Pełna dostępność zgodnie z W3C

## 🤝 Dostępność

Nasza strona wirtualnego spaceru zawiera wbudowane opcje dostępności, aby poprawić doświadczenie każdego użytkownika:

- **Tryb wysokiego kontrastu:** Przełącz na wysoki kontrast dla lepszej widoczności.
- **Zmiana rozmiaru tekstu:** Zwiększ lub zmniejsz rozmiar tekstu dla lepszej czytelności.
- **Przełącznik animacji:** Włącz lub wyłącz animacje, aby dostosować stronę do osobistych preferencji.

## 🛠️ Użyte technologie

- HTML5
- CSS3
- JavaScript
- Panellum.js 

## Znane błędy / problemy

- Czasami przy użyciu menu szybkiego dostępu, możemy zobaczyć komunikat ```"The file %s could not be accessed."``` W takim przypadku należy poprostu kliknąć na salę w menu szybkieg dostępu jeszcze raz. Ten błąd pojawia się dosyć rzadko, a jego powodem jest trudność z załadowaniem zdjęcia przez Cloudflare w odpowiednim czasie. Zdjęcia są dosyć duże a plan, dzięki któremu ta strona jest hostowana, jest darmowy więc czas jaki CPU w hostingu może przeznaczyć na zapytanie od clienta jest ograniczony
- Przy przełączaniu funkcji dostępności "Włącz / Wyłącz animacje", hotspoty mogą przesunąć się do lewego górnego rogu zamiast być tam gdzie powinny. Ten błąd nie wpływa na funkcjonalność strony. Hotspoty odrazu wracają na swoje miejsce kiedy tylko poruszymy panoramą.
- Jeśli jakieś błedy wystąpią w wersji production, zostaną dodane tutaj. Jeśli zauważyłeś/aś jakiś błąd, możesz napisać do jednego z nas najlepiej z zrzutem ekranu albo poprostu opisem błędu.  

## Dla dociekliwych
- Pliki są podpisane cyfrowo aby można było zapewnić ich integralność i autentyczność. ( Czytaj niżej )
- Jeśli jesteś zainteresowanym rozwinięciem tego projektu albo jesteś poprostu ciekaw jak to dokładniej działa i jak postępował rozwój, sprawdź koniecznie pliki <a href="./LICENSE">LICENSE</a> oraz <a href="./additional-media/devnotes.md">devnotes</a>
- Jeśli chcesz zaproponować coś albo cokolwiek, możesz napisać na <a href="https://t.me/Andrtexh" target="_blank">Telegramie</a>.

## Weryfikacja podpisów

Pliki `index.html`, `panellum.js` i `panellum.css` są podpisane cyfrowo za pomocą GPG, aby zapewnić ich integralność i autentyczność. Oznacza to, że możesz mieć pewność, iż pliki te nie zostały zmodyfikowane przez osoby trzecie od momentu ich podpisania przez nas.</br>

Pamiętaj żeby przy weryfikacji podpisów, sprawdzać je z podpisami z odpowiedniego Release, nie z najnowszymi.

**Klucz publiczny**: [AndreansxTech_0x1A5C5CDB_public.asc](./AndreansxTech_0x1A5C5CDB_public.asc)

**Odcisk cyfrowy klucza**: 9282 DF55 1096 3273 6618  5B2E 4C80 939B 1A5C 5CDB

**Importowanie klucza (wiersz poleceń):**

```bash
gpg --import AndreansxTech_0x1A5C5CDB_public.asc
```
**Weryfikacja podpisów**
```bash
gpg --verify index.html.sig index.html
gpg --verify pannellum.css.sig pannellum.css
gpg --verify pannellum.js.sig pannellum.js
```
### Struktura projektu
```
Staszic360/
├── additional-media/
│   └── ...                               ( dodatkowe devnotes, ikonki, diagramy )
├── media/
│   └── ...                               ( folder z panoramami )
├── AndreansxTech_0x1A5C5CDB_public.asc - Klucz publiczny do weryfikacji podpisów
├── index.html                          - Główny plik HTML
├── index.html.sig                      - Podpis cyfrowy index.html
├── LICENSE                             - Plik licencji
├── pannellum.css                       - Arkusz stylów Pannellum.
├── pannellum.css.sig                   - Podpis cyfrowy pannellum.css
├── pannellum.js                        - Biblioteka Pannellum
├── pannellum.js.sig                    - Podpis cyfrowy panellum.js
└── README.md
```
### Stworzone z ❤️ przez Michała Bańkowskiego ( AndreansxTech ), Mateusza Długaja ( Matkard1 ) i Gabriela Świątka ( Simonaven265 ) 2025


## Ten projekt jest licencjonowany na podstawie **Licencji MIT** (sprawdź <a href="./LICENSE">LICENSE</a>)
