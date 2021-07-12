
from nutrient_object_list import Nutrient_Object_List
from nutrition import Nutrition_Data
from selenium.common.exceptions import NoSuchElementException


def printObject(i):

    print("\n\n")

    print(i.getName() + ":")
    print("====" * 43)
    print(i.getCalorieList())
    print("====" * 43)
    print(i.getCarbList())
    print("====" * 43)
    print(i.getFatAndProteinList())
    print("====" * 43)
    print(i.getVitaminList())
    print("====" * 43)
    print(i.getMineralList())
    print("====" * 43)

    print("\n\n")



#tomato
input = "https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2682/2"

#class 'Nutrition_Data' acts as the processor of this app
d1 = Nutrition_Data(input)

# NoSuchElementException
try:
    tomato = Nutrient_Object_List("Tomato", d1.getCalories(), d1.getCarbs(), d1.getFatsAndProtein(), d1.getVitamins(), d1.getMinerals() )
    tomato.adjustValues()
    printObject(tomato)
except NoSuchElementException:
    print("====" * 43)
    print("Website was not able to be loaded. As such, it was skipped. Sorry.")

#close the firefox driver
d1.closeDriver()

#egg
input = "https://nutritiondata.self.com/facts/dairy-and-egg-products/117/2"
d2 = Nutrition_Data(input)

try:
    egg = Nutrient_Object_List("Egg", d2.getCalories(), d2.getCarbs(), d2.getFatsAndProtein(), d2.getVitamins(), d2.getMinerals() )
    egg.adjustValues()
    printObject(egg)
except NoSuchElementException:
    print("====" * 43)
    print("Website was not able to be loaded. As such, it was skipped. Sorry.")

d2.closeDriver()

#persimmon
input = "https://nutritiondata.self.com/facts/fruits-and-fruit-juices/2016/2"
d3 = Nutrition_Data(input)

try:
    persimmon = Nutrient_Object_List("Persimmon", d3.getCalories(), d3.getCarbs(), d3.getFatsAndProtein(), d3.getVitamins(), d3.getMinerals() )
    persimmon.adjustValues()
    printObject(persimmon)
except NoSuchElementException:
    print("====" * 43)
    print("Website was not able to be loaded. As such, it was skipped. Sorry.")


d3.closeDriver()



