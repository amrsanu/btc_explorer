*\*\*btc_explorer
*This can be used to explore the RPC commands to get details related to bitcoin.

\*Output will be generated in current folder.

1. sample_header.txt
2. sample_crc.txt

\*Usage steps

1.  Run bitcoin node using:
    > bitcoind
2.  Load/Create walllet
    > ./src/bitcoin-cli createwallet amrsanu_btc
3.  Run the btc_explorer script
    > python3 main.py -g <number of block headers to generate>
        Ex: python3 main.py -g 100
4.  Stop the bitcoin core using
    > ./src/bitcoin-cli stop

\*To generate the CRC16 manually

    > python .\main.py -c .\sample_headers.txt
    > python .\main.py -c .\sample_headers.txt -d 1 # For detailed crc16
