"""
catfacts — JugaadLang Cat Facts Module.
"""
import random

FACTS = [
    "🐈 Cats sleep 70% of their lives. Devs sleep 10% (rest is coding/debugging).",
    "🐈 A group of cats is called a 'clowder'. A group of programmers is called a 'meeting that could have been an email'.",
    "🐈 Cats can make over 100 vocal sounds. Devs can make over 1000 sigh sounds when looking at legacy code.",
    "🐈 Cats have 32 muscles in each ear, helping them ignore you. Developers have 0 muscles to ignore Jira notifications.",
    "🐈 The first cat in space was a French cat named Félicette in 1963. She survived the flight! 🚀",
]


def batao() -> None:
    """Print a random cat fact."""
    print(random.choice(FACTS))
