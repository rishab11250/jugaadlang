"""
jokes — JugaadLang Programmer Jokes Module.
"""

import random

JOKES = [
    "Q: Ek developer ne doosre se poocha: 'Tera code chal gaya kya?'\nA: Doosre ne jawab diya: 'Ha, chal gaya! Pata nahi kaise chala, par chal gaya!' 😂",
    "Q: Why do programmers wear glasses?\nA: Because they can't C#! 🤓",
    "Q: Developer ka sabse bada dushman kaun hota hai?\nA: Wo khud, jab wo 6 mahine purana code dekhta hai. 💀",
    "Q: What is a programmer's favorite place to hang out?\nA: The FOO BAR! 🍻",
    "Q: Ek code bina bugs ke kahan milta hai?\nA: Sirf textbooks mein aur sapno mein. 🛌",
    "Q: Why did the database administrator leave his wife?\nA: She had one-to-many relationships! 💔",
    "Q: Why did the programmer quit his job?\nA: Because he didn't get arrays! 😭",
]


def sunao() -> None:
    """Print a random funny joke."""
    print(random.choice(JOKES))
