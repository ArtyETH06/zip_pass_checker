#Imports
import zipfile
import argparse

#Création de la fonction
def has_password(zip_file):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zf:
            zf.readall()
            return False
    except:
        return True


#Parser creation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check si un fichier ZIP contient un mot de passe")
    parser.add_argument("-f", type=str, help="Sélectionne le fichier à vérifier si il contient un mot de passe.")
    args = parser.parse_args()

print(args.f)

#Affectation de Zip file à la valeur de l'argument f
zip_file = args.f

#test + Réponses
if has_password(zip_file):
    print(f'{zip_file} is password protected.')
else:
    print(f'{zip_file} is not password protected.')
