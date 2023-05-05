from pymongo import MongoClient

# Set up MongoDB connection
CONNECTION_STRING = "mongodb://localhost:27017"
DATABASE_NAME = "Vacation_Location"
CLUSTER_NAME = "Location"

client = MongoClient(CONNECTION_STRING)
cluster = client[DATABASE_NAME]
data_base = cluster[CLUSTER_NAME]

# Function to ask user questions and get input
def ask_questions():
    print("------------------------------------------------")
    print("|------- Where will you go on vacation? -------|")
    print("------------------------------------------------\n")

    warm = convert_input(input("Do you prefer a warm climate for your vacation? (Yes=y, No/n)\n> "))
    proximity_beach = convert_input(input("Is proximity to a beach important to you? (Yes=y, No/n): \n> "))
    have_nightlife = convert_input(input("Do you want to go to a destination known for its nightlife? (Yes=y, No/n)\n> "))
    budget_friendly = convert_input(input("Are you looking for a budget-friendly vacation? (Yes=y, No/n)\n> "))
    outdoor_activities = convert_input(input("Do you want to go to a place with lots of outdoor activities? (Yes=y, No/n)\n> "))
    rich_history = convert_input(input("Do you want a destination with a rich history? (Yes=y, No/n)\n> "))
    long_distance = convert_input(input("Are you willing to travel long distances for your vacation? (Yes=y, No/n)\n> "))
    tourist_attractions = convert_input(input("Is it important for you to be in a location with a lot of tourist attractions? (Yes=y, No/n)\n> "))

    return [warm, proximity_beach, have_nightlife, budget_friendly, outdoor_activities, rich_history, long_distance, tourist_attractions]

# Helper function to convert user input to boolean values
def convert_input(value):
    if value.lower() in ['yes', 'y']:
        return True
    elif value.lower() in ['no', 'n']:
        return False
    else:
        return None

# Function to search for destinations based on user input
def search_for_destination(answers):
    destinations = data_base.find({
        "warm": answers[0],
        "proximity_beach": answers[1],
        "have_nightlife": answers[2],
        "budget_friendly": answers[3],
        "outdoor_activities": answers[4],
        "rich_history": answers[5],
        "long_distance": answers[6],
        "tourist_attractions": answers[7]
    })

    # Convert cursor to list and check if there are any results
    destination_list = list(destinations)
    
    if len(destination_list) == 0:
        print("|---------------------------|")
        print("|    No location found :(   |")
        print("|---------------------------|")
    else:
        # Print out the name of each destination that matches the search criteria
        print("|-------The best location for you is:-------|")
        for doc in destination_list:
            print(f"         {doc['name']}")
        print("|-------------------------------------------|\n")

# Call the ask_questions() and search_for_destination() functions to start the program
answers = ask_questions()
search_for_destination(answers)
