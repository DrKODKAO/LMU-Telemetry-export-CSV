# LMU Telemetry Exporter

## Description

Ce script Python exporte tous les fichiers `.duckdb` de Le Mans Ultimate (LMU) en CSV compatibles Google Sheets et Excel.

Caractéristiques :
- 1 CSV par fichier `.duckdb`  
- Toutes les tables fusionnées horizontalement  
- Colonnes préfixées par le nom de la table  
- Nom du CSV contient `FINAL`  
- Compatible espaces, accents et noms longs  
- Installe automatiquement `duckdb` et `pandas` si nécessaire

## Structure du dossier

```text
LMU-Telemetry-Exporter/
│
├─ export_lmu_final.py
├─ duckdb.exe
├─ Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z.duckdb
└─ ...

Prérequis

Python 3.8+ : https://www.python.org/downloads/

DuckDB CLI Windows : https://duckdb.org/docs/installation

Placer duckdb.exe dans le même dossier que le script

Mode d’emploi

Place le script export_lmu_final.py dans le dossier contenant tes fichiers .duckdb.

Double-clique sur le script ou lance-le via python export_lmu_final.py.

Le script détecte tous les fichiers .duckdb, fusionne toutes les tables et crée un CSV par fichier avec le suffixe FINAL.

Exemple de sortie

Fichier .duckdb :

Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z.duckdb

CSV généré :

Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z_FINAL.csv
Dépendances

duckdb

pandas
