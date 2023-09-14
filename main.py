#Le projet que j’ai développé est un ChatBot codé en Python avec une base de données MySQL. Un chatbot, est un programme informatique visant à simuler une conversation écrite avec un utilisateur humain. Je n’ai pas essayé d'extraire le sens des phrases écrites par l'utilisateur. Mais le programme est en deux parties : - Apprentissage : lorsque l'utilisateur tape un message, celui-ci est compris comme une réponse à une déclaration antérieure faite par le chatbot. La phrase tapée par l'humain sera alors associée aux mots présents dans le message précédent. - Réponse : le message de l'humain est décomposé en mots. Le programme va essayer d'identifier les phrases qui correspondent le mieux à ces mots, en fonction de son "expérience" antérieure. Le robot intelligent stockera des associations de mots ( Phrases) en guise de réponse à une phrase donnée par l’utilisateur et s’en sert pour essayer de faire correspondre avec les réponses futures. 

import re
#https://docs.python.org/fr/3/library/re.html
import sqlite3
#https://zestedesavoir.com/tutoriels/1294/des-bases-de-donnees-en-python-avec-sqlite3/fonctionnalites-de-base/
from collections import Counter
#http://www.python-simple.com/python-modules-structures-donnees/collections.php
from string import punctuation
#https://www.geeksforgeeks.org/string-punctuation-in-python/
from math import sqrt


# Nous pouvons nous connecter à une BDD en utilisant la méthode connect et en lui passant l’emplacement du fichier de stockage en paramètre 
connection = sqlite3.connect('bdd.sqlite')

#Pour exécuter nos requêtes, nous allons nous servir d’un objet Cursor, récupéré en faisant appel à la méthode cursor de notre objet de type Connection.
cursor = connection.cursor()
 
 # On crée une liste de table dont nous avons besoin 
creer_table_requete_liste = [
    'CREATE TABLE mots (mot TEXT UNIQUE)',
    'CREATE TABLE phrases(phrase TEXT UNIQUE, utilise INT NOT NULL DEFAULT 0)',
    'CREATE TABLE associations (mot_id INT NOT NULL, phrase_id INT NOT NULL, poids REAL NOT NULL)',
]
# Pour chaque table, on execute sa creation
for creer_table_requete in creer_table_requete_liste:
    try:
        cursor.execute(creer_table_requete)
    except: # En cas d'erreur , L’instruction pass ne fait rien.
        pass

# Les fonctions dont nous avons besoin 


# * 1 * Récupère l'identifiant unique d'une entité dans la base de données, avec son texte associé. Si la ligne n'est pas déjà présente, elle est insérée. L'entité peut être une phrase ou un mot.  

def recup_id(nom_entite, texte):
    nom_table = nom_entite + 's'
    nom_colonne = nom_entite
    #Le rowid identifie un enregistrement d'une table dans la base de données, à partir de l'adresse physique du bloc et du numéro d'enregistrement dans le bloc. 
    cursor.execute('SELECT rowid FROM ' + nom_table + ' WHERE ' + nom_colonne + ' = ?', (texte,))
    #Pour récupérer les données, il est possible de récupérer le premier résultat avec fetchone. qui retourne un résultat sous forme de tuple, ou None, s’il n’y en a pas.
    row = cursor.fetchone()
    if row:
        return row[0] #row[0] fait simplement référence au premier champ de notre liste de champs dans le curseur. 
    else:
        cursor.execute('INSERT INTO ' + nom_table + ' (' + nom_colonne + ') VALUES (?)', (texte,))
#nous pouvons aussi récupérer l’identifiant du dernier enregistrement dans une table à l’aide de l’attribut lastrowid de notre objet de type Connection
        return cursor.lastrowid
       


# * 2 * Récupère les mots présents dans une chaîne de texte donnée. La valeur de retour est une liste de tuples où le premier membre est un mot en minuscule, et le second membre le nombre de fois qu'il est présent dans le texte.

def recup_mots(text):   

    #Les quantificateurs spécifient simplement la quantité de caractères à mettre en correspondance.

    #re.escape() renvoie une copie de <quelque chose> avec chaque caractère non-mot (tout ce qui n'est pas une lettre, un chiffre ou un trait de soulignement) précédé d'une barre oblique inverse. Ceci est utile si vous appelez l'une des fonctions du module re, et que le <regex> que vous passez contient beaucoup de caractères spéciaux que vous voulez que l'analyseur syntaxique prenne littéralement au lieu de les considérer comme des métacaractères. Cela vous évite d'avoir à mettre tous les caractères backslash manuellement.
   
    wordsRegexpStr = '(?:\w+|[' + re.escape(punctuation) + ']+)'

 #Compile un motif d'expression régulière dans un objet d'expression régulière, qui peut être utilisé pour la correspondance à l'aide de ses méthodes match(), search() et autres.

    wordsRegexp = re.compile(wordsRegexpStr)
   
 #Le module findall() est utilisé pour rechercher "toutes" les occurrences qui correspondent à un motif donné. Findall() parcourt toutes les lignes du fichier et renvoie toutes les occurrences non superposées du motif en une seule étape.
    liste_mots = wordsRegexp.findall(text.lower())

