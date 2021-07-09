""" FLAKE8 : py -m flake8 """
from classes.Block import Block
from classes.Chain import Chain
from classes.Wallet import Wallet
import time

def run():
    print("Génération de la Blockchain...")
    time.sleep(1)
    chain = Chain()
    print("La chain contient les blocs représentés par les fichiers suivants : ")
    for p in chain.blocks:
        time.sleep(0.3)
        print(p)
    print("Création de votre nouveau wallet...")
    time.sleep(1.2)
    wallet = Wallet()
    print("Terminé ! Votre Wallet a pour identifiant unique : " + str(wallet.unique_id))
    print("Vous disposez du solde suivant : " + str(wallet.balance))
    time.sleep(0.8)
    """ Poids du bloc choisi """
    bloc = chain.get_block("00")
    print("Une transaction va maintenant s'effectuer sur le premier bloc disposant d'assez de place, le bloc : " + str(bloc.hash))
    saler = Wallet("14938570948877436095580126826539516641")
    print("Wallet du vendeur = " + str(saler.unique_id))
    print("Solde du vendeur = " + str(saler.balance))
    time.sleep(0.8)
    chain.add_transaction("14938570948877436095580126826539516641", str(wallet.unique_id), 10)
    print("Vous lui créditez la somme de 10")
    time.sleep(0.8)
    print("Voici le nouveau solde du vendeur : " + str(saler.balance))
    print("Et voici le votre : " + str(wallet.balance))
    time.sleep(0.8)
    time.sleep(0.8)
    print("Fin de la démonstration")

if __name__ == '__main__':
    run()