import pandas as pd
import json
import yaml

def check_sensor_files(config:str = 'config.yml', calibrations:str = 'calibrations.csv', sensors:str = 'sensors.xlsx'):
    '''The funktion takes strings ofthe file names and outputs a json file.
    The functions first reaads the files and prosseses the information.
    It merges the sensor data and filters out the sensors that do not need calibrations.
    Then it writes a json file of the sensor that are overdue'''

    # Reads the config.yaml file 
    with open(config, 'r') as file:
        config_file=yaml.safe_load(file)

    # Set a variabel for the max ays sinse calibration useing the information for the yaml file
    max_days_since_calibration = config_file.get('max_days_since_calibration')
    # Set a variabel with the output file name form the config.yaml
    output_file = config_file.get('output_file')

    # Reads the sensors and calibrations files and separate make data frames from them. 
    df_sensors = pd.read_excel(sensors)
    df_calibrations = pd.read_csv(calibrations)

    # Merges the to data frames baist on the sensor_id
    df_merge = pd.merge(df_sensors, df_calibrations, on = 'sensor_id', how = 'inner')

    #Filters the merged dataframe for only the days since calibrations that are over the limite of max days since calibration
    df_overdue = df_merge[df_merge['days_since_calibration'] > max_days_since_calibration]

    #Wright the json file with the output file name and the overdue dataframe converted to a dictionery.
    with open(output_file, 'w') as file:
        json.dump(df_overdue.to_dict(), file, indent=2)

#The function is getting called.
check_sensor_files()