import sqlite3

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas déjà)
connection = sqlite3.connect('bibliotheque.db')

# Exécution du script de création des tables (schema.sql)
with open('schema.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour exécuter les requêtes
cur = connection.cursor()

# Insertion des utilisateurs
cur.execute("INSERT INTO Utilisateur (nom, email, date_inscription, statut) VALUES (?, ?, ?, ?)", 
            ('Jean Dupont', 'jean.dupont@example.com', '2025-01-01', 'actif'))
cur.execute("INSERT INTO Utilisateur (nom, email, date_inscription, statut) VALUES (?, ?, ?, ?)", 
            ('Alice Martin', 'alice.martin@example.com', '2025-01-05', 'actif'))
cur.execute("INSERT INTO Utilisateur (nom, email, date_inscription, statut) VALUES (?, ?, ?, ?)", 
            ('Marc Lefevre', 'marc.lefevre@example.com', '2025-01-10', 'actif'))
cur.execute("INSERT INTO Utilisateur (nom, email, date_inscription, statut) VALUES (?, ?, ?, ?)", 
            ('Sophie Tremblay', 'sophie.tremblay@example.com', '2025-01-12', 'actif'))

# Insertion des livres
cur.execute("INSERT INTO Livre (titre, auteur, genre, annee_publication, disponible) VALUES (?, ?, ?, ?, ?)",
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Fiction', 1943, 1))
cur.execute("INSERT INTO Livre (titre, auteur, genre, annee_publication, disponible) VALUES (?, ?, ?, ?, ?)",
            ('Les Misérables', 'Victor Hugo', 'Classique', 1862, 1))
cur.execute("INSERT INTO Livre (titre, auteur, genre, annee_publication, disponible) VALUES (?, ?, ?, ?, ?)",
            ('1984', 'George Orwell', 'Dystopie', 1949, 1))
cur.execute("INSERT INTO Livre (titre, auteur, genre, annee_publication, disponible) VALUES (?, ?, ?, ?, ?)",
            ('La Peste', 'Albert Camus', 'Roman', 1947, 1))

# Insertion des stocks (quantité des livres disponibles)
cur.execute("INSERT INTO Stock (livre_id, quantite_totale, quantite_disponible) VALUES (?, ?, ?)",
            (1, 5, 5))
cur.execute("INSERT INTO Stock (livre_id, quantite_totale, quantite_disponible) VALUES (?, ?, ?)",
            (2, 3, 3))
cur.execute("INSERT INTO Stock (livre_id, quantite_totale, quantite_disponible) VALUES (?, ?, ?)",
            (3, 4, 4))
cur.execute("INSERT INTO Stock (livre_id, quantite_totale, quantite_disponible) VALUES (?, ?, ?)",
            (4, 2, 2))

# Insérer un emprunt (par exemple, un utilisateur emprunte un livre)
cur.execute("INSERT INTO Emprunt (utilisateur_id, livre_id, date_emprunt, date_retour) VALUES (?, ?, ?, ?)",
            (1, 1, '2025-01-15', '2025-01-30'))  # Jean Dupont emprunte 'Le Petit Prince'

# Validation des modifications dans la base de données
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()

print("Base de données et données initiales créées avec succès !")
