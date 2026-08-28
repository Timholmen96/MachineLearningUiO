# Oppskrift: Nytt Python-prosjekt i VS Code med venv, Git og GitHub

Denne oppskriften lager en ryddig Python-prosjektstruktur med:

-   Python virtuelt miljø (`.venv`)
-   `requirements.txt`
-   `.gitignore`
-   lokalt Git-repository
-   første commit
-   GitHub-repository
-   kobling mellom lokal Git og GitHub
-   første `git push`

> Hovedregel: Én `.venv` per prosjekt -- ikke én `.venv` per Python-fil.

------------------------------------------------------------------------

## 1. Opprett prosjektmappen

Gå til mappen der du vil lagre Python-prosjektene dine:

``` bash
cd ~/Python
```

Opprett prosjektet:

``` bash
mkdir mittprosjekt
cd mittprosjekt
```

Sjekk at du står riktig:

``` bash
pwd
```

Åpne prosjektet i VS code 
``` bash
code
```
------------------------------------------------------------------------

## 2. Opprett virtuelt Python-miljø

Lag `.venv`:

``` bash
python3 -m venv .venv
```

Aktiver miljøet:

``` bash
source .venv/bin/activate
```

Terminalen skal nå begynne med noe som:

``` text
(.venv)
```

Kontroller hvilken Python som brukes:

``` bash
which python
```

Du bør få en sti som ligner:

``` text
/Users/DITTNAVN/Python/mittprosjekt/.venv/bin/python
```

Sjekk versjonen:

``` bash
python --version
```

------------------------------------------------------------------------

## 3. Oppgrader pip

``` bash
python -m pip install --upgrade pip
```

------------------------------------------------------------------------

## 4. Installer prosjektets Python-pakker

Installer bare pakkene prosjektet faktisk trenger.

Eksempel:

``` bash
python -m pip install numpy matplotlib
```

Sjekk installerte pakker:

``` bash
python -m pip list
```

------------------------------------------------------------------------

## 5. Opprett `requirements.txt`

Når prosjektets avhengigheter er installert:

``` bash
python -m pip freeze > requirements.txt
```

Se innholdet:

``` bash
cat requirements.txt
```

Dette lager en liste over de installerte pakkene og versjonene.

På en annen maskin kan miljøet senere gjenskapes med:

``` bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## 6. Opprett `.gitignore`

Lag filen:

``` text
.gitignore
```

I filen skriver du:

``` text
.venv/
```

Dette forteller Git at hele `.venv`-mappen skal ignoreres.

Ettersom prosjektet vokser kan `.gitignore` utvides. For eksempel:

``` text
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.DS_Store
```

------------------------------------------------------------------------

## 7. Opprett prosjektets første Python-fil

For eksempel:

``` text
main.py
```

Test at Python fungerer:

``` python
print("Hei fra Python!")
```

Kjør:

``` bash
python main.py
```

------------------------------------------------------------------------

## 8. Åpne prosjektet i VS Code

Fra prosjektmappen:

``` bash
code .
```

I VS Code:

1.  Åpne Command Palette med `⌘ + Shift + P`
2.  Søk etter `Python: Select Interpreter`
3.  Velg prosjektets: `Python 3.x.x ('.venv': venv)`

Kontroller at VS Code bruker `.venv`.

------------------------------------------------------------------------

## 9. Opprett lokalt Git-repository

Fra prosjektmappen:

``` bash
git init
```

Bytt hovedbranch fra `master` til `main`:

``` bash
git branch -m main
```

------------------------------------------------------------------------

## 10. Kontroller at `.gitignore` fungerer

``` bash
git status
```

Du skal se prosjektfilene, for eksempel:

``` text
.gitignore
main.py
requirements.txt
```

Du skal IKKE se:

``` text
.venv/
```

Hvis `.venv` ikke vises, fungerer `.gitignore`.

------------------------------------------------------------------------

## 11. Lag første commit

Legg prosjektfilene i staging:

``` bash
git add .
```

Kontroller:

``` bash
git status
```

Lag commit:

``` bash
git commit -m "Initial commit"
```

Kontroller:

``` bash
git status
```

Ideelt resultat:

``` text
On branch main
nothing to commit, working tree clean
```

Se historikken:

``` bash
git log --oneline
```

------------------------------------------------------------------------

# 12. Opprett repository på GitHub

Gå til:

https://github.com

Velg:

**+ → New repository**

Bruk for eksempel:

``` text
Repository name: mittprosjekt
Visibility: Private
```

Når prosjektet allerede finnes lokalt, skal du IKKE velge:

-   Add a README file
-   Add .gitignore
-   Choose a license

Repositoryet på GitHub skal være tomt.

------------------------------------------------------------------------

## 13. Koble lokalt Git-repository til GitHub

På GitHub får du en repository-adresse som ligner:

``` text
https://github.com/DITTBRUKERNAVN/mittprosjekt.git
```

Fra terminalen i prosjektmappen:

``` bash
git remote add origin https://github.com/DITTBRUKERNAVN/mittprosjekt.git
```

Kontroller:

``` bash
git remote -v
```

Du bør se:

``` text
origin  https://github.com/DITTBRUKERNAVN/mittprosjekt (fetch)
origin  https://github.com/DITTBRUKERNAVN/mittprosjekt (push)
```

------------------------------------------------------------------------

## 14. Push prosjektet til GitHub

``` bash
git push -u origin main
```

Etter dette følger den lokale `main`-branchen GitHub sin `origin/main`.

Fremover holder det vanligvis med:

``` bash
git push
```

------------------------------------------------------------------------

# 15. Den daglige arbeidsflyten

Når prosjektet allerede er satt opp, trenger du vanligvis ikke gjøre alt
over igjen.

Arbeidsflyten er:

``` text
Skriv kode
   ↓
