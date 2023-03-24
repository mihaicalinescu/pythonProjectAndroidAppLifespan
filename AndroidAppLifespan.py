import re
from pprint import pprint

stored_data = []
extracted_data = {}

def parse_the_input_file():
    with open('logcat_applications.txt', 'rt') as myfile:
        # content = myfile.read()
        # print(content)
        for myline in myfile:
            if 'ActivityTaskManager: START u0' in myline:
                stored_data.append(myline)
            if 'Destroyed ActivityRecord' in myline:
                stored_data.append(myline)

def extract_specific_data():
    for line in stored_data:
        time = re.search(r'\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', line)
        # print (time)
        package = re.search('cmp=([\w\./]+)', line)
        # print(package)
        start_date = time.group(0)
        # print (start_date)
        if time and package:
            app = 'application{}'.format(len(extracted_data) + 1)
            app_path = package.group(1)
            extracted_data[app] = {"app_path": app_path, "ts_app_started": start_date}
        if '/' in app_path:
            apps_value = app_path.split('/')[0]
            if apps_value and 'Destroyed ActivityRecord' in line:
                stop_date = time.group(0)
                extracted_data[app]['ts_app_closed'] = stop_date


    pprint(extracted_data)
if __name__ == "__main__":
    parse_the_input_file()
    extract_specific_data()
    # for data in stored_data:
    #     print (data)
