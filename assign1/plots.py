import matplotlib.pyplot as plt
import pandas as pd


def create_mean_score_line_plot(nhl_df):
    """
    Creates a line plot showing the mean scores of home and away teams in NHL games over time.

    Parameters:
        nhl_df (DataFrame): A Pandas DataFrame containing NHL game data, including columns 'date',
                            'home_team_score' and 'away_team_score'.

    Returns:
        None

    This function takes an NHL game dataset, groups the data by year, calculates the mean home
    team and away team scores for each year, and then creates a line plot to visualize how these
    mean scores have evolved over time. The x-axis represents the season (year), and the y-axis
    represents the mean team score. The plot displays two lines, one for the home team mean score
    and one for the away team mean score, with data points marked by circular markers.

    Example Usage:

        create_mean_score_line_plot(nhl_game_data)
        plt.show()  # Display the generated plot.

    """

    plt.figure(figsize=(12, 8))
    plt.plot(nhl_df.groupby(nhl_df['date'].dt.year)['home_team_score'].mean(), label='Home Team Mean Score', marker='o')
    plt.plot(nhl_df.groupby(nhl_df['date'].dt.year)['away_team_score'].mean(), label='Away Team Mean Score', marker='o')

    plt.xlabel('Year Played (Season)')
    plt.ylabel('Team Mean Score')
    plt.title('Home Team and Away Team Mean Scores Over Time')
    plt.legend()

    plt.show()


def create_scatter_plot(nhl_df):
    """
    Generate a scatter plot to visualize the relationship between pregame ratings of home and away teams with respect to their scores.

    Parameters:
        nhl_df (DataFrame): A Pandas DataFrame containing NHL game data with columns 'home_team_pregame_rating',
                            'away_team_pregame_rating', and 'home_team_score'.

    Returns:
        None

    This function takes an NHL game dataset and randomly samples 500 data points, creating a scatter plot
    to display the relationship between the pregame ratings of home and away teams. The x-axis represents the
    home team's pregame rating, the y-axis represents the away team's pregame rating, and the size of the
    plotted points is determined by the home team's score, with larger scores resulting in larger markers.
    The transparency of markers is set to 0.5.

    Example Usage:

        create_scatter_plot(nhl_game_data)
        plt.show()  # Display the generated scatter plot.

    """
    data_sampled = nhl_df.sample(n=500, random_state=42)

    plt.figure(figsize=(12, 8))
    plt.scatter(data_sampled['home_team_pregame_rating'], data_sampled['away_team_pregame_rating'], s=data_sampled['home_team_score']*10, alpha=0.5)

    plt.xlabel('Home Team Pregame Rating')
    plt.ylabel('Away Team Pregame Rating')
    plt.title('Scatter Plot of Pregame Ratings vs Scores with Size Encoding')

    plt.show()


def create_histogram(nhl_df):
    """
    Generate a histogram to display the frequency distribution of home team scores in NHL games.

    Parameters:
        nhl_df (DataFrame): A Pandas DataFrame containing NHL game data with a column 'home_team_score'.

    Returns:
        None

    This function randomly samples 1000 data points from the provided dataset and creates a histogram
    to illustrate the distribution of home team scores. The x-axis represents the home team scores, grouped
    into bins, while the y-axis shows the frequency of scores within each bin.

    Example Usage:

        create_histogram(nhl_game_data)
        plt.show()  # Display the generated histogram.

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
    nhl_data_df = pd.read_csv("nhl_elo.csv")

    nhl_data_df['date'] = pd.to_datetime(nhl_data_df['date'], format='%Y-%m-%d')

    # Filter data for years 2001 to 2023
    data_filtered_df = nhl_data_df[(nhl_data_df['date'].dt.year >= 2001) & (nhl_data_df['date'].dt.year <= 2023)]

    # plot line graph
    create_mean_score_line_plot(data_filtered_df)

    # plot scatter plot graph
    create_scatter_plot(data_filtered_df)

    # plot histogram graph
    create_histogram(data_filtered_df)