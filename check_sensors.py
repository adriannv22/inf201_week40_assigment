import pandas as pd
import json
import yaml

def check_sensor_files(config:str = 'config.yml', calibrations:str = 'calibrations.csv', sensors:str = 'sensors.xlsx'):
    '''The funktion'''

    with open(config, 'r') as file:
        config_file=yaml.safe_load(file)

    max_days_since_calibration = config_file.get('max_days_since_calibration')
    output_file=config_file.get('output_file')

    df_sensors = pd.read_excel(sensors)
    df_calibrations = pd.read_csv(calibrations)

    df_merge = pd.merge(df_sensors, df_calibrations, on = 'sensor_id', how = 'inner')

    


check_sensor_files()