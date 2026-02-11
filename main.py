from langchain_community.llms import Ollama
from typing import TypedDict, List
import pandas as pd
from graph.workflow import build_graph
from utils.preprocessing import preprocess_reviews

class FoodSenseState(TypedDict):
    recipe_id: int
    recipe_name: str
    reviews: List[str]
    review_summary: str
    sentiment_insights: str
    improvement_advice: str
    final_report: str

llm = Ollama(model="mistral")
app = build_graph(llm, FoodSenseState)


df = preprocess_reviews()
#df = pd.read_csv("data/clean_reviews.csv",encoding='UTF-8',encoding_errors='ignore')
recipes = pd.read_csv("data/recipes.csv")[["RecipeId", "Name"]]
df["RecipeId"] = pd.to_numeric(df["RecipeId"], errors="coerce")
recipes["RecipeId"] = pd.to_numeric(recipes["RecipeId"], errors="coerce")

def run_foodsense(recipe_name):
    # Normalize names
    recipe_name = recipe_name.strip().lower()
    recipes["Name"] = recipes["Name"].str.lower()

    # Find matching recipe
    match = recipes[recipes["Name"] == recipe_name]

    if match.empty:
        return "❌ Recipe not found in database."

    recipe_id = match["RecipeId"].values[0]

    # Get reviews
    reviews = df[df["RecipeId"] == recipe_id]["clean_review"].dropna().astype(str).tolist()

    if len(reviews) == 0:
        return "⚠️ No reviews available for this recipe."

    state = {
        "recipe_id": recipe_id,
        "recipe_name": recipe_name.title(),
        "reviews": reviews,
        "review_summary": "",
        "sentiment_insights": "",
        "improvement_advice": "",
        "final_report": ""
    }

    result = app.invoke(state)
    return result["final_report"]


