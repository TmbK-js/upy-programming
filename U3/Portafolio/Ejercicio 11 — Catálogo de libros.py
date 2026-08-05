books = [
      {"title": "Pedro Paramo", "ratings": [5, 4, 5]},
      {"title": "Aura",         "ratings": [3, 4, 4]},
      {"title": "Balun Canan",  "ratings": [5, 5, 5]},
  ]
best_title = None
best_avg = -1
for book in books:
    avg = sum(book["ratings"]) / len(book["ratings"])
    print(f"{book['title']}: {avg:.2f}")
    if avg > best_avg:
        best_avg = avg
        best_title = book["title"]
        print("Top-rated:", best_title)
  # Output:
  # Pedro Paramo: 4.67
  # Aura: 3.67
  # Balun Canan: 5.00
  # Top-rated: Balun Canan