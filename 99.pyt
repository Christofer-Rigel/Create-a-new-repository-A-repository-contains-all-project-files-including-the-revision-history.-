import time
import sys
import random

# ====== CONFIG ======
TARGET = "****************"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
BOLD = "\033[1m"

def slow(text, d=0.015):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d)
    print()

def bar(label, length=30, delay=0.02):
    sys.stdout.write(label + " [")
    sys.stdout.flush()
    for _ in range(length):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("]\n")
    sys.stdout.flush()

def meter(label):
    val = random.randint(82, 99)
    slow(f"{label:<25}: {val}%")

def fake_input(prompt):
    slow(prompt, 0.01)
    time.sleep(1)
    slow("> ********")

def clear():
    print("\033c", end="")

# ====== START ======
clear()
time.sleep(1)

slow(RED + BOLD + "PHANTOM INTERFACE v13.4.7" + RESET)
slow(RED + "NON-INTERACTIVE SESSION DETECTED" + RESET)
time.sleep(1)

slow(YELLOW + "Initializing environment..." + RESET)
bar("Boot sequence")
bar("Memory alignment")
bar("Entropy normalization")

slow(RED + "WARNING: Observer detected at terminal." + RESET)
time.sleep(1)

slow(CYAN + "Binding session context..." + RESET)
bar("Context lock")
bar("Identity trace")

slow(RED + BOLD + "TARGET IDENTIFICATION REQUIRED" + RESET)
fake_input("target : ")
slow(GREEN + f"target confirmed → {TARGET}" + RESET)
time.sleep(1)

slow(YELLOW + "Calibrating behavioral model..." + RESET)
bar("Neural mirror sync")
bar("Pattern extraction")
bar("Latency compensation")

slow(RED + "Anomaly detected." + RESET)
slow(RED + "Deviation exceeds tolerance." + RESET)
time.sleep(1)

slow(MAGENTA + "Running deep scan (pass 1/7)" + RESET)
bar("Signal isolation")
slow(MAGENTA + "Running deep scan (pass 2/7)" + RESET)
bar("Residual analysis")
slow(MAGENTA + "Running deep scan (pass 3/7)" + RESET)
bar("Temporal mapping")

slow(RED + BOLD + "SUBJECT RESPONSE PREDICTED" + RESET)
time.sleep(1)

meter("Compliance probability")
meter("Stress threshold")
meter("Awareness level")
meter("Reaction latency")
meter("Cognitive noise")

time.sleep(1)
slow(RED + "Result: unstable equilibrium." + RESET)

time.sleep(1)
slow(CYAN + "Preparing interface prompts..." + RESET)

fake_input("authorization token : ")
fake_input("fallback override key : ")
fake_input("manual abort command : ")

slow(RED + "No valid abort detected." + RESET)
time.sleep(1)

slow(YELLOW + "Engaging containment visuals..." + RESET)
for _ in range(6):
    bar("Stability field", length=20, delay=0.01)

slow(RED + BOLD + "DO NOT CLOSE THIS WINDOW" + RESET)
time.sleep(1)

slow(RED + "Session awareness confirmed." + RESET)
slow(RED + f"Session awareness logged for {TARGET}." + RESET)
time.sleep(1)

slow(MAGENTA + "Synchronizing perception layer..." + RESET)
bar("Visual coherence")
bar("Input echo")
bar("Feedback suppression")

time.sleep(1)
slow(RED + BOLD + "FINAL NOTICE" + RESET)
time.sleep(1)
slow(RED + f"This interface is now active, {TARGET}." + RESET)
time.sleep(1)
slow(RED + "Silence is recommended." + RESET)

time.sleep(2)
slow(CYAN + "Session will remain open." + RESET)
slow(CYAN + "You may look away." + RESET)
slow(CYAN + "It will not." + RESET)
