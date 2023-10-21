import pandas as pd

if  __name__ == '__main__':
    path = r'C:\Users\ZZC\Desktop\5546.xlsx'
    exl = pd.read_excel(path, sheet_name='Sheet1')
    print(exl)