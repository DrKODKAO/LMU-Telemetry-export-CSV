# LMU Telemetry Exporter

## Description

Ce script Python exporte tous les fichiers `.duckdb` de Le Mans Ultimate (LMU) en CSV compatibles Google Sheets et Excel.  

Caractéristiques :

- 1 CSV par session/fichier `.duckdb`  
- Toutes les tables de chaque fichier fusionnées horizontalement  
- Colonnes préfixées par le nom de la table  
- Nom du CSV contient `FINAL` pour identifier les exports finis  
- Compatible espaces, accents et noms longs de circuits  
- Installe automatiquement `duckdb` et `pandas` si nécessaire  

---

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

DuckDB CLI pour Windows : https://duckdb.org/docs/installation

Placer duckdb.exe dans le même dossier que le script

Mode d’emploi

Place le script export_lmu_final.py dans le dossier contenant tes fichiers .duckdb.

Double-clique sur le script ou lance-le via python export_lmu_final.py.

Le script va :

détecter tous les fichiers .duckdb

fusionner toutes les tables de chaque fichier

créer un CSV par session/fichier avec le nom NomFichier_FINAL.csv

installer duckdb et pandas si nécessaire

Exemple de sortie

Fichier .duckdb :

Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z.duckdb

CSV généré :

Autodromo Enzo e Dino Ferrari_R_2026-02-19T21_38_55Z_FINAL.csv
Dépendances

duckdb

pandas

Le script gère l’installation automatique si elles manquent.

Remarques

Chaque fichier .duckdb est considéré comme une session unique.

Compatible chemins avec espaces et accents.


---

## 3️⃣ Publier sur GitHub

1. Crée un compte GitHub si tu n’en as pas : [https://github.com](https://github.com)  
2. Crée un nouveau repository : `LMU-Telemetry-Exporter`  
3. Depuis ton dossier local, ouvre un terminal et tape :

```bash
git init
git add .
git commit -m "Initial commit – LMU Telemetry Exporter"
git branch -M main
git remote add origin https://github.com/TON_USERNAME/LMU-Telemetry-Exporter.git
git push -u origin main
