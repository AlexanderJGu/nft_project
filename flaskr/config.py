from web3 import Web3, HTTPProvider

import json

CHAIN_ID = 3 # 4 for Rinkeby, 56 for BSC, 97 for BSC testnet,  Ropsten 3
GAS_LIMIT = 356608
GAS_PRICE = 80 # 5 for BSC mainnet, 80 for BSC testnet, allways check network before

nft_json = "./flaskr/abi/erc721.json"

with open(nft_json) as f:
    nft_artifact = json.load(f)
nft_abi = nft_artifact['abi']

nft_address = "0x7c07AAfA429D952Ac3Fde9Ca037003EDB57cE14e"

w3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/f5e1862305274640b76f487f5bba437c"))
