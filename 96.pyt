import time
import random

def dramatic_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def summon_banner():
    banner = """
███████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗ ██╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔═══██╗██║   ██║
█████╗  ██║   ██║██████╔╝█████╗  ██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║   ██║██║   ██║
██╔══╝  ██║   ██║██╔═══╝ ██╔══╝  ██╔═══╝ ██╔═══╝ ██╔══╝  ██║╚██╗██║██║   ██║██║   ██║
██║     ╚██████╔╝██║     ███████╗██║     ██║     ███████╗██║ ╚████║╚██████╔╝╚██████╔╝
╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
    """
    print(banner)

def generate_command(index):
    verbs = ["Activate", "Deploy", "Engage", "Summon", "Trigger", "Ignite", "Unleash", "Invoke"]
    adjectives = ["Celestial", "Quantum", "Infernal", "Galactic", "Hypercharged", "Voidbound", "Radiant", "Temporal"]
    nouns = ["Nova Pulse", "Star Lance", "Gravity Hammer", "Photon Storm", "Nebula Net", "Dark Matter Surge", "Solar Flare", "Cosmic Barrage"]
    targets = ["at Target Alpha", "toward Sector 9", "on Coordinates X-42", "across the Orion Belt", "into the Void", "at Enemy Cluster", "toward Earth’s Moon", "into the Abyss"]

    command = f"{index:03d}: {random.choice(verbs)} {random.choice(adjectives)} {random.choice(nouns)} {random.choice(targets)}"
    return command

def main():
    summon_banner()
    dramatic_print("Initializing Supernova Summoner 9000...\n", 0.05)
    time.sleep(1)
    dramatic_print("Loading command arsenal...\n", 0.05)
    time.sleep(1)

    for i in range(1, 151):  # 150 epic commands
        cmd = generate_command(i)
        dramatic_print(cmd, delay=0.000000000000000000001)
        time.sleep(0.000001)

    dramatic_print("\n⚠️  WARNING: Cosmic energy levels exceeding safe thresholds.", 0.03)
    dramatic_print("💥 Recommendation: Retreat to a minimum safe distance of 3 light-years.\n", 0.03)
    dramatic_print("🛑 Terminating sequence...\n", 0.05)
    time.sleep(0.0000000001)
    dramatic_print("Supernova Summoner 9000 shutdown complete. 🌌", 0.05)

if __name__ == "__main__":
    main()