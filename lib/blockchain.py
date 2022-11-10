
import json
import os
from lib.runner import exec_command, get_output
import config

def get_difficulty():
    exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getdifficulty")

def generate_blocks(count):
    print(f"Polling for {count} blocks.")
    output, error = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockcount")
    block_count = int(output)
    if output != None and error == None:
        output, error = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -getinfo")
        if "Chain: main" in output:
            print("Cannot generate blocks on demand on Main chain.")
            print("Generating available number of block headers.")
            exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -generate {block_count}")
        elif count > block_count:
            print(f"Generating {count-int(output)+1} blocks.")
            exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -generate {count-block_count+1}")
        else:
            print("No need to generate extra blocks.")

def print_blocks(block_count):
    header_file = open("header.txt", "w")
    header_file.write("#{:<7} {:<64} {:<64} {:<8} {:<8} {:<8}\n\n".format("verHex", "previousblockhash", "merkleroot", "time", "bits", "nonce"))
    header_file.write('#{}\n'.format("="*169))
    for i in range(1, block_count+1):
        block_hash = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockhash {i}")[0]
        # print(type(block_hash), block_hash)
        block = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockheader {block_hash}")[0]
        block = json.loads(block)
        # print(type(block), block)
        block_data = f'{block["versionHex"]} {block["previousblockhash"]} {block["merkleroot"]} {hex(block["time"])} {block["bits"]} {hex(block["nonce"])}'
        print(block_data)
        header_file.write(block_data)

        
