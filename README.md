# Chatbot

## Description du projet

Le projet que j'ai développé est un ChatBot codé en Python avec une base de données MySQL. Un chatbot est un programme informatique visant à simuler une conversation écrite avec un utilisateur humain. Je n'ai pas essayé d'extraire le sens des phrases écrites par l'utilisateur. Mais le programme est en deux parties :

### Apprentissage : 
lorsque l'utilisateur tape un message, celui-ci est compris comme une réponse à une déclaration antérieure faite par le chatbot. La phrase tapée par l'humain sera alors associée aux mots présents dans le message précédent.
### Réponse : 
le message de l'humain est décomposé en mots. Le programme va essayer d'identifier les phrases qui correspondent le mieux à ces mots, en fonction de son "expérience" antérieure. Le robot intelligent stockera des associations de mots (Phrases) en guise de réponse à une phrase donnée par l'utilisateur et s'en servira pour essayer de faire correspondre avec les réponses futures.

## Comment utiliser ce code?
-Assurez-vous d'avoir Python installé sur votre système.
-Créez une base de données MySQL et nommez-la 'bdd.sqlite'.
-Exécutez le code Python fourni.
-Commencez à interagir avec le ChatBot en entrant des messages.
-Le ChatBot apprendra de vos réponses et fournira des réponses en fonction de ses apprentissages antérieurs.
Dépendances

## Le code utilise les bibliothèques Python suivantes :

- re : Pour l'utilisation d'expressions régulières. Documentation
- sqlite3 : Pour la gestion de la base de données SQLite. Documentation
- collections.Counter : Pour compter les occurrences des mots. Documentation
- string.punctuation : Pour la gestion des signes de ponctuation. Documentation
- math.sqrt : Pour effectuer des calculs mathématiques.
sqlite3: For managing the SQLite database. Documentation
collections.Counter: For counting word occurrences. Documentation
string.punctuation: For handling punctuation marks. Documentation
math.sqrt: For performing mathematical calculations.
