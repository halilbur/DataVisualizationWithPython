import csv
import math

def calculate_sample_size(sigma, margin_error, confidence_level):
    # Convert confidence level to a Z-score
    z = 0.0
    if confidence_level == 90:
        z = 1.645
    elif confidence_level == 95:
        z = 1.96
    elif confidence_level == 99:
        z = 2.576
    else:
        return None
    
    # Calculate the sample size
    n = math.ceil((z * sigma / margin_error) ** 2)
    return n

def read_csv(filename, columnname):
    with open(filename, 'r',encoding="unicode_escape") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            data.append(float(row[columnname]))
    return data

def calculate_mean(data):
    mean = sum(data) / len(data)
    return mean

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    return median

def calculate_variance(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

def calculate_standard_deviation(data):
    variance = calculate_variance(data)
    standard_deviation = variance ** 0.5
    return standard_deviation

def calculate_standard_error(data):
    standard_deviation = calculate_standard_deviation(data)
    standard_error = standard_deviation / (len(data) ** 0.5)
    return standard_error

def decide_distribution_shape(data):
    mean_of_data = calculate_mean(data)
    std_of_data = calculate_standard_deviation(data)

    if std_of_data > mean_of_data:
        print("The distribution is right skewed.")
    elif std_of_data < mean_of_data:
        print("The distribution is left skewed.")
    else:
        print("The distribution is symmetric.")
    
def find_outliers(data, threshold=1.5):
    outliers = []
    median = calculate_median(data)
    iqr = calculate_iqr(data)
    lower_bound = median - (threshold * iqr)
    upper_bound = median + (threshold * iqr)
    
    for value in data:
        if value < lower_bound or value > upper_bound:
            outliers.append(value)
    
    return outliers

def calculate_iqr(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1 = sorted_data[int(n * 0.25)]
    q3 = sorted_data[int(n * 0.75)]
    iqr = q3 - q1

    return iqr

def calculate_skewness(data):
    mean = calculate_mean(data)
    standard_deviation = calculate_standard_deviation(data)
    n = len(data)
    skewness = sum(((x - mean) / standard_deviation) ** 3 for x in data) * (n / ((n - 1) * (n - 2)))
    
    return skewness

def calculate_kurtosis(data):
    mean = calculate_mean(data)
    standard_deviation = calculate_standard_deviation(data)
    n = len(data)
    kurtosis = sum(((x - mean) / standard_deviation) ** 4 for x in data) * (n * (n + 1) / ((n - 1) * (n - 2) * (n - 3))) - (3 * ((n - 1) ** 2) / ((n - 2) * (n - 3)))
    
    return kurtosis

