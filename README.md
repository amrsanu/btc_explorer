***btc_explorer
*This can be used to explore the RPC commands to get details related to bitcoin.

*Usage steps
1. Run bitcoin node using: 
>>> bitcoind
2. Load/Create walllet
>>> ./src/bitcoin-cli createwallet amrsanu_btc 
3. Run the btc_explorer script
>>> python3 main.py -g <number of block headers to generate>
    Ex: python3 main.py -g 100
4. Stop the bitcoin core using
>>> ./src/bitcoin-cli stop