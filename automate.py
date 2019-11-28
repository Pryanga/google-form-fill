import os
import requests
import csv
import pandas as pd

form_id = "1FAIpQLScmz8YGHstPcRaBjPf5K5w3Ror_3y7mvZoaZBoQTO7PM1IjQQ"
name_id = "entry.1018914776"
email_id = "entry.322905232"
add_id = "entry.1170598938"

url = "https://docs.google.com/forms/d/e/1FAIpQLScmz8YGHstPcRaBjPf5K5w3Ror_3y7mvZoaZBoQTO7PM1IjQQ/formResponse"

# todo: read in csv file
csv_fp = "./automate.csv"
csv_df = pd.read_csv(csv_fp)

# todo: read evey entry in loop

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

