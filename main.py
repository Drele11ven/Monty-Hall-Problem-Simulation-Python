import random
import matplotlib.pyplot as plt

def monty_hall_simulation(n_trials: int):
    """
    Simulates the Monty Hall problem for a given number of trials.

    Args:
    n_trials (int): The number of trials to simulate.

    Returns:
    (list): A list of the win probabilities for each trial.
    """
    win_probabilities = []
    for _ in range(n_trials):
        # Randomly place the car behind one of the doors
        car_door = random.randint(1, 3)
        
        # The contestant initially chooses a door at random
        player_choice = random.randint(1, 3)

        # The host opens a door to reveal a goat, avoiding the car and the player's choice
        available_doors = [door for door in [1, 2, 3] if door != player_choice and door != car_door]
        host_choice = random.choice(available_doors)

        # If the contestant switches doors, the new choice is the remaining door
        if _ < n_trials - 1:  # Exclude the last trial from switching, as there is no host choice yet
            player_switch = random.choice([door for door in [1, 2, 3] if door != player_choice and door != host_choice])
        else:
            player_switch = player_choice

        # Calculate the win probability for this trial
        if player_switch == car_door:
            win_probability = 1
        else:
            win_probability = 0

        win_probabilities.append(win_probability)

    return win_probabilities

def visualize_monty_hall_simulation(win_probabilities: list):
    """
    Visualizes the results of a Monty Hall simulation.

    Args:
    win_probabilities (list): A list of the win probabilities for each trial.
    """
    plt.hist(win_probabilities, bins=10, align='left', rwidth=0.8)
    plt.xlabel('Win Probability')
    plt.ylabel('Frequency')
    plt.title('Monty Hall Problem: Win Probability Distribution')

    # Calculate the total number of trials and the width of each bin
    n_trials = len(win_probabilities)
    bin_width = 0.1

    # Add text annotations with the percentage of each bar
    for i, v in enumerate(plt.gca().patches):
        height = v.get_height()
        plt.text(v.get_x() + v.get_width() / 2, height + 3, f'{height / n_trials * 100:.2f}%', ha='center')

    plt.show()

# Run the simulation with 10,000 trials
win_probabilities = monty_hall_simulation(1000000)

# Visualize the results
visualize_monty_hall_simulation(win_probabilities)