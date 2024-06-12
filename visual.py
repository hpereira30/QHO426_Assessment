"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt
import process


def vis():
    file_name = 'data/disneyland_reviews.csv'
    data = process.read_data_from_csv(file_name)

    review_counts = {}

    for row in data:
        disneyland_name = row[4]
        try:
            review_count = 1
        except ValueError:
            continue

        if disneyland_name in review_counts:
            review_counts[disneyland_name] += review_count
        else:
            review_counts[disneyland_name] = review_count

    labels = [f"{name}\n{count} Reviews" for name, count in review_counts.items()]
    values = list(review_counts.values())

    plt.pie(values, labels=labels)
    plt.title('Review Distribution for Each Disneyland')
    plt.axis('equal')
    plt.show()


def vis2():
    file_name = 'data/disneyland_reviews.csv'
    data = process.read_data_from_csv(file_name)

    average_ratings = process.calculate_overall_average_rating(data)

    parks = list(average_ratings.keys())
    average_scores = list(average_ratings.values())

    plt.xlabel("Parks")
    plt.ylabel("Average Reviews Score")
    bars = plt.bar(parks, average_scores)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    plt.show()


def plot_bar_chart(top_locations):
    locations, ratings = zip(*top_locations)
    plt.figure(figsize=(10, 6))
    plt.bar(locations, ratings, color='skyblue')
    plt.xlabel('Location')
    plt.ylabel('Average Rating')
    plt.title('Top 10 Locations with Highest Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def vis3():
    file_name = 'disneyland_reviews.csv'
    data = process.read_data_from_csv(file_name)

    park_name = input("Enter the name of the park: ")

    top_locations = process.top_10_locations_for_park(data, park_name)
    if not top_locations:
        print(f"No reviews found for {park_name}.")
    else:
        print(f"Top 10 locations with highest average rating for {park_name}:")
        for i, (location, rating) in enumerate(top_locations, start=1):
            print(f"{i}. {location}: {rating:.2f}")
        plot_bar_chart(top_locations)


def plot_monthly_bar_chart(month_ratings):
    months, ratings = zip(*month_ratings)
    month_names = {
        '1': 'January', '2': 'February', '3': 'March', '4': 'April',
        '5': 'May', '6': 'June', '7': 'July', '8': 'August',
        '9': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    month_names = [month_names[month] for month in months]
    plt.figure(figsize=(10, 6))
    plt.bar(month_names, ratings, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title('Average Rating for Each Month of the Year')
    plt.tight_layout()
    plt.show()


def vis4():
    file_name = 'disneyland_reviews.csv'
    data = process.read_data_from_csv(file_name)

    park_name = input("Enter the name of the park: ")

    month_ratings = process.average_rating_by_month_for_park(data, park_name)
    if not month_ratings:
        print(f"No reviews found for {park_name}.")
    else:
        print(f"Average rating for {park_name} by month:")
        for month, rating in month_ratings:
            print(f"{month}: {rating:.2f}")
        plot_monthly_bar_chart(month_ratings)