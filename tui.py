import process
import visual


title = "Disneyland Review Analyser"
len_title = len(title)

print("-" * len_title)
print(f"{title}")
print("-" * len_title)

file_name = 'data/disneyland_reviews.csv'
data = process.read_data_from_csv(file_name)
print("\nData has been read successfully.")
print(f"There are {len(data)} rows in the dataset.")


def main_menu():
    while True:
        print("""
        [A] View Data
        [B] Visualise Data
        [C] Export Data
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
                    process.display_reviews_for_park(process.read_data_from_csv('data/disneyland_reviews.csv'),
                                                     park_name)

                elif (submenu_a == "B") or (submenu_a == "b"):
                    print("\nYou have chosen option B: Numbers of Reviews by Park & Reviewer Location")
                    park_name = input("Enter the name of the park:")
                    location = input("Enter the location of the reviews:")
                    counter = process.reviews_park_location(process.read_data_from_csv('data/disneyland_reviews.csv'),
                                                            park_name, location)
                    print(f"There are {counter} reviews for {park_name} from {location}.")

                elif (submenu_a == "C") or (submenu_a == "c"):
                    print("\nYou have chosen option C: Average Score per year by Park")
                    park_name = input("Enter the name of the park: ")
                    year = input("Enter the year: ")
                    average_rating = process.average_rating_for_park_in_year(process.read_data_from_csv(
                        'data/disneyland_reviews.csv'), park_name, year)
                    if average_rating == 0:
                        print(f"No reviews found for {park_name} in {year}.")
                    else:
                        print(f"The average rating for {park_name} in {year} is {average_rating:.2f}.")

                elif (submenu_a == "D") or (submenu_a == "d"):
                    print("\nYou have chosen option D: Average Score per Park by Reviewer Location")
                    process.print_average_scores(process.average_score_per_park_by_location(process.read_data_from_csv(
                        'data/disneyland_reviews.csv')))

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
                    visual.vis()

                elif (submenu_b == "B") or (submenu_b == "b"):
                    print("\nYou have chosen option B: Average Scores")
                    visual.vis2()

                elif (submenu_b == "C") or (submenu_b == "c"):
                    print("\nYou have chosen option C: Park Ranking by Nationality")
                    visual.vis3()

                elif (submenu_b == "D") or (submenu_b == "d"):
                    print("\nYou have chosen option D: Most Popular Month by Park")
                    visual.vis4()

                elif (submenu_b == "X") or (submenu_b == "x"):
                    print("\nYou have chosen option X: Previous Menu")
                    break

                else:
                    print("\nNot a Valid Choice. Try again.")
        elif (menu == "C") or (menu == "c"):
            print("\nYou have chosen option C: Export Data")
            format_choice = input("Select output format:(TXT/CSV/JSON):").upper()
            park_name = input("Enter the name of the park to export:")
            exporter = process.Exporter(process.read_data_from_csv('data/disneyland_reviews.csv'))
            if format_choice == 'TXT':
                exporter.export_to_txt(park_name)
            elif format_choice == 'CSV':
                exporter.export_to_csv(park_name)
            elif format_choice == 'JSON':
                exporter.export_to_json(park_name)
            else:
                print("Invalid format choice. Please select TXT, CSV, or JSON.")

        elif (menu == "X") or (menu == "x"):
            print("\nYou have chosen option X: Exit")
            print("Goodbye")
            break
        else:
            print("\nNot a Valid Choice. Try again.")