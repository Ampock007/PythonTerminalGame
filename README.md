# PythonTerminalGame
My first python terminal game using codecademy and claude to complete steps and design. 
# Iron Commander 🎖️

A terminal-based tank survival strategy game built in Python.

---

## About the Game

**Iron Commander** is a turn-based strategy survival game played entirely in the terminal. You take command of a squad of tanks on a hostile battlefield where enemy forces actively hunt and engage your units. Your role is not to fight directly — you play as the **Commander**, a support unit who moves across the battlefield to keep your tanks alive through shields and supplies health while your tanks do the fighting.

Survive as many waves as possible. Every decision counts.

---

## Story

The desert battlefield stretches for miles. Enemy armored divisions are closing in from both flanks. Your squad of tanks — scouts, assault units, heavy armor, and long-range artillery — stands between the enemy and total defeat. 

You are the Commander. You cannot fire a weapon. But without you, your tanks will fall. Move fast. Support wisely. Keep them alive.

---

## Gameplay

### The Battlefield

The battlefield is displayed as a text string in the terminal, showing the position of every unit:

```
ENEMY >  [ RDR ] [ ENF ]  ||  [ SCT ] [CMD] [ HVY ] [ ART ]  ||  [ SGE ]  < ENEMY
```

Enemy tanks close in from both sides. Your Commander sits among your friendly tanks, moving left or right each turn to provide support.

### Turn Structure

Each turn follows five steps:

1. **Display** — The battlefield is printed showing all unit positions, HP, shields, and your supply pool
2. **Commander action** — You choose one action: move left, move right, grant health, or set a shield
3. **Friendly tanks fire** — Your tanks automatically attack the nearest enemy in range
4. **Enemies move and attack** — Enemy tanks advance and fire on their targets
5. **Results** — Destroyed units are removed, supply is awarded for kills, and the next wave begins if all enemies are cleared

### Commander Abilities

| Ability | Effect | Cost |
|---|---|---|
| Move left / right | Reposition to support different tanks | Free |
| Grant health | Transfer HP from supply pool to a nearby tank | Supply points |
| Set shield | Apply temporary damage reduction to a nearby tank | Shield charge |

---

## Units

### Friendly Tanks

| Tank | HP | Attack | Role |
|---|---|---|---|
| Scout | 60 | 15 | Fast, spots enemies early, fragile |
| Assault | 120 | 35 | Balanced all-purpose fighter |
| Heavy | 200 | 50 | Slow, high armor, absorbs punishment |
| Artillery | 80 | 70 | Long range, high damage, must be protected |

### Enemy Tanks

| Enemy | HP | Attack | Behavior |
|---|---|---|---|
| Raider | 50 | 20 | Fast — targets the Commander directly |
| Enforcer | 100 | 30 | Standard — targets nearest friendly tank |
| Siege tank | 180 | 55 | Slow but devastating — targets heaviest unit |
| Hunter | 70 | 40 | Cunning — targets the most damaged friendly tank |

---

## Health Supply System

The Commander carries a **supply pool** used to grant health to tanks. Supply is finite and must be earned through combat.

- **Starting supply:** 100 points
- **Supply cap:** 200 points
- **Earning supply:** Destroying enemy tanks adds supply
  - Raider: +15 | Enforcer: +25 | Hunter: +30 | Siege tank: +50
- **Wave bonus:** Completing a wave without losing a friendly tank grants +40 supply

Managing your supply is the core strategic challenge. Spend it now to survive, or save it for harder waves ahead.

---

## Win and Loss Conditions

- **Loss:** The Commander is destroyed, or all friendly tanks are eliminated
- **Victory:** There is no final win — the game is a survival challenge
- **Score:** Your score is the highest wave number you survive

---

## Project Structure

```
iron-commander/
│
├── main.py              # Entry point — starts the game
├── tank.py              # Base Tank class and friendly tank types
├── enemy.py             # Enemy tank classes
├── commander.py         # Commander class and abilities
├── battlefield.py       # Display and game loop logic
├── wave.py              # Wave spawning and progression
└── README.md            # This file
```

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Ampock007/iron-commander.git
```

2. Navigate into the project folder:
```bash
cd iron-commander
```

3. Run the game:
```bash
python main.py
```

> Requires Python 3.8 or higher. No external libraries needed — built entirely with the Python standard library.

---

## Development Phases

This project is being built in stages as part of a Python learning journey:

- [x] Phase 1 — Game design and concept
- [ ] Phase 2 — Python concept research
- [ ] Phase 3 — Build core battle loop
- [ ] Phase 4 — Expand with full wave system and abilities
- [ ] Phase 5 — Polish and final testing

---

## Built With

- **Python 3** — Core language
- **Standard library only** — `random`, `time`, `os`
- No external dependencies required

---

## Author

Built as a Python learning project — combining strategy game design with core programming concepts including classes, inheritance, loops, functions, and input handling.

---

*Iron Commander — Lead wisely. Supply carefully. Survive.*
