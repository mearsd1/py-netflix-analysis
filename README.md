# Netflix Profile Watch Time Project (CodeKY)
## Description
    The Netflix profile watch time program reads a user's Netflix account data and calculates the total watch time of each profile. The program outputs a bar graph, as a png file, that visualizes each profile's total watch time.

## Setup
1. ### Install python
    Install python3 per your OS instructions.

2. ### Setup a virtual environment with venv
   Create the venv: `python -m venv venv` 
   
   Activate the venv: `source venv/bin/activate`

3. ### Install requirements
   Run the following command to install the project’s required libraries:
    
    `python -m pip install -r requirements.txt`

## Project Requirement Features
1. ### Category 1: Python Programming Basics:
    -Create and call at least three functions or methods.
    -Calculate and display data.

2. ### Category 2: Utilize External Data:
    -Read data from an external CSV file.

3. ### Category 3: Data Display:
   -Visualize data in a bar graph.
    
4. ### Category 4: Best Practices:
   -The program utilizes a venv and requirements.txt.

5. ### Stretch Features:
   -The program uses pandas to perform data analysis.
   -The program uses matplotlib to visualize data.
    
## Special Instructions
- Using your own Netflix Data:
    To access your Netflix account data you can issue a request using the following link: https://www.netflix.com/account/getmyinfo

    Request can take up to 30 days to be processed. Once you have received your Netflix data, you can access your viewing_activity.csv, which will be read by the program, inside the content_interaction directory.