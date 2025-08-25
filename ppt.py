import random
import numpy as np
from sklearn.linear_model import SGDClassifier

# ============================================================
# Juego: Piedra, Papel o Tijeras contra una IA "tramposa"
# ------------------------------------------------------------
# La IA intenta predecir la siguiente jugada del jugador basándose
# en las jugadas anteriores. Usa un modelo simple de Machine Learning
# (SGDClassifier de scikit-learn) que se entrena de forma incremental.
#
# Enfoque de predicción:
# - Cada jugada se codifica como un número: piedra=0, papel=1, tijeras=2.
# - El modelo intenta aprender la relación entre la jugada previa y
#   la siguiente del jugador.
# - Tras predecir la jugada del usuario, la IA elige la que le gana.
# ============================================================

# Mapeo entre jugadas y números
MOVES = {"piedra": 0, "papel": 1, "tijeras": 2}
REVERSE_MOVES = {0: "piedra", 1: "papel", 2: "tijeras"}

# Modelo ML (SGDClassifier permite partial_fit para aprendizaje online)
model = SGDClassifier(loss="log_loss", max_iter=1000, tol=1e-3)
trained = False  # bandera para saber si ya entrenamos al menos una vez

# Puntajes
score_player = 0
score_ai = 0
score_draws = 0

# Historial de jugadas
history_X = []  # características (jugada anterior)
history_y = []  # etiquetas (siguiente jugada real del jugador)


# ------------------------------------------------------------
# Función para predecir la próxima jugada del jugador
# ------------------------------------------------------------
def predict_next_move(last_move):
    global trained
    if not trained:
        # Si no hay entrenamiento, elegimos al azar
        return random.choice([0, 1, 2])
    else:
        # Predecir en base al último movimiento
        X = np.array([[last_move]])
        prediction = model.predict(X)[0]
        return prediction


# ------------------------------------------------------------
# Función para determinar qué jugada gana
# ------------------------------------------------------------
def determine_winner(player_move, ai_move):
    global score_player, score_ai, score_draws

    if player_move == ai_move:
        score_draws += 1
        return "Empate"
    elif (player_move == 0 and ai_move == 1) or \
         (player_move == 1 and ai_move == 2) or \
         (player_move == 2 and ai_move == 0):
        score_ai += 1
        return "La IA gana"
    else:
        score_player += 1
        return "Tú ganas"


# ------------------------------------------------------------
# Bucle principal del juego
# ------------------------------------------------------------
print("=== Piedra, Papel o Tijeras con IA tramposa ===")
print("Escribe 'piedra', 'papel', 'tijeras' o 'salir' para terminar.")

last_player_move = random.choice([0, 1, 2])  # jugada inicial aleatoria

while True:
    user_input = input("Tu jugada: ").lower().strip()

    if user_input == "salir":
        print("\nJuego terminado.")
        print(f"Marcador final -> Tú: {score_player}, IA: {score_ai}, Empates: {score_draws}")
        break

    if user_input not in MOVES:
        print("Entrada inválida. Usa 'piedra', 'papel' o 'tijeras'.")
        continue

    player_move = MOVES[user_input]

    # La IA predice la próxima jugada del jugador
    predicted_move = predict_next_move(last_player_move)

    # La IA elige la jugada que gana contra la predicción
    ai_move = (predicted_move + 1) % 3

    # Mostrar resultados
    result = determine_winner(player_move, ai_move)
    print(f"Tú: {REVERSE_MOVES[player_move]} | IA: {REVERSE_MOVES[ai_move]} -> {result}")
    print(f"Marcador -> Tú: {score_player}, IA: {score_ai}, Empates: {score_draws}\n")

    # Guardar datos para entrenamiento
    history_X.append([last_player_move])
    history_y.append(player_move)

    # Entrenamiento incremental del modelo
    if len(history_y) > 1:
        X_train = np.array(history_X)
        y_train = np.array(history_y)
        if not trained:
            model.partial_fit(X_train, y_train, classes=[0, 1, 2])
            trained = True
        else:
            model.partial_fit([history_X[-1]], [history_y[-1]])

    # Actualizar última jugada
    last_player_move = player_move