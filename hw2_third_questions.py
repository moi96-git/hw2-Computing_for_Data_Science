# Third group of questions: hw2_third_questions.py’

##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def total_registered_cases(covid_data, country):
    if country in covid_data:
        return sum(covid_data[country])
    else:
        return "No data available for the specified country."

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(covid_data):
    covid_data_grouped = {}
    for i in covid_data:
        covid_data_grouped[i] = sum(covid_data[i])
    return covid_data_grouped

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(covid_data):
    covid_data_grouped = {}
    for i in covid_data:
        covid_data_grouped[i] = sum(covid_data[i])
    return max(covid_data_grouped, key=covid_data_grouped.get)


