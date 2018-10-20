from collections import Counter

def get_most_observationsights(data):
    cnt = Counter()
    for row in data:
        cnt[row['place']] += 1    
    name = cnt.most_common(1)[0][0]
    times = cnt.most_common(1)[0][1]
    print('The most ufo observations is in: ' + name + ' with: ' + str(times) + ' observations.')


def get_lowest_and_highest_year(data):
    number = 3000
    lowest_highest = {}
    for row in data:
        if number > row['year']:
            number = row['year']
    lowest_highest['lowest'] = number
    for row in data:
        if number < row['year']:
            number = row['year']
    lowest_highest['highest'] = number
    return lowest_highest

def get_difference_of_observations(data):
    lowest_and_highest_year = get_lowest_and_highest_year(data)
    lowest = 0
    highest = 0
    for row in data:
        if lowest_and_highest_year['lowest'] == row['year']:
            lowest += 1
        if lowest_and_highest_year['highest'] == row['year']:
            highest += 1
    print('The amount of observations from the lowest year of ' + str(lowest_and_highest_year['lowest']) + ' was: ' + str(lowest) + ' observations.')
    print('The amount of observations from the highest year of ' + str(lowest_and_highest_year['highest']) + ' was: ' + str(highest) + ' observations.')

def count_months(data):
    cnt = Counter()
    for row in data:
        cnt[row['month']] += 1
    month = cnt.most_common(1)[0][0]
    times = cnt.most_common(1)[0][1]
    print('most time of the year of observations is month: ' + str(month) + ' with: ' + str(times) + " observations")

def ufo_observations(data):
    cnt = Counter()
    for row in data:
        cnt[row['shape']] += 1
    print('Different type of shapes: ')
    print(cnt)

def get_average(data):
    duration = 0
    count_rows = 0
    for row in data:
        duration += row['duration']
        count_rows += 1
    average = duration / count_rows
    print("The average is: " + str(average) + ' seconds.')
    
