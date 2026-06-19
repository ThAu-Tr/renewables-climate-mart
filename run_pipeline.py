import os
import papermill as pm

NOTEBOOK_DIR = "notebooks"

notebooks = [
    #"01_extract_renewable_genUnits_from_mastr.ipynb",
    "02_build_dimension_tables.ipynb",
    "03_build_generation_fact_table.ipynb",
    "04_build_weather_fact_table.ipynb",
    "05_load_mart_to_duckdb.ipynb",
]

os.chdir(NOTEBOOK_DIR)

for nb in notebooks:
    print(f"\n{'='*60}")
    print(f"Running {nb}")
    print(f"{'='*60}")

    pm.execute_notebook(
        nb,
        nb
    )

print("Pipeline completed.")