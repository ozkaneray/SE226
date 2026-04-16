from lab6.data_package import remove_duplicates, strip_whitespaces
from lab6.data_package import calculate_mean, find_maximum, find_minimum

raw = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

string_list = raw.split(",")
cleaned_strings = strip_whitespaces(string_list)

try:
    num_list = [float(x) for x in cleaned_strings]
except ValueError:
    print("Data Error: Please make sure you only enter numbers separated by commas.")
    exit()

unique_list = remove_duplicates(num_list)

print(f"\nCleaned and unique data: {unique_list}")
print("-" * 20)
print(f"Mean     : {calculate_mean(unique_list):.2f}")
print(f"Maximum  : {find_maximum(unique_list)}")
print(f"Minimum  : {find_minimum(unique_list)}")