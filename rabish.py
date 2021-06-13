import decimal
decimal.getcontext().prec = 100
print(decimal.Decimal(1)/decimal.Decimal(42))
print(len(str(840336134453781512605042016806722689075630252100)))
print(len(str(5882352941176470)))