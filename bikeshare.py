import time
import pandas as pd
import numpy as np

# Dictionary to store city name and raw data file relationship
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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

    # User prompt to enter data for city
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?\n")
        print()
        # if valid city option provide message to the user and then break from the loop
        if city.title() in ["Chicago", "New York", "Washington"]:
            print("Looks like you want to hear about " + city.title() + "! If this is not true, restart the program now!")
            print()
            break
        else:
            # output below message for incorrect entry

            # add changes 08/06 - provide input details to the user
            print("YOu have provided input as : ", city)
            # end changes 08/06 - provide input details to the user
            
            print("Not a valid selection. Please select any of the valid city option.")
            print()

    # User prompt to enter filter criteria
    while True:
        filter_choice = input("Would you like to filter the data by month, day, both, or not at all? "
                              "Type “none” for no time filter.\n")
        if filter_choice.lower() in ["month", "day", "both", "none"]:
            print("Filter criteria selected is :", filter_choice.title())
            break
        else:
            print("Enter a valid choice for data filter..\n")
    print()

    # if user has selected any of the filter option (month, day or both) then prompt user to enter filter criteria
    # Prompt user to select the month filter based on the above selection
    if filter_choice.lower() in ["month", "both"]:
        while True:
            month = input("Which month? Please select January, February, March, April, May, June, July, August, "
                          "September, October, November, December\n")
            if month.title() in ["January", "February","March", "April", "May", "June", "July", "August", "September",
                                 "October", "November", "December"]:
                break
            else:
                print("Enter a valid choice for month filter..\n")
    else:
        # Default month to All, if user doesn't select any month filter
        month = "All"
    print("Month filter criteria selected is :", month.title())
    print()

    # Prompt user to input day filter. This is executed based on the previous data selection by the user
    if filter_choice.lower() in ["day", "both"]:
        while True:
            day = input("Which day? Please select Monday, Tuesday, Wednesday, Thursday, Friday, "
                        "Saturday, or Sunday\n")
            if day.title() in ["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                break
            else:
                print("Enter a valid choice for day filter..\n")
    else:
        # Default day to All, if user doesn't select any day filter
        day = "All"
    print("Day filter criteria selected is :", day.title())
    print()

    print("Just a moment.. loading the data...")

    print('-'*40)
    # return the values in 'title' to ensure formatting is taken care of before next set of comparisons
    return city.title(), month.title(), day.title()


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

    # load data file into a dataframe based on the city selected by the user
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month, if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding integer representation
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week, if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    # returned dataframe after applying required filters
    return df


def time_stats(df):
    '''
    Displays statistics on the most frequent times of travel.
    This function takes dataframe as the input.
    :param df:
    :return: None
    '''

    print("Calculating statistics for most frequent times of travel...")
    print()
    start_time = time.time()

    # calculate most common/popular data using mode function, and then calculate the occurrence using value_counts

    # display the most common month
    popular_month = df['month'].mode()[0]
    count_popular_month = df['month'].value_counts()[popular_month]
    print("Most popular month for travelling is: " + str(popular_month) + ", and trip count in this month are: "
          + str(count_popular_month))

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    count_popular_day_of_week = df['day_of_week'].value_counts()[popular_day_of_week]
    print("Most popular day of week for travelling is: " + popular_day_of_week + ", and trip count on this day are: "
          + str(count_popular_day_of_week))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    count_popular_hour = df['hour'].value_counts()[popular_hour]
    print("Most popular hour for travelling is: " + str(popular_hour) + ", and trip count during this hour is: "
          + str(count_popular_hour))

    # provide response time details to the user
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    '''
    Displays statistics on the most popular stations and trip.
    This function takes dataframe as the input.
    :param df:
    :return: None
    '''
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # calculate most common/popular station using mode function, and then calculate the occurrence using value_counts

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    count_popular_start_station = df['Start Station'].value_counts()[popular_start_station]
    print("Most popular Start Station is: \"" + popular_start_station + "\", having count as: "
          + str(count_popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    count_popular_end_station = df['End Station'].value_counts()[popular_end_station]
    print("Most popular End Station is: \"" + popular_end_station + "\", having count as: "
          + str(count_popular_end_station))

    # display most frequent combination of start station and end station trip
    # using groupby function to determine the maximum occurrence of start & end station combination
    (popular_start_station, popular_end_station) = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("Most popular trips have Start Station as \"" + popular_start_station +"\" and End Station as \""
          + popular_end_station + "\"")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    '''
    Displays statistics on the total and average trip duration.
    This function takes dataframe as the input.
    :param df:
    :return: None
    '''

    print('\nCalculating Trip Duration statistics...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()     # using sum to calculate total trip durations
    print("Total travel time is: " + str(total_trip_duration))

    total_trip_count = df['Trip Duration'].count()
    print("Total number of trips are : " + str(total_trip_count))

    # display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print("Mean trip duration is: " + str(mean_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    '''
    Displays statistics on bikeshare users.
    This function takes dataframe as the input.
    :param: df
    :return: None
    '''

    print('\nCalculating next statistics.. User types...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("User type details are :\n", user_types)
    print()

    # Display counts of gender
    if {'Gender'}.issubset(df):    # verify if 'Gender' column exists in the dataframe
        gender_types = df['Gender'].value_counts().to_string()
        print("Gender type details are:\n", gender_types)
    else:
        print("Gender data is not available.")
    print()

    # Display earliest, most recent, and most common year of birth
    if {'Birth Year'}.issubset(df):     # verify if 'Birth Year' column exists in the dataframe
        earlier_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print("Earliest year of birth is: ", earlier_yob)
        print("Most recent year of birth is: ", most_recent_yob)
        print("Most common year of birth is: ", most_common_yob)
    else:
        print("Birth year data is not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    '''
    This is the main function that will call other functions to input user selections and provide bike 
    share statistics. It has interactive mode to display required data to the user.
    :param: None
    :return: None
    '''

    while True:
        # Call get_filters to get prompt user selection
        city, month, day = get_filters()

        # load_data function returns back the dataframe based on the user selections
        df = load_data(city, month, day)

        # if dataframe is null for the given filter criteria, output message and prompt user for new selection criteria
        if df.empty:
            print("No data exists for the filter criteria.. Unable to calculate statistics..")
        else:
            # this function take dataframe as input and display time statistics to the user
            time_stats(df)

            # this function take dataframe as input and display start & end station statistics to the user
            station_stats(df)

            # this function take dataframe as input and display duration statistics to the user
            trip_duration_stats(df)

            # this function take dataframe as input and display bike-users statistics to the user
            user_stats(df)

            # Display raw data to the user based on selection.. Display 5 rows at a time..

            # counter to keep track of the rows displayed to the user
            row_counter = 0

            # get # of rows in the dataframe to control the raw data print
            len_df = len(df)

            # variable step to control the # of rows to be displayed.. initialize to 5..
            step = 5

            while True:
                raw_data_flag = input("\nWould you like to view individual trip data? Please enter 'yes' or 'no'..\n")
                # if user provides 'yes', then display 5 rows and prompt again..

                # check if there are rows to be displayed from dataframe, else change step to the pending row count
                if (row_counter + step) > (len_df):
                    step = len_df - row_counter

                # using iloc function to display raw data based on the index numbers
                if raw_data_flag.lower() == 'yes' and step > 0:
                    print("\nDisplaying {} rows of data...\n".format(step))
                    print(df.iloc[row_counter : row_counter + step])
                    row_counter += step
                elif raw_data_flag.lower() == 'no':
                    break
                else:
                    print("Invalid input... Please enter a valid option...")
                    print()

                # step will be changed only when no more rows to be displayed
                if step != 5:
                    print("\nRaw data display completed.. No more rows pending.. ")
                    break


        # prompt to check if user wants to continue with new selection criteria and display corresponding statistics
        print()
        while True:
            restart = input('Would you like to restart? Enter yes or no.\n')
            print()

            if restart.lower() not in ["yes", "no"]:
                print("Please enter a valid option..")
            else:
                break

        # End the program if user doesn't select 'yes'
        if restart.lower() == 'no':
            print("Goodbye!")
            break

if __name__ == "__main__":
	main()
