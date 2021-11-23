from offer.models import Offer
from offer.services import place_sale_offer
from player.models import *
from product.models import Product, ProductKit


def index_player(request):
    user = User.objects.create(username="asd", is_client=False, is_player=False, is_supplier=False) # todo move to user creation
    account = Account.objects.create()
    player = Player.objects.create(user=user, name='Biba', account=account)

    product = Product.create('пачка сигарет', 10)
    product_kit = ProductKit.create(product, count=2, time=40)

    user_seller = User.objects.create(username="qwe", is_client=False, is_player=False, is_supplier=False) # todo move to user creation
    account_seller = Account.objects.create()
    seller = Manufacturer.objects.create(user=user_seller, name='Мальборо', account=account_seller)

    offer = place_sale_offer(product_kit, 200, user_seller)


    player.buy(offer)
    kits = player.all_product_kits()
    pass
