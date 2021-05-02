# Steganographie2
Ce code vous permet de cacher des messages dans des images
Ceci est une suite du dossier Stéganographie SAUF que la méthode utilisé est plus discrète :-)

En effet, avant, on modifier la couleur du pixel (exemple avec C : C -> +2 -> valeur pixel +2 ...)
Maintenant, le script ne tourne qu'avec des +1, +0, -1 car il prend le nb en binaire et le modif

EXEMPLE
Si j'ai "lol", le code le convertit en binaire :
  lol -> 01101100 01101111 01101100
Puis il ouvre l'image et convertit les pixels en bin :
  Img -> [45,134,67] [32,45,2] ... -> [101101,10000110,1000011] [100000,101101,10]
           |   |  |
           --------> Trois couleurs (RGB) pour 1 pixel

Après, il modifie la dernière valeur de chaque pixel par celle du message bin :
  [101101,10000110,1000011] [100000,101101,10]
  1er : 101101 et la 1ere lettre du message est 0 donc : 101100
             |                                  |             |
             -------------------------MODIF PAR 0 -------------
  2eme : 10000110 et la 2eme lettre du message est 1 donc : 10000111
  etc...
    
Pour l'étape de la lecture, on prend donc chaque pixel, on les convertit en binaire puis on regarde le dernier bit et à chaque octet obtenu on converti en txt.

PS : Pour éviter de tout traduire, mon code inscrit la taille en bit du message sur les 16 premiers nb...
