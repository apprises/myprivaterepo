# This is a sample Python script.
import random
import time
from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCWallet
from decimal import Decimal
from monero.transaction import Transaction

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
w = Wallet(JSONRPCWallet(port=28088))
address = w.address()

def send():
    unlock_time = int(3200250) - w.height() + int(1)
    transaction : [] = w.transfer(address=address, amount=Decimal('0.000000000001'), unlock_time=unlock_time)
    return transaction.pop(0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        transaction : Transaction = send()
        print(transaction.hash)
        time.sleep(random.randrange(120, 2000, 1))
