from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from web3 import Web3
import json
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/c10b7840ad8a4ff1b9da434eb67349a6"))
balance = w3.eth.getBalance("0xf4554Bc3e5D4B85Cb13BFf1C4c9B15ade90baF0a")
print(balance)
#ABI
ABI= json.loads('[{"inputs":[],"name":"pickWinner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"stateMutability":"payable","type":"receive"},{"inputs":[],"name":"admin","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"players","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
#define address
wallet_address="0xf4554Bc3e5D4B85Cb13BFf1C4c9B15ade90baF0a"
wallet_address = Web3.toChecksumAddress(wallet_address)
contract_address ="0x547B34e881D2c826505a4366460F31837e32D63b"
contract_address = Web3.toChecksumAddress(contract_address)
private_key = "eb47ea56a6e5d9db997f536803c384953f0e1686872711c55bc213f0b034a4b6"

# define contract
contract = w3.eth.contract(contract_address, abi=ABI)

#greet
print (contract.functions.getBalance().call())
print('lottery started...')
print (contract.functions.pickWinner().call())


'''
#change greeting
nonce = w3.eth.getTransactionCount(wallet_address)
transaction = contract.functions.getBalance.setGreeting("Hello Paul, Below is the total amount received for lottery").buildTransaction({
#transaction = contract.functions.getBalance.buildTransaction({
    'chainId': 4,
    'gas': 1400000,
    'gasPrice': w3.toWei('160', 'gwei'),
    'nonce': nonce,
    'from':wallet_address
})
signed_txt = w3.eth.account.signTransaction(transaction, private_key = private_key)
w3.eth.sendRawTransaction(signed_txt.rawTransaction) 
'''
  

