#! /usr/bin/env python3
## -*- encoding: utf-8 -*-



from sys import argv, exit, stderr
msg = stderr.write

## Usage
if len(argv) <= 3:
	msg("Usage: {0} (avant|arriere) ${{base}}.xml [ < ${{fait}}.xml ] [ > ${{conclusions}}.xml ]\n".format(argv[0]))
	exit(0)



## Règles et moteur
if ".xml" not in argv[2]:
	msg("{0} n'est pas un fichier XML".format(argv[2]))
	exit(1)

from xml.etree.ElementTree import parse, XML
from Moteur import Moteur
#from Logique import from, to
moteur = Moteur(parse(argv[2]))
#moteur = Moteur(from(parse(argv[2])))



## Le traitement en soi-même
#conclusion.write(XML(to( Moteur.avant(from(parse(faits.read()))) if argv[1] == "arriere" else
#                         Moteur.arriere(from(parse(faits.read())))
#                       )))
