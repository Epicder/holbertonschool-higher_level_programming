#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as csv_f:
            csv_r = csv.DictReader(csv_f)
            code = [row for row in csv_r]

            with open('data.json', mode='w', encoding='utf-8') as json_file:
                json.dump(code, json_file, indent=4)

            return True
    except FileNotFoundError:
        return False
