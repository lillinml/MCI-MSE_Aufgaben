from statistics import variance
import pandas as pd
import neurokit2 as nk
import json
import matplotlib as mpl 
import matplotlib.pyplot as plt

import logging
Log_format = "%(levelname)s:%(asctime)s:%(message)s"
logging.basicConfig(filename = "main_5_object_oriented_running_logging.logg",
                    filemode = "w",
                    format = Log_format,
                    level = logging.INFO)

class Subject():
    """
    Test-Subject with the following attributes:

    - birth_year: int
    - age: int
    - subject_max_hr: int
    - subject_id: int
    - test_power_w: int

    """
    def __init__(self, file_name):
        """
        Initialize the Subject-Object with the following attributes:	
        - birth_year: int
        - age: int
        - subject_max_hr: int
        - subject_id: int
        - test_power_w: int
    
        """
        __f = open(file_name)
        __subject_data = json.load(__f)
        self.birth_year = __subject_data["birth_year"]        
        self.age = 2022 - self.birth_year
        self.subject_max_hr = 220 - (2022 - __subject_data["birth_year"])
        self.subject_id = __subject_data["subject_id"]
        self.test_power_w = __subject_data["test_power_w"]

        logging.info('Data of Subject {}{}'.format(self.subject_id,'has been loaded'))

class PowerData():
    """
    Power data with the following attributes:
        
    - subject_id: int
    - powder_data_watts: array of int
    - duration: int
    """

    def __init__(self, file_name):
        """
        Initialize the PowerData-Object with the following attributes:
        - subject_id: int
        - powder_data_watts: array of int
        - duration: int
        """
        self.subject_id = file_name.split(".")[0][-1]
        self.power_data_watts = open(file_name).read().split("\n")
        self.power_data_watts.pop(-1)
        self.duration_s = len(self.power_data_watts)

