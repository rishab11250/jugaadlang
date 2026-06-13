import random
import time
import sys

def bahana() -> str:
    """Returns a creative, random excuse for not completing an assignment."""
    excuses = [
        "Mera laptop update ho raha tha.",
        "Wifi router pe paani gir gaya tha.",
        "Code compile toh ho raha tha, achanak power cut ho gaya.",
        "GitHub pe push karte time merge conflict ne laptop freeze kar diya.",
        "Kutte ne mera source code kha liya.",
    ]
    excuse = random.choice(excuses)
    print(f"🤥 Excuse Generated: {excuse}")
    return excuse

def cgpa_calc(grades_list: list) -> float:
    """Calculates CGPA from a list of grades (10-point scale)."""
    if not grades_list:
        print("❌ Koi grades nahi hain. 0 CGPA.")
        return 0.0
    
    total = sum(grades_list)
    cgpa = total / len(grades_list)
    print(f"🎓 Your CGPA is: {cgpa:.2f}")
    if cgpa >= 9.0:
        print("🌟 Topper alert! Sharma ji ka beta is shivering.")
    elif cgpa >= 7.0:
        print("👍 Theek hai, aage badho.")
    else:
        print("📚 Padhai pe dhyaan do.")
    return cgpa

def proxy_attendance(name: str) -> None:
    """Simulates a proxy attendance entry."""
    print(f"🤖 Booting up Proxy Attendance Script for {name}...")
    time.sleep(1)
    print(f"🕵️ Bypassing university firewall...")
    time.sleep(1)
    print(f"🎙️ Simulating voice 'Present Sir!'...")
    time.sleep(1)
    print(f"✅ Attendance marked for {name}. Proxy successful! 😎")
