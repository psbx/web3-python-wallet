# web3-python-wallet

A tiny toolbox for inspecting Ethereum wallet keys and signing payloads with `web3.py` and `eth-account`.

## Features
- Validate checksum formatting for supplied addresses.
- Derive wallet details from a raw private key.
- Sign arbitrary messages using EIP-191 semantics.

## Usage
```bash
python -m web3_python_wallet.wallet --key 0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef --message "gm" 
```

## Development
```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
pytest -q
```
