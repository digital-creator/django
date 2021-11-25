from django.db import models
from datetime import datetime
from typing import List

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


    def all_product_kits(self) -> List[ProductKit]:
        transactions = Transaction.objects.filter(from_account=self.account)

        product_kits = []
        for transaction in transactions:
            offer = transaction.offer
            sale_offer = SaleOffer.objects.get(offer=offer, offer__state=OfferState.DONE)
            product_kits.append(sale_offer.product_kit)

        return product_kits
