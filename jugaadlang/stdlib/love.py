import random
import time

def flirt() -> str:
    """Returns a cheesy programmer pickup line."""
    lines = [
        "Are you a 404 error? Because I'm looking for you everywhere.",
        "You must be my loop condition, because I can't stop thinking about you.",
        "Are you a git commit? Because you just changed my world.",
        "Are you HTTP? Because without you, I'm just a 403 Forbidden.",
        "Mera dil tumhare liye hamesha O(1) complex hai, bilkul simple.",
    ]
    line = random.choice(lines)
    print(f"💘 Pickup Line: {line}")
    return line

def date_idea() -> str:
    """Returns a budget-friendly jugaad date idea."""
    ideas = [
        "Chai aur Maggi point pe jaake life discuss karte hain.",
        "Library date: Ek saath baith ke leetcode solve karenge.",
        "Campus ke ground mein baith ke taare dekhenge.",
        "Momos khane chalte hain, meri treat (with limited budget).",
        "Video call pe ek dusre ko apna screen share karke code review karenge.",
    ]
    idea = random.choice(ideas)
    print(f"🗓️ Date Idea: {idea}")
    return idea

def sorry_message(name: str) -> str:
    """Generates a dramatic apology message."""
    print("✍️ Drafting a dramatic apology message...")
    time.sleep(1)
    message = (
        f"Dear {name},\n\n"
        "Mujhse galti ho gayi. Main jaanta hoon ki mere previous actions ek null pointer dereference ki tarah the, jiske wajah se hamare relationship ka system crash ho gaya.\n\n"
        "Main promise karta hoon ki aage se main apne saare bugs fix karunga aur emotional intelligence ke latest framework pe upgrade karunga. Tumhara gussa bilkul justified hai.\n\n"
        "Please mujhe ek retry ka mauka do. Tumhare bina meri life infinite loop mein phas gayi hai jiska koi exit condition nahi hai.\n\n"
        "Yours truly,\nEk Buggy Insaan"
    )
    print(f"💌 Message generated:\n\n{message}")
    return message
