import crc16
import config
import hashlib
import binascii
import struct


def get_block_header(verHex, previousblockhash, merkleroot, time, bits, nonce):

    if len(verHex) != 8:
        verHex = "{:<0}".format(verHex)
    
    raw_header = '{verHex}{previousblockhash}{merkleroot}{time}{bits}{nonce}'.format(
        verHex="".join(reversed([verHex[i:i+2] for i in range(0, len(verHex), 2)])),
        previousblockhash="".join(reversed([previousblockhash[i:i+2] for i in range(0, len(previousblockhash), 2)])),
        merkleroot="".join(reversed([merkleroot[i:i+2] for i in range(0, len(merkleroot), 2)])),
        time="".join(reversed([time[i:i+2] for i in range(0, len(time), 2)])),
        bits="".join(reversed([bits[i:i+2] for i in range(0, len(bits), 2)])),
        nonce="".join(reversed([nonce[i:i+2] for i in range(0, len(nonce), 2)]))
    )
    return binascii.unhexlify(raw_header)


def block_header_crc16(block_header, debug):
    # 00000001 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098 4966bc61 1d00ffff 9962e301
    (verHex, previousblockhash, merkleroot, time, bits, nonce) = block_header.strip().split()
    header_bin = get_block_header(verHex, previousblockhash, merkleroot, time, bits, nonce)

    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    
    final_hash = hash[::-1]
    final_crc16 = crc16.crc16xmodem(final_hash)
    final_hash = final_hash.hex()
    crc_lines = []
    crc_lines.append("{:<08} {} {} \n".format(nonce, final_hash, final_crc16))

    crc_file = open(config.sample_crc, "a+")

    for i in range(1, config.nonce_range+1):
        nonce = hex(int(nonce, 16) + 1)[2:]
        header_bin = get_block_header(verHex, previousblockhash, merkleroot, time, bits, nonce)

        hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
        
        final_hash = hash[::-1]
        final_crc16 = crc16.crc16xmodem(final_hash)
        final_hash = final_hash.hex()

        crc_lines.append("{:<08} {} {} \n".format(nonce, final_hash, final_crc16))

    if debug == 0:
        crc_file.write(crc_lines[-1])
    else:
        crc_file.write("\n\n## {}".format(block_header))
        crc_file.writelines(crc_lines)
    crc_file.close()

def populate_crc16(debug, sample_header = None):
    print("\nGenerating CRC16 for block headers")
    if sample_header == None:
        sample_header = config.sample_header
    
    crc_file = open(config.sample_crc, "w")
    crc_file.write("#{:<7} {:<64} {:<8} \n".format("Nonce", "Hash", "CRC16"))
    crc_file.write("#{:<7} {:<64} {:<8} \n".format("-"*7, "-"*64, "-"*8))

    crc_file.close()

    
    with open(sample_header, "r") as header:
        block_header = header.readlines()
        for line in block_header:
            if len(line.strip().split()) == 6 and line[0] != '#':
                block_header_crc16(line, debug)
    
    print("     CRC16 path: {}\n".format(config.sample_crc))