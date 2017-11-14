
def binchaine(message) :
    “Traduction d’une chaîne de caractères en binaire ASCII”
    messagebin=""
    for i in message:
        B=str(bin(ord(i)))[2:]  #Converti le caractère i en son code binaire ascii
        while len(B)<8 :  #Tant qu’il n’y a pas 8 caractères, on rajoute un 0 à gauche
            B="0"+B
        messagebin+=B
    return messagebin
