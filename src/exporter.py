import pandas as pd
from pathlib import Path


def save_to_excel(data, filename="output.xlsx"):
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    # полный путь
    file_path = output_dir / filename

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

    print(f"💾 Saved to {file_path}")