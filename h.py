import os
from datetime import date
import time
identifiantService50 = 0
identifiantService150 = 0
dentifiantService500 = 0
chaine25 = 0
factureIncre = 0

identifiantService = 0
forfait15 = 0
identifiantForfait=0
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

def forfaitID():
    identifiantForfait = input(" Entrez l'identifiant du forfait télé (B, T, E) :")
    if identifiantForfait =="B":
        saisieModePaiement()
        internetFibreHybridee=20.95
        tpss=5
        tvqq=9.975
        calculTpss = (internetFibreHybridee*tpss)/100
        calculTvqq = (internetFibreHybridee*tvqq)/100
        prixTotall = internetFibreHybridee+calculTpss+calculTvqq
        print("Sous-total                                 ",internetFibreHybridee,"$")
        print("Montant TPS                                ",calculTpss,"$")
        print("Montant TVQ                                ",calculTvqq,"$")
        print("Montant total                              ",prixTotall,"$")
        print("            --------------------------------------------")
        print("                     Merci pour votre confiance")
        global forfait15
        forfait15 += 1
    elif identifiantForfait=="T" :
        saisieModePaiement()
        global chaine25
        chaine25 += 1
        internetFibreHybrideT=25.95
        tpsT=5
        tvqT=9.975
        calculTpsT = (internetFibreHybrideT*tpsT)/100
        calculTvqT = (internetFibreHybrideT*tvqT)/100
        prixTotalT = internetFibreHybrideT+calculTpsT+calculTvqT
        print("Sous-total                                 ",internetFibreHybrideT,"$")
        print("Montant TPS                                ",calculTpsT,"$")
        print("Montant TVQ                                ",calculTvqT,"$")
        print("Montant total                              ",prixTotalT,"$")
        print("            --------------------------------------------")
        print("                     Merci pour votre confiance")
    elif identifiantForfait=="E":    
        # saisieModePaiement()
        InternetETele()
        internetFibreHybrid=55.95
        forfait=30.95
        totalInternet=(internetFibreHybrid+forfait)
        tp=5
        tv=9.975
        calculTp = (totalInternet*tp)/100
        calculTv = (totalInternet*tv)/100
        prixTota = totalInternet+calculTp+calculTv
        print("Sous-total                                 ",totalInternet,"$")
        print("Montant TPS                                ",calculTp,"$")
        print("Montant TVQ                                ",calculTv,"$")
        print("Montant total                              ",prixTota,"$")
        print("            --------------------------------------------")
        print("                     Merci pour votre confiance")
    else:
        print("Entrée invalide !")
        forfaitID()
option = int(input("Entrez votre choix :"))
def saisieService():
            numeroDeService= input("Entrez les numéros des services (1 = Internet, 2 = Télé, et 3 = Internet et Télé) : ")
            numeroDeService= int( numeroDeService)
            if numeroDeService==1 :
                saisieIdentifiant()
            elif numeroDeService==2:
               forfaitID()
            elif numeroDeService==3:
               saisieIdentifiant()
            else:
                print("Entrée invalide !")
                saisieService()
def saisieIdentifiant():
           
            identifiantService = input("Entrez l'identifiant du forfait internet (50, 150, 500 ) :")
            identifiantService = int(identifiantService)
            if identifiantService==50:
                saisieModePaiement() 
                global identifiantService50
                identifiantService50 += 1
            elif  identifiantService==150:
                saisieModePaiement()
                global identifiantService150
                identifiantService150 += 1
            elif  identifiantService==500:
               forfaitID()
               global dentifiantService500
               dentifiantService500 += 1
              
               
            else:
                print("Entrée invalide !")
                saisieIdentifiant()

