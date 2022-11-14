Spielesammlung
Überblick:
...
_______________________________________________________________________
Oberfläche:
pygame

_______________________________________________________________________
Datenbank:
postgresql - in docker container

Funktionen welche die Datenbank benötigen können nur verwendet werden,
wenn der Docker-Container mit der Postgres-Datenbank läuft.
-> Navigieren in den ProjektCode Ordner 
- Erstellen des Containers:
  docker build -t player_db .\docker\docker_postgresql\

- Starten des Containers:
  docker run -d -p 5432:5432 --name player_db_conatiner player_db

- Beenden des Conteiners (falls nicht mehr nötig / Datenverlust):
  docker stop player_db_conatiner
  docker rm player_db_container
  
- Entferne Image:
  docker image rm player_db
