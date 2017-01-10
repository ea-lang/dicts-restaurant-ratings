import sys


def read_restaurant_file(file_name):
    """Parse a file of restaurant names/ratings and return a dict of them

    (format of the file's lines is restaurant:rating)
    """

    ratings = {}
    restaurant_file = open(file_name)

    for line in restaurant_file:
        restaurant_tokens = line.rstrip().split(':')
        restaurant, rating = restaurant_tokens

        ratings[restaurant] = rating

    return ratings


def add_rating(ratings_to_add):
    """Prompt user for a new restaurant and rating, return updated dict"""
    new_restaurant = raw_input("Enter a restaurant name:")
    new_rating = raw_input("Enter the rating:")

    ratings_to_add[new_restaurant] = new_rating

    return ratings_to_add


def print_alpha_restaurant_ratings(ratings_to_sort):
    """Print restaurant names and ratings from a dict in alphabetical order"""

    sorted_restaurants = sorted(ratings_to_sort.items())
    for restaurant, rating in sorted_restaurants:
        print "%s is rated at %s." % (restaurant, rating)


def choose_action(file_name):
    """Display menu, prompt user for action and process user selection"""

    restaurant_ratings = read_restaurant_file(file_name)

    while True:
        print """Menu options:
                1. Display restaurant ratings
                2. Add a new rating
                3. Quit"""
        user_action = raw_input(">>")

        if user_action == '1':
            print_alpha_restaurant_ratings(restaurant_ratings)
        elif user_action == '2':
            restaurant_ratings = add_rating(restaurant_ratings)
        elif user_action == '3':
            break
        else:
            print "Not a valid option. Please try again."


file_name = sys.argv[1]
choose_action(file_name)
