# IN104 - Rapport du projet Hanabi

Auteurs : https://github.com/Naiina/Christine_Quach_Nina_Gregorio_Hanabi

## Stratégie retenue
- Nous avons tout d'abord choisi de modifier l'IA Cheater en faisant en sorte qu'elle ne triche plus, puis nous avons apporte des ameliorations de strategie. Il a donc fallu modifier.... 
	- les classes playable/discardable/precious/mynotprecious/myprecious pour n'avoir que la liste des cartes que l'on connait.
	- modification du debut de partie pour jouer les premiers 1 
	- peut erte rajouter code ici

- Nous avons ensuite decide d'ameliorer notre IA non-tricheuse avec la strategie de Recommendation. Il a donc fallu ... 
	- modifier les clsses playable/discardable et precious ? 
	- peut etre faire une version qui inerprete lindice a son tour et une autre ou lindice est interprete au moment ou il est donne 


## Points techniques
 on pourrait ici parler de :
 	- expliquer le truc des listes et le chiffre direct pour reduire lecriture dans deduce_number et give_a_hint  
 	- le truc de trier les liste ca cest style hahah et tres preatique 
 	- etc ... 

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


### AI NotCheater
1)Faire tourner les not cheater et voir auil joue pas de ouf bien 
2)Mettre image
3)Suggestions de pourauoi il ne marche pas bien 

Le script `son_nom.py` lance l'AI 10000 fois.

Le score moyen obtenu est [...] ; pour comparaison le Cheater de l'article fait en moyenne 24.87.

Voici l'histogramme de nos résultats :
![Histogramme de l'AI Cheater](images/mon_histogramme.png)

à comparer avec celui (c) de l'article :
![Les 3 histogrammes de l'article](images/histogrames_hatstrat.png)



Important : pensez à analyser et discuter les différences entre vos résultats et l'article.
En particulier, si vous faites mieux ou moins bien, quelles en sont les raisons, et des pistes d'amélioration.
Les parties qui finissent à moins de 25 points sont aussi intéressantes à analyser.


### AI RecommendationStrategy en sauvegardant les indices apres
1) faire pareil ici 

### AI RecommendationStrategy en sauvegardant les indices avant 
1)pareeeil 

## Conclusion et perspectives

Parce qu'il est toujours bon d'aider son lecteur à retenir les points importants,
et lui donner des nouvelles pistes de réflexion.