class Test:
    """
    Perfomance test of a subject with the following attributes:
    - subject_id: int
    - ecg_data: pandas dataframe
    - manual_termination: bool
    - terminated: bool
    - maximum_hr: int
    - average_hr_test: int
    - duration_test_min: int
    - number_of_heartbeats: int


    """
    def __init__(self, file_name):
        """
        Initialize the Test-Object with the following attributes:
        - subject_id: int
        - ecg_data: pandas dataframe
        - manual_termination: bool
        """
        self.subject_id = file_name.split(".")[0][-1]
        self.ecg_data = pd.read_csv(file_name)
        self.manual_termination = False
    
    def create_hr_data(self):
        """
        Load a dataframe of ecg_data to add additional attributes to the test object

        """

        self.ecg_data["ECG"] = self.ecg_data.iloc[:, [1]]

        # Find peaks
        self.hr_peaks, self.info = nk.ecg_peaks(self.ecg_data["ECG"], sampling_rate=1000)

        self.number_of_heartbeats = self.hr_peaks["ECG_R_Peaks"].sum()

        self.duration_test_min = self.hr_peaks.size/1000/60

        self.average_hr_test = self.number_of_heartbeats / self.duration_test_min

        ## Calculate heart rate moving average

        self.hr_peaks['average_HR_10s'] = self.hr_peaks.rolling(window=10000).mean()*60*1000
        
        self.maximum_hr = self.hr_peaks['average_HR_10s'].max()

        hrv_time = nk.hrv_time(self.hr_peaks, sampling_rate=100000, show=True)
        self.varianz = hrv_time["HRV_MeanNN"].values[0]

        plt.legend(['moving average','histogram', 'boxplot'])
        plt.ylabel("distribution")
        plt.grid(True, linestyle='-.')
        plt.savefig('R-R Intervals Subject {}'.format(self.subject_id))

    def evaluate_termination(self):
        """
        Evaluate the automatic termination of the test
        """
        self.terminated = False
        if self.maximum_hr > self.subject.subject_max_hr:
            self.terminated = True
            return self.terminated

    def add_subject(self, Subject):
        """
        Add a subject to the test object
        """
        self.subject = Subject

    def add_power_data(self, PowerData):
        """
        Add a power data to the test object
        """
        self.power_data = PowerData
    
    def create_summary(self):
        """
        create a summary of the test and print it to the console
        """
        print("Summary for Subject " + str(self.subject.subject_id))
        print("Year of birth:  " + str(self.subject.birth_year))
        print("Test level power in W:  " + str(self.subject.test_power_w))
        print("Maximum HR was: " + str(self.maximum_hr))
        print("Was test terminated because exceeding HR: " + str(self.terminated))
        print("Was test terminated because for other reasons: " + str(self.manual_termination))
        print("Durchschnitt: " + str(self.average_hr_test))
        print("Varianz: " + str(self.varianz))
        
        print("________________")
        print(" \n")

    def ask_for_termination(self):
        """
        Ask the diagnostician if the test should be terminated
        """
        self.manual_termination = False
        self.manual_termination = input("Is this test invalid? (leave blank if valid): ")

        if self.manual_termination != False:
            self.termination = True
        
        if str(self.manual_termination) != (''):
            logging.info('Test of Subject {} has been marked as invalid because of {}'.format(self.subject_id, self.manual_termination))

    def create_plot(self):
        """
        Create a plot of the test
        """
        self.plot_data = pd.DataFrame()
        self.plot_data["Heart Rate"] = self.hr_peaks[self.ecg_data.index % 1000 == 0]["average_HR_10s"]  
        self.plot_data = self.plot_data.reset_index(drop=True)

        self.plot_data["Power (Watt)"] = pd.to_numeric(self.power_data.power_data_watts)
        self.plot_data.plot()
        plt.title("Performance Test")
        plt.xlabel("time/s")
        plt.ylabel("Watt & BPM")
        plt.grid(True, linestyle='-.')
        plt.savefig('Performance test suject {}'.format(self.subject_id))

    def save_data(self):
        """
        Store the test data in a JSON file
        """
        __data = {"User ID": self.subject_id, "Reason for test termation": self.manual_termination, "Average Heart Rate": self.average_hr_test, "Maximum Heart Rate": self.maximum_hr, "Test Length (s)": self.power_data.duration_s, "Test Power (W)": self.subject.test_power_w}

        __folder_current = os.path.dirname(__file__) 
        __folder_input_data = os.path.join(__folder_current, 'result_data')
        
        __file_name = 'result_data_subject' + str(self.subject_id) +'.json'
        __results_file = os.path.join(__folder_input_data, __file_name)

        with open(__results_file, 'w', encoding='utf-8') as f:
            json.dump(__data, f, ensure_ascii=False, indent=4)
    
    def save_data_as_tree(self):
        """
        Store the test data in a JSON file with tree structure
        """
        #Daten in Baumstruktur speichern
        tree=tree()
        tree.build_tree()
        tree.add_child()
        tree.get_level()
        tree.print_tree()

        __folder_current = os.path.dirname(__file__)
        __folder_input_data = os.path.join(__folder_current, 'result_data')
        __file_name= 'result_data_subject_asTree' + str(self.subject_id) +'.json'
        __results_file = os.path.join(__folder_input_data, __file_name)
        with open(__results_file, 'w', encoding='utf-8') as f:
            json.dump(__data, f, ensure_ascii=False, indent=4)

### Erstellen leerer Liste zur Verarbeitung
list_of_new_tests = []
list_of_subjects = []
list_of_power_data = []

### Füllen der Liste mit vorhandenen Daten

import os
from re import I
import pandas as pd

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data')
for file in os.listdir(folder_input_data):
    file_name = os.path.join(folder_input_data, file)

    if file.endswith(".csv"):
        list_of_new_tests.append(Test(file_name))

    if file.endswith(".json"):
        list_of_subjects.append(Subject(file_name))

    if file.endswith(".txt"):
        list_of_power_data.append(PowerData(file_name))


# %% Programmablauf

iterator = 0                                        # Zähler, der die gefundenen Dateien und damit Tests zählt

for test in list_of_new_tests:                      # Alle Tests werden nacheinander durchlaufen
    test.create_hr_data()                           # Erstelle Herzraten aus den EKG-Daten
    test.add_subject(list_of_subjects[iterator])    # Fügt einem Test die passenden Versuchspersonen hinzu
    test.add_power_data(list_of_power_data[iterator])
    test.evaluate_termination()
    test.create_plot()
    test.ask_for_termination()
    test.create_summary()
    test.save_data()
    test.save_data_as_Tree()
    """
    Fügen Sie hier den Programmablauf ein, indem Sie die Methoden und Klassen von oben nutzen
    """

    iterator = iterator + 1
    

# %%
