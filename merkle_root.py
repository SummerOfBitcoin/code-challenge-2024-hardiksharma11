from hashing import double_hash_256,reverse_hex_bytes

def calculate_merkle_root(transactions,type):
    storeHash = []
    for i in range(len(transactions)):
        storeHash.append(reverse_hex_bytes(transactions[i][type]))

    while len(storeHash) > 1:
        if len(storeHash) % 2 != 0:
            storeHash.append(storeHash[-1])
        newStoreHash = []
        for i in range(0, len(storeHash), 2):
            newStoreHash.append(double_hash_256(storeHash[i] + storeHash[i+1]))
        storeHash = newStoreHash


    return storeHash[0]