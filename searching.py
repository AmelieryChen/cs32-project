X
import csv

#we need to request or import our website
url = "https://harvardartmuseums.org/collections"

#set the URL to the webpage with paintings we have a lot so...

#go throguht the HTML Files

#condense all the information into CSV files

#Extract the information from each painting
#' For each painting: extract title, extract artist, extract year created, extract material (if available)


with open("artworks.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        artwork_id = row["id"]  # keep as string to preserve decimals
        artworks[artwork_id] = {
            "title": row["title"].strip("'"),  # remove extra quotes
            "year": row["year"],
            "artist": row["artist"] or "Unknown",
            "classification": row["classification"],
            "culture": row["culture"],
            "dimensions": row["dimensions (cm)"]
        }



#artworks = {}

with open("artworks.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        artwork_id = row["id"]  # keep as string to preserve decimals
        artworks[artwork_id] = {
            "title": row["title"].strip("'"),  # remove extra quotes
            "year": row["year"],
            "artist": row["artist"] or "Unknown",
            "classification": row["classification"],
            "culture": row["culture"],
            "dimensions": row["dimensions (cm)"]
        }

for art in artworks:
    print(f'{artworks[artwork_id]["title"]} was made in {artworks[artwork_id]["year"]}')

