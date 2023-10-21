import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
df.to_csv('qan_stk_prc.csv')
#print(df)
