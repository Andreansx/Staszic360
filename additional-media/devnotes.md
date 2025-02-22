## Ten plik zawiera notatki dla deweloperów

## Diagramy blokowe
![Block diagram](../additional-media/block-diagram.drawio.png)

### Zdjęcia i ich obróbka
Specyfikacja sprzętu:
Kamera: Samsung Gear360 ( nie ta wersja z 2017 roku ) model CM-200
- Rozmiar zdjęcia: 7776x3888 px
- Typowa waga zdjęcia surowego zdjęcia to od ok. 5 MB do ok. 8 MB
- 350 dpi
- 24 bity
- 1.2mm
- f/2
- 1/100s
- ISO zazwyczaj około 100-120
- Przeróżne światło, ciężko było zaplanować robienie zdjęć tak aby były idealne warunki za każdym razem</br>

Zdjęcia na karcie SDXC w kamerze są w 100% surowe, nie podlegały żadnej obróbce. Po pobraniu zdjęcia na telefon ( Samsung Galaxy S8 ) zdjęcia ulegają, bezstratnemu pod względem jakości, połączeniu dwóch zdjęć ( Double fish eye ) aby przejść do equiractangular po to żeby Panellum.js mogło je w ten sposób przerobić w zdjęcie sferyczne. Można również te zdjęcia brać bezpośrednio z karty SDXC i zamienić je ( być może jeszcze bardziej bezstratnie ) do odpowiedniego zdjęcia panoramicznego. Tak więc zdjęcia w folderze <a href="../media/">media</a> podległy jedynie najbardziej jak to możliwe połączeniu dwóch obrazów typu *fish-eye* do *panoramic* 