def InternetETele():
                   
                    modePaiement = input(" Entrez le mode de paiement (P ou p pour paiement préautorisé,\n C ou c pour paiement via mon compte, L ou l pour paiement bancaire\n en lig ne, I ou i pour paiement en institution bancaire):")
                    if modePaiement=="P" or modePaiement=="p" :
                        
                        print("--------------------------------------------------------------------------------")
                        now = date.today()
                        print("Internet-Tele Pour Tous\n")
                        print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                        print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
                        print("--------------------------------------------------------------------------------")
                        print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                        print("Adresse du client : ",adresseAbonner)
                        print("\n")
                        print("Mode de paiement : Paiement preautorisé ")
                        print("Descirption - forfait(s)                                              Prix")
                        print("--------------------------------------------------------------------------------")
                        print("Internet Fibre hybride 500                                           55,96$")
                        print("Forfait Excellent – choix de 35 chaînes à la carte                   30,95$")
                        
                    elif modePaiement=="L" or modePaiement=="l":
                        
                        
                        print("--------------------------------------------------------------------------------")
                        now = date.today()
                        print("Internet-Tele Pour Tous\n")
                        print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                        # print("Facture No : 1      Date et Heure",now,time.strftime("%H:%I:%S"))
                        print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
                        print("--------------------------------------------------------------------------------")
                        print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                        print("Adresse du client : ",adresseAbonner)
                        print("\n")
                        print("Mode de paiement : Paiement bancaire en ligne")
                        print("Descirption - forfait(s)                      Prix")
                        print("--------------------------------------------------------------------------------")
                        print("Internet Fibre hybride 50                    45,95$")
                        internetFibreHybrid=45.95
                        tp=5
                        tv=9.975
                        calculTp = (internetFibreHybrid*tp)/100
                        calculTv = (internetFibreHybrid*tv)/100
                        prixTota = internetFibreHybrid+calculTp+calculTv
                        print("Sous-total                                 ",internetFibreHybrid,"$")
                        print("Montant TPS                                ",calculTp,"$")
                        print("Montant TVQ                                ",calculTv,"$")
                        print("Montant total                              ",prixTota,"$")
                        print("            --------------------------------------------")
                        print("                     Merci pour votre confiance")
                    elif modePaiement=="C" or modePaiement== "c":
                        
                        print("--------------------------------------------------------------------------------")
                        now = date.today()
                        print("Internet-Tele Pour Tous\n")
                        print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                        # print("Facture No : 1      Date et Heure",now,time.strftime("%H:%I:%S"))
                        print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
                        print("--------------------------------------------------------------------------------")
                        print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                        print("Adresse du client : ",adresseAbonner)
                        print("\n")
                        print("Mode de paiement : Paiement via mon compte ")
                        print("Descirption - forfait(s)                                 Prix")
                        print("--------------------------------------------------------------------------------")
                        print("Internet Fibre hybride 50                               20,95$")
                    elif modePaiement=="I" or modePaiement=="i":
                         
                         print("--------------------------------------------------------------------------------")
                         now = date.today()
                         print("Internet-Tele Pour Tous\n")
                         print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                        #  print("Facture No : 1      Date et Heure",now,time.strftime("%H:%I:%S"))
                         print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
                         print("--------------------------------------------------------------------------------")
                         print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                         print("Adresse du client : ",adresseAbonner)
                         print("\n")
                         print("Mode de paiement : Paiement en institution bancaire")
                         print("Descirption - forfait(s)                      Prix")
                         print("--------------------------------------------------------------------------------")
                         print("Internet Fibre hybride 500                                   55,95$")
                         print("Forfait Excellent – choix de 35 chaînes à la carte           30,95$")
                         internetFibreHybrid=55.95
                         forfait=30.95
                         totalInternet=(internetFibreHybrid+forfait)
                         tp=5
                         tv=9.975
                         calculTp = (totalInternet*tp)/100
                         calculTv = (totalInternet*tv)/100
                         prixTota = totalInternet+calculTp+calculTv
                         
                         print("Sous-total                                 ",totalInternet,"$")
                         print("Montant TPS                                ",calculTp,"$")
                         print("Montant TVQ                                ",calculTv,"$")
                         print("Montant total                              ",prixTota,"$")
                         print("            --------------------------------------------")
                         print("                     Merci pour votre confiance")
                    else:
                            print("Entrée invalide !")
                            saisieModePaiement()
