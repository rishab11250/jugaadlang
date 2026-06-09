"""
memes — JugaadLang Programmer Memes Module.
"""
import random

MEMES = [
    """
    Me: "Let me fix this tiny bug..."
    *Code compiles with 100 new errors*
    
      (╯°□°)╯︵ ┻━┻
    """,
    """
    When my code actually works:
    
      \\(•_•)/
       (   )  "It is alive!!!"
      /     \\
    """,
    """
    Senior Developer looking at junior developer's code:
    
      (ಠ_ಠ) "Kya jugaad lagaya hai bhai?"
    """,
    """
    Code works on localhost but crashes in production:
    
      ¯\\_(ツ)_/¯  "My job here is done."
    """,
]


def dikhao() -> None:
    """Print a random ASCII art programmer meme."""
    print(random.choice(MEMES))
