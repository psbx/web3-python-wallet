from web3_python_wallet import (
    account_from_private_key,
    checksum_address,
    is_valid_address,
    sign_message,
)

TEST_KEY = "0x4c0883a69102937d6231471b5dbb6204fe5129617082796feac3f27deb5cf40a"
EXPECTED_ADDRESS = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"


def test_account_from_private_key_returns_expected_checksum():
    details = account_from_private_key(TEST_KEY)
    assert details["address"] == checksum_address(EXPECTED_ADDRESS)


def test_sign_message_returns_hex_signature():
    signature = sign_message("gm", TEST_KEY)
    assert signature.startswith("0x")
    assert len(signature) == 132


def test_is_valid_address_filters_bad_inputs():
    assert is_valid_address(EXPECTED_ADDRESS)
    assert not is_valid_address("0x1234")
