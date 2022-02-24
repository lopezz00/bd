#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Pràctica 1
==========

Ivan Chamero de la Rosa & Marc López Arévalo

"""

import struct
from time import sleep



def crea_parking(places):
    
    f = open("registreaparcament.bin", "wb")
    for e in range(places):
        f.seek(e * tamany)
        d = struct.pack(format, str(e).encode(), "EMPTY".encode(), "XXXXXXX".encode())
        #d = struct.pack(format, str(e).encode(), "EMPTY".encode(), "".encode())
        f.write(d)
    f.close()


def aparca_cotxe(posicio, matricula):

    f = open("registreaparcament.bin", "r+b")
    f.seek(int(posicio) * tamany)
    d = struct.pack(format, posicio.encode(), "FULL".encode(), matricula.encode())
    f.write(d)
    f.close()


def surt_cotxe(posicio):

    f = open("registreaparcament.bin", "r+b")
    f.seek(int(posicio) * tamany)
    d = struct.pack(format, posicio.encode(), "EMPTY".encode(), "XXXXXXX".encode())
    #d = struct.pack(format, posicio.encode(), "EMPTY".encode(), "".encode())
    f.write(d)
    f.close()    


def mostra_cotxe(posicio):

    f = open("registreaparcament.bin", "rb")
    f.seek(posicio * tamany)
    d = f.read(tamany)
    t = struct.unpack(format, d)
    l = list(t)
    if (l[1] == b'FULL\x00'):
        print("Plaça ocupada --> Plaça:", l[0].decode(), " Matricula:",l[2].decode() + "\n", end = "")
    else:
        print("Plaça buida!")    
    f.close()             


def check_posicio(posicio):

    f = open("registreaparcament.bin", "rb")
    f.seek(int(posicio) * tamany)
    d = f.read(tamany)
    t = struct.unpack(format, d)
    l = list(t)
    if (l[1] == b'FULL\x00'):
        f.close()
        return False
    else:
        f.close()
        return True


def check_pos_buida():

    f = open("registreaparcament.bin", "rb")
    for e in range(places):
        f.seek(e * tamany)
        d = f.read(tamany)
        t = struct.unpack(format, d)
        l = list(t)
        if (l[1] == b'EMPTY'):
            f.close()
            pos = l[0].decode()
            return pos 
    f.close()
    print("Parking COMPLERT!\nNo pots aparcar en aquest parking")


def check_all_pos_buida():

    f = open("registreaparcament.bin", "rb")
    for e in range(places):
        f.seek(e * tamany)
        d = f.read(tamany)
        t = struct.unpack(format, d)
        l = list(t)
        if (l[1] == b'EMPTY'):
            pos = l[0].decode()
            print(pos, end = " ")
    f.close()


def check_all_pos_ocupades():

    f = open("registreaparcament.bin", "rb")
    for e in range(places):
        f.seek(e * tamany)
        d = f.read(tamany)
        t = struct.unpack(format, d)
        l = list(t)
        if (l[1] == b'FULL\x00'):
            print("Plaça:", l[0].decode(), " Matricula:", l[2].decode(), "\n", end = "")        
    f.close()   


def busca_cotxe(matricula):

    f = open("registreaparcament.bin", "rb")
    for e in range(places):
        f.seek(e * tamany)
        d = f.read(tamany)
        t = struct.unpack(format, d)
        l = list(t)
        if (l[2].decode() == matricula):
            f.close()
            return True, l[0].decode()
    f.close()
    return False, ""


def calcula_log():

    f = open("registreaparcament.bin", "rb")
    places = 0
    for e in range(1000):
        try:
            f.seek(e * tamany)
            d = f.read(tamany)
            t = struct.unpack(format, d)
            places += 1
        except Exception:
            return places    


def print_all_pos():

    f = open("registreaparcament.bin", "rb")
    for e in range(places):
        f.seek(e * tamany)
        d = f.read(tamany)
        t = struct.unpack(format, d)
        l = list(t)
        if (l[1] == b'FULL\x00'):
            print("Plaça ->", l[0].decode(), "Matricula -> ", l[2].decode() + "\n", end = "")  
        else:
            print("Plaça ->", l[0].decode(), "buida\n", end = "")
    f.close()   
        
            
def init():

    print("1. Utilitzar el parking existent ")
    print("2. Crear un parking nou \n")
    op = input("Que vols fer ? ")
    while (op != "1" and op != "2"):
            op = input("Que vols fer ? ")
    if (op == "1"):
        log = calcula_log()
        return log
    else:
        op = input("De quantes places vols el parking (1 - 1000) ? ")
        while (not(op.isdigit()) or int(op) > 1000):
            op = input("El valor ha de ser entre 0 i 1000: ")
        crea_parking(int(op))
        return op


def menu():
    
    print ("\n---------- PARKING CHAMERO/LOPEZ --------- \n")
    print("1. Aparcar en un lloc especific.")
    print("2. Aparcar en el primer lloc buit.")
    print("3. Treure un cotxe.")
    print("4. Consultar una plaça.")
    print("5. Mostrar totes les plaçes del parking buides.")
    print("6. Buscar un cotxe al parking.")
    print("7. Mostrar totes les places ocupades.")
    print("8. Mostrar totes les places del parking.")
    print("9. Sortir del programa. \n")
    


if __name__ == "__main__":       

    global format
    format = "4s5s7s"

    global tamany
    tamany = struct.calcsize(format)

    opcions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    global places 
    places = init()
    places = int(places)

    aparca_cotxe("0", "9882JPX")
    aparca_cotxe("1", "6912JBT")
    aparca_cotxe("2", "2222WWW")
    aparca_cotxe("3", "3333FFF")
    aparca_cotxe("4", "4444HHH")
    aparca_cotxe("5", "5555KKK")

    menu() 

    while (1):
        
        print("-------------------------------")
        opcio = input("\nQue vols fer ? ")
        while (opcio not in opcions):
            opcio = input("Opció no vàlida. Que vols fer ? ")

        print("\n")
        if (opcio == "1"):
            print("Places lliures per aparcar:\n")
            check_all_pos_buida()
            lloc = input("\nEn quin lloc vols aparcar ? ")
            while (not(lloc.isdigit()) or int(lloc) > places - 1):
                lloc = input("Entra una plaça valida. En quin lloc vols aparcar ? ")
            if (check_posicio(lloc)):
                matricula = input("Plaça buida. Quina es la teva matrícula ? ")
                while (len(matricula) > 7):
                    matricula = input("Matrícula no valida. Quina es la teva matrícula ? ")
                aparca_cotxe(lloc, matricula.upper())
                print("Cotxe aparcat amb èxit!")
            else:
                print("La plaça està ocupada")        

        elif (opcio == "2"):       
            print("Buscant posicio buida...")
            sleep(2)
            pos_buida = check_pos_buida()
            if (pos_buida != None):
                matricula = input("Quina es la teva matrícula ? ")
                while (len(matricula) > 7):
                    matricula = input("Matrícula no valida. Quina es la teva matrícula ? ")
                pos = ""    
                for w in pos_buida:
                    if (w.isdigit()):
                        pos += w       
                aparca_cotxe(pos, matricula.upper())
                print("Cotxe aparcat amb èxit! Posiciò del cotxe --> ", pos)

        elif (opcio == "3"):
            print("Places ocupades:\n")
            check_all_pos_ocupades()
            lloc = input("De quina plaça vols marxar ? ")
            while (not(lloc.isdigit()) or int(lloc) > places - 1):
                lloc = input("Entra una plaça valida. De quina plaça vols marxar ? ")  
            if (check_posicio(lloc)):
                print("Plaça buida. ")
            else:
                surt_cotxe(lloc)
                print("Cotxe retirat amb èxit!") 

        elif (opcio == "4"):
            lloc = input("Quina plaça vols consular ? ")
            while (not(lloc.isdigit()) or int(lloc) > places - 1):
                lloc = input("Entra una plaça valida. Quina plaça vols consular ? ")    
            if (check_posicio(lloc)):
                print("Plaça buida. ")
            else:
                mostra_cotxe(int(lloc))
                
        elif (opcio == "5"):        
            print("Llistat de places buides:\n ")
            check_all_pos_buida()
            print("\n")

        elif (opcio == "6"):        
            matricula = input("Quina matrícula estas buscant ? ")
            while (len(matricula) > 7):
                matricula = input("Matrícula no valida. Quina matrícula estas buscant ? ")
            estat, pos = busca_cotxe(matricula.upper())
            if (estat == True):
                print("Cotxe trobat a la posició --> ", pos)
            else:
                print("Aquest cotxe no està aparcat en el nostre parking.")

        elif (opcio == "7"):
            check_all_pos_ocupades()    

        elif (opcio == "8"):
            print_all_pos()

        else:
            break
     