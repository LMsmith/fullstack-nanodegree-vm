from catalog_setup import Base, Category, Item, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# add categories to the database
lighting = Category(user_id=1, name="Lighting")
session.add(lighting)
session.commit()

chairs = Category(user_id=1, name="Chairs")
session.add(chairs)
session.commit()

tables = Category(user_id=1, name="Tables + Dressers")
session.add(tables)
session.commit()

accessories = Category(user_id=1, name="Home Accessories")
session.add(accessories)
session.commit()

kitchen = Category(user_id=1, name="Kitchen")
session.add(kitchen)
session.commit()

sofas = Category(user_id=1, name="Sofas + Benches")
session.add(sofas)
session.commit()

# add items to the database
chessBoard = Item(user_id=1, name="Chess Board", description="Enjoy a game of chess in elegance with this glass and chrome chess set",
                     price="$59.50", image="../../static/images/accessories01.jpg", category=accessories)
session.add(chessBoard)
session.commit()

mask = Item(user_id=1, name="Chinese Mask", description="Charm or terrify your guests with this dragon mask. Perfect for any space!",
                     price="$89.50", image="../../static/images/accessories02.jpg", category=accessories)
session.add(mask)
session.commit()

sittingMonkey = Item(user_id=1, name="Sitting Monkey Statue", description="The perfect companion, this monkey will sit beside you and read quietly all day!",
                     price="$89.50", image="../../static/images/accessories03.jpg", category=accessories)
session.add(sittingMonkey)
session.commit()

walkingMonkey = Item(user_id=1, name="Sitting Monkey Statue", description="Add a spirit of adventure to your home with this curious monkey statue",
                     price="$89.50", image="../../static/images/accessories04.jpg", category=accessories)
session.add(walkingMonkey)
session.commit()

orange = Item(user_id=1, name="Decorative Orange Slices", description="Guaranteed not to rot!",
                     price="$8.50", image="../../static/images/accessories05.jpg", category=accessories)
session.add(orange)
session.commit()

wateringCan = Item(user_id=1, name="Orange Watering Can", description="A functional and colorful addition to your home or garden",
                     price="$29.50", image="../../static/images/accessories06.jpg", category=accessories)
session.add(wateringCan)
session.commit()

vases = Item(user_id=1, name="Metal Vases", description="If you look close enough, you can see your own reflection in these lovely decorative vases",
                     price="$79.50", image="../../static/images/accessories07.jpg", category=accessories)
session.add(vases)
session.commit()

welcomeMat = Item(user_id=1, name="Welcome Mat", description="Your guests will appreciate your hospitality",
                     price="$29.50", image="../../static/images/accessories08.jpg", category=accessories)
session.add(welcomeMat)
session.commit()

cat = Item(user_id=1, name="Wooden Cat", description="Real pets are a big responsibility. This wooden cat will keep you company even if you forget to refill its water bowl.",
                     price="$39.50", image="../../static/images/accessories09.jpg", category=accessories)
session.add(cat)
session.commit()

chair1 = Item(user_id=1, name="Covered Chair", description="A conversation piece for inside or outside your home",
                     price="$339.50", image="../../static/images/chairs01.jpg", category=chairs)
session.add(chair1)
session.commit()

chair4 = Item(user_id=1, name="Wicker Chair", description="Wicker chair with black cushions",
                     price="$199.50", image="../../static/images/chairs04.jpg", category=chairs)
session.add(chair4)
session.commit()

chair5 = Item(user_id=1, name="Translucent Chair", description="Rainbow chair that creates an interesting shadow",
                     price="$99.50", image="../../static/images/chairs05.jpg", category=chairs)
session.add(chair5)
session.commit()

chair6 = Item(user_id=1, name="Swirl Chair", description="Metal swirl-back chair",
                     price="$179.50", image="../../static/images/chairs06.jpg", category=chairs)
session.add(chair6)
session.commit()

chair7 = Item(user_id=1, name="Director's Chair", description="Orange director's chair. Folds to save space",
                     price="$59.50", image="../../static/images/chairs07.jpg", category=chairs)
session.add(chair7)
session.commit()

chair8 = Item(user_id=1, name="Drawing Chair", description="Rolling chair with high seat",
                     price="$89.50", image="../../static/images/chairs08.jpg", category=chairs)
session.add(chair8)
session.commit()

chair9 = Item(user_id=1, name="Yellow Chair", description="Comfortable yellow chair with ottoman",
                     price="$359.50", image="../../static/images/chairs09.jpg", category=chairs)
session.add(chair9)
session.commit()

