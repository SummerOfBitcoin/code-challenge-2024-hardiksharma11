from block_mining import mine_block, serialize_block_header
from merkle_root import calculate_merkle_root
from coinbase_transaction import create_coinbase_transaction
from hashing import double_hash_256, reverse_hex_bytes
from transaction_validation import validate_transaction
from generate_output import generate_output
from read_transactions import read_transactions
from serialize_transaction import serialize_transactions

import json


# Sample public key and signature for testing
SAMPLE_PUBLIC_KEY = "04b5f2b6f01b02635bf0287685a03b089f8f82e583e49f0a4714f1ef29f336ef3fcedfacd9866fcb6b20389fc48623b41c8fb14a76b2c2c10cb58b300c72c4f28"  # Example public key
SAMPLE_SIGNATURE = "3045022100e1d42fb417a3b991db2a33e72044c4f2d171dc0144075c2d08931c8b1b230c7022068f7c2c7c38cb1c4ac01e8f92a855059dfb28ef3d3e01a88342281e0708580b"  # Example signature


# Main function
def main():
    print("Reading transactions from mempool...")
    transactions = read_transactions()
    transactions = serialize_transactions(transactions)

    # Create coinbase transaction
    # print("Creating coinbase transaction...")

    # raw_coinbase_transaction = create_coinbase_transaction()
    # coinbase_transaction_id = double_hash_256(raw_coinbase_transaction)
    # transactions.insert(0, coinbase_transaction_id)

    # # Calculate merkle root
    # print("Calculating merkle root...")
    # merkle_root = coinbase_transaction_id
    # # merkle_root = calculate_merkle_root(valid_transactions)

    # # Mine the block
    # mined_block = mine_block(merkle_root)

    # generate_output(mined_block,raw_coinbase_transaction,coinbase_transaction_id)
    

if __name__ == "__main__":
    main()
