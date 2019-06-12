import os
import pandas as pd
import math


def stderr(area_name,s1,s2,n):
    t_value={"Middle":2.021,
             "South":2.000,
             "North":1.990
            }
    tmp=(math.pow(s1,2)+math.pow(s2,2))/n
    error=t_value[area_name]*math.sqrt(tmp)
    return error
        

def standard_deviation(data,sample_mean,n):
    D=0.0
    for index in range(n):
        D+=math.pow(data[index]-sample_mean,2)
    s=math.sqrt(D/(n-1))
    return s
        

def processing(area_dir,area_name):
    station_file=os.listdir(area_dir)
    print(area_name)
    area_summer=[]
    area_winter=[]
    for station in station_file:
        if(station[0]=='.'):
            continue
        summer=0.0
        winter=0.0
        station_path=os.path.join(area_dir,station)
        df=pd.read_csv(station_path)
        PM25=df.loc[1,:]
        for index in range(6,12):
            summer+=PM25[index]
        for index in range(1,6):
            winter+=PM25[index]
        winter+=PM25[12]
        area_summer.append(summer/6)
        area_winter.append(winter/6)
    n1=len(area_summer)
    df=n1-1
    print("n1=",n1,",df=",df)
    summer_total=0.0
    winter_total=0.0
    for index in range(n1):
        summer_total+=area_summer[index]
        winter_total+=area_winter[index]
    mean1=summer_total/n1
    mean2=winter_total/n1
    s1=standard_deviation(area_summer,mean1,n1)
    s2=standard_deviation(area_winter,mean2,n1)
    print("sample mean1=",mean1,"sample mean2=",mean2)
    print("s1=",s1,"s2=",s2)
    error=stderr(area_name,s1,s2,n1)
    low=mean1-mean2-error
    up=mean1-mean2+error
    print("confidence interval=",low,"<mean1-mean2<",up)
    if(low*up>0):
        print("The two means have obvious difference")
    else:
        print("The two means have no difference")
    print('\n')


if __name__ == '__main__':

    main_directory="./month_avg"
    area_file=os.listdir(main_directory)

    for area in area_file:
        area_path=os.path.join(main_directory,area)
        yn=1
        if(area=='Other'or area=='East'):
            yn=0
        if(yn):
            processing(area_path,area)

