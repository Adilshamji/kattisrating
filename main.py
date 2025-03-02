#!/usr/bin/env python3

import bs4
import sys
import requests






import bs4


def get_problem_difficulty(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    diff_card = soup.find('div', class_='metadata-difficulty-card')
    if diff_card:
        diff_number = diff_card.find('span', class_='difficulty_number')
        level_span = diff_card.find('span', class_='text-lg font-bold text-blue-200')
        number = diff_number.get_text(strip=True) if diff_number else None
        level = level_span.get_text(strip=True) if level_span else None
        return number, level
    return None, None


def main():
    for arg in sys.argv[1:]:
        newarg ="https://open.kattis.com/problems/"+arg
        newarg += "?tab=metadata"
        diff, level = get_problem_difficulty(newarg)
        print(f'{arg}: {diff} {level}')




if __name__ == '__main__':
    main()





