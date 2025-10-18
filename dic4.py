from collections import Counter

# Example dictionary where values are strings (or any hashable type)
my_dict = {
    'key1': 'apple',
    'key2': 'banana',
    'key3': 'apple',
    'key4': 'orange',
    'key5': 'banana',
    'key6': 'apple'
}

# Extract all values from the dictionary into a list
values_list = list(my_dict.values())

# Use Counter to get the frequency of each value
value_frequencies = Counter(values_list)

# Print the resulting frequency dictionary
print(value_frequencies)
