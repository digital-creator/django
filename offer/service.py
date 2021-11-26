from datetime import datetime
from typing import List

from offer.models import Offer, SaleOffer, PurchaseOffer, OfferState
from player.models import Player, Manufacturer
from product.models import ProductKit, Product
from users.models import User

from GameExceptions.TransactionExceptions import NotEnoughtBalance


def place_sale_offer(product_kit: ProductKit, price: int, seller: User) -> SaleOffer:
    offer = Offer.objects.create(price=price, timestamp=datetime.now())
    return SaleOffer.objects.create(product_kit=product_kit, offer=offer, seller=seller)


def place_purchase_offer(product: Product, price: int, customer: User) -> PurchaseOffer:
    offer = Offer.objects.create(price=price, timestamp=datetime.now())
    return PurchaseOffer.objects.create(product=product, offer=offer, customer=customer)


def find_active_sale_offers() -> List[SaleOffer]:
    return list(SaleOffer.objects.filter(offer__state=OfferState.ACTIVE))


def find_active_purchase_offers() -> List[PurchaseOffer]:
    return list(PurchaseOffer.objects.filter(offer__state=OfferState.ACTIVE))


def buy_sale_offer(player: Player, offer: SaleOffer):
    account_from = player.account
    seller = Manufacturer.objects.get(user=offer.seller)
    account_to = seller.account

    super_offer = offer.offer

    try:
         Transaction.objects.create(from_account=account_from,
                                    to_account=account_to,
                                    offer=super_offer,
                                    timestamp=datetime.now()
                                    )
    except NotEnoughtBalance:
        print("Недостаточно средств для транзакции")
            # FIXME: Create message to b == 0
    # todo call buy() from account module and check result
    # try:
    #     buy(account_from, account_to, super_offer.price)
    # except NotEnoughtBalance: todo create own exceptions
    #     print()

    super_offer.state = OfferState.DONE
    super_offer.save()
    
