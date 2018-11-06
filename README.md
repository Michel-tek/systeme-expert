# Système expert

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

	<regle>
		<conditions>
			<predicat nom="le temps" operateur="=" valeur="soleil"/>
		</conditions>
		<conclusion>
			<predicat nom="le chien peut sortir de la maison"/>
		</conclusion>
	</regle>

Les règles sont constituées de :
	- une ou plusieurs conditions
		- la relation entre chaque prédicat dans les conditons est le ET, pour créer un OU il vous faudra créer une seconde règle avec la même conclusion.
	- une conclusion représentée par un prédicat
	
## Le moteur

Le moteur est généré par la fonction "creation_moteur" de xml_reader qui demande en paramètre le nom d'un fichier xml comportant les règles (dans le projet vous pouvez utiliser le fichier "regles_chien.xml")

### Chainage avant

