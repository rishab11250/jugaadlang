"""
motivation — JugaadLang Developer Motivation Module.
"""

import random

QUOTES = [
    "🔥 Tum kar sakte ho! Ek semicolon hi to gayab hai!",
    "🔥 Git push kar do, code prod me dekha jayega. Himmat rakho!",
    "🔥 Kal ka bug aaj solve hoga, bas thodi si chai aur piyo. ☕",
    "🔥 Rome wasn't built in a day, and neither is your project. Lage raho!",
    "🔥 Bugs to aate jaate rahenge, par tumhara jugaad hamesha chalega! 💪",
    "🔥 Junior developer ho to kya hua, code to tum bhi copy-paste kar sakte ho!",
]


def gyan() -> None:
    """Print a random developer motivation quote."""
    print(random.choice(QUOTES))
