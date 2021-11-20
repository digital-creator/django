from offer.models import Offer
from player.models import *
from product.models import Product, ProductKit


def index_player(request):
    user = User.objects.create(username="asd", is_client=False, is_player=False, is_supplier=False)
    account = Account.objects.create()
    player = Player.objects.create(user=user, name='Biba', account=account)

    product = Product.objects.create(name='пачка сигарет', time=10)
    product_kit = ProductKit.objects.create(product=product, count=2, time=40)

    user_seller = User.objects.create(username="qwe", is_client=False, is_player=False, is_supplier=False)
    account_seller = Account.objects.create()
    seller = Manufacturer.objects.create(user=user_seller, name='Мальборо', account=account_seller)

    offer = Offer.objects.create(price=200, timestamp=datetime.now())
    offer = SaleOffer.objects.create(product_kit=product_kit, offer=offer, seller=user_seller)


    player.buy(offer)
    kits = player.all_product_kits()
    pass
