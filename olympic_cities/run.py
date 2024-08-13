#!/usr/bin/env python3

import random
import re

def get_dict_of_cities():
    dict_of_cities = {
        "1896" :    "Athens",
        "1900" :    "Paris",
        "1904" :    "St. Louis",
        "1908" :    "London",
        "1912" :    "Stockholm",
        "1916" :    "Berlin [cancelled due to WWI]",
        "1920" :    "Antwerp",
        "1924" :    "Paris",
        "1928" :    "Amsterdam",
        "1932" :    "Los Angeles",
        "1936" :    "Berlin",
        "1940" :    "Tokyo [cancelled due to WWII]",
        "1944" :    "London [cancelled due to WWII]",
        "1948" :    "London",
        "1952" :    "Helsinki",
        "1956" :    "Melbourne",
        "1960" :    "Rome",
        "1964" :    "Tokyo",
        "1968" :    "Mexico City",
        "1972" :    "Munich",
        "1976" :    "Montreal",
        "1980" :    "Moscow",
        "1984" :    "Los Angeles",
        "1988" :    "Seoul",
        "1992" :    "Barcelona",
        "1996" :    "Atlanta",
        "2000" :    "Sydney",
        "2004" :    "Athens",
        "2008" :    "Beijing",
        "2012" :    "London",
        "2016" :    "Rio de Janeiro",
        "2020" :    "Tokyo",
        "2024" :    "Paris",
        "2028" :    "Los Angeles",
        "2032" :    "Brisbane"
    }

    return dict_of_cities

def main():
    print("===== OLYMPIC CITY QUIZ! =====")
    dict_of_cities = get_dict_of_cities()
    list_of_years = list(dict_of_cities.keys())
    num_of_tries = 10
    correct_answers = 0

    for _ in range(num_of_tries):
        rand_index = random.randint(0, len(list_of_years)-1)
        rand_year = list_of_years[rand_index]
        rand_city = re.sub(r'\[.*?\]', '', dict_of_cities[rand_year]).strip()
        guess = input(f"(Type 'quit' to exit) Year : {rand_year} --- City : ")
        if guess.capitalize() == rand_city:
            print("\033[A\033[60C \033[92mCorrect\033[0m")
            correct_answers += 1
        else:
            print(f"\033[A\033[60C \033[91mWrong\033[0m => {rand_city}")
        if guess.lower() == 'quit':
            break

    print(f"\033[93mTotal: {correct_answers} / {num_of_tries}\033[0m")

if __name__ == '__main__':
    main()
