import random
from prettytable import PrettyTable as pt

# Classes
class Farm():
    def __init__(self, name, money, totalValue):
        self.name = name
        self.money = money
        self.totalValue = totalValue

    def TotalValue(self):
        for i in animalList, plantList, productList:
            for j in i:
                farm.totalValue += (j.number * j.price)
        return round(farm.totalValue,2)

class Animal(Farm):
    def __init__(self, name, number, product, productionCoefficient, price):
        self.name = name
        self.number = number
        self.productionCoefficient = productionCoefficient
        self.price = price
        self.lastPrice = 0
        self.production = product
        self.weeklyProduction = 0

    def Buy(self):
        if farm.money > 0:
            print(">", self.name, "Market")
            print("--------------------------------------------")
            print("> Price            :", self.price)
            print("> Total Number     :", self.number)
            print("> Last Week Prices :", self.lastPrice, "$")
            print("> Total Money      :", farm.money, "$")
            print("> Max Buy Number   :", round((farm.money/self.price), 0))
            buyNumber = int(input("How much You want to Buy? "))
            farm.money = farm.money - (self.price * buyNumber)
            self.number = self.number + buyNumber
        else:
            print("\n> Not Enough Money!\n")

    def Sell(self):
        print(">", self.name, "Market")
        print("--------------------------------------------")
        print("> Price               :", self.price)
        print("> Total Number        :", self.number)
        print("> Last Week Prices    :", self.lastPrice, "$")
        print("> Total Money         :", farm.money, "$")
        print("> Max Buy Number      :", self.number)
        sellNumber = int(input("How much You want to Sell? "))
        if sellNumber <= self.number:
            farm.money = farm.money + (self.price * sellNumber)
            self.number = self.number - sellNumber
        else:
            print("\n> Error,You dont have!")

class Plant(Farm):
    def __init__(self, name, number, production, productionCoefficient, price):
        self.name = name
        self.number = number
        self.productionCoefficient = productionCoefficient
        self.price = price
        self.lastPrice = 0
        self.production = production
        self.weeklyProduction = 0

    def Buy(self):
        if farm.money > 0:
            print(">", self.name, "Market")
            print("--------------------------------------------")
            print("> Price            :", self.price)
            print("> Total Number     :", self.number)
            print("> Last Week Prices :", self.lastPrice, "$")
            print("> Total Money      :", farm.money, "$")
            print("> Max Buy Number   :", round((farm.money/self.price), 0))
            buyNumber = int(input("How much You want to Buy? "))
            farm.money = farm.money - (self.price * buyNumber)
            self.number = self.number + buyNumber
        else:
            print("\n> Not Enough Money!\n")

    def Sell(self):
        print(">", self.name, "Market")
        print("--------------------------------------------")
        print("> Price            :", self.price)
        print("> Total Number     :", self.number)
        print("> Last Week Prices :", self.lastPrice, "$")
        print("> Total Money      :", farm.money, "$")
        print("> Max Buy Number   :", self.number)
        sellNumber = int(input("How much You want to Sell? "))
        if sellNumber <= self.number:
            farm.money = farm.money + (self.price * sellNumber)
            self.number = self.number - sellNumber
        else:
            print("\n> Error, You dont have!")

class Urun(Farm):
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price
        self.lastPrice = 0

    def Buy(self):
        if farm.money > 0:
            print(">", self.name, "Market")
            print("--------------------------------------------")
            print("> Price            :", self.price)
            print("> Total Number     :", self.number)
            print("> Last Week Prices :", self.lastPrice, "$")
            print("> Total Money      :", farm.money, "$")
            print("> Max Buy Number   :", round((farm.money/self.price), 0))
            buyNumber = int(input("How much You want to Buy? "))
            farm.money = farm.money - (self.price * buyNumber)
            self.number = self.number + buyNumber
        else:
            print("\n> Not Enough Money!\n")

    def Sell(self):
        print(">", self.name, "Market")
        print("--------------------------------------------")
        print("> Price            :", self.price)
        print("> Total Number     :", self.number)
        print("> Last Week Prices :", self.lastPrice, "$")
        print("> Total Money      :", farm.money, "$")
        print("> Max Buy Number   :", self.number)
        sellNumber = int(input("How much You want to Sell? "))
        if sellNumber <= self.number:
            farm.money = farm.money + (self.price * sellNumber)
            self.number = self.number - sellNumber
        else:
            print("\n> Error, You dont have!")

# Variables
week = 1

# Objects
farm = Farm("Farm", 5000, 0)
#
cow = Animal("Cow", 3, "Milk", 2, 750)
sheep = Animal("Sheep", 5, "Wool", 1, 250)
chicken = Animal("Chicken", 7, "Egg", 5, 50)
animalList = [cow, sheep, chicken]
#
cotton = Plant("Cotton", 3, "Fabric", 1, 200)
wheat = Plant("Wheat", 5, "Fame", 5, 500)
sunflower = Plant("Sunflower", 7, "Oil", 3, 100)
plantList = [cotton, wheat, sunflower]
#
milk = Urun("Milk", 0, 7)
wool = Urun("Wool", 0, 30)
egg = Urun("Egg", 0, 2)
fabric = Urun("Fabric", 0, 80)
fame = Urun("Fame", 0, 35)
oil = Urun("Oil", 0, 60)
feed = Urun("Feed", 200, 50)
fertilizer = Urun("Fertilizer", 300, 60)
productList = [milk, wool, egg, fabric, fame, oil, feed, fertilizer]

