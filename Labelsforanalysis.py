import pandas as pd
import numpy as np

def generate_streak_counts_and_betting_results(input_file, output_file):
    # Load the input CSV file
    df = pd.read_csv(input_file, header=None)
    df.columns = ['Color']  # Rename the first column to 'Color' for easier processing
    
    # Initialize variables to track streaks
    current_color = None
    streak_count = 0
    labels = []

    # Iterate over each row to calculate streaks
    for color in df['Color']:
        if color == current_color:
            streak_count += 1
        else:
            current_color = color
            streak_count = 1
        labels.append(f"{color}{streak_count}")

    # Add the 'Win Streak' column to the DataFrame
    df['Win Streak'] = labels

    # Initialize variables for each streak condition
    conditions = [f"🔴{i}" for i in range(1, 7)] + [f"🟢{i}" for i in range(1, 7)]

    # Iterate over each condition to simulate results
    for condition in conditions:
        balance = 0  # Track total balance for each condition
        bet_amount = 1  # Initial bet amount
        multiplier = 2  # Bet multiplier after a loss

        # Initialize a new column with NaN for storing bet amounts
        df[f'Bet Amount ({condition})'] = np.nan

        for i in range(1, len(df)):
            previous_round = df.loc[i - 1, 'Win Streak']  # Get the previous round value
            current_round = df.loc[i, 'Win Streak']  # Get the current round value

            # Attach bet amount to the round where the streak condition occurs
            if previous_round == condition:
                df.at[i - 1, f'Bet Amount ({condition})'] = bet_amount  # Attach bet amount to the streak round
                if condition[0] in current_round:
                    # Bet won
                    balance += bet_amount
                    bet_amount = 1  # Reset bet amount after a win
                else:
                    # Bet lost
                    balance -= bet_amount
                    bet_amount *= multiplier  # Increase bet amount after a loss

    # Save the updated DataFrame to the output CSV file
    df.to_csv(output_file, index=False)

# Example usage
input_file = 'C:/Users/Auton/Terminal/INFINITY.csv'
output_file = 'C:/Users/Auton/Terminal/OutPutReady.csv'
generate_streak_counts_and_betting_results(input_file, output_file)


