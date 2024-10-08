from web3 import Web3


w3 = Web3(Web3.HTTPProvider('https://1rpc.io/bnb'))

contract_address = '0xEC4549caDcE5DA21Df6E6422d448034B5233bFbC'
public_key = ""  # CHANGE THIS
amount = 1  # change 1 to whatever. e.g. 0.1 for 0.1 BNB etc. # CHANGE THIS
private_key = ""  # CHANGE THIS. put 0x in front of privkey
contract_address_of_coin = ""  # CHANGE THIS



function_signature = '0x3deec419'

# contract address, amount, min amount (prob no one mevs this)
input_params = [contract_address_of_coin, int(1000000000000000000 * amount), 1000000]

calldata = function_signature + '000000000000000000000000'
for param in input_params:
    if isinstance(param, str) and param.startswith('0x'):
        calldata += param[2:]
    else:
        calldata += f'{int(param):064x}'

nonce = w3.eth.get_transaction_count(public_key)

tx = {
    'to': contract_address,
    'data': calldata,
    'gas': 140000,
    'gasPrice': w3.to_wei('3', 'gwei'),
    'nonce': nonce,
    'chainId': 56,  # Binance Smart Chain mainnet chainId
    'value': int(1100000000000000000 * amount) 
}



signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print(f'https://bscscan.com/tx/0x{tx_hash.hex()}')
