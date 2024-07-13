import pytest
from project import DataExporter
import csv
import unittest


class TestDataExporter(unittest.TestCase):
    def setUp(self):
        test_file = 'test.csv'
        t = [{'PatientID': '6000', 'Age': "n", 'Gender': '0', 'Ethnicity': '1', 'SocioeconomicStatus': '2', 'EducationLevel': '1', 'BMI': '32.98528363147953', 'Smoking': '1', 'AlcoholConsumption': '4.499364662559289', 'PhysicalActivity': '2.443385277880059', 'DietQuality': '4.898831055237948', 'SleepQuality': '4.049885278422252'},
     {'PatientID': '6001', 'Age': '51', 'Gender': '1', 'Ethnicity': '0', 'SocioeconomicStatus': '1', 'EducationLevel': '2', 'BMI': '39.916764125880974', 'Smoking': '0', 'AlcoholConsumption': '1.578919022031171', 'PhysicalActivity': '8.301264419669659', 'DietQuality': '8.941093370790366', 'SleepQuality': '7.508150416102007'}]
        self.df = DataExporter(test_file)
        self.df.data = t

    def test_clean_data(self):
        self.df.clean_data()
        assert self.df.clean_data() == [{'PatientID': '6001', 'Age': '51', 'Gender': '1', 'Ethnicity': '0', 'SocioeconomicStatus': '1', 'EducationLevel': '2', 'BMI': '39.916764125880974', 'Smoking': '0', 'AlcoholConsumption': '1.578919022031171', 'PhysicalActivity': '8.301264419669659', 'DietQuality': '8.941093370790366', 'SleepQuality': '7.508150416102007'}]

    def test_age(self):
        self.df.clean_data()
        assert self.df.age() == (["20-35", "35-60", "60-90"], [0, 1, 0])

    def test_bmi(self):
        self.df.clean_data()
        assert self.df.bmi() == (["Underweight", "Healthy Weight", "Overweight", "Obesity"], [0, 0, 0, 1])


