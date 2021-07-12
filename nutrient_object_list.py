

#from nutrition import Nutrition_Data

class Nutrient_Object_List:

    #constructor
    def __init__(self, name, calorie_list, carb_list, fat_and_protein_list, vitamin_list, mineral_list):
        self.name = name
        self.calorie_list = []
        self.carb_list = []
        self.fat_and_protein_list = []
        self.vitamin_list = []
        self.mineral_list = []

        for i in calorie_list:
            self.calorie_list.append(i.get_nutrient())

        for i in carb_list:
            self.carb_list.append(i.get_nutrient())

        for i in fat_and_protein_list:
            self.fat_and_protein_list.append(i.get_nutrient())

        for i in vitamin_list:
            self.vitamin_list.append(i.get_nutrient())
        
        for i in mineral_list:
            self.mineral_list.append(i.get_nutrient())


    #get name
    def getName(self):
        return self.name

    #get calorie_list
    def getCalorieList(self):
        return self.calorie_list

    #get carb_list
    def getCarbList(self):
        return self.carb_list

    #get fat_and_protein_list
    def getFatAndProteinList(self):
        return self.fat_and_protein_list

    #get vitamin_list
    def getVitaminList(self):
        return self.vitamin_list

    #get mineral_list
    def getMineralList(self):
        return self.mineral_list


    #adjust list values so they are proportional to 100 calories worth of select food product
    def adjustValues(self):
        #get the item's calories, and use it to divide 100 to get a multiplier ratio
        multiplier = float(100.0/(self.calorie_list[0][1]) )

        #apply multiplier ratio to all of our lists
        #round to the nearest tenth

        for i in range(len(self.calorie_list)):
            value = self.calorie_list[i][1]
            self.calorie_list[i][1] = round((value * multiplier), 1)

        for i in range(len(self.carb_list)):
            value = self.carb_list[i][1]
            self.carb_list[i][1] = round((value * multiplier), 1)
        
        for i in range(len(self.fat_and_protein_list)):
            value = self.fat_and_protein_list[i][1]
            self.fat_and_protein_list[i][1] = round((value * multiplier), 1)

        for i in range(len(self.vitamin_list)):
            value = self.vitamin_list[i][1]
            self.vitamin_list[i][1] = round((value * multiplier), 1)
        
        for i in range(len(self.mineral_list)):
            value = self.mineral_list[i][1]
            self.mineral_list[i][1] = round((value * multiplier), 1)

    