# google-form-fill

Simple code to submit multiple google forms with information organised in .csv file

## How to use

1) Obtain relevant data:

    a. form url
    
    b. the ids of the fields to be filled in the form obtained by insepcting the form page using chrome inspection
    
2) Edit the .json file with the required data obtained in step 1
3) Install the requirements.txt in the terminal window
4) Run the code form the command line and pass the path of the csv file. For example

    `python3 ./automate/py ./automate.csv`

## Editing the Python Code

If you have different fields than the ones mentioned in the json file, then edit:

1) Edit the ids.json file
2) Edit the automate.py

_This tasks requires python knowledge_
        
  
