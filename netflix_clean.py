import pandas as pd

# Load Netflix data
df = pd.read_csv("netflix_titles.csv", encoding="utf-8")

# Keep only relevant columns
df = df[["title", "type", "country", "release_year", "rating", "listed_in", "duration"]].copy()

# Fill blanks
df["country"] = df["country"].fillna("Unknown")
df["listed_in"] = df["listed_in"].fillna("")

# Split 'country' and 'listed_in' by comma
df["Country_List"] = df["country"].str.split(", ")
df["Genre_List"] = df["listed_in"].str.split(", ")

# Explode each to rows
df = df.explode("Country_List")
df = df.explode("Genre_List")

# Clean text
df["Country_List"] = df["Country_List"].str.strip()
df["Genre_List"] = df["Genre_List"].str.strip()

# Remove empty genres or countries
df = df[(df["Genre_List"] != "") & (df["Country_List"] != "")]

# Rename columns for clarity
df = df.rename(columns={
    "title": "Title",
    "type": "Type",
    "release_year": "Year",
    "rating": "Age Rating",
    "duration": "Duration (min)",
    "Country_List": "Country",
    "Genre_List": "Genre"
})

# Drop duplicates
df = df.drop_duplicates()

# Save clean CSV
df.to_csv("netflix_clean.csv", index=False, encoding="utf-8")
print(f"✅ Saved: netflix_clean.csv | Rows: {len(df):,} | Cols: {len(df.columns)}")
