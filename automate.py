import argparse

import csv
import requests
import json

def read_csv(name):
    ret = []
    with open(name, newline='') as csvfile:
        datareader = csv.reader(csvfile, dialect='excel')
        next(datareader)
        for row in datareader:
            ret.append(row)
    return ret

parser = argparse.ArgumentParser(description="Pass in the URL and field IDs")
parser.add_argument('csv_fp', type=str, help="Pass the file path of the csv file")
args = parser.parse_args()

# csv_fp = "./automate.csv"
csv_df = read_csv(args.csv_fp)

with open('./ids.json') as json_file:
    form_field = json.load(json_file)

# form_id = form_field['form_id']
button_id   = form_field['BUTTON_ID']
text_id     = form_field['TEXT_ID']
dropdown_id = form_field['DROPDOWN_ID']
checkbox_id = form_field['CHECKBOX_ID']
url = form_field['URL']

def submit(url, submission):
    response = requests.post(url, submission)
    response_code = response.status_code
    print(response_code)

for row in csv_df:
    #print(row)
    buttonInput   = row[0]
    textInput     = row[1]
    dropdownInput = row[2]
    checkboxInput = row[3]

    #check box responses separated into a json array by ", "
    checkboxInputs = checkboxInput.split(", ")

    submission = {button_id  : buttonInput,
                  text_id    : textInput,
                  dropdown_id: dropdownInput,
                  checkbox_id: checkboxInputs}

    #print(submission)

    submit(url, submission)
    print(row, 'request sent')
