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


def check_input_greater_tha_output(transactions):
    new_transactions = []
    for transaction in transactions:
        if(transaction["vin"][0]["prevout"]["scriptpubkey_type"] != "v1_p2tr"): continue
        input_sum = 0
        output_sum = 0
        for vin in transaction["vin"]:
            input_sum += vin["prevout"]["value"]
        for vout in transaction["vout"]:
            output_sum += vout["value"]
        if input_sum > output_sum:
            transaction["fees"] = input_sum - output_sum
            new_transactions.append(transaction)


    return new_transactions

# Function to validate transactions
def validate_transaction(transactions):
    # todo
    # Implement your transaction validation logic here
    transactions = check_input_greater_tha_output(transactions)
    return transactions
