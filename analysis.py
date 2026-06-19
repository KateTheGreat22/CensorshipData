import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import os

# ── Download and load the banned books dataset from Kaggle ──
path = kagglehub.dataset_download("chielerli/banned-book-dataset")
df = pd.read_csv(path + "/merged_dataset.csv")

# ── Normalize author names from "Lastname, Firstname" to "Firstname Lastname" ──
def normalize_author(name):
    # Split on comma and reverse the order to get natural name format
    if pd.isna(name):
        return name
    parts = [p.strip() for p in name.split(",")]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name.strip()

df["Author"] = df["Author"].apply(normalize_author)

# ── Separate banned and non-banned books into their own dataframes ──
banned = df[df["Banned"] == 1].copy()
not_banned = df[df["Banned"] == 0].copy()

# ── Summary Statistics ──────────────────────────────────────
total_books = len(df)
total_banned = len(banned)
total_not_banned = len(not_banned)
overall_ban_rate = round(total_banned / total_books * 100, 1)
unique_authors = df["Author"].nunique()
unique_banned_authors = banned["Author"].nunique()
most_common_genre = (
    df.dropna(subset=["Genre"])["Genre"]
    .str.split(", ")
    .explode()
    .str.strip()
    .value_counts()
    .idxmax()
)

print("=" * 45)
print("       BANNED BOOKS DATASET — SUMMARY")
print("=" * 45)
print(f"  Total books in dataset:      {total_books}")
print(f"  Total banned:                {total_banned}")
print(f"  Total not banned:            {total_not_banned}")
print(f"  Overall ban rate:            {overall_ban_rate}%")
print(f"  Unique authors:              {unique_authors}")
print(f"  Authors with banned books:   {unique_banned_authors}")
print(f"  Most common genre overall:   {most_common_genre}")
print("=" * 45)

# ── Q1: Which genres make up the largest share of banned books? ──
# Each book can belong to multiple genres (comma-separated), so we
# split and explode the Genre column into individual rows per genre.
genre_rows = df.dropna(subset=["Genre"]).copy()
genre_rows["Genre"] = genre_rows["Genre"].str.split(", ")
genre_exploded = genre_rows.explode("Genre")

# Clean up genre names — strip whitespace and remove malformed "null" prefixed entries
genre_exploded["Genre"] = genre_exploded["Genre"].str.strip()
genre_exploded = genre_exploded[~genre_exploded["Genre"].str.startswith("null")]
genre_exploded = genre_exploded[genre_exploded["Genre"] != ""]

# Filter to only banned books and calculate each genre's share of all banned books
banned_genres = genre_exploded[genre_exploded["Banned"] == 1]
genre_share = (
    banned_genres.groupby("Genre")["Banned"].count() / total_banned * 100
).round(1).sort_values(ascending=False)

print("\n--- Q1: Top 10 Genres by Share of All Banned Books ---")
print("(Note: percentages exceed 100% because books can belong to multiple genres)")
print(genre_share.head(10).to_string())

# ── Q2: Which authors have the most banned books? ──────────
# Group banned books by author and count titles per author
author_banned = (
    banned.groupby("Author")["Title"]
    .count()
    .sort_values(ascending=False)
)

print("\n--- Q2: Top 10 Most-Banned Authors ---")
print(author_banned.head(10).to_string())

# ── Graph 1: Top 10 Genres by Share of Banned Books ────────
top_genres = genre_share.head(10)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(top_genres.index, top_genres.values, color="steelblue", edgecolor="black")

# Add percentage labels above each bar
for bar, val in zip(bars, top_genres.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f"{val}%", ha="center", va="bottom", fontsize=9)

ax.set_title("Top 10 Genres by Share of All Banned Books", fontsize=14, fontweight="bold")
ax.set_xlabel("Genre", fontsize=11)
ax.set_ylabel("% of All Banned Books", fontsize=11)
ax.set_ylim(0, max(top_genres.values) * 1.15)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the genre chart to the graphs folder
os.makedirs("graphs", exist_ok=True)
plt.savefig("graphs/ban_share_by_genre.png", dpi=150)
print("\nGraph 1 saved to graphs/ban_share_by_genre.png")
plt.show()

# ── Graph 2: Top 10 Most-Banned Authors ────────────────────
top_authors = author_banned.head(10)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(top_authors.index, top_authors.values, color="firebrick", edgecolor="black")

# Add count labels above each bar
for bar, val in zip(bars, top_authors.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
            str(val), ha="center", va="bottom", fontsize=9)

ax.set_title("Top 10 Most-Banned Authors", fontsize=14, fontweight="bold")
ax.set_xlabel("Author", fontsize=11)
ax.set_ylabel("Number of Banned Books", fontsize=11)
ax.set_ylim(0, max(top_authors.values) * 1.15)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the author chart to the graphs folder
os.makedirs("graphs", exist_ok=True)
plt.savefig("graphs/most_banned_authors.png", dpi=150)
print("Graph 2 saved to graphs/most_banned_authors.png")
plt.show()