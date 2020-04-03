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
	#
        # valeurs récupérables dans config-gvr.xml:
	# Audio port PO Début: .//common-prm/rtp/audio-port-po/min
	# Audio port PO Fin: .//common-prm/rtp/audio-port-po/max
	# Audio port Radio Début: .//common-prm/rtp/audio-port-radio/min
	# Audio port Radio Fin: .//common-prm/rtp/audio-port-radio/max
	# Audio port AG Début: .//common-prm/rtp/audio-port-ag/min
	# Audio port AG Fin: .//common-prm/rtp/audio-port-ag/max
	# Audio port PO-FS Début: .//common-prm/rtp/audio-port-po-fs/min
	# Audio port PO-FS Fin: .//common-prm/rtp/audio-port-po-fs/max	
	# Audio port pabx Début: .//common-prm/rtp/audio-port-pabx/min
	# Audio port pabx Fin: .//common-prm/rtp/audio-port-pabx/max
	# Audio port AG-SGP Début: .//common-prm/rtp/audio-port-ag-sgp/min
	# Audio port AG-SGP Fin: .//common-prm/rtp/audio-port-ag-sgp/max
	# Audio port enr Début: .//common-prm/rtp/audio-port-enr/min
	# Audio port enr Fin: .//common-prm/rtp/audio-port-enr/max
	# Audio port asterisk Début: .//common-prm/rtp/audio-port-asterisk/min
	# Audio port asterisk Fin: .//common-prm/rtp/audio-port-asterisk/max
	# Enr RTSP: .//evr-app/rtsp-port
        # GCM IP 1 : .//gcm-app/network/ip/ipaddr1
        # GCM IP 2 : .//gcm-app/network/ip/ipaddr2
        # GCM masque de sous réseau : .//gcm-app/network/ip/snmsk
        # GCM Port : .//gcm-app/network/ip/ipport (port 5064 en écoute)
        # GCA IP 1 : .//gca-app/network/ip/ipport
        # GCA masque de sous réseau : .//gca-app/network/ip/snmsk
        # GCA Port : .//gca-app/network/ip/ipport
        # ...
	# Si secured=false on prend WS .//super-list/supervisor/secured
 	# SAPEX Port WS: : .//super-list/supervisor/ws-port
	# Asterisk SIP: .//asterisk-list/asterisk/listen-port
	# INTERSGP: .//asterisk-list/asterisk/r33-port
	# SAPEX Port WSS: : .//super-list/supervisor/wss-port
	

