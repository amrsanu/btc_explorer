import os

bitcoin_src = r"src"
bitcoin_home = r"/home/intel/amrendra/bitcoin/bitcoin"
sample_header = os.path.join(os.getcwd(), "sample_header.txt")
sample_crc = os.path.join(os.getcwd(), "sample_crc.txt")


# Nonce for all the Block headers will be 100 less than the Final/End Nonce
# Increase to make the problem more complex for mining.
nonce_range = 100 

def validate_config():
    if not os.path.exists(bitcoin_home):
        raise NotADirectoryError(bitcoin_home)