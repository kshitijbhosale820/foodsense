from typing import TypedDict, List

class FoodSenseState(TypedDict):
    recipe_id: int
    data: object
    analysis: str
    llm_output: str