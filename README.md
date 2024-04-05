# OpenClassrooms: Projet 4: Chess Tournament

## Contexte et introduction

<br>

**Développez un programme logiciel en Python** est le 4ème projet de [l'école OpenClassroom](https://openclassrooms.com/fr). Il consiste à réaliser un gestionnaire de tournois d'échecs.
Ce gestionnaire permet : à travers un menu textuel dans le terminal, créer une liste de joueur, créer un tournois, sauvegarder la donnée générée et s'en servir pour éditer des rapports.
Dans ce projet nous utilisons l'architecture MVC pour séparer les différentes parties de l'application en modules disctincts.

<br>

<br>

## Arborescence du projet

Trouvez ci-dessous l'organisation du projet.
<br>

```bash
.
├── controllers                     # Dossier où se trouvent les logiques de contrôle et les interactions entre models et views.
│   └── menu.py                    
│   └── reports.py                  
│   └── tournament.py  
├── models                          # Dossier où sont définies les différentes entités avec la logique métier correspondante.
│   └── player.py                   
│   └── round.py                    
│   └── tournament.py
├── views                           # Dossier où se trouvent les différents fichiers de gestion d'interface utilisateur
│   └── menu.py
│   └── reports.py 
│   └── round.py
├── data                           # Dossier data où l'on peut retrouver toute la donnée sauvegardée dans des fichiers json pendant l'exécution du programme 
│   └── players.json  
│   └── tournaments.json 
├── main.py                        # Fichier main destiné a lancer le programme
├── flake-report                   
└── requirements.txt               # répertorie toutes les librairies et modules nécessaires à l'exécution du programme 
```
<br>

# Lancement du projet

<br>

Pour lancer le programme veuillez suivre les étapes suivantes :

<br>

Installer Python. Ouvrir le terminal, se placer dans le dossier de votre choix et cloner le projet dans ce dossier:

```bash
git clone https://github.com/Jbguerin13/chess-tournament.git
```

Se placer dans le dossier **projet_chess_tournament**, puis créer un nouvel environnement virtuel et l'activer :

```bash
python -m venv nom_env
source nom_env/bin/activate
```

Il ne reste plus qu'à installer les dépendances requises pour faire fonctionner le programme :

```bash
pip install -r requirements.txt
```

Lancez le programme en appelant la commande suivante :

```bash
python main.py
```

<br>

# Navigation dans le menu

<br>

Une fois le programme lancé via le fichier main.py, vous avez devant vous le premier menu. Vous pouvez d'ores et déjà rentrer les données de vos joueurs, créer votre tournois et éditer des rapports. Vous pouvez modifier les informations de vos joueurs et également revenir dans un tournois qui aurait été stoppé avant la fin.

<br>

## Créer vos joueurs

<br>

Vous pouvez créer vos joueurs en rentrant toutes les information nécessaires demandées par le programme. N'oubliez pas de sauvegarder ! Vous pouvez retrouver les informations sauvegardées dans le fichier players.json

<br>

## Créer votre tournois

<br>

Vous pouvez créer votre premier tournois en rentrant toutes les information nécessaires demandées par le programme. Il faut 8 joueurs dans votre base de données pour faire fonctionner le tournois. N'oubliez pas de sauvegarder ! Vous pouvez retrouver les informations sauvegardées dans le fichier tournaments.json

<br>

## Editer un rapport

<br>

Il vous faut des données déjà des données sauvegarder dans le dossier data pour pouvoir éditer un rapport. Sans celaa le programme renverra une erreur.
La partie rapport va piocher dans le dossier data et va trier les informations en fonction de votre choix. Vous pouvez faire un rapport
de tous les joueurs sauvegardés, de tous les tournois et du détail des rounds et des matches de chaque tournois.

<br>
