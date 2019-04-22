from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from random import randint

lookupTable = {
    0:"card-button--triangle",
    1:"card-button--diamond",
    2:"card-button--circle",
    3:"card-button--square"
}

class BotInstance:
    
    """ a method for choosing random names for the bots"""
    @staticmethod
    def name_chooser():
        result = ""
        source = "abcdefghijklmnopqrstvuwzyz"
        for _ in range(randint(5,11)):
            letter = source[randint(0,len(source)-1)]
            result += letter
        return result

    """"a method for choosing names for the bots which have spaces at random intervals thus the names look similar"""
    @staticmethod
    def special_names(string):
        result = ""
        for i in string:
            rand = randint(0,10)
            if rand <= 2:
                result+=" " 
            if rand == 3:
                result+="."
            result+=i
        return result
    
    """helper method for checking if a html element is visible at the moment"""
    def waitForElement(self,css):
        #try:
        WebDriverWait(self.driver,60).until(method=EC.visibility_of_element_located((By.CSS_SELECTOR,css)))
        return True
        #except:
            #print("something went wrong while trying to find element")
            #return False


    def change_name(self,newname):
        self.name = newname

    
    def __repr__(self):
        return "instance of kahootBot"

    """init. of the browser and joining the game"""
    def __init__(self,gamepass = None,name = None):
        options = Options()
        options.headless = True 
        self.helper = 0
        self.driver = webdriver.Chrome(options = options,executable_path="./driver-container/chromedriver")
        if name is None:
            self.name = BotInstance.name_chooser()
        else:
            self.name = name
        
        if gamepass is not None:
            self.joinGame(gamepass)
        else:
            return

    def joinGame(self,gamepass):
        try:
            self.driver.get("https://kahoot.it/")
            self.driver.implicitly_wait(10)
            gamepassinput = self.driver.find_element_by_css_selector("#inputSession")
            gamepassinput.send_keys(gamepass)
            gamepassinput.send_keys(Keys.ENTER)
            nameinput = self.driver.find_element_by_css_selector('#username')
            nameinput.send_keys(self.name)
            nameinput.send_keys(Keys.ENTER)
        except:
            print("something has gone wrong while trying to connect to the kahoot session")
            sys.exit(0)

 
            
    """control over the game buttons"""
    def choose(self,colorcode):
         
        
        if self.driver.current_url == "https://kahoot.it/instructions" or self.driver.current_url == "https://kahoot.it/answer/result":
            return
        elif self. driver.current_url == "https://kahoot.it/ranking":
            return "stop"

        if colorcode < 0 or colorcode > 4:
            print(f"{colorcode} is not in the correct range of inputs")
            return

        if  self.helper == 0: 

            self.waitForElement('#gameBlockIframe')
            self.driver.switch_to_frame(self.driver.find_element_by_css_selector("#gameBlockIframe"))
            self.helper += 1

        button = lookupTable[colorcode]

        try:
    
            self.waitForElement(f".quiz-board > .{button}")
            self.driver.find_element_by_css_selector(f".quiz-board > .{button}").click()
            print(f"{self.name} answered")
        except:
            print(f"{self.name} couldn't find buttons he will not answer to this question or the quiz has ended")
            return 
    
    def stop(self):
        self.driver.quit()
    
if __name__  == "__main__":
    print("can't run file as main")