# Global score variable
score = 0  

def add_points(points):
    """Increase the global score by a given number of points."""
    global score
    score += points
    print(f"Added {points} points. New Score: {score}")

def deduct_points(points):
    """Decrease the global score by a given number of points (without going negative)."""
    global score
    score = max(0, score - points)
    print(f"Deducted {points} points. New Score: {score}")

def reset_score():
    """Reset the global score to zero."""
    global score
    score = 0
    print("Score reset to 0.")

# Example gameplay actions
add_points(10)   # Score: 10
add_points(5)    # Score: 15
deduct_points(7) # Score: 8
reset_score()    # Score: 0
