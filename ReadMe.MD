```md
# Overview

This project helped me better understand the relationship between front-end programming, back-end programming, and data analysis. The purpose of the code is to analyze data from the American Library Association to determine which book genres are most frequently censored and which authors appear most consistently in censorship records.

The dataset used for this project was obtained from Kaggle under the title **"Banned Book Dataset."**

Dataset: https://www.kaggle.com/datasets/chielerli/banned-book-dataset

The motivation behind this assignment is to support my personal research project on the impact of literary censorship. Analyzing this dataset allowed me to streamline and refine my research by identifying patterns in challenged books and authors.

## YouTube Demo

**Software Demo Video:**  
https://www.youtube.com/watch?v=ZGj-qs4gwtI&feature=youtu.be

# Data Analysis Results

## Dataset Summary

| Metric | Value |
|---------|------:|
| Total books in dataset | 17,440 |
| Total banned books | 7,713 |
| Total not banned | 9,727 |
| Overall ban rate | 44.2% |
| Unique authors | 7,951 |
| Authors with banned books | 2,059 |
| Most common genre overall | Fiction |

## Top 10 Genres by Share of All Banned Books

> **Note:** Percentages exceed 100% because individual books can belong to multiple genres.

| Genre | Percentage |
|--------|-----------:|
| Fiction | 71.3% |
| Young Adult | 49.2% |
| Contemporary | 34.0% |
| Romance | 33.1% |
| Realistic Fiction | 22.6% |
| Fantasy | 22.4% |
| Audiobook | 21.1% |
| LGBT | 21.0% |
| Children's | 17.0% |
| Queer | 14.9% |

## Top 10 Most Frequently Banned Authors

| Author | Number of Banned Books |
|--------|-----------------------:|
| Stephen King | 129 |
| P. C. Cast | 49 |
| James Patterson | 41 |
| Ellen Hopkins | 39 |
| Sarah J. Maas | 36 |
| Colleen Hoover | 33 |
| Cassandra Clare | 32 |
| Meg Cabot | 30 |
| Rick Riordan | 29 |
| Jodi Picoult | 28 |

## Generated Graphs

The analysis script also generates the following visualizations:

- `graphs/ban_share_by_genre.png`
- `graphs/most_banned_authors.png`

# Development Environment

The dataset was obtained from Kaggle and analyzed using Python in Visual Studio Code. The project primarily relies on the **Pandas** library for data cleaning and analysis and uses **Matplotlib** to generate graphs that visualize censorship trends.

# Useful Websites

- Kaggle Dataset: https://www.kaggle.com/datasets/chielerli/banned-book-dataset
- American Library Association: https://www.ala.org/

# Future Work

- Improve the graph color palette to create a more cohesive visual presentation.
- Compare censorship trends between American Library Association data and PEN America data.
- Better visualize books that belong to multiple genres and examine how overlapping categories affect the analysis.
```
