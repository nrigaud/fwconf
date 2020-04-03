#!/usr/bin/env python3

#Cartouche
    #Référence,prérequis environnement, auteur, version, historique
  

#importation des modules requis
import configparser #module pour l'utilisation d'un fichier ini
import xml.etree.ElementTree #module de parcours xml
import subprocess #module utilisé pour invoquer firewall-cmd

#chargement du fichier de configuration
config = configparser.ConfigParser()
config.read('./fwconfig.ini')

#Service à déclarer (dans le fichier INI)

#Fonctions
	
#Fonction pour vérifier qu'un service est démarré
def is_active(service):
 """Return True if service is running"""
 proc = subprocess.Popen(["systemctl", "status", service], shell=True,stdout=subprocess.PIPE)
 stdout_list = proc.communicate()[0].decode("utf-8").split('\n')
 for line in stdout_list:
  if 'Active:' in line:
   if '(running)' in line:
    return True
 return False
#Exemple d'utilisation de la fonction
#if is_active("firewalld") == True:
# print("True")
#elif is_active("firewalld") == False:
# print("False")
#else:
# print("Unknown state")


#Fonction pour la création des services de pare-feu
def create_fw_services(servicename,description,port)
 #On vérifie si firewalld est démarré et on définit la commande à utiliser
 if is_active("firewalld") == True:
  fwcmd = "firewall-cmd"
 else:
  fwcmd = "firewall-offline-cmd"

 #Attention avec shell=true https://docs.python.org/fr/3/library/subprocess.html#security-considerations
 process = subprocess.run("fwcmd --permanent --add-rich-rule=\'{0}\'".format(rule),shell=True)
 
#Fonction de paramétrage des ports dans les services
	#On vérifie d'abord l'état du pare-feu
    #utilisation de la commande firewall-cmd si le pare-feu est démarré
    #utilisation de la commande firewall-offline-cmd si le pare-feu est arrêté
    
# Affectation des services dans des zones (interactif)
    # Attention deux types de zone: interface et réseau source (à utiliser en fonction des besoins)
      
#Fonction de surveillance de modification des fichiers (peut être pas utile si on charge systématiquement la configuration)
	#On regarde la date de dernière modification 

#Fonction de collecte des informations contenues dans les fichiers de configuration
    #On utilise le parser xml.etree.ElementTree
    #Prévoir de gérer les erreurs dans le cas ou le champ n'existe pas ou est vide
    #Contenu à prendre:
    # exemple de récupération d'une valeur précise
        # ipaddr1_var = root.find(".//gcm-app/network/ip/ipaddr1").text
        # valeurs récupérables dans config-gvr.xml:
        # GCM IP 1 : .//gcm-app/network/ip/ipaddr1
        # GCM IP 2 : .//gcm-app/network/ip/ipaddr2
        # GCM masque de sous réseau : .//gcm-app/network/ip/snmsk
        # GCM Port : .//gcm-app/network/ip/ipport
        # GCA IP 1 : .//gca-app/network/ip/ipport
        # GCA masque de sous réseau : .//gca-app/network/ip/snmsk
        # GCA Port : .//gca-app/network/ip/ipport
        # ...
