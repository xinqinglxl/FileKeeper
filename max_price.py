import akshare as ak
import pandas as pd
import numpy as np
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-s", "--stock", help="stock code", dest="target_stock", type=str, default="")
# args = parser.parse_args()

# daily_minutes = []
# am_minutes = pd.date_range(start = '09:31:00', end = '11:30:00', freq='min')
# for i in am_minutes:
#     daily_minutes.append(str(i)[-8:])
# pm_minutes = pd.date_range(start = '13:01:00', end = '15:00:00', freq='min')
# for i in pm_minutes:
#     daily_minutes.append(str(i)[-8:])

# print(daily_minutes)
# stock_zh_ah_daily_df = ak.stock_zh_index_daily(symbol=str(target_stock))

stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol='sz300750', period='1', adjust="qfq")
# print(stock_zh_a_minute_df)

stock_zh_a_minute_df.to_csv('daily_details/'+'sz300750.csv')

# dates = pd.date_range('1/1/2000', periods=8)
# print(dates)

# df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df)
# if __name__ == "__main__":
#     if args.target_stock.startswith('6'):
#         target_stock = 'sh' + args.target_stock
#     else:
#         target_stock = 'sz' + args.target_stock
#     print("parameter a is :", target_stock)

#     stock_zh_ah_daily_df = ak.stock_zh_index_daily(symbol=str(target_stock))
#     stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol=target_stock, period='1', adjust="qfq")
