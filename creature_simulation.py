class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"


# ===============================
# FlyingCreature Branch
# ===============================

class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.altitude = 0

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} swoops down from altitude {self.altitude}!")
        print(
            f"{self.name} performs an aerial attack on {target.name} "
            f"for {self.attack_power} damage!"
        )
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")


# ===============================
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")


# ===============================
# FireCreature Branch
# ===============================

class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = max(0, min(100, fire_level))

    def emit_fire(self, new_fire_level):
        self.fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name}'s fire level is now {self.fire_level}.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        bonus = self.fire_level // 10
        total_damage = self.attack_power + bonus

        print(
            f"{self.name} engulfs itself in flames at level {self.fire_level} "
            f"and attacks {target.name}!"
        )
        print(f"It deals {total_damage} fire damage!")
        target.hp -= total_damage
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")


if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()

    print("=== Tests Completed ===\n")

    # === FlyingCreature Tests ===
    print("=== FlyingCreature Tests ===\n")
    sky_hawk = FlyingCreature("Sky Hawk", 35, 8)
    dummy1 = Creature("Practice Dummy (Air)", 40, 0)
    sky_hawk.fly_to(120)
    print(f"Altitude should be 120 → Actual: {sky_hawk.altitude}")
    sky_hawk.attack(dummy1)
    print(f"Dummy HP should be 32 → Actual: {dummy1.hp}")
    print()

    # === SwimmingCreature Tests ===
    print("=== SwimmingCreature Tests ===\n")
    aqua_serpent = SwimmingCreature("Aqua Serpent", 50, 7)
    dummy2 = Creature("Practice Dummy (Water)", 40, 0)
    aqua_serpent.dive_to(30)
    print(f"Depth should be 30 → Actual: {aqua_serpent.depth}")
    aqua_serpent.attack(dummy2)
    print(f"Dummy HP should be 33 → Actual: {dummy2.hp}")
    print()

    # === FireCreature Tests ===
    print("=== FireCreature Tests ===\n")

    fire_drake = FireCreature("Fire Drake", 60, 9, fire_level=50)
    dummy3 = Creature("Practice Dummy (Fire)", 50, 0)

    print(f"Initial fire level should be 50 → Actual: {fire_drake.fire_level}")
    fire_drake.attack(dummy3)  # damage = 9 + 50//10 = 14
    print(f"Dummy HP should be 36 → Actual: {dummy3.hp}")

    fire_drake.emit_fire(90)
    print(f"Fire level should be 90 → Actual: {fire_drake.fire_level}")
    fire_drake.attack(dummy3)  # damage = 9 + 9 = 18
    print(f"Dummy HP should be 18 → Actual: {dummy3.hp}")

    print("\n=== Tests Completed ===")
