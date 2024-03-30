import struct
import json
import hashlib
import time
import os

# Constants
DIFFICULTY_TARGET = "0000ffff00000000000000000000000000000000000000000000000000000000"
BITS = "1f00ffff"

# Sample public key and signature for testing
SAMPLE_PUBLIC_KEY = "04b5f2b6f01b02635bf0287685a03b089f8f82e583e49f0a4714f1ef29f336ef3fcedfacd9866fcb6b20389fc48623b41c8fb14a76b2c2c10cb58b300c72c4f28"  # Example public key
SAMPLE_SIGNATURE = "3045022100e1d42fb417a3b991db2a33e72044c4f2d171dc0144075c2d08931c8b1b230c7022068f7c2c7c38cb1c4ac01e8f92a855059dfb28ef3d3e01a88342281e0708580b"  # Example signature


def reverse_hex_bytes(hex_string):

    # Convert the hexadecimal string to a byte array.
    byte_array = bytearray.fromhex(hex_string)

    # Reverse the byte array.
    byte_array.reverse()

    # Convert the reversed byte array back to a hexadecimal string.
    reversed_hex_string = byte_array.hex()

    return reversed_hex_string


def double_hash_256(hex_string):
    # Convert hexadecimal string to bytes
    bytes_data = bytes.fromhex(hex_string)

    # First hash (SHA-256)
    first_hash = hashlib.sha256(bytes_data).digest()

    # Second hash (SHA-256)
    second_hash = hashlib.sha256(first_hash).digest()

    # Convert the result to hexadecimal string
    hashed_hex = second_hash.hex()

    return hashed_hex


# Function to verify signature
def verify_signature(transaction):
    # for vin in transaction["vin"]:
    #     prev_txid = vin["txid"]
    #     prev_vout = vin["vout"]
    #     prev_scriptpubkey = vin["prevout"]["scriptpubkey"]
    #     prev_value = vin["prevout"]["value"]
    #     signature = vin["scriptsig"][0]  # First element of scriptsig array

    #     # Concatenate and hash the transaction data
    #     tx_data = prev_txid + str(prev_vout) + prev_scriptpubkey + str(prev_value)
    #     tx_hash = hashlib.sha256(tx_data.encode()).digest()

    #     # Decode signature
    #     signature = bytes.fromhex(signature)
    #     sig = ecdsa.util.sigdecode_der(signature)

    #     # Verify signature
    #     vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(SAMPLE_PUBLIC_KEY), curve=ecdsa.SECP256k1)
    #     if not vk.verify(sig, tx_hash):
    #         return False

    return True


# Function to validate transactions
def validate_transaction(transaction):
    # todo
    # Implement your transaction validation logic here
    return verify_signature(transaction)


# Function to calculate merkle root of transactions
def calculate_merkle_root(transactions):
    # todo
    # Implement your merkle root calculation logic here
    result = hashlib.sha256(transactions[0].encode()).hexdigest()
    result = hashlib.sha256(result.encode()).hexdigest()
    # result = reverse_hex_bytes(result)
    print("Merkle root: ", result)
    return result


# Function to calculate block hash
def calculate_block_hash(header):
    temp = hashlib.sha256(header.encode()).hexdigest()
    return hashlib.sha256(temp.encode()).hexdigest()


def serialize_block_header(block):
    serialized_block_header = (
        struct.pack("<I", block["version"])
        + bytes.fromhex(block["previous_block_hash"])[::-1]
        + bytes.fromhex(block["merkle_root"])[::-1]
        + struct.pack("<I", block["timestamp"])
        + bytes.fromhex(block["difficulty_target"])[::-1]
        + struct.pack("<I", block["nonce"])
    )
    return serialized_block_header.hex()


# Function to mine the block
def mine_block(merkle_root):
    block = {
        "version": 2,
        "previous_block_hash": "0000000000000000000000000000000000000000000000000000000000000000",
        "merkle_root": merkle_root,
        "timestamp": int(time.time()),
        "difficulty_target": BITS,
        "nonce": 0,
    }
    print("Mining block...")
    while True:
        block_header = serialize_block_header(block)
        block_hash = double_hash_256(block_header)
        block_hash = reverse_hex_bytes(block_hash)
        # print("Block Hash: ", block_hash)
        if block_hash < DIFFICULTY_TARGET:
            print("Block mined successfully!")
            print("Block hash: ", block_hash)
            print("Nonce: ", block["nonce"])
            return block
        block["nonce"] += 1
         # Update block header


# Main function
def main():
    print("Reading transactions from mempool...")
    transactions = []

    # Read transactions from mempool folder
    # for filename in os.listdir("mempool"):
    #     with open(os.path.join("mempool", filename), "r") as file:
    #         transaction = json.load(file)
    #         transactions.append(transaction)

    # # Serialize the transactions
    # print("Validating transactions...")
    # # Validate transactions
    # valid_transactions = [
    #     transaction for transaction in transactions if validate_transaction(transaction)
    # ]

    # Create coinbase transaction
    print("Creating coinbase transaction...")
    coinbase_transaction = {
        "version": "01000000",
        "locktime": "00000000",
        "vin": [
            {
                "txid": "0000000000000000000000000000000000000000000000000000000000000000",
                "vout": "ffffffff",
                "scriptsig": "04233fa04e028b12",
                "sequence": "ffffffff",
            }
        ],
        "vout": [
            {
                "scriptpubkey": "41047eda6bd04fb27cab6e7c28c99b94977f073e912f25d1ff7165d9c95cd9bbe6da7e7ad7f2acb09e0ced91705f7616af53bee51a238b7dc527f2be0aa60469d140ac",
                "amount": "30490b2a01000000",
            }
        ],
    }

    raw_coinbase_transaction = "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0804233fa04e028b12ffffffff0130490b2a010000004341047eda6bd04fb27cab6e7c28c99b94977f073e912f25d1ff7165d9c95cd9bbe6da7e7ad7f2acb09e0ced91705f7616af53bee51a238b7dc527f2be0aa60469d140ac00000000"
    coinbase_transaction_id = double_hash_256(raw_coinbase_transaction)
    # coinbase_transaction_id = reverse_hex_bytes(coinbase_transaction_id)
    # Add coinbase transaction to valid transactions
    transactions.insert(0, coinbase_transaction_id)

    # Calculate merkle root
    print("Calculating merkle root...")
    merkle_root = coinbase_transaction_id
    # merkle_root = calculate_merkle_root(valid_transactions)

    # Mine the block
    mined_block = mine_block(merkle_root)

    # Output the block information to output.txt
    print("Writing block information to output.txt...")
    with open("output.txt", "w") as output_file:
        block_header = serialize_block_header(mined_block)
        output_file.write(block_header)
        output_file.write("\n")

        # Write serialized coinbase transaction to output.txt
        output_file.write(raw_coinbase_transaction)
        output_file.write("\n")

        # Write transaction IDs (txids) of the transactions mined in the block
        # Start with the coinbase transaction
        output_file.write(reverse_hex_bytes(coinbase_transaction_id))
        output_file.write("\n")

        # Write txids of other transactions, if any
        # for transaction in mined_block["transactions"][1:]:
        #     output_file.write(transaction["txid"])
        #     output_file.write("\n")


if __name__ == "__main__":
    main()
