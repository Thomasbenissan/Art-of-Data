# Analysis of Premier League Players' Performance in 2020

I decided to work with a dataset about premier league players in 2020. I’ve always been super interested in how age affects a player's performance. I think the age of peak performance should be around 27 because you are at your physical peak but you are old enough to have a lot of experience in the sport, something I think is just as valuable. I wanted to see how accurate my hypothesis was by creating a performance score, made of a bunch of subfactors weighted out, and comparing that to the age of the player.

To make the performance score, I used the following variables, making sure to standardize them out of 100 and then create a weighted average using each variable's respective factors:

- ‘Appearances': 0.05,
- 'Wins': 0.2,
- 'Losses': -0.1,
- 'Goals': 0.4,
- 'Shooting accuracy %': 0.2,
- 'Big chances missed': -0.2,
- 'Duels won': 0.1,
- 'Duels lost': -0.1,
- 'Assists': 0.2,
- 'Yellow cards': -0.05,
- 'Red cards': -0.2

I used my background knowledge of soccer to decide these factors. I then created frequency graphs of the frequency distribution for both age and performance score to better visualize and understand the data.

## Age Distribution Analysis

From the age distribution analysis, the mean age of the players in the dataset was 25.79 years, with a median age of 26 years, and a standard deviation of 4.38. This means that most Premier League players in 2020 were in their mid-twenties.

## Performance Score Distribution Analysis

The mean of the performance scores was 10.01, but the distribution had a high standard deviation of 14.34, and the median was relatively lower at 4.2. This high variability in performance scores suggests a wide range of player abilities and contributions within the league. The lower median compared to the mean could indicate that while there are very well-performing outliers, most players have moderate performance scores.

## Visualizations and Relationships

In visualizing the dataset, I created scatter plots to examine the relationship between age and performance score. The scatter plot allowed me to clearly see a sort of upside-down U-shaped trendline, peaking around the 27-year age mark. This allowed me to conclude that my hypothesis, in this analysis of the data, was correct.

## Limitations of the Analysis

However, a big limitation of this analysis is that there was really no reasoning behind the weights attributed to each stat other than my knowledge. Additionally, the values that had the highest weights were goals and assists, skewing the data as midfielders and forwards will have the most goals/assists and ultimately underrepresenting higher-performing defenders.

## Conclusion

In conclusion, the analysis of this dataset offered valuable insights but also highlighted the complexities of evaluating athletic performance. Since a lot of metrics such as mental toughness, mental state, injuries, etc., cannot be accurately quantified, creating an accurate metric for a player's performance is arguably impossible. However, we can use the truly quantifiable data to make some correlations, although we must keep in mind the inevitable flaws with the conclusions drawn.
