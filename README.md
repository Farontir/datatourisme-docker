# Environnement full-stack Docker

## Utilisation



Le fichier ainsi obtenu doit être copié dans le répertoire `dataset/kb/data` pour être chargé dans la base de
données lors de la création du conteneur Docker.

Vous pouvez maintenant lancer l'environnement :

```
$ docker-compose up
```

### Mise à jour des données

Lorsque vous souhaitez mettre à jour les données de votre environnement, vous devez procéder ainsi :

1. Stoppez l'environnement s'il est actif : `docker-compose stop`
1. Téléchargez le nouveau fichier de donnée et remplacez le dans **dataset/kb/data**
2. Supprimez le conteneur Blazegraph : `docker-compose rm blazegraph`
3. Relancez l'environnement : `docker-compose up`

