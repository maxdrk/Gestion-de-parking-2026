#!/usr/bin/env bash

set -e

echo "Création du venv"
python3 -m venv venv

echo "Activation du venv"
source venv/bin/activate

echo "Installation des dépendances"
python -m pip install -r requirement.txt

echo "Lancement du programme de gestion de paiement"
python ./main.py