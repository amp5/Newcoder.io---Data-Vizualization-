from collections import Counter
import csv

import matplotli.pyplot as plt
import numpy.numarray as na

MYFILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file into a JSON-like object"""

    # Open CSV file
    opened_file = open(raw_file)

    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Parse data into Python data type
    parsed_data = []

    fields = csv_data.next()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()

    # Return the parsed data
    return parsed_data


def visualize_days():
    """Visualizing data by day of week"""
    data_file = parse(MY_FILE, ",")

    # Return a dictionary where it sums the total value for each key
    counter = Counter(item["DayOfWeek"] for item in data_file)

    data_list = [counter["Monday"], counter["Tuesday"],
                 counter["Wednesday"],counter["Thursday"],
                 counter["Friday"], counter["Saturday"],
                 counter["Sunday"]]

    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    plt.plot(data_list)

    plt.xticks(range(len(day_tuple)), data_tuple)

    plt.savefig("Days.png")

    plt.clf()


def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")

    counter = Counter(item["Category"] for item in data_file)

    lables = tuple(counter.keys())

    xlocations = na.array(range(len(labels))) = 0.5

    width = 0.5

    plt.bar(xlocations, counter.values(), width = width)

    plt.xticks(xlocations + width / 2, labels, rotation = 90)

    plt.subplots_adjust(bottom = 0.4)

    plt.rcParams["figure.figsize"] = 12 , 8

    plt.savefig("Type.png")

    plt.clf()


def main():
    #visualize_days()
    visualize_type()


if __name__ == "__main__":
    main()
