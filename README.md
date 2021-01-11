# ryans-bingo

This is an app I created for my family to play bingo together during COVID.

# Overview
The app is hosted [here](https://ryans-bingo.herokuapp.com/)
It provides a platform to both generate Bingo Cards and Call Bingo numbers. 

There are three pages:
* Landing
* Caller
* Card

## Landing
The landing page simply directs you to either the caller page or the bingo card page.

## Caller
The caller page allows the user to generate Bingo Calls. It will randomly generate new calls until all 75 options have been called. It will also log all of the 
past calls allowing the user to go back and verify numbers.

## Bingo Card
The bingo card page provides the user with a randomly generated Bingo card. The card is generated from a "seed" that can be inputted into the url like 
https://ryans-bingo.herokuapp.com/card/<seed_number>/. This means that if you were to put, say, 34 into the url then you'd recieve the same card every reload. 
This card would be different than anyother card you get with any other seed number. If you use 0 (or the sites "generate random card" button) you will recieve 
a different random card every time.

You can mark cells as they are called and unmark them if you made a mistake. 

# Tools Used
* Django
* Python
* NumPy
* HTML
* Javascript
* CSS

# Enjoy!!!
