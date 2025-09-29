from __future__ import annotations

import argparse
from typing import Dict

from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3

Account.enable_unaudited_hdwallet_features()


def _normalize_private_key(private_key: str) -> str:
    key = private_key.strip()
    if not key:
        raise ValueError("private key cannot be empty")
    if not key.startswith("0x"):
        key = "0x" + key
    if len(key) != 66:
        raise ValueError("expected 32-byte hex private key")
    return key


def checksum_address(address: str) -> str:
    """Return the EIP-55 checksum address."""
    return Web3.to_checksum_address(address)


def is_valid_address(address: str) -> bool:
    try:
        Web3.to_checksum_address(address)
    except ValueError:
        return False
    return True


def account_from_private_key(private_key: str) -> Dict[str, str]:
    key = _normalize_private_key(private_key)
    account = Account.from_key(key)
    return {
        "address": Web3.to_checksum_address(account.address),
        "private_key": key,
    }


def sign_message(message: str, private_key: str) -> str:
    key = _normalize_private_key(private_key)
    payload = encode_defunct(text=message)
    signed = Account.sign_message(payload, key)
    return signed.signature.hex()


def _main() -> None:
    parser = argparse.ArgumentParser(description="Inspect Ethereum keys and sign messages")
    parser.add_argument("--key", required=True, help="hex-encoded private key")
    parser.add_argument("--message", required=True, help="message to sign")
    args = parser.parse_args()

    details = account_from_private_key(args.key)
    signature = sign_message(args.message, args.key)

    print(f"Address: {details['address']}")
    print(f"Signature: {signature}")


if __name__ == "__main__":
    _main()
