from pathlib import Path
base_folder = Path(__file__).parent.resolve()
data_file = base_folder / "data.csv"
for i in range(10):
    with open(data_file, "w", buffering=1) as f:
        f.write(f"Some data: {i}")