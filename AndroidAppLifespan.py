class ParseRobot:
    def __init__(self, content):
        self.content = content

    def parse_the_input_file(self, content):
        with open('logcat_applications.txt', 'rt') as myfile:
            content = myfile.read()
        print(content)

    def search_for_specific_data(self):
        pass


if __name__ == "__main__":
    test = ParseRobot()
    test.parse_the_input_file()
