# main.py
# Iron Commander — Entry Point
# Phase 3: Core build — Step 5
#
# This is the only file you need to run.
# It imports the game loop from battlefield.py
# and launches Iron Commander.
#
# Run with:
#   python main.py

import sys
import os

# ─────────────────────────────────────────────
# VERSION CHECK
# Requires Python 3.8 or higher.
# Warns the player and exits cleanly if not met.
# ─────────────────────────────────────────────

if sys.version_info < (3, 8):
    print("\n  Iron Commander requires Python 3.8 or higher.")
    print(f"  You are running Python {sys.version_info.major}."
          f"{sys.version_info.minor}.")
    print("  Please upgrade Python and try again.\n")
    sys.exit(1)


# ─────────────────────────────────────────────
# DEPENDENCY CHECK
# Confirms all required game files are present
# before attempting to import them.
# Gives a clear error if a file is missing.
# ─────────────────────────────────────────────

REQUIRED_FILES = [
    "tank.py",
    "enemy.py",
    "commander.py",
    "battlefield.py"
]

missing = [f for f in REQUIRED_FILES if not os.path.exists(f)]
if missing:
    print("\n  Iron Commander could not start.")
    print("  The following required files are missing:")
    for f in missing:
        print(f"    ✕  {f}")
    print("\n  Make sure all game files are in the same folder"
          " as main.py.\n")
    sys.exit(1)


# ─────────────────────────────────────────────
# IMPORT GAME
# All game logic lives in battlefield.py.
# main.py simply calls run_game() to start.
# ─────────────────────────────────────────────

from battlefield import run_game


# ─────────────────────────────────────────────
# PLAY AGAIN LOOP
# After each game ends, asks the player
# if they want to play again.
# Loops until the player chooses to quit.
# ─────────────────────────────────────────────

def main():
    while True:
        # Run one full game
        run_game()

        # Ask to play again
        print("\n  Would you like to play again?")
        print("  1. Yes — deploy a new squad")
        print("  2. No  — exit")

        while True:
            choice = input("\n  Enter 1 or 2: ").strip()
            if choice == "1":
                break
            elif choice == "2":
                print("\n  Iron Commander out. Good luck, Commander.\n")
                sys.exit(0)
            else:
                print("  Please enter 1 or 2.")


# ─────────────────────────────────────────────
# ENTRY POINT
# Standard Python entry point guard.
# Only runs main() when this file is executed
# directly — not when imported by another file.
# ─────────────────────────────────────────────

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handles Ctrl+C gracefully instead of
        # printing a messy traceback
        print("\n\n  Game interrupted. Iron Commander out.\n")
        sys.exit(0)