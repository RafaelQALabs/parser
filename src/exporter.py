import pandas as pd
from pathlib import Path


COLUMNS = [
    "title",
    "total_area",
    "living_area",
    "floors",
    "bedrooms",
    "dimensions",
    "price",
    "url"
]


def save_to_excel(data, filename="output.xlsx"):
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / filename

    df = pd.DataFrame(data)

    # 🔥 КЛЮЧЕВОЕ ИСПРАВЛЕНИЕ
    df = df.reindex(columns=COLUMNS)

    df.to_excel(file_path, index=False)

    print(f"💾 Saved to {file_path}")