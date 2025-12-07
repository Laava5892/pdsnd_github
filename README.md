### Date Created
Dec 7th, 2025


### Project Title
US Bikeshare Data Analysis
A Python Project for the Udacity Programming for Data Science Nanodegree

### Project Purpose
This project explores US bikeshare data from three major cities Chicago, New York City, and Washington, allowing users to filter data by city, month, and day of the week. Through a command-line interface, users can investigate travel patterns, station popularity, trip durations, and user demographics, gaining insights from real-world data while applying data wrangling and analysis techniques.

### Technologies Used
Python 3 for scripting and control flow

Pandas for data manipulation and analysis

NumPy for numeric operations

time (Python standard library) for performance measurement

CSV files for raw data input

IPython for interactive command-line execution

## Installation Instructions
1. Ensure Python 3 is installed on your machine.
2. Install required libraries (if not already installed):
   ```bash
   pip install pandas numpy
   ```
3. The `time` module is part of Python standard library, so no separate installation is needed.
4. Place the following CSV files in the same directory as the script:
   - `chicago.csv`
   - `new_york_city.csv`
   - `washington.csv`

### Usage Instructions
Run the script using:
```bash
ipython bikeshare_FinalFile.py
```
- You will be prompted to select a **city**, **month**, and/or **day** to filter the data.
- The program will then display statistics on:
  - Most frequent travel times
  - Popular stations and trips
  - Trip durations
  - User demographics
- Optionally, you can view 5 rows of raw trip data at a time and restart the analysis.

### Learning Experience
This project provided hands-on experience with:
- Reading and filtering datasets using Pandas
- Extracting and transforming date and time data
- Using `mode()`, `mean()`, `sum()` and conditional indexing for analysis
- Writing modular, interactive Python scripts
- Implementing exception handling and input validation
- Building CLI-based tools that simulate real-world data investigation workflows

### Acknowledgements
- This project was developed as part of the **Udacity Programming for Data Science with Python Nanodegree**.
- Datasets provided by **Motivate** (a bike share system provider) under open data licenses.
- Special thanks to Udacity mentors and reviewers for their guidance and feedback.

### References
These resources were invaluable in learning the foundational concepts and practical techniques used in this project:

- **Python for Data Analysis** by Wes McKinney  
  A comprehensive guide to data wrangling with Pandas, NumPy, and IPython, written by the creator of Pandas.

- **Automate the Boring Stuff with Python** by Al Sweigart  
  Great for understanding input/output, control flow, and scripting basics that are essential for building interactive programs.

- **Real Python Tutorials**  
  [realpython.com](https://realpython.com) offers practical tutorials on everything from data manipulation to building CLI applications.

- **W3Schools Python Reference**  
  [w3schools.com/python](https://www.w3schools.com/python/) is an excellent quick-reference for syntax and standard library modules like `time`.

- **Stack Overflow**  
  Helpful for resolving bugs, clarifying syntax, and optimizing performance with real-world advice from the programming community.

- **Udacity Classroom and Knowledge Base**  
  Provided guided lessons, walkthroughs, and best practices for applying Python in data science workflows.
