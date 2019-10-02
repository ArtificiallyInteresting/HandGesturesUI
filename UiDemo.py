import subprocess
# from playsound import playsound
import pygame

class UiDemo:


    def __init__(self):
        self.needsNeutral = True
        self.menu = {0: "Guesture UI", 1: "Steam Games", 2: "Music", 3:"Settings", 4:"Quick Play", 5:"Team Fortress 2", 6: "Super Meat Boy", 7: "Counter Strike"}
        self.transitions = {0: {"SELECT": 1},
                            1: {"LEFT": 3, "RIGHT": 2, "BACK": 0, "SELECT": 5},
                            2: {"LEFT": 1, "RIGHT": 3, "BACK": 0, "SELECT": 4},
                            3: {"LEFT": 2, "RIGHT": 1, "BACK": 0},
                            4: {"BACK": 2},
                            5: {"BACK": 1, "LEFT": 7, "RIGHT": 6},
                            6: {"BACK": 1, "LEFT": 5, "RIGHT": 7},
                            7: {"BACK": 1, "LEFT": 6, "RIGHT": 5},
                            }
        self.currentMenu = 0

    def getCurrentText(self):
        return self.menu[self.currentMenu]

    def newGuess(self, guess):
        if guess == '':
            return
        if guess == "NOTHING":
            self.needsNeutral = True
        if self.needsNeutral:
            if guess == "NEUTRAL":
                self.needsNeutral = False
            return
        if self.currentMenu in (5,6,7) and guess is "SELECT":
            self.launchGame(self.currentMenu)
            self.needsNeutral = True
        if self.currentMenu is 4 and guess is "SELECT":
            self.startMusic()
            self.needsNeutral = True
        if guess in self.transitions[self.currentMenu].keys():
            self.needsNeutral = True
            self.currentMenu = self.transitions[self.currentMenu][guess]

    def launchGame(self, gameNo):
        print("Launching game")
        subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 40800")

    def startMusic(self):
        print("Playing music")
        # playsound('5CentsBack.mp3')
        pygame.init()
        pygame.mixer.init()
        # pygame.display.set_mode()
        pygame.mixer.music.load('5CentsBack.mp3')
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(0)