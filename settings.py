import pygame
import os
from os import walk
import xml.etree.ElementTree as ET
import numpy as np

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

SCALE_FACTOR = 2.5

PLAYER_SPEED = 200
PLAYER_SPRINT_SPEED = 300

TILE_SIZE = 16

