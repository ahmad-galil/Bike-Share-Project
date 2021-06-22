import numpy as np
import pandas as pd

# Assign keys to .csv files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


# Creates a function to take city, month, day chosen by user as inputs and return DataFrame of selected inputs
def load_data(city,month,day):
    city_data = pd.read_csv(CITY_DATA[city.lower()])                              #load .csv file to city_data
    df = pd.DataFrame(city_data)                                                  #Creates dataframe
    df['Day'] = pd.to_datetime(df['Start Time']).dt.day_name()                    #Creates a new column and extract Day
    df['Month'] = pd.to_datetime(df['Start Time']).dt.month_name()                #Creates a new column and extract Month
    if month != 'all':                                                            #Filters month if it is not all
        df = df[df['Month'] == month.title()]
    if day != 'all':                                                              #Filters day if it is not all
        df = df[df['Day'] == day.title()]
    return(df)


# Creates a function to ask user to specify city, month, day he/she wants to explore
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    ok = input('Reply with OK to continue\n')
    while ok.lower() != 'ok':
        ok = input('Please reply with OK to continue\n')
    print("The available states to be explored are: 'Washington', 'New York' and 'Chicago'.")
    state = input('Reply with the state you would like to explore.\n')
    while state.lower() != 'washington' and state.lower() != 'new york' and state.lower() != 'chicago':          #condition to ensure right input from user
        state = input('Please choose one of the 3 states and avoid typos\n')
    print("The available months to be explored are: 'January', 'February', 'March', 'April', 'May', 'June'.")
    month = input("Reply with the month you would like to explore or 'All' for half-year data.\n")
    while month.lower() != 'january' and month.lower() != 'february' and month.lower() != 'march' and month.lower() != 'april' and month.lower() != 'may' and month.lower() != 'june' and month.lower() != 'all':                   #condition to ensure right input from user
        month = input("Please choose one of the 6 months or 'All' and avoid typos\n")
    print("All week days are available to be explored: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' and 'Sunday'.")
    day = input("Reply with the day you would like to explore or 'All' for all days data.\n")
    while day.lower() != 'monday' and day.lower() != 'tuesday' and day.lower() != 'wednesday' and day.lower() != 'thursday' and day.lower() != 'friday' and day.lower() != 'saturday' and day.lower() != 'sunday' and day.lower() != 'all':                   #condition to ensure right input from user
        day = input("Please choose one of the weekdays or 'All' and avoid typos\n")
    return (state,month,day)


# Creates a function that takes DataFrame as input and print most common month, day and hour
def time_stats(df):
    common_month = df['Month'].mode()[0]                                          #Most common month
    common_day = df['Day'].mode()[0]                                              #Most common day
    hour = pd.to_datetime(df['Start Time']).dt.hour                               #Creates a new column and extract hour
    common_hour = hour.mode()[0]                                                  #Most common hour
    print('Most common month is: ' + str(common_month))
    print('Most common day is: ' + str(common_day))
    print('Most common hour is: ' + str(common_hour))


# Creates a function that takes DataFrame as input and print most common start station, end station and trip
def station_stats(df):
    common_start_station = df['Start Station'].mode()[0]                                   #Most common start station
    common_end_station = df['End Station'].mode()[0]                                       #Most common end station
    trip = 'from station: ' + df['Start Station'] + ' to station: ' + df['End Station']    #Adds start station and end station in one column
    common_trip = trip.mode()[0]                                                           #Most common trip
    print('Most common start station is: ' + str(common_start_station))
    print('Most common end station is: ' + str(common_end_station))
    print('Most common trip is: ' + common_trip)


# Creates a function that takes DataFrame as input and print average and total travel time
def trip_duration_stats(df):
    total_travel_time = df['Trip Duration'].sum()                                 #Sums up trip duration
    average_travel_time = df['Trip Duration'].mean()                              #Average of all trips duration
    print('Total travel time is: ' + str(total_travel_time))
    print('Average travel time is: ' + str(average_travel_time))


# Creates a function that takes DataFrame as input and print user type count, gender count, earliest year, recent year and most common year, if available
def user_stats(df):
    user_type_count = df['User Type'].value_counts().to_frame()                   #Counts all user types
    print(user_type_count)
    try:
        gender_count = df['Gender'].value_counts().to_frame()
        print(gender_count)
    except KeyError as key:                                                       #exception to avoid error if info is not available
        print('Gender data is not available')
    try:
        earliest_year = df['Birth Year'].min()                                    #Earliest year
        recent_year = df['Birth Year'].max()                                      #Most recent year
        common_year = df['Birth Year'].mode()[0]                                  #Most common year
        print('Earliest year is: ' + str(int(earliest_year)))
        print('Recent year is: ' + str(int(recent_year)))
        print('Most common year is: ' + str(int(common_year)))
    except KeyError as key:                                                       #exception to avoid error if info is not available
        print('Birth year data is not available')


# Main function
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print(df.describe())                                                      #a brief on data of city
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data = input('Would you like to view 5 rows of raw data?\nEnter yes or no.\n')
        i=0
        while raw_data.lower() == 'yes':                                           #while loop to view 5 rows of raw data unless user stops it
            print(df.iloc[i:i+5,:])
            i += 5
            raw_data = input('Would you like to view 5 more rows?\nEnter yes or no.\n')


        restart = input('Would you like to restart?\nEnter yes or no.\n')        #asks user if he/she wants to explore other cities
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
