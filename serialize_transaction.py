from hashing import double_hash_256, reverse_hex_bytes, sha_256, compact_size

def serialize_transactions(transactions):
    for i in range(len(transactions)):
        serialized_transaction = serialize_transaction(transactions[i])
        txid=""
        
        txid = double_hash_256(serialized_transaction)
        
        natural_txid = reverse_hex_bytes(txid)
        txid_hash = sha_256(natural_txid)
        if(txid_hash != transactions[i]["txid_hash"]):
            print("Transaction ID: ", transactions[i]["vin"][0]["txid"])
            print("Serialized Transaction: ", serialized_transaction)
            
        transactions[i]["txid"] = natural_txid
        transactions[i]["raw_transaction"] = serialized_transaction
    
    return transactions

def serialize_transaction(transaction):
    serialized_transaction = ""
    
    version = reverse_hex_bytes(hex(transaction["version"]).lstrip("0x").zfill(8))

    marker_flag = "0001"

    input_count = compact_size(int(len(transaction["vin"])))

    vin = serialize_vin(transaction["vin"])

    output_count = compact_size(int(len(transaction["vout"])))

    vout = serialize_vout(transaction["vout"])

    locktime = reverse_hex_bytes(hex(transaction["locktime"]).lstrip("0x").zfill(8))

    serialized_transaction += version + input_count + vin + output_count + vout + locktime

    return serialized_transaction


def serialize_vin(vin):
    serialized_vin = ""
    for i in range(len(vin)):
        txid = reverse_hex_bytes(vin[i]["txid"])
        vout = reverse_hex_bytes(hex(vin[i]["vout"]).lstrip("0x").zfill(8))
        script_sig_size = compact_size(int(len(vin[i]["scriptsig"])/2))
        script_sig = vin[i]["scriptsig"]
        sequence = reverse_hex_bytes(hex(vin[i]["sequence"]).lstrip("0x").zfill(8))

        serialized_vin += txid + vout + script_sig_size + script_sig + sequence

    return serialized_vin

def serialize_vout(vout):
    serialized_vout = ""
    for i in range(len(vout)):
        amount = reverse_hex_bytes(hex(vout[i]["value"]).lstrip("0x").zfill(16))
        scriptpubkey_size = compact_size(int(len(vout[i]["scriptpubkey"])/2))
        scriptpubkey = vout[i]["scriptpubkey"]

        serialized_vout += amount + scriptpubkey_size + scriptpubkey

    return serialized_vout

    
