# Creature Battle Project (OOP + Git Branching Practice)

This project is designed to help me learn **object-oriented programming** in Python — especially **inheritance** — while also practicing key **Git concepts** like branching, merging, conflict resolution, and version history.

I begin with a base class (`Creature`) and create additional subclasses on separate Git branches to simulate a real development workflow.

---

## Learning Objectives

### Python / OOP
- Understand and implement **classes**
- Use **inheritance** to extend behaviors
- Override and extend methods (e.g., `attack()`)
- Practice writing simple test code in `main`

### Git / Version Control
- Create and switch branches
- Merge branches into `main`
- Resolve merge conflicts
- View commit history (`git log --graph --all`)

---

## Project Structure

```text
oop_creature_code/
│
├── creature_simulation.py   # Base class + subclasses and test code
└── README.md
```

---

## How to Run and Test
1. Make sure you have Python 3 installed.
2. Clone or download this repository:

```bash
git clone https://github.com/Debut17/oop-lab-4
cd oop_creature_code
```

3. Run the simulation:

```bash
python creature_simulation.py
```

4. The program will:
- Run basic tests for the Creature base class.
- Run extra tests for:
    - FlyingCreature (altitude + aerial attack)
    - SwimmingCreature (depth + underwater attack)
    - FireCreature (fire level + boosted fire attacks)
