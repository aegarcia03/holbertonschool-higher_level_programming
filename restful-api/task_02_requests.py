#!/usr/bin/python3
import requests
import json
import csv


def fetch_and_print_posts():
    """Parses the fecthed data into a JSON object"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        json_obj = response.json()

        for obj in json_obj:
            print(obj['title'])


def fetch_and_save_posts():
    """Structures data into a list of dictionaries"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        json_obj = response.json()
        data = []
        for obj in json_obj:
            dic_data = {
                "id": obj["id"],
                "title": obj["title"],
                "body": obj["body"]
            }
            data.append(dic_data)

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
