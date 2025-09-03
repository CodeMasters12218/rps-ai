# 🪨📄✂️ Piedra, Papel o Tijeras con IA Tramposa

> This README is also available in [English](README_en.md)


Un juego en Python donde compites contra una **IA que aprende de tus jugadas**.
La IA usa *scikit-learn* para intentar predecir tu siguiente movimiento y jugar en tu contra.

---

## 📑 Tabla de Contenidos

* [Acerca de](#acerca_de)
* [Comenzando](#comenzando)
* [Uso](#uso)
* [Ejemplos](#ejemplos)
* [Licencia](#licencia)

---

## 🧾 Acerca de <a name="acerca_de"></a>

Este proyecto es una variación del clásico juego *Piedra, Papel o Tijeras*.
En lugar de jugar contra un oponente aleatorio, te enfrentas a una **IA adaptativa** que intenta explotar los patrones de tus jugadas.

El objetivo: comprobar si puedes engañar a la IA que "hace trampa" al anticipar tu estrategia.

---

## 🚀 Comenzando <a name="comenzando"></a>

Estas instrucciones te permitirán ejecutar el proyecto en tu máquina local.

### Requisitos

Necesitas tener lo siguiente instalado en tu sistema:

```
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
```

### Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/CodeMasters12218/rps-ai.git
```

2. Accede al directorio del proyecto:

```bash
cd rps-ai
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🕹️ Uso <a name="uso"></a>

Ejecuta el juego desde la línea de comandos:

```bash
python ppt.py
```

Se te pedirá que introduzcas tu jugada (`piedra`, `papel` o `tijeras`) en cada ronda.
La IA responderá en base a sus predicciones.

Para terminar el juego, simplemente escribe `salir`.

---

## ✨ Ejemplos <a name="ejemplos"></a>

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

Puedes intentar jugar de forma aleatoria, seguir patrones o engañar a la IA para que prediga mal.

---

## 📜 Licencia <a name="licencia"></a>

Este proyecto está licenciado bajo la **MIT License** – consulta el archivo [LICENSE](LICENSE) para más detalles.