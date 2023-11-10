import matplotlib.pyplot as plt
import pandas as pd


def generate_mean_score_line_plot(nhl_df):
    """
    Generates a line plot showing the mean scores of home and away teams in NHL games over time.

    Parameters:
        nhl_df (DataFrame): A Pandas DataFrame containing NHL game data, including columns 'date',
                            'home_team_score' and 'away_team_score'.

    Returns:
        None

    This function takes an NHL game dataset, groups the data by year, calculates the mean home
    team and away team scores for each year, and then creates a line plot to visualize how these
    mean scores have evolved over time. Season (year) is on X-axis, Mean Team Score is on Y-axis.
    The plot displays two lines, one for the home team mean score and one for the away team mean 
    score, with data points marked by circular markers.

    Example Usage:

        generate_mean_score_line_plot(nhl_game_data)
        plt.show()  # show graph

    """

    plt.figure(figsize=(12, 8))
    plt.plot(nhl_df.groupby(nhl_df['date'].dt.year)['home_team_score'].mean(), label='Home Team Mean Score', marker='o')
    plt.plot(nhl_df.groupby(nhl_df['date'].dt.year)['away_team_score'].mean(), label='Away Team Mean Score', marker='o')

    plt.xlabel('Year Played (Season)')
    plt.ylabel('Team Mean Score')
    plt.title('Home Team and Away Team Mean Scores Over Time')
    plt.legend()

    plt.show()


def generate_scatter_plot(nhl_df):
    """
    Generate a scatter plot to visualize the relationship between pregame ratings of home and away teams with respect to their scores.

    Parameters:
        nhl_df (DataFrame)

    Returns:
        None

    This function takes an NHL game dataset and randomly samples 500 data points, creating a scatter plot
    between the teams with home_team on X-axis & away_team on Y-axis and density of plotted points is
    determined by the home teams score with larger score resulting in larger markers. The transparency
    of markers is set to 0.5 

    Example Usage:

        generate_scatter_plot(nhl_game_data)
        plt.show()  # show graph

    """
    data_sampled = nhl_df.sample(n=500, random_state=42)

    plt.figure(figsize=(12, 8))
    plt.scatter(data_sampled['home_team_pregame_rating'], data_sampled['away_team_pregame_rating'], s=data_sampled['home_team_score']*10, alpha=0.5)

    plt.xlabel('Home Teams')
    plt.ylabel('Away Teams')
    plt.title('Scatter Plot of Pregame Ratings vs Scores with Size Encoding')

    plt.show()


def generate_histogram(nhl_df):
    """
    Generate a histogram to display the frequency distribution of home team scores in NHL games.

    Parameters:
        nhl_df (DataFrame): A Pandas DataFrame containing NHL game data with a column 'home_team_score'.

    Returns:
        None

    This function randomly samples 1000 data points from the provided dataset and creates a histogram
    to illustrate the distribution of home team scores. The x-axis represents the home team scores, grouped
    into bins, with scores frequency in Y-axis.

    Example Usage:

        generate_histogram(nhl_game_data)
        plt.show()  # show graph

    """
    data_sampled = nhl_df.sample(n=1000, random_state=42)

    plt.figure(figsize=(12, 8))
    plt.hist(data_sampled['home_team_score'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)

    plt.xlabel('Home Team Score')
    plt.ylabel('Frequency')
    plt.title('Histogram of Home Team Scores')

    plt.show()


if __name__ == "__main__":

    # Read the data
    nhl_dataframe = pd.read_csv("nhl_elo.csv")

    nhl_dataframe['date'] = pd.to_datetime(nhl_dataframe['date'], format='%Y-%m-%d')

    # Filter records for years 2001 to 2023
    data_filtered_df = nhl_dataframe[(nhl_dataframe['date'].dt.year >= 2001) & (nhl_dataframe['date'].dt.year <= 2023)]

    # plot line graph
    generate_mean_score_line_plot(data_filtered_df)

    # plot scatter plot graph
    generate_scatter_plot(data_filtered_df)

    # plot histogram graph
    generate_histogram(data_filtered_df)