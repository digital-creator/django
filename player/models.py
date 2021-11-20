from datetime import datetime
from typing import List

from django.db import models

from account.models import Account, Transaction
from offer.models import SaleOffer, OfferState
from product.models import ProductKit
from users.models import User


class Manufacturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    account = models.OneToOneField(Account, models.CASCADE)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    account = models.OneToOneField(Account, models.CASCADE)

    def buy(self, offer: SaleOffer):
        account_from = self.account
        seller = Manufacturer.objects.get(user=offer.seller)
        account_to = seller.account

        super_offer = offer.offer
        Transaction.objects.create(
            from_account=account_from,
            to_account=account_to,
            offer=super_offer,
            timestamp=datetime.now()
        )
        super_offer.state = OfferState.DONE
        super_offer.save()

    def all_product_kits(self) -> List[ProductKit]:
        transactions = Transaction.objects.filter(from_account=self.account)

        product_kits = []
        for transaction in transactions:
            offer = transaction.offer
            sale_offer = SaleOffer.objects.get(offer=offer, offer__state=OfferState.DONE)
            product_kits.append(sale_offer.product_kit)

        return product_kits
