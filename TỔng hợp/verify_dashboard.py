import openpyxl

wb = openpyxl.load_workbook('./Feature_02_SA_Tham_So_He_Thong/test case/ProfiX_Master_Test_Cases.xlsx', data_only=False)
dash = wb['📊 Dashboard']
print("Dashboard Formulas:")
for i, row in enumerate(dash.iter_rows(values_only=True)):
    if i >= 2 and i <= 4:
        print(row)
