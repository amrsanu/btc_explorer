
import json
import os
from lib.runner import exec_command, get_output
import config

def get_difficulty():
    """To print the diffficulty of the block.
    """
    exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getdifficulty")

def generate_blocks(count):
    """To generate more blocks in case of mined blocks are less than required number of blocks
    Invoked in case of regtest chain mining.

    Args:
        count (int): To check and generate required number of blocks in not already mined.
    """
    print(f"Polling for {count} blocks.")
    output, error = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockcount")
    block_count = int(output)
    if output != None and error == None:
        output, error = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -getinfo")
        if "Chain: main" in output:
            print("Cannot generate blocks on demand on Main chain.")
            print("Using available number of block headers.")
        elif "Chain: regtest" in output and count > block_count:
            print(f"Generating {count-int(output)+1} blocks.")
            exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -generate {count-block_count+1}")
        else:
            print("No need to generate extra blocks.")

def print_blocks(block_count):
    """To generate sample block headers.

    Args:
        block_count (int): Count of number of block headers to generate
    """
    header_file = open(config.sample_header, "w")
    header_file.write("# Nonce_range: {} Total_headers: {} \n\n".format(config.nonce_range, block_count))
    header_file.write("#{:<7} {:<64} {:<64} {:<8} {:<8} {:<8}\n\n".format("verHex", "previousblockhash", "merkleroot", "time", "bits", "nonce"))
    header_file.write('#{}\n'.format("="*169))
    for i in range(1, block_count+1):
        block_hash = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockhash {i}")[0]
        # print(type(block_hash), block_hash)
        block = get_output(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} getblockheader {block_hash}")[0]
        block = json.loads(block)
        # print(type(block), block)
        block_data = f'{block["versionHex"]} {block["previousblockhash"]} {block["merkleroot"]} {hex(block["time"])[2:]} {block["bits"]} {hex(block["nonce"]-config.nonce_range)[2:]}\n'
        print(block_data, end=" ")
        header_file.write(block_data)
    
    print("Sample header path: {}\n".format(config.sample_header))

        
