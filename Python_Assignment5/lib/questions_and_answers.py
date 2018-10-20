import csv_data_conversion, tasks


data = csv_data_conversion.get_data_set()

# Hvilket sted er der flest UFO observationer?

tasks.get_most_observationsights(data)

# Hvordan har antallet af observationer udviklet sig over tid?

tasks.get_difference_of_observations(data)

# Hvornår på året er der flest observationer?

tasks.count_months(data)

# Hvordan ser en ufo ud?

tasks.ufo_observations(data)

# Hvor lang tid kunne de se ufoen(gennemsnit)?

tasks.get_average(data)

# På hvilke dage er det sandsynligt at se ufoer(i procentvis fordeling)?

#tasks.plot1(data)

#tasks.plot2(data)
print('-------------------------')

tasks.plot3(data)
