import re
from pprint import pprint
import time
from datetime import datetime
import yaml

stored_data = []
extracted_data = {}
start_android_app = "ActivityTaskManager: START u0"
stop_android_app = "Layer: Destroyed ActivityRecord"

def parse_the_input_file():
    with open('logcat_applications.txt', 'rt') as myfile:
        # content = myfile.read()
        # print(content)
        for myline in myfile:
            if start_android_app in myline:
                stored_data.append(myline)
            if stop_android_app in myline:
                stored_data.append(myline)


def extract_specific_data():
    for line in stored_data:
        time = re.search(r'\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', line)
        # print (time)
        package = re.search('cmp=([\w\./]+)', line)
        # print(package)
        start_date = time.group(0)
        # print (start_date)

        if package and time:
            app_path = package.group(1)
            app = 'application_{}'.format(len(extracted_data) + 1)
            extracted_data[app] = {"app_path": app_path, 'ts_app_started': start_date, 'ts_app_closed': None, 'lifespan': None}

        else:
            if stop_android_app in line:
                pack = re.search(r"com.([\w.]+)", line)
                stop_date = time.group(0)
                path = pack.group(0)
                for applications in extracted_data.items():
                    if path in applications[1]['app_path']:
                        applications[1]['ts_app_closed'] = stop_date
                        time_stop = datetime.strptime(stop_date, '%m-%d %H:%M:%S.%f')
                        time_start = datetime.strptime(applications[1]['ts_app_started'], '%m-%d %H:%M:%S.%f')
                        lifespan = time_stop - time_start
                        applications[1]['lifespan'] = str(lifespan.total_seconds()) + "s"



    pprint(extracted_data)
    # for my_dict in extracted_data:
    #     print(my_dict)


if __name__ == "__main__":
    parse_the_input_file()
    extract_specific_data()
    file = open("data.yaml", "w")
    yaml.dump(extracted_data, file)
    file.close()
    # for data in stored_data:
    #     print (data)