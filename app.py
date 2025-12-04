import streamlit as st
import pandas as pd
import os

# Load dataset
df = pd.read_csv("jewellery_custom.csv")

# Streamlit Page Config
st.set_page_config(page_title="Luxury Gems", layout="wide")
st.markdown("<h1 style='text-align:center; color:#4B0082;'>💎 GemFinder</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#555;'>Discover, filter, and explore exquisite jewellery pieces</h4>", unsafe_allow_html=True)
st.markdown("---")


# Sidebar Filters
with st.sidebar:
    st.header("Filters")
    query = st.text_input("Search keyword")
    categories = st.multiselect(
        "Category",
        options=df["category"].unique(),
        default=list(df["category"].unique())
    )
    min_price, max_price = st.slider(
        "Price range",
        float(df["price"].min()),
        float(df["price"].max()),
        (float(df["price"].min()), float(df["price"].max()))
    )
    min_rating = st.slider("Minimum rating", 3.0, 5.0, 3.0)
    sort_option = st.radio("Sort by", ["Rating (High → Low)", "Price (Low → High)", "Price (High → Low)"])



# Filter function
def filter_products(df, query, categories, min_price, max_price, min_rating):
    filtered = df[
        (df["title"].str.contains(query, case=False, na=False) |
         df["description"].str.contains(query, case=False, na=False)) &
        (df["category"].isin(categories)) &
        (df["price"].between(min_price, max_price)) &
        (df["rating"] >= min_rating)
    ]
    if sort_option == "Rating (High → Low)":
        filtered = filtered.sort_values(by="rating", ascending=False)
    elif sort_option == "Price (Low → High)":
        filtered = filtered.sort_values(by="price", ascending=True)
    elif sort_option == "Price (High → Low)":
        filtered = filtered.sort_values(by="price", ascending=False)
    return filtered

# Display products
if query:
    results = filter_products(df, query, categories, min_price, max_price, min_rating)
    if len(results) > 0:
        st.subheader(f"Top {len(results)} results for '{query}'")
        cols = st.columns(3)
        for i, row in enumerate(results.itertuples()):
            with cols[i % 3]:
                # Card layout
                st.markdown(
                    f"<div style='border:1px solid #e6e6e6; border-radius:10px; padding:10px;'>"
                    f"<h4 style='text-align:center'>{row.title}</h4></div>",
                    unsafe_allow_html=True
                )

                # Image loading with path check
                if row.image_url:
                    img_path = os.path.join(os.getcwd(), row.image_url)
                    if os.path.exists(img_path):
                        st.image(img_path, width=350)
                    else:
                        st.warning(f"Image not found: {img_path}")

                st.markdown(f"**Category:** 🏷️ {row.category}")
                st.markdown(f"**Price:** ${row.price:.2f}")
                st.markdown(f"**Rating:** {row.rating} ⭐")
                st.write(row.description[:150] + "...")
                st.markdown("")
    else:
        st.warning("No products found with these filters.")
else:
    st.info("Enter a keyword to search jewellery products.")
