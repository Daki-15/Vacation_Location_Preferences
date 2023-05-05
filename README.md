# README

## Introduction
This code is a simple program that prompts the user with a series of questions to determine their preferred vacation location based on their answers. It uses a MongoDB database to store vacation location data and retrieve the corresponding locations that match the user's preferences.

## Prerequisites
To run this code, you will need to have Python 3 installed on your computer, as well as the following packages:

- pymongo
- dnspython

You will also need to have a MongoDB instance set up and running. The code assumes that you have a local MongoDB instance running on the default port (27017), but you can modify the CONNECTION_STRING variable to connect to a different MongoDB instance.

## Installation
To install the required packages, you can use pip:
```Terminal
pip install pymongo dnspython
```

## Usage
To use this code, you can simply run the questions_and_answers() function, which will prompt the user with a series of questions to determine their preferred vacation location. The function will return a list of boolean values representing the user's answers to the questions.

The program then uses these boolean values to query the MongoDB database and retrieve the corresponding vacation locations that match the user's preferences. The program then prints the names of the matching locations to the console.

To run the code, simply execute the main.py file:
```Terminal
python main.py
```

## Conclusion
This code is a simple example of how to use MongoDB to store and retrieve data based on user preferences. You can modify the database schema and the questions to match your specific needs and preferences.