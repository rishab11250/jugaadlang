"""
fortune — JugaadLang Developer Fortune Teller Module.
"""

import random

FORTUNES = [
    "🔮 Aaj aapka code first-try mein compile ho jayega! Bahut badi khushkhabri aane wali hai.",
    "🔮 Shani bhaari hai aapke database queries par. Index lagana na bhoolna.",
    "🔮 Agle 2 ghante mein StackOverflow par sahi answer milne ke chances 99% hain.",
    "🔮 Aaj koi bug report nahi aane wali. Mast sojao! 🛌",
    "🔮 Aaj variable name badalne se naseeb badal sakta hai.",
]


def batao() -> None:
    """Print a random developer fortune."""
    print(random.choice(FORTUNES))
