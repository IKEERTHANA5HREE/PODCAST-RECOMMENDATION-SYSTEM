import pandas as pd
import random

titles_prefix = [
    "Tech Talks", "Startup Stories", "Health Matters", "Crime Chronicles",
    "Comedy Nights", "Science Weekly", "History Uncovered", "Mindfulness Podcast",
    "Finance Simplified", "Movie Buffs", "AI Insights", "Travel Diaries",
    "Food Lovers", "Sports Arena", "Book Talks", "Digital Marketing Hub",
    "Motivation Daily", "Gaming World", "Space Explorers", "Career Guide"
]

genres = [
    "Technology", "Business", "Health", "True Crime", "Comedy", "Science",
    "History", "Wellness", "Finance", "Entertainment", "Travel", "Food",
    "Sports", "Education", "Marketing", "Self Help", "Gaming"
]

descriptions = [
    "Insights and discussions on latest trends",
    "Expert interviews and deep dives",
    "Tips and practical knowledge",
    "Stories and real world experiences",
    "Guides and useful strategies",
    "Latest updates and analysis",
    "Educational and informative content",
    "Fun and engaging conversations"
]

data = []

for i in range(1000):
    title = random.choice(titles_prefix) + " " + str(i)
    genre = random.choice(genres)
    description = random.choice(descriptions)
    
    data.append([title, genre, description])

df = pd.DataFrame(data, columns=["title", "genre", "description"])

df.to_csv("podcasts.csv", index=False)

print("✅ 1000 podcast dataset created!")