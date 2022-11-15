from lib.runner import exec_command
from time import sleep
import argparse
import os
from lib.blockchain import generate_blocks, print_blocks
import config
from lib.bist import populate_crc16


def start_bitcoin_daemon():
    exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoind')} -daemon")
    
    sleep(10)

def stop_bitcoin_daemon():
    exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} stop")
    sleep(5)


def load_wallet():

    pass


if __name__ == "__main__":
    # os.chdir(config.bitcoin_home)
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", dest="block_count", type=int, default=1, help="Number of block header to generate")
    parser.add_argument("-d", dest="debug", type=int, default=0, help="Debug Mode: Generates detailed CRC16 of all the block headers")
    parser.add_argument("-c", dest="header_crc", type=str, default=None, help="To generate the CRC16 for any sample header ")

    args = parser.parse_args()
    print(args)

    try:
        if args.header_crc == None:
            config.validate_config()

            start_bitcoin_daemon()
            load_wallet()
            exec_command(f"./{os.path.join(config.bitcoin_src, 'bitcoin-cli')} -getinfo")
            generate_blocks(args.block_count)
            print_blocks(args.block_count)

        populate_crc16(args.debug, args.header_crc)
        
    finally:
        # stop_bitcoin_daemon()
        print("Exiting BTC-Explorer thread.")
