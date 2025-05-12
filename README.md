🗺️ U.S. States Guessing Game (Python Turtle + Pandas)
This is an interactive U.S. States Guessing Game created using Python Turtle graphics and Pandas. The user is presented with a blank map of the United States and has to guess all 50 states by typing their names. Correct guesses appear on the map in their correct location.

🎮 Features
Blank U.S. map rendered using Turtle

User types guesses into a prompt

Correct states are written on the map at the correct coordinates

Keeps track of guessed states

Ends the game when all 50 states are guessed or when the user exits

Generates a .csv file with states the user missed

🛠️ Requirements
Python 3.x

turtle (standard Python library)

pandas

Install Pandas if not already installed:

bash
Copy
Edit
pip install pandas
📦 How to Run
Clone or download this repository.

Ensure the following files are present:

us_states_game.py (main Python script)

50_states.csv (data file with state names and their x, y coordinates)

blank_states_img.gif (map image used as background)

Run the script:
python main.py
Start typing state names into the popup dialog.


main.py: Main script to run the game

50_states.csv: Contains state names and coordinates

blank_states_img.gif: Background image of the U.S. map


🧠 Concepts Used
Turtle graphics for interactive drawing

Pandas for data manipulation and lookup

Input handling via screen.textinput()

CSV file reading and writing

![Screenshot 2025-05-12 184141](https://github.com/user-attachments/assets/7d5ae04a-2f01-4405-9659-60bab74d0dea)
