# CO % 2 ; NO2 % 5 ; O3 % 7 ; PM10 % 8 ; PM2.5 % 9 ; SO2 % 12
#   8hr     1hr        8hr       24hr      24hr         1hr
import os
import math
import xlrd
#import calmap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

def file_processing(df) :
    
    df = pd.DataFrame(df)
    h_00 = pd.to_numeric(df['00'], errors = 'coerce').fillna(0, downcast='infer')
    h_01 = pd.to_numeric(df['01'], errors = 'coerce').fillna(0, downcast='infer')
    h_02 = pd.to_numeric(df['02'], errors = 'coerce').fillna(0, downcast='infer')
    h_03 = pd.to_numeric(df['03'], errors = 'coerce').fillna(0, downcast='infer')
    h_04 = pd.to_numeric(df['04'], errors = 'coerce').fillna(0, downcast='infer')
    h_05 = pd.to_numeric(df['05'], errors = 'coerce').fillna(0, downcast='infer')
    h_06 = pd.to_numeric(df['06'], errors = 'coerce').fillna(0, downcast='infer')
    h_07 = pd.to_numeric(df['07'], errors = 'coerce').fillna(0, downcast='infer')
    h_08 = pd.to_numeric(df['08'], errors = 'coerce').fillna(0, downcast='infer')
    h_09 = pd.to_numeric(df['09'], errors = 'coerce').fillna(0, downcast='infer')
    h_10 = pd.to_numeric(df[10], errors = 'coerce').fillna(0, downcast='infer')
    h_11 = pd.to_numeric(df[11], errors = 'coerce').fillna(0, downcast='infer')
    h_12 = pd.to_numeric(df[12], errors = 'coerce').fillna(0, downcast='infer')
    h_13 = pd.to_numeric(df[13], errors = 'coerce').fillna(0, downcast='infer')
    h_14 = pd.to_numeric(df[14], errors = 'coerce').fillna(0, downcast='infer')
    h_15 = pd.to_numeric(df[15], errors = 'coerce').fillna(0, downcast='infer')
    h_16 = pd.to_numeric(df[16], errors = 'coerce').fillna(0, downcast='infer')
    h_17 = pd.to_numeric(df[17], errors = 'coerce').fillna(0, downcast='infer')
    h_18 = pd.to_numeric(df[18], errors = 'coerce').fillna(0, downcast='infer')
    h_19 = pd.to_numeric(df[19], errors = 'coerce').fillna(0, downcast='infer')
    h_20 = pd.to_numeric(df[20], errors = 'coerce').fillna(0, downcast='infer')
    h_21 = pd.to_numeric(df[21], errors = 'coerce').fillna(0, downcast='infer')
    h_22 = pd.to_numeric(df[22], errors = 'coerce').fillna(0, downcast='infer')
    h_23 = pd.to_numeric(df[23], errors = 'coerce').fillna(0, downcast='infer')

    data = pd.concat(
        [h_00, h_01, h_02, h_03, h_04, h_05, h_06, h_07, h_08, h_09, h_10, h_11,
        h_12, h_13, h_14, h_15, h_16, h_17, h_18, h_19, h_20, h_21, h_21, h_22, h_23], axis = 1)
    
    return data

# convert to heatmap_dataframe -> not finish yet.
def heatmap_data(data, years) :
    
    months = ['Jenuary', 'Febuary', 'March', 'April', 'May', 'June',
              'July', 'Augest', 'September', 'October', 'November', 'December']
    days = range(1, 32)
    
    # judge whether this years is lear or not.
    if years != 2016:
        # month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    else:
        # month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 363]
        
    jan = data[0 : month[0]]
    feb = data[month[0] : month[1]] 
    if years == 2016 :
        for i in range(3) :
            feb.append(0)
    else :
        for i in range(2) :
            feb.append(0)        
    mar = data[month[1] : month[2]]
    apr = data[month[2] : month[3]]
    apr.append(0)
    may = data[month[3] : month[4]]
    jun = data[month[4] : month[5]]
    jun.append(0)
    jul = data[month[5] : month[6]]
    aug = data[month[6] : month[7]]
    sep = data[month[7] : month[8]]
    sep.append(0)
    octo = data[month[8] : month[9]]
    nov = data[month[9] : month[10]]
    nov.append(0)
    dec = data[month[10] : month[11]]
    
    values = jan + feb + mar + apr + may + jun + jul + aug + sep + octo + nov + dec
          
    calmap.yearplot(values, year = years)
    pt.head()
        
