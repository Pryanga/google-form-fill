import argparse

import pandas as pd
import requests
import json

parser = argparse.ArgumentParser(description="Pass in the URL and field IDs")

parser.add_argument('csv_fp', type=str, help="Pass the file path of the csv file")

args = parser.parse_args()

# csv_fp = "./automate.csv"
csv_df = pd.read_csv(args.csv_fp)

with open('./ids.json') as json_file:
    form_field = json.load(json_file)

form_id = form_field['form_id']
name_id = form_field['name_id']
email_id = form_field['email_id']
add_id = form_field['add_id']
url = form_field['url']

def submit(url, submission):
    response = requests.post(url, submission)
    response_code = response.status_code
    print(response_code)

for index, row in csv_df.iterrows():
    # print(row)
    name = row['Name']
    email = row['Email']
    address = row['Address']

    submission = {"entry.1018914776": name,
                  "entry.322905232": email,
                  "entry.1170598938": address}

    submit(url, submission)

    print(index, 'request sent')

