from typing import Dict
from review import Review
from game import Game
from enums import Genre, MaturityRating, ArtStyle

game_db: Dict[str, Review] = {}

def save_review(game_name: str, review: Review) -> None:
    game_db[game_name] = review

def search_reviews(search_term: str = "") -> Dict[str, Review]:
    if not search_term:
        return game_db.copy()
    return {name: review for name, review in game_db.items() 
            if search_term.lower() in name.lower()}
            
def load_default_reviews():
    """Load the 10 default game reviews into the system"""
    default_reviews = [
        {
            "name": "Destiny 2",
            "score": 6,
            "genres": {Genre.ACTION, Genre.SHOOTER},
            "maturity": MaturityRating.TEEN,
            "cost": 0,
            "art_style": ArtStyle.PHOTOREALISTIC,
            "summary": "This game sucks, Its my favorite game"
        },
        {
            "name": "Elden Ring",
            "score": 10,
            "genres": {Genre.ACTION, Genre.ADVENTURE, Genre.RPG},
            "maturity": MaturityRating.TEEN,
            "cost": 60,
            "art_style": ArtStyle.PHOTOREALISTIC,
            "summary": "The greatest Fantasy game ever made, recommended to everyone."
        },
        {
            "name": "Path of Exile 2",
            "score": 8,
            "genres": {Genre.RPG, Genre.ACTION},
            "maturity": MaturityRating.MATURE,
            "cost": 30,
            "art_style": ArtStyle.PHOTOREALISTIC,
            "summary": "Wonderful game that suffers from its own success. It is too big, too deep, and too confusing. Easily scares off new players."
        },
        {
            "name": "Marvel Rivals",
            "score": 9,
            "genres": {Genre.ACTION, Genre.RPG, Genre.STRATEGY},
            "maturity": MaturityRating.EVERYONE,
            "cost": 0,
            "art_style": ArtStyle.CEL_SHADED,
            "summary": "This Game takes everything Overwatch has done right and does better, while also avoiding everything that made overwatch bad."
        },
        {
            "name": "Terraria",
            "score": 10,
            "genres": {Genre.ADVENTURE, Genre.RPG, Genre.ACTION},
            "maturity": MaturityRating.TEEN,
            "cost": 10,
            "art_style": ArtStyle.PIXEL_ART,
            "summary": "One of the most in depth, bang for your buck games ever created. There is a reason why this game is considered one of the GOATs."
        },
        {
            "name": "Voices of the Void",
            "score": 9,
            "genres": {Genre.HORROR, Genre.ADVENTURE},
            "maturity": MaturityRating.MATURE,
            "cost": 0,
            "art_style": ArtStyle.PIXEL_ART,
            "summary": "The chillest game that will make you crap your pants. It's only drawback is that the game isn't finished yet."
        },
        {
            "name": "Cyberpunk 2077",
            "score": 8,
            "genres": {Genre.ACTION, Genre.RPG, Genre.ADVENTURE},
            "maturity": MaturityRating.ADULTS_ONLY,
            "cost": 60,
            "art_style": ArtStyle.PHOTOREALISTIC,
            "summary": "Started off really ruff, but grew to become something truly great. Has an S-tier story that truly draws you in."
        },
        {
            "name": "Castle Crashers",
            "score": 10,
            "genres": {Genre.ACTION, Genre.RPG},
            "maturity": MaturityRating.TEEN,
            "cost": 15,
            "art_style": ArtStyle.HAND_DRAWN,
            "summary": "A game from my childhood that still holds up to this day. Music is peak and combat that's fun."
        },
        {
            "name": "Age of Mythology",
            "score": 9,
            "genres": {Genre.STRATEGY, Genre.ACTION, Genre.SIMULATION},
            "maturity": MaturityRating.TEEN,
            "cost": 30,
            "art_style": ArtStyle.LOW_POLY,
            "summary": "An all time classic for the RTS genre. While not as popular as others of its genre, that does not diminish how great of a game it is."
        },
        {
            "name": "Armored Core 6",
            "score": 9,
            "genres": {Genre.ACTION, Genre.RPG, Genre.STRATEGY},
            "maturity": MaturityRating.TEEN,
            "cost": 60,
            "art_style": ArtStyle.PHOTOREALISTIC,
            "summary": "Before this game I had never played a Mech game before. Now it's one of my favorite genres"
        }
    ]

    for review_data in default_reviews:
        game = Game(
            name=review_data["name"],
            genres=review_data["genres"],
            maturity_rating=review_data["maturity"],
            art_style=review_data["art_style"]
        )
        review = Review(
            game=game,
            score=review_data["score"],
            cost=review_data["cost"],
            summary=review_data["summary"]
        )
        save_review(review_data["name"], review)