from enum import Enum, Flag

class Genre(Flag):
    ACTION = 1
    ADVENTURE = 2
    RPG = 4
    STRATEGY = 8
    SIMULATION = 16
    SPORTS = 32
    PUZZLE = 64
    HORROR = 128
    PLATFORMER = 256
    SHOOTER = 512

    def __str__(self):
        return self.name.replace('_', ' ').title()

class MaturityRating(Enum):
    EVERYONE = "E"
    EVERYONE_10 = "E10+"
    TEEN = "T"
    MATURE = "M"
    ADULTS_ONLY = "AO"
    RATING_PENDING = "RP"

class ArtStyle(Enum):
    PHOTOREALISTIC = "Photorealistic"
    CEL_SHADED = "Cel-Shaded"
    PIXEL_ART = "Pixel Art"
    LOW_POLY = "Low Poly"
    HAND_DRAWN = "Hand-Drawn"
    VOXEL = "Voxel"
    ABSTRACT = "Abstract"