# note that there's an unkwoun error about hour[key][21]. Current solution is ingore it.

hour_cols = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11,
            12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


def list_to_float(data):

    if isinstance(data, list):
        del data[0]
        data = data[0]
        #print("After Delete ", data)

    return data


def count_for_month(hour_avg, month) :     
    
    m = []

    for i in range(0,12):
        m.append(month[i+1] - month[i])
    
    month_avg = []

    # [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    #print(month)
    # [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #print(m)

    for i in range(0,12):
        for j in range(month[i], month[i+1]):
            #print(len(hour_avg))
            if hour_avg[j] == 0:
                m[i] = m[i] - 1

    for i in range(0,12):
        month_avg.append(sum(hour_avg[month[i] : month[i+1]]) / m[i])
    
    return month_avg


# count CO2, O3
def count_for_8_hours(index, days, hour, year, iteration, df):

    month = [0]
    hour_avg = []

    for i in range(index, days, iteration):
    
        key_loop = 0
        cnt1 = 8
        cnt2 = 8
        cnt3 = 7
        tmp_avg = [0, 0, 0]

        
        if df["日期"][i] == "2016/02/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/03/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/04/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/05/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/06/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/07/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/08/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/09/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/10/01":
            month.append(len(hour_avg))

        elif df["日期"][i] == "2016/11/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/12/01":
            month.append(len(hour_avg))
        
    
        # calculate the mean without zero value.
        for key in hour_cols : 
            
            pd_to_list = hour[key].iloc[i].tolist()
            final_data = list_to_float(pd_to_list)

            if key_loop < 8:
                tmp_avg[0] = tmp_avg[0] + final_data
            elif key_loop >= 8 and key_loop < 16 :
                tmp_avg[1] = tmp_avg[1] + final_data
            else :
                tmp_avg[2] = tmp_avg[2] + final_data            

            if final_data == 0:
                if key_loop < 8:
                    cnt1 = cnt1 - 1
                elif key_loop >= 8 and key_loop < 16:
                    cnt2 = cnt2 - 1
                else:
                    cnt3 = cnt3 - 1
        
            key_loop = key_loop + 1

        if cnt1 == 0:
            tmp_avg[0] = 0
        else:
            tmp_avg[0] = tmp_avg[0] / cnt1

        if cnt2 == 0:
            tmp_avg[1] = 0
        else:
            tmp_avg[1] = tmp_avg[1] / cnt2

        if cnt3 == 0:
            tmp_avg[2] = 0
        else:
            tmp_avg[2] = tmp_avg[2] / cnt3
        
        for j in range(0,3) :
            if math.isnan(tmp_avg[j]):
                tmp_avg[j] = 0

        hour_avg.append(max(tmp_avg))
    
    month.append(len(hour_avg))
    #print(month)

    month_avg = count_for_month(hour_avg, month)
              
    return month_avg


# count for pm2.5, pm10
def count_for_24_hours(index, days, hour, year, iteration, df) :
    
    month = [0]
    hour_max = []

    for i in range(index, days, iteration):
        maxmun = []

        if df["日期"][i] == "2016/02/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/03/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/04/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/05/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/06/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/07/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/08/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/09/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/10/01":
            month.append(len(hour_max))

        elif df["日期"][i] == "2016/11/01":
            month.append(len(hour_max))
        
        elif df["日期"][i] == "2016/12/01":
            month.append(len(hour_max))


        for key in hour_cols :
            pd_to_list = hour[key].iloc[i].tolist()
            final_data = list_to_float(pd_to_list)
            maxmun.append(final_data)
            
        hour_max.append(max(maxmun))

    month.append(len(hour_max))
    #print(month)

    month_avg = count_for_month(hour_max, month)
              
    return month_avg


