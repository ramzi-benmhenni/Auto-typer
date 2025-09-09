import tkinter as tk
import pyautogui
import pyperclip
import time
import random  # On importe la bibliothèque pour la génération de nombres aléatoires

# --- FONCTION PRINCIPALE MISE À JOUR ---
def start_typing():
    # Récupérer le texte (inchangé)
    text_to_type = text_entry.get("1.0", tk.END)
    
    # --- NOUVELLE LOGIQUE POUR LA VITESSE ---
    try:
        # Récupérer les deux valeurs de vitesse depuis les champs de saisie
        min_speed = float(min_speed_entry.get())
        max_speed = float(max_speed_entry.get())
    except ValueError:
        # En cas d'erreur (champs vides ou invalides), on utilise des valeurs par défaut sûres
        min_speed = 0.04
        max_speed = 0.12
    
    # Sécurité : si l'utilisateur inverse min et max, on les corrige
    if min_speed > max_speed:
        min_speed, max_speed = max_speed, min_speed # Astuce pour échanger les valeurs

    if not text_to_type.strip():
        status_label.config(text="Erreur : Veuillez entrer du texte.")
        return

    # --- COMPTE À REBOURS (inchangé) ---
    for i in range(5, 0, -1):
        status_label.config(text=f"Début dans {i} secondes... Changez de fenêtre !")
        window.update()
        time.sleep(1)

    status_label.config(text="Frappe en cours...")
    window.update()

    # --- LOGIQUE DE FRAPPE AVEC DÉLAI ALÉATOIRE ---
    for char in text_to_type:
        pyperclip.copy(char)
        pyautogui.hotkey('ctrl', 'v')
        
        # Calculer un délai aléatoire pour CETTE lettre, entre les bornes min et max
        random_delay = random.uniform(min_speed, max_speed)
        
        # Attendre pendant cette durée aléatoire
        time.sleep(random_delay)

    status_label.config(text="Terminé ! Prêt pour le prochain texte.")

# --- INTERFACE GRAPHIQUE MISE À JOUR ---
window = tk.Tk()
window.title("Auto Typer - Vitesse Variable")

main_label = tk.Label(window, text="Copiez votre texte ici et réglez la vitesse de frappe :")
main_label.pack(pady=5)

text_entry = tk.Text(window, height=10, width=60, wrap="word", font=("Arial", 10))
text_entry.pack(pady=5, padx=10)

# --- NOUVEAU CADRE POUR LES RÉGLAGES DE VITESSE ---
speed_frame = tk.Frame(window)
speed_frame.pack(pady=5)

# Champ pour la vitesse minimale
min_speed_label = tk.Label(speed_frame, text="Vitesse Min (sec):")
min_speed_label.pack(side=tk.LEFT, padx=(0, 5))
min_speed_entry = tk.Entry(speed_frame, width=6)
min_speed_entry.insert(0, "0.04")  # Une valeur par défaut réaliste pour les frappes rapides
min_speed_entry.pack(side=tk.LEFT)

# Champ pour la vitesse maximale
max_speed_label = tk.Label(speed_frame, text="Max (sec):")
max_speed_label.pack(side=tk.LEFT, padx=(10, 5))
max_speed_entry = tk.Entry(speed_frame, width=6)
max_speed_entry.insert(0, "0.12")  # Une valeur par défaut pour simuler de courtes pauses
max_speed_entry.pack(side=tk.LEFT)

start_button = tk.Button(window, text="Démarrer la frappe", command=start_typing)
start_button.pack(pady=10)

status_label = tk.Label(window, text="En attente...", relief="sunken", anchor="w")
status_label.pack(fill="x", side="bottom")

window.mainloop()