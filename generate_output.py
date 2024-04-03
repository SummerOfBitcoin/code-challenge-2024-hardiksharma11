from block_mining import serialize_block_header

def generate_output(mined_block, raw_coinbase_transaction, coinbase_transaction_id):

    print("Writing block information to output.txt...")
    with open("output.txt", "w") as output_file:
        block_header = serialize_block_header(mined_block)
        output_file.write(block_header)
        output_file.write("\n")

        # Write serialized coinbase transaction to output.txt
        output_file.write(raw_coinbase_transaction)
        output_file.write("\n")

        # Write transaction IDs (txids) of the transactions mined in the block
        # Start with the coinbase transaction
        output_file.write(coinbase_transaction_id)
        # output_file.write(reverse_hex_bytes(coinbase_transaction_id))
        output_file.write("\n")

        # Write txids of other transactions, if any
        # for transaction in mined_block["transactions"][1:]:
        #     output_file.write(transaction["txid"])
        #     output_file.write("\n")