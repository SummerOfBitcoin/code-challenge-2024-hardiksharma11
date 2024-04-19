from block_mining import mine_block, serialize_block_header
from merkle_root import calculate_merkle_root
from coinbase_transaction import create_coinbase_transaction
from hashing import double_hash_256, reverse_hex_bytes
from transaction_validation import validate_transaction
from generate_output import generate_output
from read_transactions import read_transactions
from serialize_transaction import serialize_transactions
from transaction_validation import validate_transaction
import json

def get_fee(transaction):
    return transaction['fees']

# Main function
def main():

    transactions = read_transactions()
    transactions = serialize_transactions(transactions)
    transactions = validate_transaction(transactions)
    # transactions = sorted(transactions, key=get_fee)
    transactions = transactions[0:5]

    print(json.dumps(transactions,indent=4))

    fees = 0
    for transaction in transactions:
        fees += transaction["fees"]
    
    wtxid_commitment = calculate_merkle_root(transactions,"wtxid")
    print("wtxid_commitment1: ", wtxid_commitment)
    wtxid_commitment = double_hash_256(wtxid_commitment + "0000000000000000000000000000000000000000000000000000000000000000")
    wtxid_commitment = "6a24aa21a9ed" + wtxid_commitment
    print("wtxid_commitment: ", wtxid_commitment)
    
    coinbase = create_coinbase_transaction(fees,wtxid_commitment)
    transactions.insert(0, coinbase)

   
    # coinbase_transaction_id = double_hash_256(raw_coinbase_transaction)
    # transactions.insert(0, coinbase_transaction_id)

    # # Calculate merkle root
    # print("Calculating merkle root...")
    # merkle_root = coinbase_transaction_id
    merkle_root = calculate_merkle_root(transactions,"txid")

    # # Mine the block
    mined_block = mine_block(reverse_hex_bytes(merkle_root))

    generate_output(mined_block,coinbase["raw"],transactions)
    

if __name__ == "__main__":
    main()
