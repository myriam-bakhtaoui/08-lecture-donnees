"""Module de gestion de liste de nombre entiers"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename,"r", encoding='utf-8') as file:  # Ouverture du fichier en lecture
        lines = file.readlines() # lecture de toutes les ligne

    l = []
    for line in lines:
        line_clean = line.strip()
        if line_clean:
            number_str = line_clean.split(';')
            number_int = [int(x) for x in number_str]
            l.append(number_int)

    return l

def get_list_k(data, k):
    """ retourne la k-ième liste de data"""
    l = data[k]
    return l

def get_first(l):
    """retourne le premier élément de la liste l"""
    return l[0]

def get_last(l):
    """retourne le dernier élément de la liste l"""
    return l[-1]

def get_max(l):
    """retourne le maximum de la liste l"""
    return max(l)

def get_min(l):
    """retourne le minimum de la liste l"""
    return min(l)

def get_sum(l):
    """retourne la somme des élémennts de la liste l"""
    return sum(l)

def main():
    """fonction principale"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
