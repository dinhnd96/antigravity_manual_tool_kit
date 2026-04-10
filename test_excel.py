import pandas as pd
import sys

def check_excel(file_path):
    xl = pd.ExcelFile(file_path)
    for sheet in xl.sheet_names:
        print(f"Sheet: {sheet}")
        df = xl.parse(sheet)
        if not df.empty:
            print("Columns:", df.columns.tolist())
            print("First row:", df.iloc[0].to_dict())

if __name__ == "__main__":
    check_excel(sys.argv[1])
