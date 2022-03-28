# Netflix Profile Watch Time Project (CodeKY)
## Project Description

The Netflix profile watch time program reads a user's Netflix account data and calculates the total watch time of each profile. The program outputs a bar graph, that visualizes each profile's total watch time. For more details on how the program works, please read the comments in the `profile_watch_time.py` file.

## Description of Data

The data used in this project consists of my family Netflix's viewing activity. I accessed the data by issuing a personal data request to Netflix. The program also uses the current date to calculate how many days have passed since the Netflix's data was received.
To view the raw data, please reference the `viewing-activity-data.csv`.

## Setup
1. ### Install python
    Install python3 per your OS instructions.

2. ### Setup a virtual environment with venv
   Create the venv: `python -m venv venv` 
   
   Activate the venv per your terminal instructions.

3. ### Install requirements
    The following packages are required to run the program:
        -pandas
        -matplotlib
        -datetime

   Run the following command to install the project’s required libraries:
    
    `python -m pip install -r requirements.txt`

4. ### Running the program
    Launch your terminal and enter the path to the `py-netflix-analysis` directory.
    From the command line, run `python profile_watch_time.py`

## Project Requirement Features
1. ### Category 1: Python Programming Basics
    -Calculate and display data based on an external factor.
        -Line 28 retrieves today's date and calculates how many days have passed since the Netflix data was received. The amount of days passed is displayed in the bar graph.

2. ### Category 2: Utilize External Data
    -Read data from an external CSV file.
        -Line 7 imports data from a CSV file and creates a data frame.

3. ### Category 3: Data Display
   -Visualize data in a bar graph.
        -Lines 34-54 create a bar graph that visualizes the Netflix Profiles Total Watch Time.
    
4. ### Category 4: Best Practices
   -The program utilizes a venv and requirements.txt.

5. ### Stretch Features:
   -The program uses pandas to perform data analysis.
        -Line 1 imports pandas.
   -The program uses matplotlib to visualize data.
        -Line 2 imports matplotlib.
    
## Special Instructions
Using your own Netflix Data:

To access your Netflix account data you can issue a request using the following link: https://www.netflix.com/account/getmyinfo

Request can take up to 30 days to be processed. Once you have received your Netflix data, you can access your viewing_activity.csv, which will be read by the program, inside the content_interaction directory.

To use your own Netflix data, update line 7 of the profile_watch_time.py file to the title of your CSV file.

`df = pd.read_csv('name_of_your_file.csv')`