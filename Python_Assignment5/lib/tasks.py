from collections import Counter
from textblob import TextBlob
import datetime
import matplotlib.pyplot as plt

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

# change name
def plot1(data):
    
    max_day = len(data)
    week_day_dic = {}
    week_day_procent = []
    week_day_text = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    for row in data:
        week_day_number = datetime.datetime(row['year'], row['month'], row['day']).weekday()

        if week_day_number == 0:
            week_day_dic.setdefault('monday', 0)
            week_day_dic['monday'] += 1
        elif week_day_number == 1:
            week_day_dic.setdefault('tuesday', 0)
            week_day_dic['tuesday'] += 1
        elif week_day_number == 2:
            week_day_dic.setdefault('wednesday', 0)
            week_day_dic['wednesday'] += 1
        elif week_day_number == 3:
            week_day_dic.setdefault('thursday', 0)
            week_day_dic['thursday'] += 1
        elif week_day_number == 4:
            week_day_dic.setdefault('friday', 0)
            week_day_dic['friday'] += 1
        elif week_day_number == 5:
            week_day_dic.setdefault('saturday', 0)
            week_day_dic['saturday'] += 1
        elif week_day_number == 6:
            week_day_dic.setdefault('sunday', 0)
            week_day_dic['sunday'] += 1

    week_day_procent.append(week_day_dic['monday'] / max_day * 100 / 100)
    week_day_procent.append(week_day_dic['tuesday'] / max_day * 100 / 100)
    week_day_procent.append(week_day_dic['wednesday'] / max_day * 100 / 100)
    week_day_procent.append(week_day_dic['thursday'] / max_day * 100 / 100)
    week_day_procent.append(week_day_dic['friday'] / max_day * 100 / 100)
    week_day_procent.append(week_day_dic['saturday'] / max_day * 100 / 100)
    week_day_procent.append(week_day_dic['sunday'] / max_day * 100 / 100)
    print(week_day_procent)      

    plt.title('Scatter-Plot weekday procentchance of spotting an ufo', fontsize=12)
    plt.xlabel("Procent", fontsize=10)
    plt.ylabel("Weekday", fontsize=10)
    plt.scatter(week_day_text, week_day_procent, s=100)
    plt.ylim((0,1))
    plt.show()

#change name
def plot2(data):
    polarity_list = []
    subjectivity_list = []
    for row in data[:1000]:
        sentiment_text = TextBlob(row['comments']).sentiment
        polarity_list.append(sentiment_text.polarity * -1)
        subjectivity_list.append(sentiment_text.subjectivity)

    plt.title('polaritet and sentiment', fontsize=12)
    plt.xlabel("comments", fontsize=10)
    plt.ylabel("0-1", fontsize=10)
    plt.plot(polarity_list, 'C1', linewidth=1)
    plt.plot(subjectivity_list, 'C2', linewidth=1)
    plt.ylim((0,1))
    plt.xlim((0, len(polarity_list)))
    plt.show()

def plot3(data):
    ufo_seeings_per_state = {}
    for row in data:
        if row['country'] == 'us':
            ufo_seeings_per_state.setdefault(row['state'], 0)
            ufo_seeings_per_state[row['state']] += 1


    