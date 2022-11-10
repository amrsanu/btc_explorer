
import json
import os
from lib.runner import exec_command, get_output
import config

def get_difficulty():
    exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getdifficulty")

def generate_blocks(count):
    print(f"Polling for {count} blocks.")
    output, error = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockcount")
    if output != None and error == None:
        if count > int(output):
            print(f"Generating {count-int(output)+1} blocks.")
            exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -generate {count-int(output)+1}")

def print_blocks(block_count):
    for i in range(1, block_count+1):
        block_hash = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockhash {i}")[0].decode()
        # print(type(block_hash), block_hash)
        block = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockheader {block_hash}")[0].decode()
        block = json.loads(block)
        # print(type(block), block)
        block_data = f'{block["versionHex"]} {block["previousblockhash"]} {block["merkleroot"]} {block["time"]} {block["bits"]} {block["nonce"]}'
        print(block_data)

        

