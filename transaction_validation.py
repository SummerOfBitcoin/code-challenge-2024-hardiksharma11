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
