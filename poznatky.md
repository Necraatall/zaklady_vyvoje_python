# Poznatky

## Extensiony ve VSCODE:

Nainstalovano:

- Code Spell Checker
- Python
- Jupyter
- Intellicode (napovidani syntaxe)

## Python

- `argparse` - parsuje argumenty z prikazoveho radku

### Nainstalovane knihovny

Jsou instalovane v globalnim repository abych je mohl pouzivat. 
Tzn. v knihovnach Pythonu. 
`pip3 install jupyterlab`

- `jupyterlab` - kompletni server pro jupyter, spust z prikazove radky pomoci `jupyter lab` (da se pouzit k tvorbe jupyter notebooku)
- `ipython` - Interaktivni prikazovy radek pro Python s napovedou a zvyraznovanim syntaxe, spustit pomoci `ipython`
    - syntaxe `_cislo` muze byt pouzito k reference vysledku, treba: `_1`

- `pandas` je knihovna k praci a analyze dat (import csv, export to db...)
    - za pomoci knihovny `requests` si mohu vytahnout html ze stranek a pandas vyzere data

- `beautifulsoup4` - https://pypi.org/project/beautifulsoup4/ - veme element a printne... napriklad - pro delani Xpathu
- `scapy` - pro manipulaci s packetama https://pypi.org/project/scapy/


### Virtualni prostredi s knihovny instalovanymi pro projekt

samostatne oddelene od mych knihoven
`pipenv install requests`
`pipenv run python module` - `https://pypi.org/project/pipenv/`

- `pipenv` - pro tvorbu a pouzivani virtualnich prostredi
- `requests` - instalace `pipenv install requests` nainstaluje do virtualu knihovnu pro praci s REST, HTML...

- `gooey` - z programu pracujicich v bashi, udela gui apku
- `sqlalchemy` - umoznuje pristup ke vsem druhum sql databazi jako k objektum - dokumentace https://www.sqlalchemy.org/docs/
- `django` - slouzi k vytvareni webovych api ktere potrebuji neco jako spravu uctu a pod., napul redakcni system
- `flask` - pro vytvareni rest https://pypi.org/project/Flask/
- `fastapi` - pro vytvareni rest -ma + automaticky generuje swagger
            - `pipenv install fastapi`
            - koukni na stranky
            - `pipenv install "uvicorn[standard]" --dev`
                - --dev development dependency neni v projektu, kdo si zkopne kod si to musi pustit
                - napriklad chci pouzivat nose2 abych si neco otestoval, ale zakaznikovi to nechci posilat
            - `pipenv uvicorn main:app --reload`
            - dojdi na url co ti teminal ukaze
            - dojdi na url vyse a dej za adresu /docs
                    - bere z komentaru documentaci
            - schemata a pod na: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
            - https://fastapi.tiangolo.com/tutorial/
- `pywebio` - vytvori webovej kontext - vcetne funkcnich a interaktivnich prvku
- `mkdocs`  - pro tvorbu dokumentace https://pypi.org/project/mkdocs/ 
- `textblob`- parsuje text, spellcheck, co je podst jmeno... dokaze pluralizovat - mnozne cislo 
- `pipenv pelican content` vytvori blog spusti se
    - spustim vizualizaci v do browseru
    - `python3 -m http.server` 
    -    `pipenv run pelican content`

### Tipy pro Python radek

Pro vylistovani vsech modulu, pouzijte nasledujici kod v Pythonu:
 
```py
help("modules")
```

Pokud chcete vice informaci ohledne nejakeho modulu, tak pouzijte opet help:

```py
help("textwrap")
```

### Hledani novych knihoven

Nove knihovny se daji najit na strance https://pypi.org

Na teto strance se da najit i dokumentace k temto knihovnam.

Knihovny standartne existujici v Pythonu maji dokumentaci a priklady pouziti primo na strankach https://www.python.org

### Vytvareni exe souboru

Extra knihovny jako `pyinstaller` nebo `py2exe` se na toto daji pouzit.

### Nose2

Lepsi knihovna pro testovani a vytvareni unitovych a jinych testu, podporuje nekolik vystupnich formatu.

