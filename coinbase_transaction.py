from hashing import reverse_hex_bytes,double_hash_256

def amount(fees):
    amt = fees + 5000000000
    return reverse_hex_bytes(hex(amt).lstrip("0x").zfill(16))

def create_coinbase_transaction(fees):
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

    raw_coinbase_transaction = "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0804233fa04e028b12ffffffff01" +amount(fees) + "4341047eda6bd04fb27cab6e7c28c99b94977f073e912f25d1ff7165d9c95cd9bbe6da7e7ad7f2acb09e0ced91705f7616af53bee51a238b7dc527f2be0aa60469d140ac00000000"

    txid = double_hash_256(raw_coinbase_transaction)
    natural_txid = reverse_hex_bytes(txid)
    coinbase_transaction["txid"] = natural_txid
    coinbase_transaction["raw"] = raw_coinbase_transaction

    return coinbase_transaction

