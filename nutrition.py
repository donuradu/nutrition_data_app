from nutrient_object import Nutrient_Object
from selenium import webdriver
from selenium.webdriver.firefox.options import Options #for headless browser
from shutil import which



class Nutrition_Data:

    # constructor
    def __init__(self, url):

        #for setting up a headless browser
        
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        
        firefox_path = which("geckodriver")
        #self.driver = webdriver.Firefox(executable_path=firefox_path)
        self.driver = webdriver.Firefox(executable_path=firefox_path, options=firefox_options)

        self.url = url
        self.driver.get(url)


    #Test Method
    def getVitaminA(self):
        vitamin_a = self.driver.find_element_by_id('NUTRIENT_97')
        print("Vitamin A: ", float(vitamin_a.text) )
    #Test Method
    def getCalcium(self):
        calcium = self.driver.find_element_by_id('NUTRIENT_117')
        print("Calcium: ", float(calcium.text) )

    #Return total amount of calories; useful for adjusting the values to 100 calories
    def getTotalCalories(self):
        return float((self.driver.find_element_by_id('NUTRIENT_0')).text)

    
    #Test Method - get "iron" from just "NUTRIENT-118" value, using XPATH expressions
    def getIron(self):
        mineral = self.driver.find_element_by_xpath("//span[@id='NUTRIENT_118']/parent::div/parent::div/child::div[1]/*[1]")
        return mineral.text


    #Retrieve calorie values from webpage
    def getCalories(self):
        #returns a list of size 4

        nutrient_object_list = []

        #tuple of nutrients
        nutrients = 'NUTRIENT_0', 'NUTRIENT_1', 'NUTRIENT_2', 'NUTRIENT_3'

        for nutrient in nutrients:
            nutrient_element = self.driver.find_element_by_id(nutrient)

            nutrient_value = 0.0
            # '~' means null on the website
            if nutrient_element.text != '~':    #else, nutrient_value remains = 0
                nutrient_value = float(nutrient_element.text)
            
            #get the nutrient_name
            #note that for consistency purposes, this xpath is different than all the other ones, due to how the data is setup in the site
            modified_xpath = "//span[@id='{}']/parent::div/parent::div/child::div[1]".format(nutrient)
            nutrient_name = (self.driver.find_element_by_xpath(modified_xpath)).text

            #get the nutrient_unit
            #append "KJ_" to the beginning of nutrient value, ie: "KJ_" + "NUTRIENT_0"
            modified_unit_id_string = "KJ_{}".format(nutrient)
            nutrient_unit_id = (self.driver.find_element_by_id(modified_unit_id_string)).text

            #final step, create nutrient_object instance, and add it to nutrient_object_list
            i = Nutrient_Object(nutrient_name, nutrient_value, nutrient_unit_id)
            nutrient_object_list.append(i)

        return nutrient_object_list


    
    #Retrieve carb values from webpage
    def getCarbs(self):
        #returns a list of size 4

        nutrient_object_list = []

        #tuple of nutrients
        nutrients = 'NUTRIENT_4', 'NUTRIENT_5', 'NUTRIENT_6', 'NUTRIENT_7'

        for nutrient in nutrients:
            nutrient_element = self.driver.find_element_by_id(nutrient)

            nutrient_value = 0.0
            # '~' means null on the website
            if nutrient_element.text != '~':    #else, nutrient_value remains = 0
                nutrient_value = float(nutrient_element.text)


            #get the nutrient_name
            modified_xpath = ""
            #tricky, NUTRIENT_4 xpath is different than all the other ones
            if nutrient == 'NUTRIENT_4':
                modified_xpath = "//span[@id='{}']/parent::div/parent::div/child::div[1]/*[1]".format(nutrient)
            else:
                modified_xpath = "//span[@id='{}']/parent::div/parent::div/child::div[1]/span".format(nutrient)
            
            nutrient_name = (self.driver.find_element_by_xpath(modified_xpath)).text


            #get the nutrient_unit
            #append "UNIT_" to the beginning of nutrient value, ie: "UNIT_" + "NUTRIENT_4"
            modified_unit_id_string = "UNIT_{}".format(nutrient)
            nutrient_unit_id = (self.driver.find_element_by_id(modified_unit_id_string)).text

            #final step, create nutrient_object instance, and add it to nutrient_object_list
            i = Nutrient_Object(nutrient_name, nutrient_value, nutrient_unit_id)
            nutrient_object_list.append(i)

        return nutrient_object_list

    #Retrieve fat and protein values from webpage
    def getFatsAndProtein(self):
        #returns a list of size 8

        nutrient_object_list = []

        nutrients = 'NUTRIENT_14', 'NUTRIENT_15', 'NUTRIENT_31', 'NUTRIENT_46', 'NUTRIENT_70', 'NUTRIENT_139', 'NUTRIENT_140', 'NUTRIENT_77'
        for nutrient in nutrients:
            nutrient_element = self.driver.find_element_by_id(nutrient)

            nutrient_value = 0.0
            # '~' means null on the website
            if nutrient_element.text != '~':    #else, nutrient_value remains = 0
                nutrient_value = (float(nutrient_element.text))
            

            #get the nutrient_name
            #tricky, because total_fat/NUTRIENT_14 and total_protein/NUTRIENT_77 have different XPATHS than the rest, similar to getCarbs()

            if nutrient == "NUTRIENT_14" or nutrient == "NUTRIENT_77":
                modified_xpath = "//span[@id='{}']/parent::div/parent::div/child::div[1]/*[1]".format(nutrient)
            else:
                modified_xpath = "//span[@id='{}']/parent::div/parent::div/child::div[1]/span".format(nutrient)

            nutrient_name = (self.driver.find_element_by_xpath(modified_xpath)).text


            #get the nutrient_unit
            #append "UNIT_" to the beginning of nutrient value, ie: "UNIT_" + "NUTRIENT_14"
            modified_unit_id_string = "UNIT_{}".format(nutrient)
            nutrient_unit_id = (self.driver.find_element_by_id(modified_unit_id_string)).text

            #final step, create nutrient_object instance, and add it to nutrient_object_list
            i = Nutrient_Object(nutrient_name, nutrient_value, nutrient_unit_id)
            nutrient_object_list.append(i)

        return nutrient_object_list


    #Retrieve vitamins values from webpage
    def getVitamins(self):
        #returns a list of size 12
        nutrient_object_list = []

        nutrients = 'NUTRIENT_97', 'NUTRIENT_100', 'NUTRIENT_101', 'NUTRIENT_102', 'NUTRIENT_103', 'NUTRIENT_107', 'NUTRIENT_108', 'NUTRIENT_109','NUTRIENT_110', 'NUTRIENT_111', 'NUTRIENT_115', 'NUTRIENT_116'

        for nutrient in nutrients:
            nutrient_element = self.driver.find_element_by_id(nutrient)

            nutrient_value = 0.0
            # '~' means null on the website
            if nutrient_element.text != '~':    #else, nutrient_value remains = 0
                nutrient_value = (float(nutrient_element.text))

            #get the nutrient_name
            modified_xpath = "//span[@id='{}']/parent::div/parent::div/child::div[1]/*[1]".format(nutrient)
            nutrient_name = (self.driver.find_element_by_xpath(modified_xpath)).text

            #get the nutrient_unit
            #append "UNIT_" to the beginning of nutrient value, ie: "UNIT_" + "NUTRIENT_97"
            modified_unit_id_string = "UNIT_{}".format(nutrient)
            nutrient_unit_id = (self.driver.find_element_by_id(modified_unit_id_string)).text

            #final step, create nutrient_object instance, and add it to nutrient_object_list
            i = Nutrient_Object(nutrient_name, nutrient_value, nutrient_unit_id)
            nutrient_object_list.append(i)

        return nutrient_object_list


    #Retrieve mineral values from webpage
    def getMinerals(self):
        #returns a list of size 10
        nutrient_object_list = []

        nutrients = 'NUTRIENT_117', 'NUTRIENT_118', 'NUTRIENT_119', 'NUTRIENT_120', 'NUTRIENT_121', 'NUTRIENT_122', 'NUTRIENT_123', 'NUTRIENT_124','NUTRIENT_125', 'NUTRIENT_126'

        for nutrient in nutrients:
            nutrient_element = self.driver.find_element_by_id(nutrient)

            nutrient_value = 0.0
            # '~' means null on the website
            if nutrient_element.text != '~':    #else, nutrient_value remains = 0
                nutrient_value = (float(nutrient_element.text))
            
            #get the nutrient_name
            modified_xpath = "//span[@id='{}']/parent::div/parent::div/child::div[1]/*[1]".format(nutrient)
            nutrient_name = (self.driver.find_element_by_xpath(modified_xpath)).text

            #get the nutrient_unit
            #append "UNIT_" to the beginning of nutrient value, ie: "UNIT_" + "NUTRIENT_97"
            modified_unit_id_string = "UNIT_{}".format(nutrient)
            nutrient_unit_id = (self.driver.find_element_by_id(modified_unit_id_string)).text

            #final step, create nutrient_object instance, and add it to nutrient_object_list
            i = Nutrient_Object(nutrient_name, nutrient_value, nutrient_unit_id)
            nutrient_object_list.append(i)

        return nutrient_object_list


    def closeDriver(self):
        self.driver.close()
