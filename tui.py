import process
import visual


def menu_title():
    title = "Disneyland Review Analyser"
    len_title = len(title)
    print("-" * len_title)
    print(f"{title}")
    print("-" * len_title)


def read_dataset():
    file_name = 'data/disneyland_reviews.csv'
    data = process.read_data_from_csv(file_name)
    print("\nData has been read successfully.")
    print(f"There are {len(data)} rows in the dataset.")


def main_menu():
    file_name = 'data/disneyland_reviews.csv'
    while True:
        print("""
        [A] View Data
        [B] Visualise Data
        [X] Exit
        """)
        menu = input("Please enter your choice:")
        if (menu == "A") or (menu == "a"):
            print("\nYou have chosen option A - View Data")
            while True:
                print("""
                [A] View Reviews by Park
                [B] Numbers of Reviews by Park & Reviewer Location
                [C] Average Score per year by Park
                [D] Average Score per Park by Reviewer Location
                [X] Previous Menu
                """)
                submenu_a = input("Please enter your choice:")
                if (submenu_a == "A") or (submenu_a == "a"):
                    print("\nYou have chosen option A: View Reviews by Park")
                    park_name = input("Enter the name of the park:")
                    process.display_reviews_by_park(process.read_data_from_csv(file_name), park_name)

                elif (submenu_a == "B") or (submenu_a == "b"):
                    print("\nYou have chosen option B: Numbers of Reviews by Park & Reviewer Location")
                    park_name = input("Enter the name of the park:")
                    location = input("Enter the location of the reviews:")
                    counter = process.reviews_by_park_and_location(process.read_data_from_csv(file_name), park_name,
                                                                   location)
                    print(f"There are {counter} reviews for {park_name} from {location}.")

                elif (submenu_a == "C") or (submenu_a == "c"):
                    print("\nYou have chosen option C: Average Score per year by Park")
                    park_name = input("Enter the name of the park: ")
                    year = input("Enter the year: ")
                    average_rating = process.average_score_per_park_by_year(process.read_data_from_csv(file_name),
                                                                            park_name, year)
                    if average_rating == 0:
                        print(f"No reviews found for {park_name} in {year}.")
                    else:
                        print(f"The average rating for {park_name} in {year} is {average_rating:.2f}.")

                elif (submenu_a == "D") or (submenu_a == "d"):
                    print("\nYou have chosen option D: Average Score per Park by Reviewer Location")
                    process.print_average_scores(process.average_score_per_park_by_location(process.read_data_from_csv
                                                                                            (file_name)))

                elif (submenu_a == "X") or (submenu_a == "x"):
                    print("\nYou have chosen option X: Previous Menu")
                    break
                else:
                    print("\nNot a Valid Choice. Try again.")
        elif (menu == "B") or (menu == "b"):
            print("\nYou have chosen option B: Visualise Data")
            while True:
                print("""
                        [A] Most Reviewed Parks
                        [B] Average Scores
                        [C] Park Ranking by Nationality
                        [D] Most Popular Month by Park
                        [X] Previous Menu
                        """)
                submenu_b = input("Please enter your choice:")
                if (submenu_b == "A") or (submenu_b == "a"):
                    print("\nYou have chosen option A: Most Reviewed Parks")
                    visual.reviews_per_park()

                elif (submenu_b == "B") or (submenu_b == "b"):
                    print("\nYou have chosen option B: Average Scores")
                    visual.average_review_score()

                elif (submenu_b == "C") or (submenu_b == "c"):
                    print("\nYou have chosen option C: Park Ranking by Nationality")
                    visual.park_ranking_nationality()

                elif (submenu_b == "D") or (submenu_b == "d"):
                    print("\nYou have chosen option D: Most Popular Month by Park")
                    visual.popular_month_park()

                elif (submenu_b == "X") or (submenu_b == "x"):
                    print("\nYou have chosen option X: Previous Menu")
                    break
                else:
                    print("\nNot a Valid Choice. Try again.")
        elif (menu == "X") or (menu == "x"):
            print("\nYou have chosen option X: Exit")
            print("Goodbye")
            break
        else:
            print("\nNot a Valid Choice. Try again.")