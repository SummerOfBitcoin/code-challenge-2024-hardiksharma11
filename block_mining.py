import struct
from hashing import double_hash_256, reverse_hex_bytes
import time

DIFFICULTY_TARGET = "0000ffff00000000000000000000000000000000000000000000000000000000"
BITS = "1f00ffff"

def serialize_block_header(block):
    serialized_block_header = (
        bytes.fromhex(block["version"])
        + bytes.fromhex(block["previous_block_hash"])[::-1]
        + bytes.fromhex(block["merkle_root"])[::-1]
        + struct.pack("<I", block["timestamp"])
        + bytes.fromhex(block["difficulty_target"])[::-1]
        + struct.pack("<I", block["nonce"])
    )
    return serialized_block_header.hex()

def mine_block(merkle_root):
    block = {
        "version": "00000020",
        "previous_block_hash": "0000000000000000000000000000000000000000000000000000000000000000",
        "merkle_root": merkle_root,
        "timestamp": int(time.time()),
        "difficulty_target": BITS,
        "nonce": 0,
    }
    print("Mining block...")
    while True:
        block_header = serialize_block_header(block)
        block_hash = double_hash_256(block_header)
        block_hash = reverse_hex_bytes(block_hash)
        # print("Block Hash: ", block_hash)
        if block_hash < DIFFICULTY_TARGET:
            print("Block mined successfully!")
            print("Block hash: ", block_hash)
            print("Nonce: ", block["nonce"])
            return block
        block["nonce"] += 1
    
