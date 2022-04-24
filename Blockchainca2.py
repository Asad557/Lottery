from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from web3 import Web3
import json
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/c10b7840ad8a4ff1b9da434eb67349a6"))
balance = w3.eth.getBalance("Admin_account address")
print(balance)
#ABI
ABI= json.loads('[{"inputs":[],"name":"pickWinner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"stateMutability":"payable","type":"receive"},{"inputs":[],"name":"admin","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"players","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
#define address
wallet_address="Admin_account address"
wallet_address = Web3.toChecksumAddress(wallet_address)
contract_address ="Lottery Contract address"
contract_address = Web3.toChecksumAddress(contract_address)
private_key = "Private Key"

# define contract
contract = w3.eth.contract(contract_address, abi=ABI)

#greet
print (contract.functions.getBalance().call())
print('lottery started...')
print (contract.functions.pickWinner().call())

  
#pick winner -> only admins can call this funcion
def pickwinner():
    nonce = w3.eth.getTransactionCount(admin_wallet_address)
    transaction = contract.functions.pickWinner().buildTransaction({
        'chainId': 4,
        'gas': 1400000,
        'gasPrice': w3.toWei('160', 'gwei'),
        'nonce': nonce,
        'from': admin_wallet_address
    })
    signed_txt = w3.eth.account.signTransaction(transaction, private_key = admin_private_key)
    w3.eth.sendRawTransaction(signed_txt.rawTransaction)
