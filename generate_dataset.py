import pandas as pd
import random

# Categories and sample adjectives/materials
categories = ["Ring", "Necklace", "Bracelet", "Earrings", "Pendant", "Anklet"]
adjectives = ["Elegant", "Stylish", "Luxury", "Golden", "Silver", "Diamond", "Pearl", "Trendy", "Classic", "Modern"]
materials = ["Gold", "Silver", "Diamond", "Pearl", "Platinum", "Rose Gold"]

# Map each category to your proper image
category_images = {
    "Ring": "images/Ring.jpg",
    "Necklace": "images/Necklace.jpg",
    "Bracelet": "images/Bracelet.jpg",
    "Earrings": "images/Earrings.jpg",
    "Pendant": "images/Pendant.jpg",
    "Anklet": "images/Anklet.jpg"
}

products = []

for i in range(500):
    category = random.choice(categories)
    material = random.choice(materials)
    adj = random.choice(adjectives)
    title = f"{adj} {material} {category}"
    description = f"A beautiful {material} {category.lower()} perfect for any occasion."
    price = round(random.uniform(50, 2000), 2)
    rating = round(random.uniform(3.0, 5.0), 1)

    # Assign the proper image for the category
    image_url = category_images.get(category, None)
    
    products.append([title, description, price, category, rating, image_url])

df = pd.DataFrame(products, columns=["title", "description", "price", "category", "rating", "image_url"])
df.to_csv("jewellery_custom.csv", index=False)
print("Custom dataset generated with 500 products and proper category images.")
