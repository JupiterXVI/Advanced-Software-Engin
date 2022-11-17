Spielesammlung
Überblick: <br/>
...

_______________________________________________________________________
Oberfläche: <br/>
pygame

_______________________________________________________________________
Setup: <br/>
Erstelle Virtaul Environment:
- Navegiere in Ordner "Code"
- > python -m venv env
- > .\env\Skripts\activate
- > pip install pygame
- > pip install psycopg2
<br/>
Datenbank: <br/>
postgresql - in docker container <br/>
<br/>
Funktionen welche die Datenbank benötigen können nur verwendet werden, <br/>
wenn der Docker-Container mit der Postgres-Datenbank läuft.
- Navigieren in den ProjektCode Ordner

- Erstellen des Containers:
  - docker build -t player_db .\docker\docker_postgresql\
- Starten des Containers:
  - docker run -d -p 5432:5432 --name player_db_conatiner player_db
- Beenden des Conteiners (falls nicht mehr nötig / Datenverlust):
  - docker stop player_db_conatiner
  - docker rm player_db_container
- Entferne Image:
  - docker image rm player_db

_______________________________________________________________________
Zusammenarbeit im GitHub: <br/>
!! Main bleibt eine lauffähige Version !! 
- Von main pullen:

  - git main pull
- Neuer Branch erstellen:
  - git checkout -b <name des Branches>
- Veröffentlichen auf GitHub:
  - git push --set-upstream origin <name der in GitHub steht>
- Änderungen Speichern und Hochladen
  - git add . && git commit -m "this is my change"
  - git push
- Wenn die Änderung Luffähig ist im Web per pull request mergen
