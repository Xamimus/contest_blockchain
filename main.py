""" FLAKE8 : py -m flake8 """
from classes.Block import Block
from classes.Chain import Chain
from classes.Wallet import Wallet

def run():
    chain = Chain()
    bloc224 = chain.get_block("00006e5a02837f52d461b50c6523d3e14174db729c51d325838703707132579b")
    """ poids du bloc choisi """
    print(bloc224.weight)
    client = Wallet("14938570948877436095580126826539516641")
    print(client.balance)
    chain.add_transaction("101171254103012972354878941626424419326","14938570948877436095580126826539516641", 10)


if __name__ == '__main__':
    run()