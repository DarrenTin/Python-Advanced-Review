import random

class Player:
    """Represents a player in the game with a name and score tracking."""
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1

    def add_points(self, points):
        """Increase the player's score and check for level-ups."""
        self.score += points
        print(f"{self.name} gained {points} points. New Score: {self.score}")
        self.check_level_up()

    def deduct_points(self, points):
        """Decrease the player's score but prevent negative values."""
        self.score = max(0, self.score - points)
        print(f"{self.name} lost {points} points. New Score: {self.score}")

    def check_level_up(self):
        """Increase level if the player reaches a score threshold."""
        new_level = self.score // 50 + 1  # Level up every 50 points
        if new_level > self.level:
            self.level = new_level
            print(f"{self.name} leveled up! Now at Level {self.level}")

    def reset_score(self):
        """Reset the player's score and level."""
        self.score = 0
        self.level = 1
        print(f"{self.name}'s score has been reset.")

class Game:
    """Manages multiple players, scoring rules, and leaderboards."""
    
    def __init__(self):
        self.players = {}

    def add_player(self, name):
        """Add a new player to the game."""
        if name not in self.players:
            self.players[name] = Player(name)
            print(f"Player '{name}' added to the game.")

    def remove_player(self, name):
        """Remove a player from the game."""
        if name in self.players:
            del self.players[name]
            print(f"Player '{name}' removed from the game.")

    def reward_random_bonus(self):
        """Randomly give a player a bonus."""
        if not self.players:
            print("No players in the game.")
            return
        
        player = random.choice(list(self.players.values()))
        bonus = random.randint(5, 20)
        print(f"🎉 Bonus Time! {player.name} gets an extra {bonus} points!")
        player.add_points(bonus)

    def apply_random_penalty(self):
        """Randomly penalize a player."""
        if not self.players:
            print("No players in the game.")
            return
        
        player = random.choice(list(self.players.values()))
        penalty = random.randint(5, 15)
        print(f"⚠️ Penalty! {player.name} loses {penalty} points!")
        player.deduct_points(penalty)

    def show_leaderboard(self):
        """Display players sorted by score."""
        if not self.players:
            print("No players in the game.")
            return
        
        print("\n🏆 Leaderboard 🏆")
        sorted_players = sorted(self.players.values(), key=lambda p: p.score, reverse=True)
        for rank, player in enumerate(sorted_players, 1):
            print(f"{rank}. {player.name} - Score: {player.score}, Level: {player.level}")

# --- Game Simulation ---
game = Game()

# Adding players
game.add_player("Alice")
game.add_player("Bob")
game.add_player("Charlie")

# Simulating gameplay
game.players["Alice"].add_points(30)
game.players["Bob"].add_points(60)
game.players["Charlie"].add_points(45)
game.reward_random_bonus()
game.apply_random_penalty()
game.players["Alice"].deduct_points(15)

# Show leaderboard
game.show_leaderboard()
