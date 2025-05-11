from plugins.plugins import BasePlugin
import logging
import random
from colorama import Fore, Style

class BlueBugPlugin(BasePlugin):
    def __init__(self):
        print(f"{Fore.LIGHTBLUE_EX}BlueBugPlugin init{Style.RESET_ALL}")
        # Setup any state variables here
        pass
    
    def transform_caption(self, caption:str):

        listOfCaptions = [line.strip() for line in caption.split("\n")]
        selectedCaption = random.choice(listOfCaptions)
        splitBySpace = selectedCaption.split(" ")
        typeNoter = splitBySpace[0]
        content = " ".join(splitBySpace[1:])
        returnedCaption = ""
        if(typeNoter is "T"):
            #caption is tags
            tagList = [tag.strip() for tag in content.split(",")]
            random.shuffle(tagList)
            tags =  ', '.join(tagList)
            returnedCaption = f"{tags}"
        elif(typeNoter is "S"):
            #caption is sentence
            returnedCaption  = f"{content}"
        else:
            #caption is neither in format of this plugin
            returnedCaption  = " ".join(splitBySpace[0:])

        return returnedCaption
