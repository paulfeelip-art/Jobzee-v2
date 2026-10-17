# RoleSwitch

Selectorul „Rol activ” din Cont: arată rolul curent (Client sau Jobzer) și deschide foaia Schimbă rolul.

## Reguli

- Stă în cardul de profil, sub nume. Rolul activ are pastila albă cu umbră.
- Atingerea oriunde deschide foaia cu comutatorul mare (2 opțiuni, pastila glisează în 500 ms cu `ease-spring`).
- Prima trecere la Jobzer cere activarea (identitate obligatorie; restul mai târziu). Revenirea la client e instantă.
- Același cont, aceleași date: se schimbă doar meniul și ecranul Acasă.
