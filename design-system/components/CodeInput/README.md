# CodeInput

Câmpurile pentru coduri de 4 cifre: codul SMS la autentificare și codul de start pe care Jobzerul îl cere clientului.

## Stări

- Gol / completat: celule `surface`, 72 px înălțime, `radius-md`, cifre 30 px bold tabulare.
- Activ: contur 2 px `brand` cu puls ușor.
- Eroare: contur `danger`, cifre `danger-text`, tot rândul tremură 500 ms; dedesubt mesajul cu încercările rămase. După 3 greșeli: blocat 10 minute.

## Reguli

- Tastatură numerică, completare automată din SMS (`textContentType="oneTimeCode"` pe iOS).
- Codul de start îl vede doar clientul; la client se afișează mare, cu spațiere 8 px (`numeral-code`), nu în câmpuri.
