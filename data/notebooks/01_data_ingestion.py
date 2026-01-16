# notebooks/01_data_ingestion.py
# Download TQQQ historical data and save as CSV

from pathlib import Path
import pandas as pd

try:
    import yfinance as yf
except ImportError:
    raise SystemExit(
        "yfinance is not installed yet.\n"
        "This is expected for now.\n"
        "Later we will install it locally or run this in SageMaker."
    )

# --------------------
# Configuration
# --------------------
TICKER = "TQQQ"
START_DATE = "2015-01-01"

DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = DATA_DIR / "tqqq_ohlcv.csv"

# --------------------
# Download data
# --------------------
df = yf.download(
    TICKER,
    start=START_DATE,
    auto_adjust=False,
    progress=False
)

# Clean column names
df.columns = [c.lower().replace(" ", "_") for c in df.columns]
df = df.reset_index()

# --------------------
# Save
# --------------------
df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved {len(df)} rows to {OUTPUT_FILE}")
print(df.head())
