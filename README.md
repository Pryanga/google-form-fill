# google-form-fill

Simple code to submit multiple google forms with information organised in .csv file

## How to use

1) Obtain relevant data:

    a. form url
    
    b. the ids of the fields to be filled in the form obtained by inspecting the form page using chrome inspection:
        `ctrl+shift+i, ctrl+f:"entry."`
    
    - Make sure that each id corresponds with its question because they sometimes appear out of order
    
2) Edit the .json file with the required data obtained in step 1
    - Separate inputs for checkbox questions with ", "
3) Install the packages listed in requirements.txt
4) Run the code from the command line and pass the path of the csv file. For example:

    `python3 ./automate/py ./automate.csv`

## Editing the Python Code

If you have different fields than the ones mentioned in the json file:

1) Edit ids.json
2) Edit automate.py

_These tasks require python knowledge_
        
  
