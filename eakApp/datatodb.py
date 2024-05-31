import pandas as pd

excelfile = 'C:\\Users\\HP\Desktop\\med.xlsx'

pf = pd.read_excel(excelfile, engine ='openpyxl')

for line in pf:
    print(line)

# with open (excelfile ,'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)
