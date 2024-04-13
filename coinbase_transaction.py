from hashing import reverse_hex_bytes, double_hash_256, compact_size


def amount(fees):
    amt = fees + 1250000000
    return reverse_hex_bytes(hex(amt).lstrip("0x").zfill(16))


def create_coinbase_transaction(fees, wtxid_commitment):
    coinbase_transaction = {
        "version": "01000000",
        "marker": "00",
        "flag": "01",
        "inputcount": "01",
        "inputs": [
            {
                "txid": "0000000000000000000000000000000000000000000000000000000000000000",
                "vout": "ffffffff",
                "scriptsigsize": "25",
                "scriptsig": "03233708184d696e656420627920416e74506f6f6c373946205b8160a4256c0000946e0100",
                "sequence": "ffffffff",
            }
        ],
        "outputcount": "02",
        "outputs": [
            {
                "amount": amount(fees),
                "scriptpubkeysize": "19",
                "scriptpubkey": "76a914edf10a7fac6b32e24daa5305c723f3de58db1bc888ac",
            },
            {
                "amount": "0000000000000000",
                "scriptpubkeysize": compact_size(int(len(wtxid_commitment) / 2)),
                "scriptpubkey": wtxid_commitment,
            },
        ],
        "witness": [
            {
                "stackitems": "01",
                "0": {
                    "size": "20",
                    "item": "0000000000000000000000000000000000000000000000000000000000000000",
                },
            }
        ],
        "locktime": "00000000",
    }

    # raw_coinbase_transaction = (
    #     "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0804233fa04e028b12ffffffff01"
    #     + amount(fees)
    #     + "4341047eda6bd04fb27cab6e7c28c99b94977f073e912f25d1ff7165d9c95cd9bbe6da7e7ad7f2acb09e0ced91705f7616af53bee51a238b7dc527f2be0aa60469d140ac00000000"
    # )

    raw_coinbase_transaction = (
        "010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff2503233708184d696e656420627920416e74506f6f6c373946205b8160a4256c0000946e0100ffffffff02 "
        + amount(fees)
        + "1976a914edf10a7fac6b32e24daa5305c723f3de58db1bc888ac0000000000000000"
        + compact_size(int(len(wtxid_commitment) / 2))
        + wtxid_commitment
        + "0120000000000000000000000000000000000000000000000000000000000000000000000000"
    )

    txid = double_hash_256(raw_coinbase_transaction)
    natural_txid = reverse_hex_bytes(txid)
    coinbase_transaction["txid"] = natural_txid
    coinbase_transaction["raw"] = raw_coinbase_transaction
    coinbase_transaction["wtxid"] = (
        "0000000000000000000000000000000000000000000000000000000000000000"
    )

    return coinbase_transaction