# Functions
def PricesChange():
    for i in animalList:
        i.lastPrice = i.price
        i.price = round(i.price * (random.uniform(0.9, 1.1)), 2)

    for i in plantList:
        i.lastPrice = i.price
        i.price = round(i.price * (random.uniform(0.85, 1.15)), 2)

    for i in productList:
        i.lastPrice = i.price
        i.price = round(i.price * (random.uniform(0.75, 1.25)), 2)

def Production():
    milk.number = milk.number + (cow.number * cow.productionCoefficient)
    wool.number = wool.number + (sheep.number * sheep.productionCoefficient)
    egg.number = egg.number + (chicken.number * chicken.productionCoefficient)
    fabric.number = fabric.number + (cotton.number * cotton.productionCoefficient)
    fame.number = fame.number + (wheat.number * wheat.productionCoefficient)
    oil.number = oil.number + (sunflower.number * sunflower.productionCoefficient)

    cow.weeklyProduction = cow.number * cow.productionCoefficient
    sheep.weeklyProduction = sheep.number * sheep.productionCoefficient
    chicken.weeklyProduction = chicken.number * chicken.productionCoefficient
    cotton.weeklyProduction = cotton.number * cotton.productionCoefficient
    wheat.weeklyProduction = wheat.number * wheat.productionCoefficient
    sunflower.weeklyProduction = sunflower.number * sunflower.productionCoefficient

def FeedConsumption():
    if feed.number > 0:
        feed.number -= (cow.number * 3)+(sheep.number * 2)+(chicken.number * 1)
        print("\nFeed Consumption Week :", int(feed.number/((cow.number * 3)+(sheep.number * 2)+(chicken.number * 1))), "Week")
        print("Feed Consumption        :", ((cow.number * 3) +(sheep.number * 2)+(chicken.number * 1)))

    else:
        print("Not Enough Souurces! Buy some Feed for the Animals. Your animals will die")
        print("Cow Died:", 2)
        print("Sheep Died:", 3)
        print("Chicken Died:", 5)
        cow.number  -= 2
        sheep.number -= 3
        chicken.number -= 5
    
        if cow.number <= 0:
            cow.number = 0
            print("You dont have any Cow!")

        if sheep.number <= 0:
            sheep.number = 0
            print("You dont have any Sheep!")

        if chicken.number <= 0:
            chicken.number = 0
            print("You dont have any Chicken!")

def FertilizerConsumption():
    if fertilizer.number > 0:
        fertilizer.number -= (cotton.number * 2)+(wheat.number * 2)+(sunflower.number * 3)
        print("\nFeed Consumption Week :", str(int(fertilizer.number/((cotton.number * 2)+(wheat.number * 2)+(sunflower.number * 3)))), "Week")
        print("Fertilizer Consumption  :", ((cotton.number * 2) +(wheat.number * 2)+(sunflower.number * 3)))

    else:
        print("Not Enough Souurces! Buy some Fertilizer for the Plants. Your plants will fade")
        print("Cotton Faded :", 2)
        print("Wheat Faded :", 2)
        print("Sunflower Faded :", 3)
        cotton.number  -= 2
        wheat.number -= 2
        sunflower.number -= 3
    
        if cotton.number <= 0:
            cotton.number = 0
            print("You dont have any Cotton!")

        if wheat.number <= 0:
            wheat.number = 0
            print("You dont have any Wheat!")

        if sunflower.number <= 0:
            sunflower.number = 0
            print("You dont have any Sunflower!")

def MarketplaceBuy(list):
    buyIndex = 1
    print("\n-----------------------------------------------")
    for i in list:
        print(buyIndex, i.name)
        print("Number:", i.number)
        print("-----------------------------------------------")
        buyIndex += 1
    buyInput = int(input("Enter the Product Number"))
    
    if buyInput == 0:
        print("\n> Enter a Valid Value!\n")
    
    else:
        try:
            list[buyInput-1].Buy()

        except:
            print("\n> Enter a Valid Value!\n")

def MarketplaceSell(list):
    sellIndex = 1
    print("\n-----------------------------------------------")
    for i in list:
        print(sellIndex, i.name)
        print("Number:", i.number)
        print("-----------------------------------------------")
        sellIndex += 1
    sellInput = int(input("Enter the Product Number"))

    if sellInput == 0:
        print("\n> Enter a Valid Value!\n")

    else:
        try:
            list[sellInput-1].Sell() 

        except:
            print("\n> Enter a Valid Value!\n")

