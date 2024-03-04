# Monty Hall Problem Simulation with Python and Matplotlib
The Monty Hall problem is a classic probability puzzle that has stumped many a math enthusiast. This repository contains a Python script that simulates the Monty Hall problem and visualizes the results using Matplotlib.
<p align="center">
  <img src='https://github.com/Drele11ven/Monty-Hall-Problem-Simulation-Python/blob/main/monty.png' alt='monty hall'>
</p>

## What is the Monty Hall Problem?
The Monty Hall problem is a probability puzzle based on a game show scenario. In this problem, a contestant is given the choice of three doors. Behind one door is a car, and behind the other two doors are goats. The contestant initially chooses a door, and the game show host, who knows what's behind each door, opens another door to reveal a goat. The host then offers the contestant the chance to switch doors. The question is: Should the contestant switch doors, and if so, what is the probability of winning the car by switching?

### The Monty Hall Problem Simulation Script
This repository contains a Python script called monty_hall.py that simulates the Monty Hall problem for a given number of trials and visualizes the distribution of win probabilities for each trial.

The script is composed of two main functions:

1. monty_hall_simulation: This function simulates the Monty Hall problem for a given number of trials and returns a list of win probabilities for each trial.
2. visualize_monty_hall_simulation: This function takes the list of win probabilities and visualizes the distribution using a histogram. The function also calculates the percentage of each bar and adds it as a text annotation below the bar.
### Running the Script
To run the script, simply execute the monty_hall.py file with Python. By default, the script runs the simulation with 1,000,000 trials and displays the resulting histogram. For example, to run the simulation with 1,000,000 trials, use the following command:
```
python main.py
```
The resulting histogram shows the distribution of win probabilities for each trial. The x-axis represents the win probability, and the y-axis represents the frequency of occurrence. The percentage of each bar is also shown below the bar. `The distribution should show that the probability of winning by switching doors is approximately 2/3, while the probability of winning by sticking with the initial choice is approximately 1/3.`
<p align="center">
  <img src='https://github.com/Drele11ven/Monty-Hall-Problem-Simulation-Python/blob/main/prev.png' alt='monty-hall statistic'>
</p>

### Requirements
The script uses the random and matplotlib libraries, so make sure to install them before running the script. You can install these libraries using pip:

```
pip install random matplotlib
```
### Contributing
We welcome contributions to this script! If you have an idea for how to improve the script or add new features, please submit a pull request. We'll review your changes and provide feedback as soon as possible.

### License
This script is released under the MIT License. See the LICENSE file for more information.

### Conclusion
I hope this script helps you understand the Monty Hall problem and how to simulate and visualize it using Python and Matplotlib. Your best friend Mehdi(Dr.ele11ven)ArmaniFar!
