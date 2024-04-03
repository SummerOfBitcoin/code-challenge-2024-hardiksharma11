import os
import json

def read_transactions():
    # Read transactions from mempool folder
    transactions = []
    for filename in os.listdir("mempool"):
        with open(os.path.join("mempool", filename), "r") as file:
            transaction = json.load(file)
            transaction["txid_hash"]= filename.split(".")[0]
            transactions.append(transaction)

    return transactions