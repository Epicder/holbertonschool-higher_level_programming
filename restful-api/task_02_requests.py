#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    url_string = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url_string)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url_string = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url_string)

    if response.status_code == 200:
        posts = response.json()

        post_list = []

        for post in posts:
            post_dictionary = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
                }
            post_list.append(post_dictionary)

        with open('posts.csv', mode='w', newline='', encoding="utf-8") as csvfile:
            
            fields = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(post_list)
