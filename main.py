import os
import json
import hashlib
import time
import ecdsa

# Constants
DIFFICULTY_TARGET = "0000ffff00000000000000000000000000000000000000000000000000000000"

# Sample public key and signature for testing
SAMPLE_PUBLIC_KEY = "04b5f2b6f01b02635bf0287685a03b089f8f82e583e49f0a4714f1ef29f336ef3fcedfacd9866fcb6b20389fc48623b41c8fb14a76b2c2c10cb58b300c72c4f28"  # Example public key
SAMPLE_SIGNATURE = "3045022100e1d42fb417a3b991db2a33e72044c4f2d171dc0144075c2d08931c8b1b230c7022068f7c2c7c38cb1c4ac01e8f92a855059dfb28ef3d3e01a88342281e0708580b"  # Example signature

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
    #todo
    # Implement your transaction validation logic here
    return verify_signature(transaction)  

# Function to calculate merkle root of transactions
def calculate_merkle_root(transactions):
    #todo
    # Implement your merkle root calculation logic here
    return "merkle_root"  

# Function to calculate block hash
def calculate_block_hash(header):
    return hashlib.sha256(header.encode()).hexdigest()

# Function to mine the block
def mine_block(transactions, merkle_root):
    block = {
        "version": 1,
        "previous_block_hash": "0000000000000000000000000000000000000000000000000000000000000000",
        "merkle_root": merkle_root,
        "timestamp": int(time.time()),
        "difficulty_target": DIFFICULTY_TARGET,
        "nonce": 0,
        "transactions": transactions
    }
    block_header = json.dumps(block, separators=(',', ':'), sort_keys=True)  # Serialize block header
    print("Mining block...")
    while True:
        block_hash = calculate_block_hash(block_header)
        if block_hash < DIFFICULTY_TARGET:
            print("Block mined successfully!")
            return block
        block["nonce"] += 1
        block_header = json.dumps(block, separators=(',', ':'), sort_keys=True)  # Update block header

# Main function
def main():
    print("Reading transactions from mempool...")
    transactions = []

    # Read transactions from mempool folder
    for filename in os.listdir("mempool"):
        with open(os.path.join("mempool", filename), "r") as file:
            transaction = json.load(file)
            transactions.append(transaction)

    print("Validating transactions...")
    # Validate transactions
    valid_transactions = [transaction for transaction in transactions if validate_transaction(transaction)]

    # Create coinbase transaction
    print("Creating coinbase transaction...")
    coinbase_transaction = {
        "txid": "coinbase_txid",
        "fee": 50,  
        "vin": [],

    }

    # Add coinbase transaction to valid transactions
    valid_transactions.insert(0, coinbase_transaction)

    # Calculate merkle root
    print("Calculating merkle root...")
    merkle_root = calculate_merkle_root(valid_transactions)

    # Mine the block
    mined_block = mine_block(valid_transactions, merkle_root)

    # Output the block information to output.txt
    print("Writing block information to output.txt...")
    with open("output.txt", "w") as output_file:
        output_file.write(json.dumps(mined_block, indent=4))

if __name__ == "__main__":
    main()
