import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n Please, which city do you want to check? \n chicago, new york city, washington... ").lower()
        if city.lower() in CITY_DATA:
            print("\n Your data is analyzing now....")
            break
        else:
            print("\n Please, try again to enter a valid city name")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n Please, choose form the list Which month would you prefer to be involved?\n january, february, march, april, may, june? or Type 'all' to get all the months... ").lower()
        if month not in MONTHS and month.lower() != 'all':
            print("\n Please, enter the vaild month to get the result") 
            
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Please, define which day?\n monday, tuesday, wednesday, thursday, friday, saturday, sunday... ").lower()
        if day not in DAYS and day.lower() != 'all':
            print("\n Please, enter the vaild days to continue the analysis\n")
        else:
            break


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month.lower() != 'all':
        month = MONTHS.index(month) + 1
        df=df[df['month'] == month]
        
    if day.lower() != 'all':
        df = df[df['day_of_week'] == day.title()]
           
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print('\n The most common month is : ', MONTHS[df['month'].mode()[0] - 1])
        
    # TO DO: display the most common day of week
    
    print(' The most common day of week is : ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
   
    print(' The most common start hour is : ', df['hour'].mode()[0], 'Hr')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n The most common start station is : ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print(' The most common end station is : ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['gathering'] = df['Start Station'] + ' until ' + df['End Station']
    print(' The frequent combination of start & end station trip are : ', df['gathering'].mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\n The total travel time is : ', df['Trip Duration'].sum(), 'seconds')

    # TO DO: display mean travel time
    print(' The mean travel time is : ', df['Trip Duration'].mean(), 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    

    # TO DO: Display counts of user types
    print('\n The total counts of user are : ',df['User Type'].count())
    print(df['User Type'].value_counts())
    
        
    # TO DO: Display counts of gender
    
    if 'Gender' not in df:
        print('\n There is no gender data for this city')
        
        
    else:
        print(' The counts of gender are : \n',df['Gender'].value_counts())
   

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\n The earlist year is : ', int(df['Birth Year'].min()))
        print(' The most recent year is : ', int(df['Birth Year'].max()))
        print(' The most commom year of birth is : ', int(df['Birth Year'].mode()[0]))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    answer = ['yes', 'no']
    x = 0
    while True:
        display_data = input("\n There is another option  which is displaying 5 rows of each trip data?\n Enter (yes/ no)... ").lower()
        if display_data in answer:
            if display_data.lower() == 'yes':
                rows = df.iloc[x: x+5]
                print(rows)
                x +=5  
            else:
                break
        else:
            print('\n Please enter the right answer')
            
    return display_data        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