Test koden
   ↓
git status
   ↓
git diff
   ↓
git add .
   ↓
git commit -m "Beskriv endringen"
   ↓
git push
```

Eksempel:

``` bash
git status
git diff
git add .
git commit -m "Add image preprocessing"
git push
```

------------------------------------------------------------------------

# 16. Viktige Git-kommandoer

## Se hva som er endret

``` bash
git status
```

## Se nøyaktig hva som er endret

``` bash
git diff
```

## Legg alle ikke-ignorerte endringer i staging

``` bash
git add .
```

## Lag commit

``` bash
git commit -m "Beskrivelse av endringen"
```

## Send commits til GitHub

``` bash
git push
```

## Hent endringer fra GitHub

``` bash
git pull
```

## Se commit-historikken

``` bash
git log --oneline
```

## Se hvor GitHub-repositoryet ligger

``` bash
git remote -v
```

------------------------------------------------------------------------

# 17. Viktig forskjell mellom Git og GitHub

**Git** er versjonskontrollen som kjører lokalt på Mac-en.

**GitHub** er en nettjeneste hvor Git-repositoryet kan lagres og deles.

Derfor:

``` text
Mac
│
├── prosjektfiler
├── .venv
└── .git
      │
      │ git push
      ▼
   GitHub
```

`git commit` lagrer historikken lokalt.

`git push` sender historikken til GitHub.

------------------------------------------------------------------------

# 18. Hva skal og skal ikke være i Git?

Typisk:

``` text
mittprosjekt/
├── .gitignore          ✅ Git
├── main.py             ✅ Git
├── requirements.txt    ✅ Git
├── README.md           ✅ Git
├── src/                ✅ Git
├── tests/              ✅ Git
└── .venv/              ❌ Ikke Git
```

`.venv` skal normalt ikke pushes til GitHub.

Den kan alltid opprettes på nytt fra `requirements.txt`.

------------------------------------------------------------------------

# 19. Starte et eksisterende prosjekt på nytt på en annen Mac

Hvis prosjektet allerede ligger på GitHub:

``` bash
git clone https://github.com/DITTBRUKERNAVN/mittprosjekt.git
cd mittprosjekt
```

Opprett nytt virtuelt miljø:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Installer avhengighetene:

``` bash
python -m pip install -r requirements.txt
```

Åpne i VS Code:

``` bash
code .
```

Velg `.venv` som Python-interpreter.

Da har du i praksis gjenskapt utviklingsmiljøet.

------------------------------------------------------------------------

# 20. Kort huskeliste

Når du starter et HELT NYTT prosjekt:

``` bash
cd ~/Python
mkdir mittprosjekt
cd mittprosjekt

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install numpy matplotlib

python -m pip freeze > requirements.txt
```

Lag `.gitignore`:

``` text
.venv/
```

Initialiser Git:

``` bash
git init
git branch -m main
git add .
git commit -m "Initial commit"
```

Opprett et tomt repository på GitHub og koble det:

``` bash
git remote add origin https://github.com/DITTBRUKERNAVN/mittprosjekt.git
git push -u origin main
```

Ferdig.

------------------------------------------------------------------------

# Den viktigste regelen

**Ikke tenk på `.venv` som en del av selve koden.**

Tenk:

``` text
Prosjekt
│
├── Kode              → Git/GitHub
├── Data/config       → etter behov
├── requirements.txt  → Git/GitHub
├── .gitignore        → Git/GitHub
└── .venv             → lokal maskin
```

Én `.venv` per prosjekt. Mange `.py`-filer kan bruke samme `.venv`.
