import pygame as pg
from game import Game
from units.squad import Squad
#mostly a bunch of global variables in here

activeGame = Game()
selected = []
squad = Squad()
mleftdownpos = None


def clearSelected():
    selected = []
    squad.clear()

def select(unit):
    selected.append(unit)

