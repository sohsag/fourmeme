from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://1rpc.io/bnb'))


contract_address = '0xEC4549caDcE5DA21Df6E6422d448034B5233bFbC'
function_signature = '0x3deec419'

# contract address of coin, change 1 to whatever. e.g. 0.1 for 0.1 BNB etc., leave as is
input_params = ['0x5c9e15ff4aded6b1ebcbc83f18f6554175bd82ac', 1000000000000000000 * 1, 1000000]


calldata = function_signature + '000000000000000000000000'
for param in input_params:
    if isinstance(param, str) and param.startswith('0x'):
        calldata += param[2:]
    else:
        calldata += f'{int(param):064x}'


sender_address = '' # ur address
nonce = w3.eth.get_transaction_count(sender_address)


tx = {
    'to': contract_address,
    'data': calldata,
    'gas': 140000,
    'gasPrice': w3.to_wei('3', 'gwei'),
    'nonce': nonce,
    'chainId': 56,  # Binance Smart Chain mainnet chainId
    'value': 1100000000000000000 * 1 # change 1 to whatever. e.g. 0.1 for 0.1 BNB etc.
}


private_key = '' # privkey with 0x infront
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)


tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print(f'https://bscscan.com/tx/0x{tx_hash.hex()}')
