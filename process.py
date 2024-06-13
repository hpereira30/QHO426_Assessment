import csv


def read_data_from_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    return data


def display_reviews_by_park(data, park_name):
    for row in data:
        if row[4] == park_name:
            print(row[1])


def reviews_by_park_and_location(data, park_name, location):
    counter = 0
    for row in data:
        if row[4] == park_name and row[3] == location:
            counter += 1
    return counter


def calculate_overall_average_rating(data):
    park_ratings = {}
    for row in data:
        park_name = row[4]
        rating = float(row[1])
        if park_name in park_ratings:
            park_ratings[park_name].append(rating)
        else:
            park_ratings[park_name] = [rating]

    overall_average_ratings = {}
    for park, ratings in park_ratings.items():
        overall_average_ratings[park] = sum(ratings) / len(ratings)

    return overall_average_ratings


def top_10_locations_for_park(data, park_name):
    location_ratings = {}
    for row in data:
        if row[4] == park_name:
            location = row[3]
            rating = float(row[1])
            if location in location_ratings:
                location_ratings[location].append(rating)
            else:
                location_ratings[location] = [rating]

    avg_ratings = {location: sum(ratings) / len(ratings) for location, ratings in location_ratings.items()}
    top_10_locations = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10_locations


def average_score_per_park_by_year(data, park_name, year):
    total_rating = 0
    count = 0
    for row in data:
        if row[4] == park_name and row[2][:4] == year:
            total_rating += float(row[1])
            count += 1
    if count == 0:
        return None
    else:
        return total_rating / count


def average_score_per_park_by_location(data):
    park_locations = {}
    for row in data:
        park_name = row[4]
        location = row[3]
        rating = float(row[1])

        if park_name in park_locations:
            if location in park_locations[park_name]:
                park_locations[park_name][location].append(rating)
            else:
                park_locations[park_name][location] = [rating]
        else:
            park_locations[park_name] = {location: [rating]}

    average_scores = {}
    for park, locations in park_locations.items():
        average_scores[park] = {}
        for location, ratings in locations.items():
            average_scores[park][location] = sum(ratings) / len(ratings)

    return average_scores


def print_average_scores(average_scores):
    for park, locations in average_scores.items():
        print(f"\nPark: {park}")
        for location, score in locations.items():
            print(f"Location: {location}, Average Score: {score:.2f}")


def average_scores_by_month_per_park(data, park_name):
    month_ratings = {}
    month_counts = {}
    for row in data:
        if row[4] == park_name:
            date_parts = row[2].split('-')
            if len(date_parts) >= 2:
                month = date_parts[1]
                rating = float(row[1])
                if month in month_ratings:
                    month_ratings[month] += rating
                    month_counts[month] += 1
                else:
                    month_ratings[month] = rating
                    month_counts[month] = 1

    avg_ratings = {}
    for month, rating_sum in month_ratings.items():
        if month_counts[month] != 0:
            avg_ratings[month] = rating_sum / month_counts[month]
        else:
            avg_ratings[month] = 0

    sorted_avg_ratings = sorted(avg_ratings.items(), key=lambda x: int(x[0]))
    return sorted_avg_ratings