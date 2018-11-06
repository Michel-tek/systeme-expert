# Système expert

### Info

Vous aurez besoin du package Pmw pour lancer le programme (gestion du comboBox dans l'interface graphique)

	pip install Pmw

## Lancement du programme

	./main.py
### Chainage avant
Si vous voulez tester avec le chainage avant : 

	- cliquez sur "chargement des fichiers",
	- puis selectionnez "avant",
	- vous pouvez éventuellement choisir un but dans la liste,
	- cliquez sur "lancement du moteur".
### Chainge arrière
Si vous voulez tester avec le chainage arrière : 
	
	- changez le texte "faits_chien_avant.xml" par "faits_chien_arriere.xml" *,
	- cliquez sur "chargement des fichiers",
	- puis selectionnez "arrière",
	- vous devez choisir un but dans la liste,
	- cliquez sur "lancement du moteur".

*(en principe le moteur fonctionne aussi avec le 1er fichier mais vous pourrez faire plus d'itérations avec le fichier "faits_chien_arriere.xml")

### Cohérence
Pour tester la gestion de la cohérence vous pouvez ajouter le prédicat :
	
	<predicat nom="l'humeur du chien" operateur="=" valeur="triste"/>

à la liste des faits de base dans l'un ou l'autre des fichiers "fait_*.xml"

## Le projet

Ce projet est divisé en 3 parties principales :

	- la gestion des fichiers xml,
	- le moteur,
	- l'interface graphique.

### Les fichiers xml

#### Faits

Représentation :

	<faits>
		<predicat nom="le temps" operateur="=" valeur="soleil"/>
		<predicat nom="la couleur de la balle" operateur="=" valeur="bleue"/>
		<predicat nom="le facteur arrive"/>
	</faits>

Un prédicat est constitué obligatoirement d'un nom et éventuellement d'un opérateur et d'une valeur

#### Règles

Représentation :

	<regles>
		<regle>
			<conditions>
				<predicat nom="le temps" operateur="=" valeur="soleil"/>
			</conditions>
			<conclusion>
				<predicat nom="le chien peut sortir de la maison"/>
			</conclusion>
		</regle>
		<coherences>
			<coherence>
				<predicat nom="le temps" operateur="=" valeur="soleil"/>
				<predicat nom="le temps" operateur="=" valeur="pluie"/>
			</coherence>
		</coherences>
	</regles>

Les règles sont constituées de :

	- une ou plusieurs conditions,
	- une conclusion représentée par un prédicat.

La gestion des incohérences est ajoutée entre les balises "coherences" chaque bloc "coherence" est constitué de prédicats qui ne peuvent pas avoir lieu en même temps.

La relation entre chaque prédicat dans les conditons est le ET, pour créer un OU il vous faudra créer une seconde règle avec la même conclusion.

## Le moteur

Le moteur est généré par la fonction "creation_moteur" de xml_reader qui demande en paramètre le nom d'un fichier xml comportant les règles (dans le projet vous pouvez utiliser le fichier "regles_chien.xml")

### Chainage avant

Le chainage avant correspond à la fonction "chainage_avant" du moteur qui demande une liste de faits de départ et éventuellement un but (le but doit être de type Predicat (de moteur.py) et non simplement une chaine de caractère).

Vous pouvez utiliser le fichier "faits_chien_avant.xml" pour tester que vous chargerez avec la fonction "recuperation_des_faits" de xml_reader.

La fonction "chainage_avant" modifie la liste de faits passée en paramètre et  renvoie une string résumant le déroulement du chainage avant.

### Chainage arrière

Le fonctionnement est le même que pour le chainage avant, la fonction à utiliser est "chainage_arriere" en revanche vous devez renseigner un but lors de l'appel.

Vous pouvez utiliser le fichier "faits_chien_arriere.xml" pour tester.

## L'interface graphique

L'interface graphique, généree en grande partie avec PAGE (http://page.sourceforge.net/), affiche les règles et les faits après les avoir renseigné dans les champs correspondant et avoir cliqué sur "chargement des fichiers".

Vous devez ensuite choisir entre chainage avant ou arrière et renseigner un but, le clic sur Lancement du moteur gérera l'execution de celui ci et affichera le déroulement de l'algorithme sur la gauche et les faits sur la droite
