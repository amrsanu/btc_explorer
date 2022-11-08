from lib.runner import exec_command
from time import sleep
import argparse
from lib.blockchain import generate_blocks, print_blocks

def start_bitcoin_daemon():
    exec_command("bitcoind -daemon")
    sleep(10)


def load_wallet():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", dest="block_count", type=int, default=1, help="Number of block header to generate")

    args = parser.parse_args()

    try:
        start_bitcoin_daemon()
        load_wallet()
        exec_command("bitcoin-cli -getinfo")
        generate_blocks(args.block_count)
        print_blocks(args.block_count)

    finally:
        exec_command("bitcoin-cli stop")
        sleep(5)
        print("Stopped Bitcoind -deamon.")