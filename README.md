# Final CS50P Project
> Dedicated to Giang Hoang Nguyen 
## Requirements:
Write a program matches the following requirements:
- File name: main.py
- Language: Python 3 (Preferably at least 3.12)

When you run the file with `python main.py` it should display menu (X) in the console:
```
Choose an action from the menu:
1. Clean data
2. Visualize data
3. Exit
Your choice: <input user goes here>
```
If user inputs an option that not in (1, 2, 3), tell user to re-input.
If user inputs 1:
- Ask user if they want to also export cleaned data to another file in csv format. 
- If yes, ask them to input the file name, and export the file with that file name
- Else overwrite current file. 
- Data should be read from the file `diabetes_data.csv`

Definition of clean data: if a row contains a cell that contains a malformed data type, **REMOVE** that row from the file.
For example: row 2, column 2 (age) if data is "abc", then row 1 should be removed.

If user inputs 2:
- Ask user if they want to see a statistic base on (a) basic characteristics (age/gender/ethnicity/socioeconomic/education) or (b) habits (bmi/smoking/alcohol/physical activity/diet quality/sleep quality).
- If user input (a) export an image of bar chart (chart.png/jpg - overwrite if necessary): the percentage of diabetes base on basic characteristics
- If user input (b) export an image of bar chart (chart.png/jpg - overwrite if necessary): the percentage of diabetes base on habits
- Data should be read from the file provided by Huy Quang Vu.

If user inputs 3:
- Exit the program

When action (1) or (2) are finished, navigate user back to initial menu (X), only exit if they choose option (3).
If any error and exception occur during each action, the program should print "Failed to perform action" and navigate user back to menu (X).
## Implementation Requirements:
For the (1) and (2) option, you should:
- Write a class named: `DataExporter`. It **MUST** contain methods: `clean_data`, `export_file`, `export_image` (you can add as many as additional methods you want)
- Each method/function should **NOT** be longer than 15 lines, and **NOT** contain more than 8 if-else-try-except clauses . 

### Data file
Data file is in `CSV` format and is expected to *at least* have the following columns:
- Age
- Gender
- Ethnicity
- SocioeconomicStatus
- EducationLevel
- BMI
- Smoking
- AlcoholConsumption
- PhysicalActivity
- DietQuality
- SleepQuality

If any column is missing, it should be failed to read. 

## Notes:
- You can add any library you want (Ex visualization lib: `Matplotlib`, `Seaborn`, `Bokeh`, `Plotly`, etc.)
- Any supporting tool is welcome (StackOverFlow, ChatGPT, etc.)
- Dataset was retrieved from: https://www.kaggle.com/datasets/rabieelkharoua/diabetes-health-dataset-analysis