import hashlib

def calculate_merkle_root(transactions):
    # todo
    # Implement your merkle root calculation logic here
    result = hashlib.sha256(transactions[0].encode()).hexdigest()
    result = hashlib.sha256(result.encode()).hexdigest()
    # result = reverse_hex_bytes(result)
    print("Merkle root: ", result)
    return result