# IN104 - Rapport du projet Hanabi

-Auteurs : Quach Christine - Gregorio Nina
-lien githubb https://github.com/Naiina/Christine_Quach_Nina_Gregorio_Hanabi

## Stratégie retenue
-Nous avons d'abord créer un alogrithme qui joue de façon aléatoire afin d'apprivoiser le code.
- Puis nous avons tout d'abord choisi de modifier l'IA Cheater en faisant en sorte qu'elle ne triche plus.
Puis nous avons apporté des ameliorations de strategie. Il a donc fallu modifier:
	- les classes playable/discardable/precious/mynotprecious/myprecious pour n'avoir que la liste des cartes que l'on connait.
	- le debut de partie pour jouer les premiers 1 
	- jouer uniquement les cartes dont on est 100% surs

- Nous avons ensuite decidé d'ameliorer notre IA non-tricheuse avec la strategie de Recommendation détaillé dans l'article.
	
-Enfin, les indices n'étaient pas exploités au maximum. On a choisi d'indiquer également combien de joueurs peuvent jouer de façon simultanée afin d'obtimiser l'utilisation des indices


## Points techniques
 on pourrait ici parler de :
 	- expliquer le truc des listes et le chiffre direct pour reduire lecriture dans deduce_number et give_a_hint  
 	- le truc de trier les liste ca cest style hahah et tres preatique 
-Algo RecommendationStrategy
 	- ajout dans deck d'une liste mémoire afin que les joueurs puissent mémoriser au moment où est donné l'indice ce qu'ils doivent faire.
	- utilisation de sefl.game.moves pour déduir quel est le numéro du joueur en cours, combien de cartes ont éte jouées depuis le dernier indice, quel est le dernier indice donné.
	-des fonctions qui fond les conversions entre les indices en string du type "c1A" les indices en int entre 0 et 7 et ce qu'ils représentent pour le joueur dont c'est le tour en fonction de quand ils ont étés données, afin de ne pas se mélanger dans touuus ces indices différents
	-un fichier pour lancer le jeu en uneligne de commende au lieu de 4
-Algo RecommendationStrategy_3
	-une liste qui tient compte du nombre de joueurs pouvant jouer d'affilé pour optimiser l'algo précédent (nécéssité de modifier la maorité des fonctions en conséquence)

```python
    def add_blue_coin(self):
        if self.blue_coins == 8:
            raise ValueError("Already 8 blue coins. Can't get an extra one.")
        self.blue_coins += 1

```


## Tests unitaires ou de non-régression

Présentez quelques (disons 2) tests unitaires.
Dans l'idéal, pour celles et ceux qui sont tombés sur un (gros) bug qui leur a pris du temps, il devrait y avoir un test unitaire qui protège contre sa réapparition.

Exemple :

- Le test `game_42.py` replace la partie dans une situation où l'AI est obligée de défausser une carte précieuse ; je veux garantir que c'est le 5 vert parce que celle celui qui fait perdre le moins de points.

- Le test `fin_de_partie.py` vérifie que les noms des joueurs sont les bons sur le dernier tour de jeu, parce que dans [telle situation...] ça n'avait pas été le cas.



## Tests en série - statistiques - analyse des résultats

Le script `plot_games.py` lance les AI 10000 fois.

 ### Random and NotCheater AI






![Histogramme de l'AI NotCheater](images/NotCheater_10000.png)


![Les 3 histogrammes de l'AI Random](images/Random_10000.png)
Le score moyen obtenu est de 1.97 pour le NotCheater et de 1.26 pour le Random ce qui est evidament peu satisfaisant. L'algorithme NotCheater dans des indices sans forcément tenter de compltéter des demi-indices ce qui explique que peu de joueurs ont assez d'informations pour poser une carte. Il consomme de plus beaucoup d'indices ce qui oblige les joueurs a jetter souvent; Jettant à l'aveugle le jeu est rapidement bolqué. 

### AI RecommendationStrategy en sauvegardant les indices apres

![Histogramme de l'AI RecommendationStrategy](images/RecommendationStrategy_10000.png)
Le score moyen est de 21.20, ce qui est étonnant car l'article atteind 23. Il nous semble pourtant avoir suivi les instruction précises du document. 

### AI RecommendationStrategy en sauvegardant les indices avant 
![Histogramme de l'AI RecommendationStrategy_3](images/RecommendationStrategy_3)
Le score moyen est de 23.17, ce qui est un peu suppérieur à l'article. Pourtant certains jeux se terminent avec un score iférieur à 15 ce qui n'était pas observé pour l'algo précédent. Certaines cartes sont certainement jetée de façon non optimales et bloquent le jeu. 

## Conclusion et perspectives

Parce qu'il est toujours bon d'aider son lecteur à retenir les points importants,
et lui donner des nouvelles pistes de réflexion.    

Il serait intéréssant de pouvoir indicer au joueurs suivant le premier joueur qui pose une carte, de jouer par dessus celle ci si cela est possible, sans avoir besoin d'un indice suplémentaire.    
Par exemple:    
Benji: B1 W5 ...    
Clara: B1 B2 ...    
si benji pose son B1 clara aurait intérêt a poser le B2 et non le B1 qui est pourtant indicé d'après l'ordre des priorités actelles. Avec les indices 5 restant on pourrait peut-etre indiquer aux joueurs qui peuvent jouer s'ils doivent prendre en compte leur première ou leur deuxième carte par ordre de priorité
En poussant le raisonnement plus loin on pourrait essayer d'optimiser chaque indice afin qu'il permette au plus de joueurs de jouer d'affilé. par exemple:   
Alice: B1 R1    
Benji: R2..    
on indicerait plutôt a alice de jouer son R1 qui son B1, ie elle jouerait sa carte de priorité 2 et benji la première.