chair10 = Item(user_id=1, name="Geometric Chair", description="Armchair with a whimsical geometric pattern",
                     price="$289.50", image="../../static/images/chairs10.jpg", category=chairs)
session.add(chair10)
session.commit()

chair11 = Item(user_id=1, name="Office Chair", description="Leather office chair",
                     price="$159.50", image="../../static/images/chairs11.jpg", category=chairs)
session.add(chair11)
session.commit()

chair12 = Item(user_id=1, name="Barstool", description="Attractive seating for your home bar",
                     price="$99.50", image="../../static/images/chairs12.jpg", category=chairs)
session.add(chair12)
session.commit()

chair13 = Item(user_id=1, name="Barstool With Rounded Back", description="Attractive seating for your home bar",
                     price="$99.50", image="../../static/images/chairs13.jpg", category=chairs)
session.add(chair13)
session.commit()

chair14 = Item(user_id=1, name="Barstool With Straight Legs", description="Attractive seating for your home bar",
                     price="$99.50", image="../../static/images/chairs14.jpg", category=chairs)
session.add(chair14)
session.commit()

chair15 = Item(user_id=1, name="Barstool With Straight Back", description="Attractive seating for your home bar",
                     price="$99.50", image="../../static/images/chairs15.jpg", category=chairs)
session.add(chair15)
session.commit()

chair16 = Item(user_id=1, name="Red Barstool", description="Attractive seating for your home bar",
                     price="$99.50", image="../../static/images/chairs16.jpg", category=chairs)
session.add(chair16)
session.commit()

chair17 = Item(user_id=1, name="Red Chair", description="Comfortable red chair with ottoman",
                     price="$359.50", image="../../static/images/chairs17.jpg", category=chairs)
session.add(chair17)
session.commit()

blueBowl = Item(user_id=1, name="Blue Bowl", description="Ceramic bowl for soup or cereal",
                     price="$11.50", image="../../static/images/kitchen01.jpg", category=kitchen)
session.add(blueBowl)
session.commit()

woodenDish = Item(user_id=1, name="Wooden Serving Dish", description="Triangular wooden serving dish",
                     price="$39.50", image="../../static/images/kitchen02.jpg", category=kitchen)
session.add(woodenDish)
session.commit()

teaSet = Item(user_id=1, name="CMY Tea Set", description="Colorful set of tea cups and matching saucers",
                     price="$49.50", image="../../static/images/kitchen03.jpg", category=kitchen)
session.add(teaSet)
session.commit()

teaCup = Item(user_id=1, name="Glass Mug", description="Glass mug for hot or cold beverages",
                     price="$11.50", image="../../static/images/kitchen04.jpg", category=kitchen)
session.add(teaCup)
session.commit()

espresso = Item(user_id=1, name="Espresso Cup and Saucer", description="Purple espresso cup with saucer",
                     price="$11.50", image="../../static/images/kitchen05.jpg", category=kitchen)
session.add(espresso)
session.commit()

glassBowl = Item(user_id=1, name="Glass Bowl", description="Glass bowl for fruit or snacks",
                     price="$15.50", image="../../static/images/kitchen06.jpg", category=kitchen)
session.add(glassBowl)
session.commit()

paintedBowl = Item(user_id=1, name="Painted Bowl", description="Painted ceramic bowl",
                     price="$15.50", image="../../static/images/kitchen07.jpg", category=kitchen)
session.add(paintedBowl)
session.commit()

wineGlass = Item(user_id=1, name="Wine Glass", description="Wine glass with stem",
                     price="$8.50", image="../../static/images/kitchen08.jpg", category=kitchen)
session.add(wineGlass)
session.commit()

plates = Item(user_id=1, name="Plate Set", description="Set of black and red square ceramic plates",
                     price="$29.50", image="../../static/images/kitchen09.jpg", category=kitchen)
session.add(plates)
session.commit()

plates2 = Item(user_id=1, name="Plate Set", description="Set of red and yellow round plates with gold-colored accents",
                     price="$29.50", image="../../static/images/kitchen10.jpg", category=kitchen)
session.add(plates2)
session.commit()

teaHolder = Item(user_id=1, name="Tea Holder", description="Metal base for holding hot tea cups",
                     price="$11.50", image="../../static/images/kitchen11.jpg", category=kitchen)
session.add(teaHolder)
session.commit()

lamp = Item(user_id=1, name="Butterfly Lamp", description="Stylish table lamp with butterfly cutouts",
                     price="$49.50", image="../../static/images/lighting01.jpg", category=lighting)
session.add(lamp)
session.commit()

