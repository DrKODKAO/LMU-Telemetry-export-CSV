Ce script Python permet d’exporter tous les fichiers de télémétrie LMU (.duckdb) en CSV prêts à être utilisés dans Excel ou Google Sheets.

Caractéristiques :

1 CSV par session / fichier .duckdb

Toutes les tables de la session sont fusionnées horizontalement, avec colonnes préfixées par le nom de la table

Nom du fichier exporté contient FINAL pour identifier les exports finis

Compatible avec espaces, accents et noms longs de circuits

Installe automatiquement les dépendances Python nécessaires (duckdb, pandas)

Structure du dossier

Pour que le script fonctionne correctement, place-le à la racine du dossier Telemetry, avec la structure suivante :

Telemetry/
│
├─ export_lmu_final.py   <- Le script Python
├─ duckdb.exe            <- DuckDB CLI pour Windows
├─ Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z.duckdb
├─ Autodromo José Carlos Pace_R_2026-02-28T23_17_49Z.duckdb
└─ ... (tous les autres fichiers .duckdb)
Pré-requis

Python 3.8+ installé sur votre machine : https://www.python.org/downloads/

DuckDB CLI pour Windows : téléchargeable ici : https://duckdb.org/docs/installation

Place duckdb.exe dans le même dossier que le script pour qu’il fonctionne

Mode opératoire

Télécharge le script export_lmu_final.py et place-le dans le dossier Telemetry contenant tes fichiers .duckdb.

Télécharge duckdb.exe et place-le au même endroit.

Vérifie que Python 3 est installé et accessible depuis l’invite de commandes (ou double-clique sur le script).

Double-clique sur export_lmu_final.py → le script va :

détecter automatiquement tous les fichiers .duckdb

fusionner toutes les tables pour chaque fichier

créer un CSV par session/fichier avec le nom NomFichier_FINAL.csv

installer automatiquement duckdb et pandas si nécessaire

Exemple de sortie

Si tu as un fichier :

Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z.duckdb

Le script générera :

Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z_FINAL.csv

Toutes les tables de ce fichier sont combinées horizontalement

Les colonnes sont préfixées par le nom de la table (ex : Brake Migration_ABS, Laps_Best LapTime)

Prêt à être ouvert dans Google Sheets ou Excel

Dépendances

Le script gère l’installation automatique de :

duckdb

pandas

Remarques

Chaque fichier .duckdb est considéré comme une session unique

Aucun traitement des sessions internes (session_id) n’est nécessaire

Compatible Windows et chemins avec espaces et accents

Tu peux publier ce README directement dans ton dépôt GitHub, à la racine, et mettre le script + duckdb.exe dans le même dossier.
