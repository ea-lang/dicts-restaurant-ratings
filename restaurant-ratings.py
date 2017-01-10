import sys


def read_restaurant_file(file_name):
    """Parses a file of restaurant names and ratings (format restaurant:rating) and adds them to a dict"""

    ratings = {}
    restaurant_file = open(file_name)

    for line in restaurant_file:
        restaurant_tokens = line.rstrip().split(':')
        restaurant, rating = restaurant_tokens

        ratings[restaurant] = rating

    return ratings


def add_rating(ratings):
    new_restaurant = raw_input("Enter a restaurant name:")
    new_rating = raw_input("Enter the rating:")

    ratings[new_restaurant] = new_rating

    return ratings


def print_alpha_restaurant_ratings(rating_dict):
    """Prints restaurant names and ratings from a dict in alphabetical order"""

    sorted_restaurants = sorted(rating_dict.items())
    for restaurant, rating in sorted_restaurants:
        print "%s is rated at %s." % (restaurant, rating)


file_name = sys.argv[1]
restaurant_ratings = read_restaurant_file(file_name)
add_rating(restaurant_ratings)
print_alpha_restaurant_ratings(restaurant_ratings)
