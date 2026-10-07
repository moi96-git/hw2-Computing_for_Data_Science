# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(x):
    return x * 3


# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(x, y):
    return x - y    

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3), ('hi', 5)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly

def dictionary_maker(tuple_list: list[tuple]):
    output = {}
    for a, b in tuple_list:
        output[a] = b
    return output

if __name__ == "__main__":
    test = [('foo', 1), ('bar', 3), ('hi', 5)]
    print(dictionary_maker(test))


    

############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#

cv = [{'user': 'john', 'jobs': ['analyst', 'engineer']}, {'user': 'jane', 'jobs': ['finance', 'software']}]

#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cv_list: list[dict], job_title: str):
    users = []
    for cv in cv_list:
        if job_title in cv['jobs']:
            users.append(cv['user'])
    return users


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cv_list: list[dict]):
    job_count_dict = {}
    for cv in cv_list:
        for job in cv['jobs']:
            job_count_dict[job] = job_count_dict.get(job, 0) + 1
    return job_count_dict

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(list_cv: list[dict]) -> tuple[str, int]:
    job_count_dict = job_counts(list_cv)
    most_popular = max(job_count_dict.items(), key=lambda x: x[1])
    return most_popular



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
def total_registered_cases(data: dict, country: str) -> int:
    if country not in data:
        return 0
    weekly_cases = data[country]
    total = 0
    for cases in weekly_cases:
        total = total + cases

    return total

cases_per_country = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}

print(total_registered_cases(cases_per_country, 'Spain'))    
print(total_registered_cases(cases_per_country, 'Germany'))  

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#
def total_registered_cases_per_country(data: dict) -> dict:
    total_cases_dict = {}
    for country, weekly_cases in data.items():
        total_cases_dict[country] = sum(weekly_cases)
    return total_cases_dict

cases_per_country = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}

print(total_registered_cases_per_country(cases_per_country))

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data: dict) -> str:
    total_cases_dict = total_registered_cases_per_country(data)
    country_with_most = max(total_cases_dict.items(), key=lambda x: x[1])
    return country_with_most[0]

###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the average of the ratio death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.


