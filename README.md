
# Description du Projet

Création et lecture de code QR en langage ASCII

# Membres

Arthur Réauté, Blanche Jansen, Annaëlle Moreau et Camille Huitorel

# Etapes

I-Du message au QR-code :

    1-Traduction du message binaire 8bits via le langage ASCII
    
    2-Choix de la version/du format du QR selon la taille
    
    3-Création de la "matrice QR"
    
        a)création d'une première matrice avec le masque 0
        
        b)détection des problèmes visuels gênant dans la reconnaissance du code (Position Detection Patterns, Zones unicolores...)
        
        c)répétition des étapes a (avec un masque différent) et b si problèmes il y a
    
    4-Création de l'image 2D QR-code

II-Du QR-code au message
    
    (1-analyse d'une photo grâce aux Position Dection Patterns)
    
    2-Traduction de l'image QR-code en "matrice QR"
    
    3-Détection de la version/du format
    
    4-Détection et retraît du masque
    
    5-Analyse du code du QR
    
    C'est cool
lol