greenLantern = Item(user_id=1, name="Green Lantern", description="Mint-colored decorative lantern with tea light",
                     price="$39.50", image="../../static/images/lighting02.jpg", category=lighting)
session.add(greenLantern)
session.commit()

redLantern = Item(user_id=1, name="Red Lantern", description="Red-colored decorative lantern with tea light",
                     price="$39.50", image="../../static/images/lighting03.jpg", category=lighting)
session.add(redLantern)
session.commit()

streetLight = Item(user_id=1, name="Vintage Street Light", description="Vintage street light stands 12ft tall",
                     price="$159.50", image="../../static/images/lighting04.jpg", category=lighting)
session.add(streetLight)
session.commit()

teaLight = Item(user_id=1, name="Replacement Tea Light", description="Replacement tea light for lanterns",
                     price="$3.50", image="../../static/images/lighting05.jpg", category=lighting)
session.add(teaLight)
session.commit()

porchLight = Item(user_id=1, name="Fancy Porch Light", description="Fancy porch light. Adds immediate curb appeal!",
                     price="$149.50", image="../../static/images/lighting06.jpg", category=lighting)
session.add(porchLight)
session.commit()

ceilingLight = Item(user_id=1, name="Stained Glass Ceiling Light", description="This decorative ceiling light will be the focal point of any room!",
                     price="$259.50", image="../../static/images/lighting07.jpg", category=lighting)
session.add(ceilingLight)
session.commit()

bench = Item(user_id=1, name="Indoor/Outdoor Bench", description="Indoor/outdoor bench is portable and perfect for adding extra seating",
                     price="$89.50", image="../../static/images/sofas01.jpg", category=sofas)
session.add(bench)
session.commit()

sectional1 = Item(user_id=1, name="Sectional", description="Brown sectional with beige cushions",
                     price="$599.50", image="../../static/images/sofas02.jpg", category=sofas)
session.add(sectional1)
session.commit()

sectional2 = Item(user_id=1, name="Sectional", description="Black sectional with black and beige pillows",
                     price="599.50", image="../../static/images/sofas03.jpg", category=sofas)
session.add(sectional2)
session.commit()

leatherSofa = Item(user_id=1, name="Black Leather Sofa", description="Black tufted leather sofa",
                     price="$699.50", image="../../static/images/sofas04.jpg", category=sofas)
session.add(leatherSofa)
session.commit()

modernSofa = Item(user_id=1, name="Modern Sofa", description="Chocolate brown modern sofa ",
                     price="$699.50", image="../../static/images/sofas05.jpg", category=sofas)
session.add(modernSofa)
session.commit()

leatherSofa2 = Item(user_id=1, name="Red-Brown Leather Sofa", description="Red-brown oversized leather sofa",
                     price="$699.50", image="../../static/images/sofas06.jpg", category=sofas)
session.add(leatherSofa2)
session.commit()

leatherSofa3 = Item(user_id=1, name="Red Leather Sofa", description="Bright red leather sofa",
                     price="$699.50", image="../../static/images/sofas07.jpg", category=sofas)
session.add(leatherSofa3)
session.commit()

table1 = Item(user_id=1, name="Floral Rounded Dresser", description="Rounded dresser with 3 drawers",
                     price="$499.50", image="../../static/images/tables01.jpg", category=tables)
session.add(table1)
session.commit()

table2 = Item(user_id=1, name="Red Wardrobe", description="Red wardrobe with 2 doors and storage drawer",
                     price="$599.50", image="../../static/images/tables02.jpg", category=tables)
session.add(table2)
session.commit()

table3 = Item(user_id=1, name="Picnic Table", description="Picnic table for indoor or outdoor use",
                     price="$499.50", image="../../static/images/tables03.jpg", category=tables)
session.add(table3)
session.commit()

table4 = Item(user_id=1, name="Nightstand", description="Nightstand with drawer and 2 doors",
                     price="$499.50", image="../../static/images/tables04.jpg", category=tables)
session.add(table4)
session.commit()

table5 = Item(user_id=1, name="Meeting Table with 4 Chairs", description="Square wooden table and 4 chairs with rounded backs",
                     price="$999.50", image="../../static/images/tables05.jpg", category=tables)
session.add(table5)
session.commit()

table6 = Item(user_id=1, name="Round Table", description="Small round wooden table with 4 legs",
                     price="$299.50", image="../../static/images/tables06.jpg", category=tables)
session.add(table6)
session.commit()

table7 = Item(user_id=1, name="Distressed Table", description="Brand new!",
                     price="$499.50", image="../../static/images/tables07.jpg", category=tables)
session.add(table7)
session.commit()
