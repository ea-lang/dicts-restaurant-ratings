# your code goes here
import sys


restaurant_ratings_dict = {}


def read_restaurant_file(file_name):
    """Parses a file of restaurant names and scores and adds them to a dict"""
    restaurant_file = open(file_name)
    for line in restaurant_file:
        line = line.rstrip()
        restaurant_pairs = line.split(':')

        restaurant = restaurant_pairs[0]
        rating = restaurant_pairs[1]

        restaurant_ratings_dict[restaurant] = rating


def print_alpha_restaurant_ratings(dict):
    """Prints restaurant names and ratings from a dict in alphabetical order"""
    sorted_restaurants = sorted(dict.items())
    for restaurant, rating in sorted_restaurants:
        print "%s is rated at %s." % (restaurant, rating)


file_name = sys.argv[1]

read_restaurant_file(file_name)

print_alpha_restaurant_ratings(restaurant_ratings_dict)