def saisieModePaiement():
               
            
                modePaiement = input(" Entrez le mode de paiement (P ou p pour paiement préautorisé,\n C ou c pour paiement via mon compte, L ou l pour paiement bancaire\n en lig ne, I ou i pour paiement en institution bancaire):")
                if modePaiement=="P" or modePaiement=="p" :
                   global factureIncre
                   factureIncre +=1
                   print("--------------------------------------------------------------------------------")
                   now = date.today()
                   print("Internet-Tele Pour Tous\n")
                   print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                   # print("Facture No : 1      Date et Heure",now,ti++me.strftime("%H:%I:%S"))
                   print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
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
                        
                        print("--------------------------------------------------------------------------------")
                        now = date.today()
                        print("Internet-Tele Pour Tous\n")
                        print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                        # print("Facture No : 1      Date et Heure",now,time.strftime("%H:%I:%S"))
                        print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
                        print("--------------------------------------------------------------------------------")
                        print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                        print("Adresse du client : ",adresseAbonner)
                        print("\n")
                        print("Mode de paiement : Paiement bancaire en ligne")
                        print("Descirption - forfait(s)                      Prix")
                        print("--------------------------------------------------------------------------------")
                        print("Internet Fibre hybride 50                    45,95$")
                   
                        internetFibreHybrid=45.95
                        tp=5
                        tv=9.975
                        calculTp = (internetFibreHybrid*tp)/100
                        calculTv = (internetFibreHybrid*tv)/100
                        prixTota = internetFibreHybrid+calculTp+calculTv
                        print("Sous-total                                 ",internetFibreHybrid,"$")
                        print("Montant TPS                                ",calculTp,"$")
                        print("Montant TVQ                                ",calculTv,"$")
                        print("Montant total                              ",prixTota,"$")
                        print("            --------------------------------------------")
                        print("                     Merci pour votre confiance")
                elif modePaiement=="C" or modePaiement== "c":
                    
                    print("--------------------------------------------------------------------------------")
                    now = date.today()
                    print("Internet-Tele Pour Tous\n")
                    print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                    # print("Facture No : 1      Date et Heure",now,time.strftime("%H:%I:%S"))
                    print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
                    print("--------------------------------------------------------------------------------")
                    print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                    print("Adresse du client : ",adresseAbonner)
                    print("\n")
                    print("Mode de paiement : Paiement via mon compte ")
                    print("Descirption - forfait(s)                                 Prix")
                    print("--------------------------------------------------------------------------------")
                    print("Internet Fibre hybride 50                               20,95$")
                elif modePaiement=="I" or modePaiement=="i":   
                         print("--------------------------------------------------------------------------------")
                         now = date.today()
                         print("Internet-Tele Pour Tous\n")
                         print("2020 rue Matata, Hakuna, QC    (450)  515-0055")
                        #  print("Facture No : 1      Date et Heure",now,time.strftime("%H:%I:%S"))
                         print("Facture No : ",factureIncre,"    Date et Heure  ",now,time.strftime("%H:%I:%S"))
                         print("--------------------------------------------------------------------------------")
                         print("Nom et prenom :",nomAbonner+" "+prenomAbonner,"  Telephone :",numeroTelAbonner)
                         print("Adresse du client : ",adresseAbonner)
                         print("\n")
                         print("Mode de paiement : Paiement en institution bancaire")
                         print("Descirption - forfait(s)                      Prix")
                         print("--------------------------------------------------------------------------------")
                         print("Internet Fibre hybride 500                                   55,95$")
                         print("Forfait Excellent – choix de 35 chaînes à la carte           30,95$")
                         internetFibreHybrid=55.95
                         forfait=30.95
                         totalInternet=(internetFibreHybrid+forfait)
                         tp=5
                         tv=9.975
                         calculTp = (totalInternet*tp)/100
                         calculTv = (totalInternet*tv)/100
                         prixTota = totalInternet+calculTp+calculTv
                         
                         print("Sous-total                                 ",totalInternet,"$")
                         print("Montant TPS                                ",calculTp,"$")
                         print("Montant TVQ                                ",calculTv,"$")
                         print("Montant total                              ",prixTota,"$")
                         print("            --------------------------------------------")
                         print("                     Merci pour votre confiance")
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
            now = date.today()
            print("---------------------------------------------")
            print("Internet-Télé Pour Tous")
            print("Date et Heure",now,time.strftime("%H:%I:%S"))
            print("-----------------------------------------------------")
            print("Forfaits                              nb.d'abonnes")
            print("******************************************************")
            print("Internet Fibre hybride 50                           ",identifiantService50)
            print("Internet Fibre hybride 150                          ",identifiantService150)
            print("Internet Fibre hybride 500                          ",dentifiantService500)
            print("Forfait Bien – choix de 15 chaînes à la carte       ",forfait15)
            print("Forfait Bien – choix de 25 chaînes à la carte       ",chaine25)
            print("Forfait Excellent – choix de 35 chaînes à la carte  ",dentifiantService500)

        elif option==3:
            option3()
        else:
            print("Entrée invalide !")
            print("***  Menu de choix  ***")
        print()
        menuChoix()
        option = int(input("Entrez votre choix :"))
print("Merci et à la prochaine !")
menuChoix()

