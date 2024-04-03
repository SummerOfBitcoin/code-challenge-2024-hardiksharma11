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

def sha_256(hex_string):
    
        bytes_data = bytes.fromhex(hex_string)
        hashed = hashlib.sha256(bytes_data).hexdigest()
        return hashed

def compact_size(i):
    if i <= 252:
        compactsize = i.to_bytes(1, 'little').hex()
    elif i <= 65535:
        compactsize = 'fd' + i.to_bytes(2, 'little').hex()
    elif i <= 4294967295:
        compactsize = 'fe' + i.to_bytes(4, 'little').hex()
    elif i <= 18446744073709551615:
        compactsize = 'ff' + i.to_bytes(8, 'little').hex()
    else:
        raise ValueError("Integer is too large")

    return compactsize