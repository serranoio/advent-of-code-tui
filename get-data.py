#!/usr/bin/env python3
import requests
from dotenv import load_dotenv
import os
import argparse

load_dotenv()

def fetch_day_input(day):
    if not (1 <= day <= 25):
        raise ValueError('Day must be between 1 and 25')
    
    url = f'https://adventofcode.com/2024/day/{day}/input'
    resp = requests.get(
        url, 
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }, 
        cookies={
            'session': os.getenv('SESSION_TOKEN')
        }
    )

    if resp.status_code != 200:
        print(f"Error {resp.status_code}: {resp.reason}")
    else:
        print(resp.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Fetch Advent of Code input for a specific day'
    )
    parser.add_argument(
        '-d', '--day', 
        type=int, 
        help='Day of Advent of Code to fetch input for (1-25)'
    )
    
    args = parser.parse_args()
    try:
        fetch_day_input(args.day)
    except ValueError as e:
        print(e)
