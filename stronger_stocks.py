import akshare as ak
import pandas as pd
import talib
import time
import os

# stock_zh_ah_name_dict = ak.stock_zh_ah_name()
# print(stock_zh_ah_name_dict)
# for k in stock_zh_ah_name_dict.keys():
#     print(k)
#     stock_zh_ah_daily_df = ak.stock_zh_ah_daily(symbol=str(k), start_year="2019", end_year="2020")
#     # if stock_zh_ah_daily_df:
#     print(stock_zh_ah_daily_df)
#     i+=1
#     if i > 10:
#         break
# target_stocks = ['sz300200', 'sz300576', 'sz300537', 'sz300346', 'sz002338']
target_stocks_customize = []
with open('watch_list_customize.txt', 'r') as f:
    for line in f.readlines():
        stock_id = str(line.strip())
        if stock_id.startswith('6'):
            target_stocks_customize.append('sh' + stock_id)
        else:
            target_stocks_customize.append('sz' + stock_id)

target_stocks_industry = []
with open('watch_list_industry.txt', 'r') as f:
    for line in f.readlines():
        stock_id = str(line.strip())
        if stock_id.startswith('6'):
            target_stocks_industry.append('sh' + stock_id)
        else:
            target_stocks_industry.append('sz' + stock_id)

ex_list = []
with open('ex_list.txt', 'r') as f:
    for line in f.readlines():
        stock_id = str(line.strip())
        if stock_id.startswith('6'):
            ex_list.append('sh' + stock_id)
        else:
            ex_list.append('sz' + stock_id)

if os.path.exists('summary_industry.txt'):
    os.remove('summary_industry.txt')
else:
    print('file not exists: summary.txt')

if os.path.exists('summary_custimize.txt'):
    os.remove('summary_custimize.txt')
else:
    print('file not exists: summary.txt')

def download_data(target_stocks):
    for target_stock in target_stocks:
        print(target_stock)
        if target_stock in ex_list:
            print('Skip: ' + target_stock)
            continue
        if os.path.exists('daily_summary/' + target_stock + '.csv'):
            os.remove('daily_summary/' + target_stock + '.csv')
        else:
            print('file not exists: ' + target_stock + '.csv')
        stock_zh_ah_daily_df = ak.stock_zh_index_daily(symbol=str(target_stock))
    #     print(stock_zh_ah_daily_df)
        stock_zh_ah_daily_df.to_csv('daily_summary/' + target_stock + '.csv')
        time.sleep(6)

def calc_summary(target_stocks, summary_file):
    with open(summary_file, 'w') as f:
        for target_stock in target_stocks:
            if not os.path.exists('daily_summary/' + target_stock + '.csv'):
                f.write(target_stock + ' 0 0 0 0 0 0 0\n')
                continue
            df = pd.read_csv('daily_summary/' + target_stock + '.csv')

            f.write(target_stock + ' ')

            today_close = float(df[-1:]['close'])
            f.write(str(today_close) + ' ')

    # # print(df)
            try:
                temp_df = df[-20:]
                df_c_20 = temp_df['close']
                ema20 = talib.EMA(df_c_20.values, timeperiod = 20)
                f.write(str(ema20[19]) + ' ')
            except Exception as e:
                f.write('0 ')

        #     print(ema20[19])
            try:
                temp_df = df[-60:]
                df_c_60 = temp_df['close']
                ema60 = talib.EMA(df_c_60.values, timeperiod = 60)
                f.write(str(ema60[59]) + ' ')
            except Exception as e:
                f.write('0 ')

            try:
                temp_df = df[-120:]
                df_c_120 = temp_df['close']
                ema120 = talib.EMA(df_c_120.values, timeperiod = 120)
                f.write(str(ema120[119]) + ' ')
            except:
                f.write('0 ')
            # today_close = temp_df[-1:]['close']
            # today_open = float(temp_df[-1:]['open'])
            yes_close = temp_df['close'].values[-2]

            range_1 = (today_close - yes_close) / yes_close * 100
            f.write(str(range_1) + ' ')

            try:
                temp_df = df[-6:]['close'].values
                # range_5 = temp_df[1] - temp_df[0] + temp_df[2] - temp_df[1] + temp_df[3] - temp_df[2] + temp_df[4] - temp_df[3]
                range_5 = (float(temp_df[5]) - float(temp_df[0])) / float(temp_df[0]) * 100
                f.write(str(range_5) + ' ')
            except:
                f.write('0 ')

            try:
                temp_df = df[-21:]['close'].values
                # range_5 = temp_df[1] - temp_df[0] + temp_df[2] - temp_df[1] + temp_df[3] - temp_df[2] + temp_df[4] - temp_df[3]
                range_20 = (float(temp_df[20]) - float(temp_df[0])) / float(temp_df[0]) * 100
                f.write(str(range_20) + '\n')
            except:
                f.write('0 ' + '\n')

if __name__ == "__main__":
    download_data(target_stocks_customize)
    calc_summary(target_stocks_customize, 'summary_custimize.txt')

    download_data(target_stocks_industry)
    calc_summary(target_stocks_industry, 'summary_industry.txt')
# #     print(float(today_close))
    
# # for row in df.iterrows():
