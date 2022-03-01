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
print("***  Menu de choix  ***")
def menuChoix(facturationAbonner = "1. Facturer un abonnement",AfficherForfait= "2. Afficher le nombre d’abonnés par forfaits",quitterProg= "3. Quitter le programme"):
    print(" {} \n {} \n {}".format(facturationAbonner,AfficherForfait,quitterProg) )

menuChoix()

def option3():
    print("option3")


option = int(input("Entrez votre choix :"))
def saisieService():
            numeroDeService= input("Entrez les numéros des services (1 = Internet, 2 = Télé, et 3 = Internet et Télé) : ")
            numeroDeService= int( numeroDeService)
            if numeroDeService==1 :
                saisieIdentifiant()
            elif numeroDeService==2:
                print("tele")
            elif numeroDeService==3:
                print("Internet et Télé")
            else:
                print("Entrée invalide !")
                saisieService()
def saisieIdentifiant():
    
            identifiantService = input("Entrez l'identifiant du forfait internet (50, 150, 500 ) :")
            identifiantService = int(identifiantService)
            if identifiantService==50:
                saisieModePaiement()
            elif  identifiantService==150:
                    print("150")
            elif  identifiantService==500:
                print("500")
            else:
                print("Entrée invalide !")
                saisieIdentifiant()
def saisieModePaiement():
               
            
                modePaiement = input(" Entrez le mode de paiement (P ou p pour paiement préautorisé,\n C ou c pour paiement via mon compte, L ou l pour paiement bancaire\n en lig ne, I ou i pour paiement en institution bancaire):")
                if modePaiement=="P" or modePaiement=="p" :
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
                   print("                     Merci pour votre confiance")
                   
                elif modePaiement=="L" or modePaiement=="l":
                        print("acces")
                elif modePaiement=="I" or modePaiement=="i":   
                        print("acces")
                else:
                            print("Entrée invalide !")
                            saisieModePaiement()
while option !=3:
        if option==1:
            nomAbonner = input("Entrez le nom de l'abonné :")
            prenomAbonner = input("Entrez le prénom de l'abonné :")
            numeroTelAbonner = input("Entrez le numéro de téléphone de l'abonné :")
            adresseAbonner = input(" Entrez l'adresse de l'abonné :")
            saisieService()
                
        elif option==2:
             print("2")
        elif option==3:
            option3()
        else:
            print("Entrée invalide !")
            print("***  Menu de choix  ***")
        print()
        menuChoix()
        option = int(input("Entrez votre choix :"))
print("Merci et à la prochaine !")

