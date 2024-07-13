import csv
import plotly.express as px
import pandas as pd
import os
import sys
import re


columns = [
"Age",
"Gender",
"Ethnicity",
"SocioeconomicStatus",
"EducationLevel",
"BMI",
"Smoking",
"AlcoholConsumption",
"PhysicalActivity",
"DietQuality",
"SleepQuality"
]

class DataExporter():
    def __init__(self, data):
        patients = []
        with open(data) as csvfile:
             reader = csv.DictReader(csvfile)
             for row in reader:
                 patients.append(row)
        self.data = patients

    def clean_data(self):
         for patient in self.data:
            for column in columns:
                try:
                    #print("?" , patient[column], column)
                    float(patient[column])
                except ValueError:
                    print(patient[column])
                    self.data.remove(patient)
                    #print("!" , self.data)
                    break
         return self.data


    def export_file(self, export_file):
        with open(export_file, 'w', newline = "") as csvfile:
            fieldnames = columns
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, extrasaction='ignore')
            writer.writeheader()
            for patient in self.data:
                writer.writerow(patient)
            return export_file

    def overwrite_file(self, original_file):
        with open(original_file, 'a', newline = "") as csvfile:
            fieldnames = columns
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, extrasaction='ignore')
            writer.writeheader()
            for patient in self.data:
                writer.writerow(patient)
            return original_file


    def age(self):
        age_list = []
        count_20_35 = 0
        count_35_60 = 0
        count_60_90 = 0
        for i in range(0, len(self.data)):
            age = int(self.data[i]["Age"])
            age_list.append(age)
        for i in age_list:
            if 20 <= i < 35:
                count_20_35 += 1
            elif 35 <= i <= 60:
                count_35_60 += 1
            else:
                count_60_90 += 1
        age_groups =["20-35", "35-60", "60-90"]
        age_count =[count_20_35, count_35_60, count_60_90]
        return age_groups, age_count


    def export_image_by_age(self, age_groups, age_count):
        data_frame = pd.DataFrame.from_dict({'age' : age_groups, 'count' : age_count})
        fig = px.bar(data_frame, x = "age", y = "count")
        fig.write_image("images/fig1.png")

    def bmi(self):
        bmi_list = []
        count_below_185 = 0
        count_185_249 = 0
        count_250_299 = 0
        count_above_300 = 0
        for i in range(0, len(self.data)):
            bmi = float(self.data[i]["Age"])
            bmi_list.append(bmi)
        for i in bmi_list:
            if i < 18.5:
                count_below_185 += 1
            elif 18.5 <= i <= 24.9:
                count_185_249 += 1
            elif 25 <= i <= 29.9:
                count_250_299 += 1
            else:
                count_above_300 += 1
        bmi_groups =["Underweight", "Healthy Weight", "Overweight", "Obesity"]
        bmi_count =[count_below_185, count_185_249, count_250_299, count_above_300]
        return bmi_groups, bmi_count

    def export_image_by_bmi(self, bmi_groups, bmi_count):
        data_frame = pd.DataFrame.from_dict({'Weight Status' : bmi_groups, 'Count of Diabetes' : bmi_count})
        fig = px.bar(data_frame, x = "Weight Status", y = "Count of Diabetes")
        fig.write_image("images/fig2.png")

def main():
    df = DataExporter('diabetes_data.csv')
    while True:
        ans = input("""
        Choose an action from the menu:
        1.Clean data
        2.Visualize data
        3.Exit
        Your choice goes here:
        """)
        if ans == "1":
            df.clean_data()
            export = input("\nExport to another csv file?yes/no ")
            if export == "yes":
                while True:
                    filename = input("\nName your csv file ")
                    if re.match(r"^\w+\.csv$", filename):
                        df.export_file(filename)
                        break
                    else:
                        print("Invalid file name")
            if export == "no":
                df.overwrite_file('diabetes_data.csv')
        elif ans == "2":
            df.clean_data()
            if not os.path.exists("images"):
                os.mkdir("images")
            while True:
                criteria = input("\nVisualize based on (a)age or (b)bmi? ")
                if criteria == "a":
                    age_groups, age_count = df.age()
                    df.export_image_by_age(age_groups, age_count)
                    break
                elif criteria == "b":
                    bmi_groups, bmi_count = df.bmi()
                    df.export_image_by_bmi(bmi_groups, bmi_count)
                    break
                else:
                    print("Invalid criteria")
        elif ans == "3":
            sys.exit("Exit program")
        else:
            continue

if __name__ == "__main__":
    main()







