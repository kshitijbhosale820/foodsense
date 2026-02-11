import pandas as pd

REVIEWS_PATH = "data/clean_reviews.csv"
RECIPES_PATH = "data/recipes.csv"


def load_data():
    """Load review and recipe datasets"""
    reviews_df = pd.read_csv(REVIEWS_PATH)
    recipes_df = pd.read_csv(RECIPES_PATH)[["RecipeId", "Name"]]
    return reviews_df, recipes_df


def get_recipe_name(recipe_id, recipes_df):
    """Fetch recipe name from RecipeId"""
    match = recipes_df[recipes_df["RecipeId"] == recipe_id]
    if not match.empty:
        return match["Name"].values[0]
    return "Unknown Dish"


def get_reviews_for_recipe(recipe_id, reviews_df):
    """Fetch all reviews for a given RecipeId"""
    return reviews_df[reviews_df["RecipeId"] == recipe_id]["clean_review"].tolist()
