# Example dataset with a NaN value
data = [5.0, 7.0, float('nan'), 8.0, 10.0]

# Mean (BUGGY: NaN in data makes result NaN)
mean_value = sum(data) / len(data)

# Median (BUGGY: NaN in data breaks correct sorting)
sorted_data = sorted(data)
mid_index = len(sorted_data) // 2
if len(sorted_data) % 2 == 0:
    median_value = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
else:
    median_value = sorted_data[mid_index]

# Standard deviation (BUGGY: NaN breaks subtraction/squaring)
variance = sum((x - mean_value) ** 2 for x in data) / len(data)
std_dev_value = variance ** 0.5

print("BUGGY MEAN   :", mean_value)
print("BUGGY MEDIAN :", median_value)
print("BUGGY STDDEV :", std_dev_value)
