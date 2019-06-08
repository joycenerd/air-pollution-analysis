if __name__ == '__main__':
    import time
    start_time = time.time()
    main_directory = "./AirPolution_Taiwan"
    year_file = os.listdir(main_directory)  # list directory name in directory AirPolution_Taiwan

    for year in year_file:
        coun_path = os.path.join(main_directory, year)
        coun_file = os.listdir(coun_path)

        for country in coun_file:
            station_path = os.path.join(coun_path, country)
            station_file = os.listdir(station_path)

            i=0
            for station in station_file:
                if station.endswith(".xls"):
                    i+=1
                    dst=country+str(i)+".xls"
                    src=os.path.join(station_path,station)
                    dst=os.path.join(station_path,dst)
                    os.rename(src,dst)
                    process_path = os.path.join(station_path, station)
                    print("Processing: ", process_path)
                    processing(process_path, station[:-4], int(year), country)
    print("--- %s seconds ---" % (time.time() - start_time))