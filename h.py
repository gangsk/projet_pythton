import os
from datetime import date
import time
clear = lambda: os.system('cls')
print("----------------------------------------------------------------------------------------------------------------")
nom_projet = "Bienvenue dans le système de facturation d'Internet-Télé Pour Tous.\n Ce Système permet de calculer la " \
"facture des abonnés selon le prix  et le nombre de forfaits choisis.\n Il affiche aussi le nombre  " \
"d'abonnés par forfait."
print(nom_projet)
print("----------------------------------------------------------------------------------------------------------------")
input("Taper sur entrer pour continuer..........")
clear()
#Fonction du menu au choix
print("***  Menu de choix  ***")

def menuChoix(facturationAbonner = "1. Facturer un abonnement",AfficherForfait= "2. Afficher le nombre d’abonnés par forfaits",quitterProg= "3. Quitter le programme"):
    print(" {} \n {} \n {}".format(facturationAbonner,AfficherForfait,quitterProg) )

menuChoix()

#la saisie du choix

entrerChoix = input("Entrez votre choix :")
entrerChoix = int(entrerChoix)
if entrerChoix==1 :
    nomAbonner = input("Entrez le nom de l'abonné :")
    prenomAbonner = input("Entrez le prénom de l'abonné :")
    numeroTelAbonner = input("Entrez le numéro de téléphone de l'abonné :")
    numeroTelAbonner=int(numeroTelAbonner)
    adresseAbonner = input(" Entrez l'adresse de l'abonné :")
    numeroDeService= input("Entrez les numéros des services (1 = Internet, 2 = Télé, et 3 = Internet et Télé) : ")
    numeroDeService= int( numeroDeService)
    if numeroDeService==1 :
       identifiantService = input("Entrez l'identifiant du forfait internet (50, 150, 500 ) :")
       identifiantService = int(identifiantService)
       if identifiantService==50:
           modePaiement = input(" Entrez le mode de paiement (P ou p pour paiement préautorisé,\n C ou c pour paiement via mon compte, L ou l pour paiement bancaire\n en lig ne, I ou i pour paiement en institution bancaire):")
           if modePaiement=="P" or "p":
                print("--------------------------------------------------------------------------------")
                now = date.today()
                print("Internet-Tele Pour Tous\n")
                print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                print("Facture No : 1      Date et Heure",now,time.strftime("%H:%I:%S"))
               
                print("--------------------------------------------------------------------------------")
                print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                print("Adresse du client : ",adresseAbonner)
                print("\n")
                print("Mode de paiement : Paiement preautorisé ")
                print("Descirption - forfait(s)                      Prix")
                print("--------------------------------------------------------------------------------")
                print("Internet Fibre hybride 50                    35,95$")
                internetFibreHybride=35.95
                tps=5
                tvq=9.975
                calculTps = (internetFibreHybride*tps)/100
                calculTvq = (internetFibreHybride*tvq)/100
                prixTotal = internetFibreHybride+calculTps+calculTvq
                print("Sous-total                                 ",internetFibreHybride,"$")
                print("Montant TPS                                ",calculTps,"$")
                print("Montant TVQ                                ",calculTvq,"$")
                print("Montant total                              ",prixTotal,"$")
                print("            --------------------------------------------")
                print("                     Merci pour votre confian")
           elif modePaiement=="L" or "l":
               print("acces")
           elif modePaiement=="I" or "i":   
               print("acces")
           else:
                print("Entrée invalide !")
                
       elif identifiantService==50:
            print("150")
       elif  identifiantService==150:
            print("150")
       elif  identifiantService==500:
           print("150")
       else:
           print("Entrée invalide !")

    elif numeroDeService==2:
        print("tele")
    elif numeroDeService==3:
        print("Internet et Télé")
    else:
        print("Entrée invalide !")


#ENtrer un choix
elif entrerChoix==2 :
    print("2")
elif entrerChoix==2 :
    print("3")
else:
    print("Entrée invalide !")









