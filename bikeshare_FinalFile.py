
"""
Bikeshare Data Exploration Program
Created for Udacity Programming for Data Science with Python Nanodegree
This script allows users to filter and analyze US bikeshare data.

"""

import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    
    """
    
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington)
    
    while True:
        city = input("\nWhich city would you like to see data for New York City, Washington or Chicago?\n") .lower()
        if city in CITY_DATA:
            break
        else:
            print("\nInvalid input. Please choose within a city of New York City, Washington or Chicago.\n")

    # user's choice filter type
    
    choice=input("\nChoose which filter of data would you like to add: Month, Day, Both or None.\n Type None for no time filter: ").lower()
    while choice not in(['month', 'day', 'both','none']):
        print('please enter a valid filter choice such as: Day, Month, Both or None.')
        choice = input('\nchoose which filter of data would you like to add: Month, Day, Both or None.\n Type None for no time filter:' ).lower()


    # get user input for month (all, january, february, ... , june) 
   
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    if choice == 'month' or choice == 'both':
        month = input("\nPlease enter a month name from January to June.\n").lower()
        while month not in months:
            print("\nPlease enter a valid month input between January to June.\n")
            month = input("\nPlease enter a month name from January to June.\n").lower()
    else:
        month='all'
        
     #  get user input for day of week (all, monday, tuesday, ... sunday)   
        
    days= ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    if choice == 'day' or choice == 'both':
        day = input("\nPlease enter a day name\n").lower()
        while day not in days:
            print("\nPlease enter a valid day input\n")
            day = input("\nPlease enter a day name\n").lower()
    else:
        day='all'


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)   #load city data file to a dataframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])  #convert from a start to data time

    df['month'] = df['Start Time'].dt.month     #create month column from exatracting its data from Start Time
    df['day_of_week'] = df['Start Time'].dt.day_name()  #create day column from exatracting its data from Start Time

    #filtering month input
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june'] 
        month = months.index(month) + 1  # use the index of the months list to get the corresponding int
        df = df[df['month'] == month]   # filter by month to create the new dataframe

    #filtering day input
    if day != 'all' :
        df = df[df['day_of_week'] == day.title()]    # filter by day of week to create the new dataframe

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = df['month'].mode()[0]
    print("The most common month is:",months[common_month-1],".")

    # display the most common day of week
    print("The most common day is: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour  #create hour column through extracting it from start time
    print("The most common hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    print("The most common start statioin is: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most common end statioin is: ", df['End Station'].mode()[0])


    #  display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    def convert_to_hour(x):
        """
        convert from second to hours.
        
        
        Args:
         x - number of second
        
        """

        result= x/(3600)
        return result

    
    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print("The total travel time is:",int(travel_time), " Seconds. Or ", int(convert_to_hour(travel_time))," Hours. Or",int(convert_to_hour(travel_time)//24)," Days.")

    
    #  display mean travel time
    travel_avg = df['Trip Duration'].mean()
    print("The average travel time is:",int(travel_avg), " Seconds. Or ",int(convert_to_hour(travel_avg)*60) ," Minutes. Or",int(convert_to_hour(travel_avg)) ," Hours.")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    Subscribers = len(df[df["User Type"] == "Subscriber"])
    Customers = len(df[df["User Type"] == "Customer"])
    print ('Count of subscribers:' , Subscribers, sep = " ")
    print ('Count of customers:', Customers, sep = " ")


    # Display counts of gender
    try:    
        Males = len(df[df["Gender"] == "Male"])
        Females = len(df[df["Gender"] == "Female"])
    except:    
        print('There is no Gender data available for this city')
    else:
        print('Count of Males :', Males, sep = " ")
        print('Count of Females :', Females, sep = " ")


    # Display earliest, most recent, and most common year of birth
    try:    
        earliest = df['Birth Year'].min() 
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()
    except:
        print('There is no Birth Year data available for this city')
    else:
        print ('The most earliest year of birth is:', int(earliest), sep = " ")
        print ('The most recent year of birth is:', int(most_recent), sep = " ")
        print ('The most common year of birth is:', int(most_common), sep = " ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def display_data(df):
    """
    display rows of data depending on user answer "load 5 rows"

    Args:
         df - filitered city dataframe that returned from load_data function

    """
    five_row_display = input("\nWould you like to view 5 rows of individual trip data? Yes or No:\n").lower()
    if  five_row_display == 'yes':
        r = 0
        while True:
            print(df.iloc[r: r+5])
            r += 5
            more_rows = input("\nDo you wish to continue? Yes or No:\n").lower()
            if more_rows != 'yes':
                break

def main():
    while True:
        city,month,day= get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)



        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()