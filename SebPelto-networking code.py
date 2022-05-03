
#tehtävä 2
import json
from os import X_OK
my_list = {"type": "LoRa-sensor", "identifier": "ABC-123", "location": 15701}
unformatted = json.dumps(my_list)
print(unformatted)
formatted = json.dumps(my_list,
                       indent = 4,
                       separators = (", " , " = "),
                       sort_keys = True
                       )

print(formatted)




f = open(r"C:\Users\Sebastian\OneDrive\Työpöytä\written.json","w")
f.write(formatted)

f.close()


#tehtävä 3

with open(r"C:\Users\Sebastian\OneDrive\Työpöytä\weather-data.json") as weather_data_dict:
    read_content = json.load(weather_data_dict)
    weatherStations_data = read_content['weatherStations']

    
    for getting_data in weatherStations_data: 
        
        sensorValues_access = getting_data['sensorValues']
        

        for sensorValues_data in sensorValues_access:
            
            getting_sensorvalue_data = sensorValues_data['sensorValue']
                    

    def get_sensor_value_data():
        weatherStations_data = read_content['weatherStations']
        for getting_data in weatherStations_data:
            sensorValues_access = getting_data['sensorValues']
            for sensorValues_data in sensorValues_access:
                getting_sensorvalue_data = sensorValues_data['sensorValue']
                name_check = sensorValues_data['name']
                if name_check == 'PINTASIGNAALI_1' or name_check == 'PINTASIGNAALI_2':
                    new_data.append(getting_sensorvalue_data)

                
    new_data = []
    get_sensor_value_data()

    filtered_measurements = json.dumps(new_data, indent = 4, separators = (",", " :"), sort_keys = True,)
    x = open(r"C:\Users\Sebastian\OneDrive\Työpöytä\filtered_measurements.json'" ,'w')
    x.write(filtered_measurements)
    x.close()


