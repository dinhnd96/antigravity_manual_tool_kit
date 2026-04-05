import pandas as pd
df = pd.read_excel('Feature_02_SA_Tham_So_He_Thong/test case/Test_Cases_SA09_Final_Standard.xlsx', sheet_name='Test Cases')
for index, row in df.iterrows():
    print(f"[{row['TC_ID']}] ({row['BR_Ref']}) - {row['Title']}")
    print(f"Precondition:\n{row['Precondition']}")
    print(f"Steps:\n{row['Steps']}")
    print(f"Expected:\n{row['Expected']}")
    print("-" * 40)
