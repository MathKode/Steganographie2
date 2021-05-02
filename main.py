from numpy import asarray
from PIL import Image
import os


def _number_binary(nb):
    nb = int(nb)
    final = ""
    while nb > 0:
        if nb%2 == 0: final = "0" + final
        else : final = "1" + final
        nb = nb // 2
    while len(final) < 8:
        final = "0" + final
    return final

def _binary_number(binary):
    nb = 0
    tour = 0
    for bit in str(binary)[::-1] :
        nb += int(bit)*(2**tour)
        tour += 1
    return nb

    
def chiffrer(image_name,message):
    data = asarray(Image.open(str(image_name))).copy()
    data2 = data.copy()
    #Converti chaque lettre en sa valeur ASCII puis en binaire (octet)
    message_final = []
    for l in message:
        nb = ord(l)
        message_final.append(str(_number_binary(nb)))
    message_final = "".join(message_final)
    taille = _number_binary(len(message_final))
    while len(taille) < 16:
        taille = "0" + taille
    tour = 0
    y = 0
    for line in data:
        x = 0
        for column in line:
            rgb = 0
            for color in column:
                if tour < 16 :
                    nb = str(_number_binary(color))
                    nb = list(nb)
                    nb[-1] = str(taille)[tour]
                    nb = "".join(nb)
                    data2[y][x][rgb] = int(_binary_number(nb)) 
                elif len(message_final)+16 > tour :
                    nb = str(_number_binary(color))
                    nb = list(nb)
                    nb[-1] = str(message_final)[tour-16]
                    nb = "".join(nb)
                    data2[y][x][rgb] = int(_binary_number(nb))
                else :
                    break
                rgb += 1
                tour += 1
            x += 1
        y += 1  
    imagefinal = Image.fromarray(data2)
    imagefinal = imagefinal.save(str("MODIF_"+image_name+".png")) #Ne fonctionne qu'avec les .png (ATTENTION LES .PNG ne fonctionne pas)

def show(image_name):
    data = asarray(Image.open(str(image_name))).copy()
    message = [[]]
    taille_b = ""
    tour = 0
    for line in data:
        for column in line:
            for color in column:
                if tour < 16:
                    taille_b += str(_number_binary(color))[-1]
                elif tour < taille + 16 :
                    if len(message[-1]) < 8:
                        l = message[-1]
                        l += str(_number_binary(color))[-1]
                        message[-1] = l
                    else :
                        message.append([str(_number_binary(color))[-1]])
                if tour == 15 :
                    taille = _binary_number(taille_b)
                tour += 1
                
    finalmessage = []
    for i in message :
        i = "".join(i)
        finalmessage.append(chr(_binary_number(i)))
    finalmessage = "".join(finalmessage)
    print("-"*len(finalmessage))
    print(finalmessage)
    print("-"*len(finalmessage))

if __name__ == "__main__":
    while True:
        ls = os.listdir()
        print('Write a H, the number of the file and the message if you want hide, a S and the number of file if you want show (ex : H3lol or S4):\n')
        t=1
        for i in ls:
            print(t,i)
            t+=1
        print('\n')
        c = input('-> ')
        if str(c)[0] == "H":
            chiffrer(ls[int(str(c)[1])-1],str(c[2:]))
        else :
            show(ls[int(str(c)[1])-1])
