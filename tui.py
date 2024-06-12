"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

import process
import visual

file_name = 'data/disneyland_reviews.csv'
data = process.read_data_from_csv(file_name)
print("\nDataset has been read successfully.")
print(f"There are {len(data)} rows in the dataset.")


def main_menu():
    menu = True
    while menu:
        print("""
        [A] View Data
        [B] Visualise Data
        [C] Export Data
        [X] Exit
        """)
        menu = input("Please enter the letter which corresponds with your desired menu choice: ")
        if menu in ["A", "a"]:
            print("\nYou have chosen option A - View Data")
            menu_a = True
            while menu_a:
                print("""
                [A] View Reviews by Park
                [B] Numbers of Reviews by Park and Reviewer Location
                [C] Average Score per year by Park
                [D] Average Score per Park by Reviewer Location
                [X] Previous Menu
                """)
                menu_a = input("Please enter the letter which corresponds with your desired menu choice: ")
                if menu_a in ["A", "a"]:
                    print("\nYou have chosen option A - View Reviews by Park")
                    park_name = input("Enter the name of the park: ")
                    process.display_reviews_for_park(process.read_data_from_csv('disneyland_reviews.csv'), park_name)

                elif menu_a in ["B", "b"]:
                    print("\nYou have chosen option B - Numbers of Reviews by Park and Reviewer Location")
                    park_name = input("Enter the name of the park: ")
                    location = input("Enter the location of the reviews: ")
                    count = process.reviews_park_location(process.read_data_from_csv('disneyland_reviews.csv'),
                                                          park_name, location)
                    print(f"There are {count} reviews for {park_name} from {location}.")

                elif menu_a in ["C", "c"]:
                    print("\nYou have chosen option C - Average Score per year by Park")
                    park_name = input("Enter the name of the park: ")
                    year = input("Enter the year: ")
                    average_rating = process.average_rating_for_park_in_year(process.read_data_from_csv(
                        'disneyland_reviews.csv'), park_name, year)
                    if average_rating is None:
                        print(f"No reviews found for {park_name} in {year}.")
                    else:
                        print(f"The average rating for {park_name} in {year} is {average_rating:.2f}.")

                elif menu_a in ["D", "d"]:
                    print("\nYou have chosen option D - Average Score per Park by Reviewer Location")
                    process.print_average_scores(process.average_score_per_park_by_location(process.read_data_from_csv(
                        'disneyland_reviews.csv')))

                elif menu_a in ["X", "x"]:
                    print("\nYou have chosen option X - Previous Menu")
                    break
                else:
                    print("\nNot a Valid Choice. Try again.")
        elif menu in ["B", "b"]:
            print("\nYou have chosen option B - Visualise Data")
            menu_b = True
            while menu_b:
                print("""
                        [A] Most Reviewed Parks
                        [B] Average Scores
                        [C] Park Ranking by Nationality
                        [D] Most Popular Month by Park
                        [X] Previous Menu
                        """)
                menu_b = input("Please enter the letter which corresponds with your desired menu choice: ")
                if menu_b in ["A", "a"]:
                    print("\nYou have chosen option A - Most Reviewed Parks")
                    visual.vis()

                elif menu_b in ["B", "b"]:
                    print("\nYou have chosen option B - Average Scores")
                    visual.vis2()

                elif menu_b in ["C", "c"]:
                    print("\nYou have chosen option C - Park Ranking by Nationality")
                    visual.vis3()

                elif menu_b in ["D", "d"]:
                    print("\nYou have chosen option D - Most Popular Month by Park")
                    visual.vis4()

                elif menu_b in ["X", "x"]:
                    print("\nYou have chosen option X - Previous Menu")
                    break
                else:
                    print("\nNot a Valid Choice. Try again.")

        elif menu in ["C", "c"]:
            print("\nYou have chosen option C - Export Data")
            format_choice = input("Select output format (TXT/CSV/JSON): ").upper()
            park_name = input("Enter the name of the park to export: ")
            exporter = process.ParkExporter(process.read_data_from_csv('disneyland_reviews.csv'))
            if format_choice == 'TXT':
                exporter.export_to_txt(park_name)
            elif format_choice == 'CSV':
                exporter.export_to_csv(park_name)
            elif format_choice == 'JSON':
                exporter.export_to_json(park_name)
            else:
                print("Invalid format choice. Please select TXT, CSV, or JSON.")
        elif menu in ["X", "x"]:
            print("\nYou have chosen option X - Exit - Goodbye")
            menu = None
        else:
            print("\nNot a Valid Choice. Try again.")