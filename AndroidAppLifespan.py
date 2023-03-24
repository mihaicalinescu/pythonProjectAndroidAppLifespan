stored_data = []

def parse_the_input_file():
    with open('logcat_applications.txt', 'rt') as myfile:
        # content = myfile.read()
        # print(content)
        for myline in myfile:
            if 'ActivityTaskManager: START u0' in myline:
                stored_data.append(myline)
            if 'Destroyed ActivityRecord' in myline:
                stored_data.append(myline)

def search_for_specific_data(self):
    pass

if __name__ == "__main__":
    parse_the_input_file()
