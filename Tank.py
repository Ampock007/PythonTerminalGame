# tank.py
# Iron Commander — Base Tank Class and Friendly Tank Types
# Phase 3: Core build — Step 1

# ─────────────────────────────────────────────
# BASE TANK CLASS
# Every unit in the game inherits from this class.
# Think of it like a template data structure in RPGLE —
# all tanks share these fields and subprocedures.
# ─────────────────────────────────────────────

class Tank:
    def __init__(self, name, hp, attack, symbol):
        self.name      = name      # Display name e.g. "Assault Tank"
        self.symbol    = symbol    # Short label shown on battlefield e.g. "AST"
        self.max_hp    = hp        # Maximum HP — never changes after creation
        self.hp        = hp        # Current HP — goes down when hit
        self.attack    = attack    # Damage this tank deals per hit
        self.shield    = 0         # Shield points — absorbs damage before HP
        self.position  = 0         # Position on the battlefield string
        self.is_alive  = True      # False when HP reaches zero

    # ── TAKE DAMAGE ──────────────────────────────
    # Shield absorbs damage first.
    # Any remaining damage reduces HP.
    # If HP hits zero the tank is marked destroyed.
    def take_damage(self, amount):
        if self.shield > 0:
            if amount <= self.shield:
                # Shield absorbs all the damage
                self.shield -= amount
                print(f"  {self.name}'s shield absorbs {amount} damage! "
                      f"({self.shield} shield remaining)")
                return
            else:
                # Shield absorbs partial damage, rest hits HP
                leftover = amount - self.shield
                print(f"  {self.name}'s shield absorbs {self.shield} damage "
                      f"and breaks!")
                self.shield = 0
                amount = leftover

        # Apply remaining damage to HP
        self.hp -= amount
        print(f"  {self.name} takes {amount} damage! "
              f"({max(self.hp, 0)}/{self.max_hp} HP remaining)")

        # Check if tank is destroyed
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"  *** {self.name} has been DESTROYED! ***")

    # ── RECEIVE HEALTH ────────────────────────────
    # Commander uses this to grant HP from the supply pool.
    # Cannot heal above max_hp.
    def receive_health(self, amount):
        if not self.is_alive:
            print(f"  {self.name} is already destroyed — cannot heal.")
            return 0

        before = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        actual_healed = self.hp - before
        print(f"  {self.name} receives {actual_healed} HP! "
              f"({self.hp}/{self.max_hp} HP)")
        return actual_healed  # Return actual amount used from supply

    # ── RECEIVE SHIELD ────────────────────────────
    # Commander uses this to apply a damage-absorbing shield.
    # Shields stack — adding to any existing shield value.
    def receive_shield(self, amount):
        if not self.is_alive:
            print(f"  {self.name} is already destroyed — cannot shield.")
            return

        self.shield += amount
        print(f"  {self.name} receives a {amount}-point shield! "
              f"(Total shield: {self.shield})")

    # ── STATUS DISPLAY ────────────────────────────
    # Returns a single-line status string for battlefield display.
    # Example: [ AST | HP:120/120 | SH:0 ]
    def status(self):
        shield_str = f" SH:{self.shield}" if self.shield > 0 else ""
        return f"[{self.symbol}|HP:{self.hp}/{self.max_hp}{shield_str}]"

    # ── HP BAR ────────────────────────────────────
    # Visual bar showing health percentage.
    # Example: [████████░░] 80%
    def hp_bar(self, width=10):
        if self.max_hp == 0:
            return "[" + "░" * width + "]"
        filled = int((self.hp / self.max_hp) * width)
        empty  = width - filled
        return f"[{'█' * filled}{'░' * empty}] {self.hp}/{self.max_hp}"

    # ── STRING REPRESENTATION ─────────────────────
    # What prints when you do print(tank)
    def __str__(self):
        alive_str = "ALIVE" if self.is_alive else "DESTROYED"
        return (f"{self.name} | {alive_str} | "
                f"HP: {self.hp}/{self.max_hp} | "
                f"ATK: {self.attack} | Shield: {self.shield}")


# ─────────────────────────────────────────────
# FRIENDLY TANK CLASSES
# Each inherits from Tank and sets its own stats.
# This is Python inheritance — like an RPGLE subtype
# that shares the parent's subprocedures but has
# its own field values.
# ─────────────────────────────────────────────

class ScoutTank(Tank):
    """Fast and light. Spots enemies early but falls quickly without support."""
    def __init__(self):
        super().__init__(
            name   = "Scout Tank",
            hp     = 60,
            attack = 15,
            symbol = "SCT"
        )
        self.speed = 2  # Moves faster — future use in wave system


class AssaultTank(Tank):
    """Balanced all-purpose fighter. Primary damage dealer."""
    def __init__(self):
        super().__init__(
            name   = "Assault Tank",
            hp     = 120,
            attack = 35,
            symbol = "AST"
        )


class HeavyTank(Tank):
    """High armor, high HP. Absorbs punishment for the squad."""
    def __init__(self):
        super().__init__(
            name   = "Heavy Tank",
            hp     = 200,
            attack = 50,
            symbol = "HVY"
        )
        self.speed = 0  # Slow — future use in wave system


class ArtilleryTank(Tank):
    """Long range, devastating damage, but fragile. Protect at all costs."""
    def __init__(self):
        super().__init__(
            name   = "Artillery Tank",
            hp     = 80,
            attack = 70,
            symbol = "ART"
        )
        self.range = 3  # Attacks from further away — future use


# ─────────────────────────────────────────────
# QUICK TEST
# Run this file directly to verify all classes
# work correctly before connecting to the game.
# Command: python tank.py
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  IRON COMMANDER — Tank Class Test")
    print("=" * 50)

    # Create one of each friendly tank
    scout    = ScoutTank()
    assault  = AssaultTank()
    heavy    = HeavyTank()
    artillery = ArtilleryTank()

    squad = [scout, assault, heavy, artillery]

    # Display all tank stats
    print("\n--- Initial Squad Status ---")
    for tank in squad:
        print(f"  {tank}")

    # Test HP bars
    print("\n--- HP Bars ---")
    for tank in squad:
        print(f"  {tank.name:<16} {tank.hp_bar()}")

    # Test taking damage
    print("\n--- Damage Test (Assault Tank takes 40 damage) ---")
    assault.take_damage(40)

    # Test shield absorbing damage
    print("\n--- Shield Test (Heavy Tank receives 60 shield, then takes 80 damage) ---")
    heavy.receive_shield(60)
    heavy.take_damage(80)

    # Test healing
    print("\n--- Heal Test (Scout Tank receives 30 HP) ---")
    scout.take_damage(25)
    scout.receive_health(30)

    # Test destruction
    print("\n--- Destruction Test (Artillery takes 999 damage) ---")
    artillery.take_damage(999)
    artillery.receive_health(50)  # Should not work — already destroyed

    # Final battlefield status display
    print("\n--- Final Battlefield Status ---")
    for tank in squad:
        print(f"  {tank.status()}")

    print("\n" + "=" * 50)
    print("  Tank class test complete.")
    print("=" * 50)