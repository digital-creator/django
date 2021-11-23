from datetime import datetime

from account.models import Account, Transaction
from offer.models import Offer


def transfer(account_from: Account, account_to: Account, offer: Offer):
    if account_from.balance < offer.price:
        raise Exception("account from have not enought money")

    Transaction.objects.create(
        from_account=account_from,
        to_account=account_to,
        offer=offer,
        timestamp=datetime.now()
    )


def create_account(balance: int) -> Account:
    if balance < 0:
        raise Exception("balance cant be sm then 0")

    account = Account.objects.create()
    if balance > 0:
        Transaction.objects.create(
            from_account=None,
            to_account=account,
            offer=offer
        )

    return account

