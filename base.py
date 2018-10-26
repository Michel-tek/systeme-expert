#! /usr/bin/env python3
## -*- encoding: utf-8 -*-



from sys import argv, exit, stderr
msg = stderr.write

## Usage
usage = ( "Usage: {0} interactive [ <base> ]\n"
        + "     | {0} avant         <base> [ < <faits> ] [ > <conclusions> ])\n"
        + "     | {0} arriere       <base> [ < <faits> ] [ > <conclusions> ])\n").format(argv[0])

if len(argv) == 1:
	msg(usage)
	exit(0)



## Règles et moteur
from xml.etree.ElementTree import parse, XML
from Moteur import Moteur



## Triage du mode d'opération
if argv[1] == "interactive":
	from Interface import Interface

	try:
		## Analyser la base de connaissances en entrée et
		## initialiser l'application là-dessus
		application = Interface()
	except IndexError:
		application = Interface()

	application.mainloop()

elif argv[1] in {"avant", "arriere"}:
	from sys import stdin, stdout

	## À compléter en fonction du modèle qui sera adopté

else:
	msg(usage)
	exit(1)
