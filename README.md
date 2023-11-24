# TP Caching 

_Groupe:_ JOFFRE Mathis EONO Mathis

> L’objectif de cette série de TPs est d’explorer et de comparer les performances des politiques de mise en cache en mettant en œuvre la politique Min et la politique LRU, en utilisant la fonction Zipf pour générer des séquences de demandes.Le but est de calculer la probabilité de succès de chaque élément en utilisant ces politiques et éventuellement de vérifier les résultats en utilisant le modèle Che. Vous allez également visualiser vos résultats à travers des graphiques. La seconde partie du projet s’intéresse à l’analyse de la politique LRU, et sa comparaison à une politique Min. Les parties qui suivront analyseront les autres points.

# Installation

```
git clone 
```

# Usage

Simply run `python main.py [options]` and let's play with the Command Line Interface.

## CLI

```
Usage: python main.py [options]

    Options:
        -h, --help      Show this screen.
        -m, --min       Run the example simulation for the Min algorithm.
        -l, --lru       Run the example simulation for the LRU algorithm.
        -s, --simulate  Run the example simulation for both algorithms.
        -z, --zipf      Run the simulation for both algorithms with Zipf distribution. It will take a while.
        -zM, --zipf-min Run the simulation for the Min algorithm with Zipf distribution. It will take a while.
        -zL, --zipf-lru Run the simulation for the LRU algorithm with Zipf distribution. It will take a while.
```

# Rendu

Chaque fichier est commenté. Au dessus de chaque fonction et de chaque déclaration de classe il est indiqué l’objectif de celles-ci. Pour étudier la documentation de ce module, il suffit de lancer pydoc dans le répertoire contenant le code avec la commande suivante : `python -m pydoc -p 1234`

## Fichiers

- [`lru.py`](./lru.py): Il contient la définition de la classe `LRU`. C’est une classe qui définit les attendues de fonctionnement de l’algorithme  “Least Recently Used”.

- [`min.py`](./min.py): Il contient la définition de la classe `MIN`. C’est une classe qui définit les attendues de fonctionnement de l’algorithme “MIN policy”.

- [`cache.py`](./cache.py): Il contient la définition de la classe `Cache`. C’est ici qu’on définit ce qu’est un cache. Ce cache est le cache utilisé par les algorithmes LRU et MIN. Cela permet de reduire la redondance de code.

- [`algorithm.py`](./algorithm.py): Il contient la définition de la classe abstraite `Algorithm`. Il s’agit d’une classe abstraite qui représente ce qui est attendue d’un algorithme de caching.

- [`main.py`](./main.py): Il contient le code principal. Il permet de lancer les simulations et de visualiser les résultats.

- [`zipf.py`](./zipf.py): Il contient la définition de la classe `Zipf`. C’est une classe qui définit les attendues de fonctionnement de la distribution Zipf. (NB: cette classe est singleton)
