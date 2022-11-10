from lib.runner import exec_command
from time import sleep
import argparse
import os
from lib.blockchain import generate_blocks, print_blocks
import config

def start_bitcoin_daemon():
    exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoind')} -daemon")
    
    sleep(10)

def stop_bitcoin_daemon():
    exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} stop")
    sleep(5)


def load_wallet():

    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", dest="block_count", type=int, default=1, help="Number of block header to generate")

    args = parser.parse_args()

    try:
        # start_bitcoin_daemon()
        load_wallet()
        exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -getinfo")
        generate_blocks(args.block_count)
        print_blocks(args.block_count)

    finally:
        # stop_bitcoin_daemon()
        print("Exiting BTC-Explorer thread.")
