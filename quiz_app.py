import tkinter as tk
from tkinter import messagebox

# Liste de questions et réponses (QCM)
questions = [
    {"question": "Quelle est la capitale de la France ?", "options": [
        "Paris", "Londres", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Combien font 2 + 2 ?",
        "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Quel est l'élément chimique symbolisé par 'O' ?", "options": [
        "Or", "Oxygène", "Osmium", "Oganesson"], "answer": "Oxygène"},
    {"question": "Qui a écrit 'Les Misérables' ?", "options": [
        "Victor Hugo", "Molière", "Flaubert", "Balzac"], "answer": "Victor Hugo"},
    {"question": "En quelle année a eu lieu la Révolution française ?",
        "options": ["1789", "1815", "1848", "1870"], "answer": "1789"},
    {"question": "Qui est l'inventeur du téléphone ?", "options": [
        "Bell", "Edison", "Tesla", "Newton"], "answer": "Bell"},
    {"question": "Quelle est la planète la plus proche du Soleil ?",
        "options": ["Vénus", "Terre", "Mars", "Mercure"], "answer": "Mercure"},
    {"question": "Combien de continents y a-t-il ?",
        "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Quelle est la monnaie du Japon ?", "options": [
        "Dollar", "Euro", "Yuan", "Yen"], "answer": "Yen"},
    {"question": "Qui a peint la Joconde ?", "options": [
        "Van Gogh", "Da Vinci", "Michel-Ange", "Picasso"], "answer": "Da Vinci"}
]

# Variables globales
score = 0
current_question = 0

# Fonction pour vérifier la réponse et passer à la question suivante


def check_answer():
    global score, current_question
    selected_option = var.get()

    # Vérifier si aucune option n'est sélectionnée
    if selected_option == "":
        messagebox.showwarning(
            "Avertissement", "Veuillez sélectionner une réponse avant de continuer.")
        return  # Ne pas passer à la question suivante si aucune réponse n'est sélectionnée

    # Vérifier si la réponse est correcte
    if selected_option == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question >= len(questions):
        messagebox.showinfo(
            "Résultat", f"Quiz terminé! Votre score est : {score}/{len(questions)}")
        root.quit()  # Fermer l'application
    else:
        show_question(current_question)

# Fonction pour afficher une question


def show_question(q_num):
    question_label.config(text=questions[q_num]["question"])
    options = questions[q_num]["options"]
    var.set(None)  # Réinitialiser la sélection
    for i, option in enumerate(options):
        radio_buttons[i].config(text=option, value=option)


# Initialisation de la fenêtre Tkinter
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

# Label pour afficher la question
question_label = tk.Label(root, text="", font=(
    "Arial", 12), wraplength=300, justify="left")
question_label.pack(pady=20)

# Variable pour suivre l'option sélectionnée
var = tk.StringVar()
var.set(None)  # Aucune option n'est sélectionnée par défaut

# Création des boutons radio pour les options de réponse
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=var, font=(
        "Arial", 10), value="", wraplength=300)
    rb.pack(anchor="w")
    radio_buttons.append(rb)

# Bouton pour valider la réponse
submit_button = tk.Button(root, text="Soumettre", command=check_answer)
submit_button.pack(pady=20)

# Afficher la première question
show_question(current_question)

# Lancer la boucle principale de Tkinter
root.mainloop()
