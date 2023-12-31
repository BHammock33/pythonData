a_list = [4444, 8897, 9896, 4835, 4324, 10, 6445, 661, 1246, 1000, 7429, 1376, 8121,
            647, 1280, 3993, 4881, 9500, 6701, 1199, 6251, 4432]
ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
print(content_ratings)            

def square(a_number):
    squared_number = a_number * a_number
    return squared_number
print(square(a_number=6))
print(square(a_number=4))
print(square(a_number=9))
print(square(10))

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
    return column
genres = extract(11)

def freq_table(column):
    freq_list = {}
    for value in column:
        if value in freq_list:
            freq_list[value] += 1
        else:
            freq_list[value] = 1
    return freq_list
genres_ft = freq_table(genres)
print(genres_ft)        

def freq_table_2(index):
    ratings_table2 = {}
    for row in apps_data[1:]:
        value = row[index]
        if value in ratings_table2:
            ratings_table2[value] += 1
        else:
            ratings_table2[value] =1
    return ratings_table2
ratings_ft = freq_table_2(7)
print(ratings_ft)


def freq_table_multi(data_set, index):
    frequency_table = {}
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table: 
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table
ratings_ft_mutli = freq_table_multi(apps_data, 7)

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(a_list_of_numbers):
    sum_list = find_sum(a_list_of_numbers)
    len_list =  find_length(a_list_of_numbers)
    mean_list = sum_list / len_list
    return mean_list
list_1 = [10,5,15]
print(mean(list_1))
def extract_better(data_set, index):
    column = []
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    return column

def mean_better(data_set, index):
    values_list = extract_better(data_set, index)
    return find_sum(values_list) / find_length(values_list)

avg_price = mean_better(apps_data, 4)
print(avg_price)    