# count for NO2, SO2
def count_for_1_hour(index, days, hour, year, iteration, df):
    
    month = [0]
    hour_avg = []

    for i in range(index, days, iteration):
        value = 0
        cnt = 24

        if df["日期"][i] == "2016/02/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/03/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/04/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/05/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/06/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/07/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/08/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/09/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/10/01":
            month.append(len(hour_avg))

        elif df["日期"][i] == "2016/11/01":
            month.append(len(hour_avg))
        
        elif df["日期"][i] == "2016/12/01":
            month.append(len(hour_avg))


        for key in hour_cols:
            pd_to_list = hour[key].iloc[i].tolist()
            final_data = list_to_float(pd_to_list)
            value = value + final_data

            if final_data == 0:
                cnt = cnt - 1

        if cnt == 0:
            hour_avg.append(0)

        else:
            hour_avg.append(value / cnt)
        
    month.append(len(hour_avg))
    #print(month)

    month_avg = count_for_month(hour_avg, month)
              
    return month_avg

'''
def plot(info, polution, country, year) :   
    month = range(1, 13)
    plt.figure()
    plt.plot(month, info)
    plt.xlabel('months')
    plt.ylabel('value')
    plt.title(polution + ' Polution in ' + country)
    plt.savefig("AirPolution_Taiwan/" + repr(year) + "/" + country + "/" + polution + "_" + country + ".png")
'''

def processing(excel, station, year, country):
    df = pd.read_excel(excel)
    days = df.shape[0] + 1
    data = file_processing(df)
    cnt = 0
    
    for i in range(1, 30):
        if df['測項'][i] == "CO":        
            cnt = cnt + 1
            
            if cnt == 1:
                print("CO: ", i)
                CO = i

            elif cnt == 2:
                iteration = i - CO
                print('iteration: ', iteration)
                break

#        elif df['測項'][i] == "O3":
#            print(i)
#            O3 = i
        
        elif df['測項'][i] == "PM2.5":
            print("PM2.5:", i)
            PM25 = i
        
        elif df['測項'][i] == "PM10":
            print("PM10: ", i)
            PM10 = i
        
        '''
        elif df['測項'][i] == "NO2":
            print(i)
            NO2 = i

        elif df['測項'][i] == "SO2":
            print(i)
            SO2 = i
        '''

    print("day: ", days)
    co_info=count_for_8_hours(CO, days, data, year, iteration, df)
    print("Done Analyzing CO's Information")
    #plot(co_info, 'CO', station, year)

    #o3_info = count_for_8_hours(O3, days, data)
    #print("Done Analyzing O3's Information")
    #plot(o3_info, 'O3', station, year)

    pm25_info = count_for_24_hours(PM25, days, data, year, iteration, df)
    print("Done Analyzing PM2.5's Information")
    #plot(pm25_info, 'PM2.5', station, year)

    pm10_info = count_for_24_hours(PM10, days, data, year, iteration, df)
    print("Done Analyzing PM10's Information")
    #plot(pm10_info, 'PM10', station, year)

    #no2_info = count_for_1_hour(5, days, data)
    #print("Done Analyzing NO2's Information")
    #plot(no2_info, 'NO2', station, year)
    
    #so2_info = count_for_1_hour(12, days, data)
    #print("Done Analyzing SO2's Information")
    #plot(so2_info, 'SO2', station, year)
    
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    classes = ["CO", "PM2.5", "PM10"]
    #classes = ["CO", "O3", "PM2.5", "PM10", "NO2", "SO2"]
    print(station, '\n')
    info=np.vstack((co_info,pm25_info,pm10_info))
    #import pdb; pdb.set_trace()
    output_csv = pd.DataFrame(columns = month, index = classes, data = info)
    output_csv.to_csv("Air/" + repr(year) + "/" + country + "/" + repr(year) + "_" + station + ".csv", encoding = 'gbk')


if __name__ == '__main__':
    import time
    start_time = time.time()
    main_directory = "./Air"
    #main_directory = "./tmp"
    year_file = os.listdir(main_directory)

    for year in year_file:
        coun_path = os.path.join(main_directory, year)
        coun_file = os.listdir(coun_path)

        for country in coun_file:
            station_path = os.path.join(coun_path, country)
            station_file = os.listdir(station_path)
            
            for station in station_file:
                if station.endswith(".xls"):
                    process_path = os.path.join(station_path, station)
                    print("Processing: ", process_path)
                    processing(process_path, station[:-4], int(year), country)
    print("--- %s seconds ---" % (time.time() - start_time))