# Main Loop
while True:
    print("\n----------------------------------------")
    print("          Farm Simulator Game           ")
    print("----------------------------------------")
    print("> 1: My Farm")
    print("> 2: Next Week >", week, ". week")
    print("> 3: Prices")
    print("> 4: Marketplace")
    print("> 5: Statistics")
    print("> 6: Info")
    print("> 0: Exit")
    print("----------------------------------------")
    mainpagePage = int(input("Enter Page Number: "))

    # Exit
    if mainpagePage == 0:
        print("Quited Game")
        break

    # Farm
    elif mainpagePage == 1:
        while True:
            print("\n----------------------------------------")
            print("                My Farm                 ")
            print("----------------------------------------")
            print("> 1: Barn")
            print("> 2: Field")
            print("> 3: Inventory")
            print("> 0: Exit")
            farmPage = int(input("Enter Page Number: "))

            # Exit
            if farmPage == 0:
                break

            # Barn
            elif farmPage == 1:
                tb = pt()
                tb.field_names = ["Name", "Number", "Price", "Last Price", "Total Value", "Product", "Weekly Production"]
                for i in animalList:
                    tb.add_row([i.name, i.number, i.price, i.lastPrice,round((i.number*i.price),2), i.production, i.weeklyProduction])
                print(tb)

            # Field
            elif farmPage == 2:
                tb = pt()
                tb.field_names = ["Name", "Number", "Price", "Last Price", "Total Value", "Product", "Weekly Production"]
                for i in plantList:
                    tb.add_row([i.name, i.number, i.price, i.lastPrice,round((i.number*i.price),2) ,i.production, i.weeklyProduction])
                print(tb)

            # Inventory
            elif farmPage == 3:
                tb = pt()
                tb.field_names = ["Name", "Number", "Price", "Last Price","Total Value"]
                for i in productList:
                    tb.add_row([i.name, i.number, i.price, i.lastPrice,round((i.number*i.price),2)])
                print(tb)

            # Error
            else:
                print("\n> Enter a Valid Value!\n")

    # Next Week
    elif mainpagePage == 2:
        week += 1
        PricesChange()
        Production()
        FeedConsumption()
        FertilizerConsumption()

    # Prices
    elif mainpagePage == 3:
        print("\n----------------------------------------")
        print("           Prices This Week             ")
        print("----------------------------------------")
        tb = pt()
        tb.field_names = ["Name", "Number", "Price", "Last Price"]
        for i in animalList:
            tb.add_row([i.name, i.number, i.price, i.lastPrice])
        tb.add_row(["--------", "--------", "--------", "--------"])
        for i in plantList:
            tb.add_row([i.name, i.number, i.price, i.lastPrice])
        tb.add_row(["--------", "--------", "--------", "--------"])
        for i in productList:
            tb.add_row([i.name, i.number, i.price, i.lastPrice])
        print(tb)

    # Marketplace
    elif mainpagePage == 4:
        print("\n----------------------------------------")
        print("                 Marketplace              ")
        print("----------------------------------------\n")
        print("Animal")
        print("> 1: Buy")
        print("> 2: Sell")
        print("------------------------\n")
        print("Plant")
        print("> 3: Buy")
        print("> 4: Sell")
        print("------------------------\n")
        print("Produc")
        print("> 5: Buy")
        print("> 6: Sell")
        print("------------------------\n")
        print("> 0: Exit")
        print("------------------------")
        marketplacePage = int(input("Enter Page Number: "))

        # Exit
        if marketplacePage == 0:
            print("Mainpage.")

        # Animal Buy
        elif marketplacePage == 1:
            MarketplaceBuy(animalList)

        # Animal Sell
        elif marketplacePage == 2:
            MarketplaceSell(animalList)

        # Plant Buy
        elif marketplacePage == 3:
            MarketplaceBuy(plantList)

        # Plant Sell
        elif marketplacePage == 4:
            MarketplaceSell(plantList)

        # Product Buy
        elif marketplacePage == 5:
            MarketplaceBuy(productList)

        # Product Sell
        elif marketplacePage == 6:
            MarketplaceSell(productList)

        # Error
        else:
            print("\n> Enter a Valid Value!\n")

    # Statistics
    elif mainpagePage == 5:
        print("\n----------------------------------------")
        print("            Farm Statistics             ")
        print("----------------------------------------")
        farm.totalValue = 0
        print("> Total Farm Value :", farm.TotalValue())
        print("> Money            :", farm.money)

    # Info
    elif mainpagePage == 6:
        print("\n > Developer: ErenElagz")
        print("The Farm Game starts on a small farm where you have a barn and a field.")
        print("And you start the game with a few animals, a few fields and 5000$.")
        print("Your Goal is a game where you produce every week and sell your products in the market place and invest with the money you get.")
        print("But everything is not that simple! Prices change every week, sometimes the prices crash and sometimes they can fly.")
        print("So now it's your turn to sell what you have? will you wait?")

    # Error
    else:
        print("\n> Enter a Valid Value!\n")
