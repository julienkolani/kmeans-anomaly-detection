#KOLANI Julien IS

"""
Exo 2:
Écrire une fonction en python qui lit une chaîne de texte (représentant le contenu d'un fichier) et renvoie les dernières lignes par type de manière efficace. La fonction ne doit conserver que les N dernières lignes pour chaque type, et doit gérer les fichiers de grande taille sans consommer une quantité excessive de mémoire.

Détails de l'exercice :

Entrée :

Une chaîne de texte txt contenant plusieurs lignes de données. Chaque ligne est structurée comme suit :


TYPE,VALEUR1,VALEUR2,...,VALEURn
où TYPE est un identifiant de type et les autres valeurs sont des données associées.

Un nombre entier numberOfLines qui représente le nombre de lignes à conserver pour chaque type.

Sortie :

Un objet python où chaque clé est un type (TYPE), et la valeur associée est un tableau contenant les numberOfLines dernières lignes pour ce type.
Contraintes :

Exemple :
Entrée :

<code>
const txt = `TYPE I,2024,719,17,6,90,86,42,78,57,353,0,0
TYPE I,2024,720,17,6,76,83,61,35,46,301,0,0
TYPE V,2013,0,4,6,22,1,5,5,28,
TYPE V,2013,1,4,6,77,29,71,5,28,210
TYPE V,2013,2,11,6,12,35,15,80,9,151`;

const numberOfLines = 2;
Sortie :

<code>
{
  "TYPE I": [
    "TYPE I,2024,719,17,6,90,86,42,78,57,353,0,0",
    "TYPE I,2024,720,17,6,76,83,61,35,46,301,0,0",
  ],
  "TYPE V": [
    "TYPE V,2013,1,4,6,77,29,71,5,28,210",
    "TYPE V,2013,2,11,6,12,35,15,80,9,151",
  ]
}

"""

def parse_type (txt):
    group_lines = {}

    for line in txt.splitlines():
        line_as_list = line.split(',')
        key = line_as_list[0]
        #print(key)
        if key not in group_lines:
            group_lines[key] = []

        group_lines[key].append(line)
    return  group_lines

def last_lines(txt, numberOfLines):

    group_lines = parse_type(txt)
#    print(group_lines)
    output = """{\n"""
    for key, lines in group_lines.items():
        output += f"""  "{key}": [\n"""
#        count : int = 0
        for l in lines[-numberOfLines:]:
            output += f"""      "{l}",\n"""
#            count+=1
        output += f"""  ],\n"""
    output += """}"""
    return  output
#    print(output)

#last_lines(txt)


txt = """TYPE I,2024,719,17,6,90,86,42,78,57,353,0,0
TYPE I,2024,720,17,6,76,83,61,35,46,301,0,0
TYPE V,2013,0,4,6,22,1,5,5,28,
TYPE V,2013,1,4,6,77,29,71,5,28,210
TYPE V,2013,2,11,6,12,35,15,80,9,151"""

numberOfLines = 2
print(last_lines(txt, numberOfLines))


