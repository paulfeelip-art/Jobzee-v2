# Switch

Comutatorul iOS pentru opțiuni pornit/oprit care se aplică imediat.

## Reguli

- 51 × 31 px, buton alb de 27 px. Oprit: `surface-3`. Pornit: `success` (verde, ca iOS), nu portocaliu.
- Stă la dreapta unui rând de listă; eticheta rândului spune ce pornește („Factură pe firmă”, „Sunt flexibil ± 1 h”).
- Tranziție `dur-state`. În app: `Switch` nativ cu `trackColor` din tokeni.
- Excepție: butonul mare ON/OFF de pe Acasă Jobzer nu e un Switch, e un buton rotund portocaliu cu halo.
