# 🪨📄✂️ Rock, Paper, Scissors with a Cheating AI

> Este README también está disponible en [Español](README.md)

A Python game where you compete against an **AI that learns from your moves**.
The AI uses *scikit-learn* to try to predict your next move and play against you.

---

## 📑 Table of Contents

* [About](#about)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Examples](#examples)
* [License](#license)

---

## 🧾 About <a name="about"></a>

This project is a twist on the classic *Rock, Paper, Scissors* game.
Instead of playing against a random opponent, you face an **adaptive AI** that tries to exploit the patterns in your plays.

The goal: see if you can outsmart the "cheating" AI that anticipates your strategy.

---

## 🚀 Getting Started <a name="getting-started"></a>

These instructions will help you run the project on your local machine.

### Requirements

You need to have the following installed on your system:

```
- Python 3.8 or higher
- pip (Python package manager)
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/CodeMasters12218/rps-ai.git
```

2. Navigate to the project directory:

```bash
cd rps-ai
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🕹️ Usage <a name="usage"></a>

Run the game from the command line:

```bash
python ppt.py
```

You’ll be prompted to enter your move (`piedra`, `papel`, or `tijeras`) each round.
The AI will respond based on its predictions.

To end the game, simply type `salir`.

---

## ✨ Examples <a name="examples"></a>

```
=== Piedra, Papel o Tijeras con IA tramposa ===
Escribe 'piedra', 'papel', 'tijeras' o 'salir' para terminar.
Tu jugada: piedra
Tú: piedra | IA: piedra -> Empate
Marcador -> Tú: 0, IA: 0, Empates: 1

Tu jugada: tijeras

Tú: tijeras | IA: tijeras -> Empate
Marcador -> Tú: 0, IA: 0, Empates: 2

Tu jugada: papel
Tú: papel | IA: papel -> Empate
Marcador -> Tú: 0, IA: 0, Empates: 3

Tu jugada: piedra
Tú: piedra | IA: tijeras -> Tú ganas
Marcador -> Tú: 1, IA: 0, Empates: 3

Tu jugada: salir

Juego terminado.
Marcador final -> Tú: 1, IA: 0, Empates: 3

...
```

You can try playing randomly, following patterns, or attempting to trick the AI into making bad predictions.

---

## 📜 License <a name="license"></a>

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
