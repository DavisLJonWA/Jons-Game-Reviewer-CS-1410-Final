from review import Review
from game import Game
from storage import game_db, save_review, search_reviews, load_default_reviews
from enums import Genre, MaturityRating, ArtStyle

class GameReviewSystem:
    def __init__(self):
        self.current_review = None
        # Load default reviews when system starts
        if not game_db:
            load_default_reviews()

    def get_game_score(self) -> int:
        while True:
            try:
                score = int(input("Enter game score (1-10): "))
                if 1 <= score <= 10:
                    return score
                print("Score must be between 1 and 10.")
            except ValueError:
                print("Please enter a valid integer.")

    def get_game_cost(self) -> float:
        while True:
            try:
                cost = float(input("Enter game cost: $"))
                if cost >= 0:
                    return round(cost, 2)
                print("Cost cannot be negative.")
            except ValueError:
                print("Please enter a valid number.")

    def select_enum(self, enum_class, prompt: str):
        print(f"\n{prompt}")
        for i, rating in enumerate(enum_class, 1):
            print(f"{i}: {rating.name}")
        while True:
            try:
                choice = int(input(f"Enter your choice (1-{len(enum_class)}): "))
                if 1 <= choice <= len(enum_class):
                    return list(enum_class)[choice-1]
                print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")

    def select_genres(self) -> set:
        selected_genres = set()
        while True:
            print("\nSelect a genre:")
            for i, genre in enumerate(Genre, 1):
                print(f"{i}: {genre}")
            
            try:
                choice = int(input(f"Enter genre choice (1-{len(Genre)}): "))
                if 1 <= choice <= len(Genre):
                    selected_genre = list(Genre)[choice-1]
                    if selected_genre in selected_genres:
                        print("This genre is already selected.")
                    else:
                        selected_genres.add(selected_genre)
                        print(f"Added {selected_genre} to genres.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")

            another = input("Add another genre? (y/n): ").strip().lower()
            if another != 'y':
                break
        return selected_genres

    def create_review(self):
        print("\n=== Create a New Review ===")
        game_name = input("Enter game name: ").strip()
        if not game_name:
            print("Game name cannot be empty.")
            return

        # Check for existing review
        if game_name in game_db:
            print(f"\nA review already exists for {game_name}:")
            print(game_db[game_name])
            overwrite = input("Overwrite existing review? (y/n): ").strip().lower()
            if overwrite != 'y':
                return

        score = self.get_game_score()
        genres = self.select_genres()
        maturity = self.select_enum(MaturityRating, "Select maturity rating:")
        cost = self.get_game_cost()
        art_style = self.select_enum(ArtStyle, "Select art style:")
        summary = input("Enter game summary: ").strip()

        game = Game(game_name, genres, maturity, art_style)
        self.current_review = Review(game, score, cost, summary)
        
        save_review(game_name, self.current_review)
        print(f"\nReview for {game_name} has been saved!")

    def search_reviews(self):
        print("\n=== Search Reviews ===")
        search_term = input("Enter game name to search (leave blank to see all): ").strip()
        results = search_reviews(search_term)
        
        if not results:
            print("No reviews found.")
            return
        
        # Convert to list of (name, review) tuples for easier indexing
        results_list = list(results.items())
        total_pages = (len(results_list) + 4) // 5  # Calculate total pages (rounding up)
        current_page = 1
        
        while True:
            print(f"\n=== Search Results (Page {current_page}/{total_pages}) ===")
            
            # Calculate start and end indices for current page
            start_idx = (current_page - 1) * 5
            end_idx = min(start_idx + 5, len(results_list))
            
            # Display reviews for current page
            for i in range(start_idx, end_idx):
                game_name, review = results_list[i]
                print(f"\nReview #{i+1}: {game_name}")
                print(review)
            
            # Show navigation options
            print("\nNavigation:")
            if current_page > 1:
                print("'prev' - Previous page")
            if current_page < total_pages:
                print("'next' - Next page")
            print("'exit' - Return to main menu")
            
            # Get user input
            choice = input("\nWhat would you like to do? ").strip().lower()
            
            if choice == 'next' and current_page < total_pages:
                current_page += 1
            elif choice == 'prev' and current_page > 1:
                current_page -= 1
            elif choice == 'exit':
                break
            else:
                print("Invalid option. Please try again.")

    def run(self):
        """Main application loop"""
        while True:
            print("\n1: Search for reviews")
            print("2: Create a new review")
            print("3: Exit")
            choice = input("\nWhat would you like to do? (1-3): ").strip()
            
            if choice == "1":
                self.search_reviews()
            elif choice == "2":
                self.create_review()
            elif choice == "3":
                print("\nThank you for using the Game Review System!")
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    system = GameReviewSystem()
    system.run()