#Retourne la chaîne de caractères en minuscules à partir de la chaîne de caractères donnée. Elle convertit tous les caractères majuscules en minuscules.
    return Counter(liste_mots).items()


# message de Bienvenue
Robot = 'Discutes avec moi !'
while True:
    # message de sortie du robot
    print('Robot: ' + Robot)
    # demander la replique de l'utilisateur ; si la ligne est vide, sortir de la boucle.
    Vous = input('Vous: ').strip()
    #La méthode strip() supprime les caractères de tête et de queue. 
    if Vous == '':
        break

# * 3 * Mémoriser l'association entre les mots du message du robot et es mots du message de l'utilisateur

    #On appelle notre fonction qui renvoie une liste de tupple
    mots = recup_mots(Robot)
 
    #La longueur du message du robot
    longueur_mots = sum([n * len(mot) for mot, n in mots])
 
    #Récupère l'identifiant unique de la replique dans la base de données, avec son texte associé. Si la ligne n'est pas déjà présente, elle est insérée. L'entité peut être une phrase ou un mot. word
    phrase_id = recup_id('phrase', Vous)

    for mot, n in mots:
        #Récupère l'identifiant unique de chaque mot dans la base de données. Si le mot n'est pas déjà présent, il est insérée.
        mot_id = recup_id('mot', mot)
         
        #On attribue un poid au mot en fonction du nombre de lettre par rapport a la phrase
        poids = sqrt(n / float(longueur_mots))

        # On insere dans la table associations l'identitfiant de chaque mot avec le mot et son poid
        cursor.execute('INSERT INTO associations VALUES (?, ?, ?)', (mot_id, phrase_id, poids))
     #La méthode commit() est utilisée pour s'assurer que les modifications apportées à la base de données sont cohérentes. Elle fournit essentiellement à la base de données une confirmation des modifications apportées par un utilisateur ou une application dans la base de données.   
    connection.commit()
    

# * 4 * Récupérer la réponse la plus probable dans la base de données pour que ce soit la réponse du robot

    # On cree une table temporairement avec comme colonne l'identifiant des phrases / phrase / poid ( c'est une valeur approchée qui est stockée)
    cursor.execute('CREATE TEMPORARY TABLE results(phrase_id INT, phrase TEXT, poids REAL)')

    #On appelle notre fonction qui renvoie une liste de tupple de la phrase de l'humain
    mots = recup_mots(Vous)
    
    #La longueur du message du robot
    longueur_mots = sum([n * len(mot) for mot, n in mots])
    

    for mot, n in mots:
       #On attribue un poid au mot en fonction du nombre de lettre par rapport a la phrase words
      poids = sqrt(n / float(longueur_mots))

      cursor.execute('INSERT INTO results SELECT associations.phrase_id, phrases.phrase, ?*associations.poids/(4+phrases.utilise) FROM mots INNER JOIN associations ON associations.mot_id=mots.rowid INNER JOIN phrases ON phrases.rowid=associations.phrase_id WHERE mots.mot=?', (poids, mot))

       
# * 5 * si des correspondances ont été trouvées, donnez la meilleure

 
    #Affiche identifiant des phrases humaines , phrases humaines ;la somme du poids de cette phrase ordoneee par celle ci.
    cursor.execute('SELECT phrase_id, phrase, SUM(poids) AS sum_poids FROM results GROUP BY phrase_id ORDER BY sum_poids DESC LIMIT 1')

    
    #Récupérer le premier résultat avec fetchone. qui retourne un résultat sous forme de tuple, ou None, s’il n’y en a pas.
    row = cursor.fetchone()
    
    #La commande DROP TABLE en SQL permet de supprimer définitivement une table d'une base de données. 
    cursor.execute('DROP TABLE results')
   


    if row is None:
        #Si on ne trouve aucune correspondance on prend la phrase qui est le moins utilisee
        cursor.execute('SELECT rowid, phrase FROM phrases WHERE utilise = (SELECT MIN(utilise) FROM phrases) ORDER BY RANDOM() LIMIT 1')

        #Récupérer le premier résultat avec fetchone. qui retourne un résultat sous forme de tuple, ou None, s’il n’y en a pas.
        row = cursor.fetchone()
        
    #row est un tuple donc la reponse du robot est le deuxieme element du tuple soit la phrase
    Robot = row[1]
    
    #mettre a jour la bdd en ajoutant une utilisation 
    cursor.execute('UPDATE phrases SET utilise=utilise+1 WHERE rowid=?', (row[0],))
    
