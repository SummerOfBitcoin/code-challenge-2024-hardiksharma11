import hashlib

def double_hash_256(hex_string):

    bytes_data = bytes.fromhex(hex_string)
    first_hash = hashlib.sha256(bytes_data).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    hashed_hex = second_hash.hex()
    return hashed_hex

def reverse_hex_bytes(hex_string):

    byte_array = bytearray.fromhex(hex_string)
    byte_array.reverse()
    reversed_hex_string = byte_array.hex()
    return reversed_hex_string
