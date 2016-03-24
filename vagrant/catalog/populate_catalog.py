from catalog_setup import Base, Category, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# add categories to the database
clothing = Category(name = "Clothing")
session.add(clothing)

accessories = Category(name = "Accessories")
session.add(accessories)

gifts = Category(name = "Gifts")
session.add(gifts)

figures = Category(name = "Wax Figures")
session.add(figures)

journals = Category(name = "Journals")
session.add(journals)

stickers = Category(name = "Stickers")
session.add(stickers)


# add items to the database

mysteryShirt = Item(name="Mystery Shack Staff T-shirt", description="", price="$25", image="soos_shirt.jpg", category_id=1)
session.add(mysteryShirt)

rainbowSweater = Item(name="Rainbow Sweater", description="", price="$35", image="mabel_sweater.jpg", category_id=1)
session.add(rainbowSweater)

vest = Item(name="Explorer Vest", description="", price="$35", image="dipper_vest.jpg", category_id=1)
session.add(vest)

plaidShirt = Item(name="Green Plaid Shirt", description="", price="$35", image="wendy_shirt.jpg", category_id=1)
session.add(plaidShirt)

skullSweatshirt = Item(name="Robbie V Hooded Sweatshirt", description="", price="$50", image="robbie_shirt.jpg", category_id=1)
session.add(skullSweatshirt)

blueSuit = Item(name="Powder Blue Suit (small sizes only)", description="", price="$60", image="gideon_suit.jpg", category_id=1)
session.add(blueSuit)

bolo = Item(name="Bolo", description="", price="$20", image="stan_bolo.jpg", category_id=2)
session.add(bolo)

fez = Item(name="Fez", description="", price="$30", image="stan_fez.jpg", category_id=2)
session.add(fez)

eyepatch = Item(name="Eyepatch", description="", price="$20", image="stan_eyepatch.jpg", category_id=2)
session.add(eyepatch)

treeHat = Item(name="Gravity Falls Souvenir Hat", description="", price="$30", image="dipper_hat.jpg", category_id=2)
session.add(treeHat)

flappyHat = Item(name="Hat With Flaps", description="", price="$30", image="wendy_hat.jpg", category_id=2)
session.add(flappyHat)

wornHat = Item(name="Vintage Hat", description="", price="$30", image="mcgucket_hat.jpg", category_id=2)
session.add(wornHat)

mug = Item(name="Mystery Shack Souvenir Mug", description="", price="$15", image="mug.jpg", category_id=3)
session.add(mug)

bobblehead = Item(name="Stan Bobblehead", description="", price="$25", image="bobblehead.jpg", category_id=3)
session.add(bobblehead)

camera = Item(name="Disposable Camera", description="", price="$15", image="camera.jpg", category_id=3)
session.add(camera)

puppet = Item(name="Bumblebee Puppet", description="", price="$25", image="puppet.jpg", category_id=3)
session.add(puppet)

flashlight = Item(name="Magic Flashlight", description="", price="$75", image="flashlight.jpg", category_id=3)
session.add(flashlight)

stan = Item(name="Wax Stanford Pines", description="", price="$250", image="stan.jpg", category_id=4)
session.add(stan)

coolio = Item(name="Wax Coolio", description="", price="$250", image="coolio.jpg", category_id=4)
session.add(coolio)

king = Item(name="Wax Larry King", description="", price="$250", image="king.jpg", category_id=4)
session.add(king)

nixon = Item(name="Wax Richard Nixon", description="", price="$250", image="nixon.jpg", category_id=4)
session.add(nixon)

journal0 = Item(name="Journal 1", description="", price="$20", image="journal0.jpg", category_id=5)
session.add(journal0)

journal2 = Item(name="Journal 2", description="", price="$20", image="journal2.jpg", category_id=5)
session.add(journal2)

journal3 = Item(name="Journal 3", description="", price="OUT OF STOCK", image="journal3.jpg", category_id=5)
session.add(journal3)

dino = Item(name="Ext-ROAR-dinary Sticker", description="", price="$5", image="dino.jpg", category_id=6)
session.add(dino)

GFbumper = Item(name="Gravity Falls Souvenir Bumper Sticker", description="", price="$5", image="GFbumper.jpg", category_id=6)
session.add(GFbumper)

shackSticker = Item(name="Mystery Shack Souvenir Bumper Sticker", description="", price="$5", image="shackSticker.jpg", category_id=6)
session.add(shackSticker)

sevral = Item(name="Sev'ral Timez Biggest Fan Sticker", description="", price="$5", image="sevral.jpg", category_id=6)
session.add(sevral)

please = Item(name="Please Sticker", description="", price="$5", image="please.jpg", category_id=6)
session.add(please)

sticktionary = Item(name="Sticktionary", description="", price="$20", image="sticktionary.jpg", category_id=6)
session.add(sticktionary)

session.commit()