# get-ExecutionPolicy in windows to get status, if restricted:
# Windows Powershell as admin -> Set-ExecutionPolicy Unrestricted -Force
# Also -> Set-ExecutionPolicy Unrestricted -Scope CurrentUser
# You can put it in restricted again once you finish if you want.
import sys

print("\nLOADING STATUS: Loading Programs...\n")
print("Checking dependencies: ")
try:
    import pandas as pd  # type: ignore
    print(f"[OK] {pd.__name__} {pd.__version__}"
          " - Data manipulation ready.")
    import numpy as np
    print(f"[OK] {np.__name__} {np.__version__}"
          " -  Numerical computation ready.")
    import requests  # type: ignore
    print(f"[OK] {requests.__name__} {requests.__version__}"
          " - Network access ready.")
    import matplotlib as mlt  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    print(f"[OK] {mlt.__name__} {mlt.__version__}"
          " - Visualization ready.")
except ModuleNotFoundError as err_msg:
    module = (str.split(str(err_msg), " "))[-1]
    print(f"[KO] Required module {module} not found.\n"
          "\nTo install all the requested dependencies run:\n"
          "Using PIP:\n\tpip install -r requirements.txt\n"
          "Using Poetry:\n\tpoetry install\n\tpoetry run python loading.py\n")
    sys.exit(1)

print("\n[#1] - Gathering data from PokeAPI using request: ...")

url = "https://pokeapi.co/api/v2/pokemon?limit=151"
pokemon_list = requests.get(url).json()["results"]

data_dict = []

for pokemon in pokemon_list:
    data = requests.get(pokemon["url"]).json()

    stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}

    data_dict.append({
        "hp": stats["hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "special_attack": stats["special-attack"],
        "special_defense": stats["special-defense"],
        "speed": stats["speed"]
    })

print("[#2] - Building the DataFrame using pandas: ...")

df = pd.DataFrame(data_dict)

stats_cols = [
    "hp",
    "attack",
    "defense",
    "special_attack",
    "special_defense",
    "speed"
]

print("[#3] - Calculate statistics using numpy: ...")

avg = np.mean(df[stats_cols], axis=0)

summary = pd.DataFrame({
    "average": avg,
}, index=stats_cols)

print("[#4] - Generating visualization using matplotlib: ...")

x = np.arange(len(stats_cols))

plt.figure(figsize=(10, 6))

plt.plot(x, summary["average"], marker="o", label="Average")

plt.xticks(x, stats_cols)
plt.ylabel("Stat Value")
plt.title("Pokémon Gen 1 Stats")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "pokemon_stats_summary.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nFile saved at: pokemon_stats_summary.png\n")
