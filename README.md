# NHL Data Visualization Module
This module provides functions to visualize NHL (National Hockey League) game data. It includes methods to create various plots for analyzing different aspects of NHL game statistics.

## Functions Included:
  - create_mean_score_line_plot(nhl_df): Generates a line plot illustrating the mean scores of home and away teams in NHL games over time.
  - create_scatter_plot(nhl_df): Creates a scatter plot displaying the relationship between pregame ratings of home and away teams concerning their scores.
  - create_histogram(nhl_df): Produces a histogram showcasing the frequency distribution of home team scores in NHL games.

## Requirements
  - matplotlib
  - pandas

## Usage
  ```import matplotlib.pyplot as plt
import pandas as pd
from nhl_data_visualization import create_mean_score_line_plot, create_scatter_plot, create_histogram

if __name__ == "__main__":
    # Read your NHL game data as a Pandas DataFrame
    nhl_data_df = pd.read_csv("nhl_game_data.csv")

    # Example: Visualize mean scores over time
    create_mean_score_line_plot(nhl_data_df)

    # Example: Visualize relationship between pregame ratings and scores
    create_scatter_plot(nhl_data_df)

    # Example: Visualize frequency distribution of home team scores
    create_histogram(nhl_data_df)
```
