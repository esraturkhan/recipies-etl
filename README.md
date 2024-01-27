# Recipes ETL Project
## Description
This project is designed to extract, process, and analyze recipes from a JSON file containing recipes with the ingredient 'Chilies'. The 'prepTime' and 'cookTime' in the recipes are converted to minutes, and a 'difficulty' rating is calculated based on the total time.

## How to Run
1)Download or clone the project 

2)Navigate to the project directory (e.g., cd recipes-etl).

3)Install the required packages: pip install -r requirements.txt.

4)Run the Python script: python HELLOFRESH_CASESTUDY.py.

## What It Does and How It Does It
Our script reads the specified JSON file and filters out recipes containing the word 'Chilies', taking into account various spellings and inflections of 'Chilies'. It then converts the 'prepTime' and 'cookTime' specified in the recipes into minutes and calculates a 'difficulty' rating for each recipe based on the total time. The results are saved in a CSV file.

## Installing Third-Party Modules
The project uses the Pandas library. When the project Python code is executed, the Pandas library will automatically be downloaded, as the line of code that downloads the library is included. 

Otherwise, to install Pandas, use the following command:
pip install pandas

Alternatively,(in case) to install all required packages listed in requirements.txt, use:
pip install -r requirements.txt

## Python Version Used
This project was developed in Python 3.11.5



