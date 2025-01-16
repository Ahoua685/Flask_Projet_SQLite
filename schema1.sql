-- Création de la table 'Utilisateur'
CREATE TABLE Utilisateur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    date_inscription DATE NOT NULL,
    statut VARCHAR(50) NOT NULL DEFAULT 'actif'
);

-- Création de la table 'Livre'
CREATE TABLE Livre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre VARCHAR(255) NOT NULL,
    auteur VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    annee_publication INTEGER,
    disponible BOOLEAN NOT NULL DEFAULT 1 -- 1 = disponible, 0 = emprunté
);

-- Création de la table 'Stock'
CREATE TABLE Stock (
    livre_id INTEGER PRIMARY KEY,
    quantite_totale INTEGER NOT NULL DEFAULT 0,
    quantite_disponible INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (livre_id) REFERENCES Livre(id) ON DELETE CASCADE
);

-- Création de la table 'Emprunt'
CREATE TABLE Emprunt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utilisateur_id INTEGER NOT NULL,
    livre_id INTEGER NOT NULL,
    date_emprunt DATE NOT NULL,
    date_retour DATE NOT NULL,
    date_retour_effective DATE,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id) ON DELETE CASCADE,
    FOREIGN KEY (livre_id) REFERENCES Livre(id) ON DELETE CASCADE
);

-- Création d'index pour améliorer la performance des recherches de livres
CREATE INDEX idx_livre_titre ON Livre(titre);
CREATE INDEX idx_livre_auteur ON Livre(auteur);
CREATE INDEX idx_livre_genre ON Livre(genre);

-- Création d'un trigger pour mettre à jour la quantité de livres disponibles dans 'Stock' à chaque emprunt
CREATE TRIGGER update_stock_after_emprunt
AFTER INSERT ON Emprunt
FOR EACH ROW
BEGIN
    UPDATE Stock
    SET quantite_disponible = quantite_disponible - 1
    WHERE livre_id = NEW.livre_id;
END;

-- Création d'un trigger pour mettre à jour la quantité de livres disponibles dans 'Stock' à chaque retour de livre
CREATE TRIGGER update_stock_after_retour
AFTER UPDATE ON Emprunt
FOR EACH ROW
WHEN NEW.date_retour_effective IS NOT NULL
BEGIN
    UPDATE Stock
    SET quantite_disponible = quantite_disponible + 1
    WHERE livre_id = NEW.livre_id;
END;
