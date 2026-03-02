import subprocess
import sys
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import duckdb
except ImportError:
    print("duckdb non trouvé, installation en cours...")
    install("duckdb")
    import duckdb

try:
    import pandas as pd
except ImportError:
    print("pandas non trouvé, installation en cours...")
    install("pandas")
    import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)
print(f"Dossier courant : {folder}")

duckdb_files = [f for f in os.listdir(folder) if f.lower().endswith(".duckdb")]

if not duckdb_files:
    print("Aucun fichier .duckdb trouvé dans ce dossier.")
    input("Appuyez sur Entrée pour quitter...")
    sys.exit()

for db_file in duckdb_files:
    print(f"\n=== Traitement : {db_file} ===")
    conn = duckdb.connect(db_file)

    # Lister toutes les tables
    try:
        tables = conn.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='main';"
        ).fetchall()
        tables = [t[0] for t in tables]
    except Exception as e:
        print(f"Erreur récupération tables : {e}")
        continue

    if not tables:
        print("Aucune table trouvée !")
        continue

    table_dfs = []
    for table in tables:
        try:
            df = conn.execute(f'SELECT * FROM "{table}"').fetchdf()
            df = df.add_prefix(f"{table}_")
            table_dfs.append(df)
        except Exception as e:
            print(f"Erreur lecture table {table} : {e}")

    if table_dfs:
        try:
            combined_df = pd.concat(table_dfs, axis=1)
            csv_name = f"{os.path.splitext(db_file)[0]}_FINAL.csv"
            combined_df.to_csv(csv_name, index=False)
            print(f"Export FINAL : {csv_name}")
        except Exception as e:
            print(f"Erreur fusion tables : {e}")

print("\n=== Export FINAL terminé ! ===")
input("Appuyez sur Entrée pour quitter...")
