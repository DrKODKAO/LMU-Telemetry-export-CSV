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
