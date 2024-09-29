# ML_OPS

# Prévision de prix de logement

## Introduction

Notre projet

a pour objectif de fournir un modèle de machine learning opérationnel permettant de prédire les prix de l'immobilier à partir de diverses caractéristiques des logements. Ce projet se concentre sur l'aspect opérationnel, en facilitant l'accès aux utilisateurs via une API REST, qui permet d'effectuer des requêtes de prédiction en temps réel.

Nous avons mis en place des outils de monitoring pour suivre les performances du modèle, ainsi qu'un système d'alerting pour détecter d'éventuels problèmes. Cela garantit une utilisation efficace et fiable du modèle par d'autres utilisateurs.

## Installation

Instructions pour installer les dépendances et cloner le dépôt.

```bash
# Cloner le dépôt
git clone https://github.com/Dixtawi/ML_OPS
cd ML_OPS

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation de l'API

Instruction pour lancer et utiliser l'API :

```
make run
```

Rendez-vous sur le lien "https://votre_ip:5000". Ce lien est la dernière ligne affichée lorsque vous effectuez "make run".

Une fois sur le site, vous pouvez entrer les informations du logement dans le formulaire pour avoir une prédiction du prix de vente.

## **Données**

Le dataset utilisé dans ce projet provient de [Kaggle](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset) et contient des informations détaillées sur les prix de logements ainsi que sur diverses caractéristiques de ces logements. Ce dataset a été choisi en raison de sa richesse et de sa pertinence pour la tâche de prévision des prix.

### Description du Dataset :

* **Format** : CSV
* **Nombre d'Entrées** : 545
* **Nombre de Caractéristiques** : 12

### Caractéristiques Principales :

Les caractéristiques incluses dans le dataset comprennent :

* **Surface** : La superficie du logement en pieds carrés.
* **Chambres** : Le nombre de chambres dans le logement.
* **Salles de Bain** : Le nombre de salles de bain dans le logement.
* **Etages** : Le nombre d'étages du logement.
* **Route Principale** : Si le logement est connectée à la route principale.
* **Chambre d'ami** : Si le logement possède une chambre d'ami.
* **Sous-sol** : Si le logement possède un sous-sol.
* **Chauffe d'eau** : Si le logement possède un chauffe-eau.
* **Air conditionné** : Si le logement possède l'ai conditionné.
* **Parking** : Le nombre de places de parking que possède le logement.
* **Préfabriqué** : Si le logement possède un préfabriqué
* **Ameublement** : Peut être fourni, semi fourni, ou pas du tout

## Modèle

Dans ce projet, nous avons utilisé le modèle Gradient Boosting. Ce modèle a été choisi en raison de sa capacité à capturer des relations complexes dans les données et à fournir des prédictions précises.

### Détail du Modèle

Type de Modèle : Gradient Boosting
Objectif : Prévoir les prix de logement en fonction de caractéristiques spécifiques (surface, nombre de chambres, localisation, etc.).

### Evaluation des performances

Les performances du modèle ont été évaluées à l'aide de métriques telles que :

Erreur Absolue Moyenne (MAE) : Le score mesure l'erreur moyenne des prédictions.
Coefficient de Détermination (R²) : Le score indique la proportion de variance des prix de logement expliquée par le modèle.