1. vytvoreni folderu pro testy
2. vytvoreni file counting.py
3. vytvoreni file test_counting.py
4. ... atd.
5. klik ve VS Code na Testing
6. dopsani testu
7. run nose2

- `unittest` - viz folder tests, counting.py
- `counting` - modul co jsme si udelali counting.py
- `parameterized` - knihovna https://pypi.org/project/parameterized/
    - > pipenv install parameterized --dev
- `nose2` 
    - > pipenv install nose2 --dev
    - > pipenv run nose2 -v

### K api ci webowce potrebuji jen

- fastapi
- sqlalchemy

#
# Hlavni titulek - navod na psani v Markdown

## podtitulek

###### atd sdfsdfsdf

```py
print(kod)
```

> blokova hlaska

[odkaz](https://www.google.com) nebo https://www.google.com

*kurziva*

**Tucne**

~preskrknuto~

`dalsi moznost` zobrazeni

####lze i psat html tagy

<ins>test<ins>

<b style="color:Tomato;">Barvy</b>

#

| jmeno | prijmeni | vek |
|-------|----------|-----|
| John  | Doe      | 35  |
| John  | Bee      | 25  |

#

![Tohle je target](https://img.superzoo.cz/img_1577712441/school_article/406.jpg)

#

- odrazkovy seznam
- seznam 
    - vcetne pod-odrazek

1. cislovany seznam
2. etc.
    1. daji se pouzit i pododrazky

Jiny seznam

1. jiny typ cislovaneho seznamu 
1. s dalsi odrazkou

#

# yUML extension pro VS Code

generuje uml - extension do VS Code
- stahni si extensionu
- vytvor si file xxx.yuml
- clickni do file xxx.yuml
- ctrl + space
- vyber si diagram z nabidky - zacinaji ctvereckem
- vytvor si splitscreen na vs code (split editor right)
- view by se melo otevrit
- koukni na: diagram.yuml

# pyreverse

- pracuje s Class, vetsinou jsou TC jako Classy
- .dot vystup se pouziva
- da se do obrazku
- soucasti `Linteru`: `Pylint` 
    - `Pylint` do pippenv - https://pipi.org

#
# Lintery
# Pylint

- na souboru s kodem pro test
- VS Code F1
- Select Linter
- pokud nemam, nainstaluje to do pipenv  

### Test
- na souboru s kodem pro test
- VS Code F1
- Select Python: Run Lintering
- najdi vlnovku modrou a oprav chyby

### Setup Pylint

- vygeneruji si setup file `rcfile` pro Linter
    > pipenv run pylint --generate-rcfile > .pylintrc
    - u powershellu:
        > pipenv run pylint --generate-rcfile > .pylintrc | Out-File -Encoding utf8 .pylintrc
#
- pycodestyle - radi jak kod zformatovat z nudle na vicero radku
- flake8 - kontroluje kod podle standartu PEP8 (konvence psani - Pylint to ma v sobe)
- > ### <ins>__*`mypy` - pro staticke typovani - resi parametry a jejich datove typy a spravnost vystupu*__<ins>


#
# Emmetove snippety Vs Code


# HTML - rychlej generator

- >`!` 
    - nabidlo mi Emetovy snippet

- generovani elementi emetem
    - https://code.visualstudio.com/docs/editor/emmet


#
# VS Code

### `multicursor` 
    1. levej alt + click
    2. ctrl + alt plus mackat sipku dolu

### `porovnani 2 souboru jako win merge`

1. right click na prvni soubor
2. select for Compare
3. right click na druhy soubor
4. Compare with selected
#### `prirustek`
1. click na menu vedle tabu otevrenych souboru `...`
2. Inline view


#
# Priste

- `GIT`
- `django`
- `Docker`
#
### `Ve volnem casu`
- (`Kubernetes`)
- `Jenkins`
- `AWS` 
- `hooky` - sample

#
# Hooky

musim mit git init abych mel repositary
- > sudo apt install git
- > git init
#
1. klikni na vs.code folder
2. settings.json
3. pridam si sekci 
    - > "files.exclude": {
        "**/.git": false,
    }
4. objevi se slozka git v ni je slozka hooks a tam jsou priklady
#
