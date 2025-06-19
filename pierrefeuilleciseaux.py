import random
import time

chifoumi = ["pierre", "papier", "ciseaux"]

def gagne(ordi, joueur):
    if ordi == joueur:
        return "nul"
    elif (ordi == "papier" and joueur == "ciseaux") or \
         (ordi == "ciseaux" and joueur == "pierre") or \
         (ordi == "pierre" and joueur == "papier"):
        return True
    else:
        return False

def valide(choix):
    return choix.lower() == "oui"

mode = int(input(f"Jouer une partie : 1\nJouer 10 parties : 2\nFaire Jouer 2 Robots : 3\n   Choix : "))

if mode == 1:
    indiceOrdi = random.randint(0, 2)
    choixOrdi = chifoumi[indiceOrdi]
    verifvalide = False
    while not verifvalide:
        choixJoueur = input("Choisissez 'pierre', 'papier' ou 'ciseaux' : ").lower()
        if choixJoueur not in chifoumi:
            print("Choix invalide.")
            continue
        choixValide = input(f"Vous avez choisi '{choixJoueur}'. Valider ? (oui/non) : ").lower()
        verifvalide = valide(choixValide)
    resultat = gagne(choixOrdi, choixJoueur)
    print(f"L'ordinateur a choisi : {choixOrdi}")
    if resultat == True:
        print("Vous avez gagné !")
    elif resultat == "nul":
        print("Match nul.")
    else:
        print("Vous avez perdu.")

elif mode == 2:
    parties = 10
    perdu = 0
    gagner = 0
    nul = 0
    def afficher_parties():
        print(f"Parties joués : {i+1}\nParties Gagnées : {gagner} | Parties perdus : {perdu} | Parties nulles : {nul}")
    for i in range(parties):
        afficher_parties()
        indiceOrdi = random.randint(0, 2)
        choixOrdi = chifoumi[indiceOrdi]
        verifvalide = False
        while not verifvalide:
            choixJoueur = input("Choisissez 'pierre', 'papier' ou 'ciseaux' : ").lower()
            if choixJoueur not in chifoumi:
                print("Choix invalide.")
                continue
            choixValide = input(f"Vous avez choisi '{choixJoueur}'. Valider ? (oui/non) : ").lower()
            verifvalide = valide(choixValide)
        resultat = gagne(choixOrdi, choixJoueur)
        print(f"L'ordinateur a choisi : {choixOrdi}")
        if resultat == True:
            print("Vous avez gagné !\n")
            gagner += 1
        elif resultat == "nul":
            print("Match nul.\n")
            nul += 1
        else:
            print("Vous avez perdu.\n")
            perdu += 1

elif mode == 3:
    parties = int(input("Choisissez le nombre de parties : "))
    perdu = 0
    gagner = 0
    nul = 0
    def afficher_parties():
        print(f"Parties joués : {i+1}\nOrdi 1 : {gagner} | Ordi 2 : {perdu} | Parties nulles : {nul}")
    for i in range(parties):
        time.sleep(1)
        afficher_parties()
        indiceOrdi1 = random.randint(0, 2)
        indiceOrdi2 = random.randint(0, 2)
        choixOrdi1 = chifoumi[indiceOrdi1]
        choixOrdi2 = chifoumi[indiceOrdi2]
        resultat = gagne(choixOrdi1, choixOrdi2)
        time.sleep(1)
        print(f"L'ordinateur 1 a choisi : {choixOrdi1}")
        print(f"L'ordinateur 2 a choisi : {choixOrdi2}")
        if resultat == True:
            print("l'ordinateur 1 a gagné !\n")
            gagner += 1
        elif resultat == "nul":
            print("Match nul.\n")
            nul += 1
        else:
            print("l'ordinateur 2 a gagné !\n")
            perdu += 1
else:
    print("Choix invalide.")
