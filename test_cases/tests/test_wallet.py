import pytest

from wallet import Wallet,InsufficientFunds

def test_default_amount():
    wallet=Wallet()
    assert wallet.balance==0

def test_setting_initial_amount():
    wallet=Wallet(100)
    assert wallet.balance==100


def test_wallet_add_cash():
    wallet = Wallet(100)
    wallet.add_cash(50)
    assert wallet.balance == 150


def test_wallet_spend_cash():
    wallet = Wallet(100)
    wallet.spend_cash(50)
    assert wallet.balance == 50


def test_for_exceptions():
    wallet = Wallet(100)
    with pytest.raises(InsufficientFunds):
        wallet.spend_cash(150)
