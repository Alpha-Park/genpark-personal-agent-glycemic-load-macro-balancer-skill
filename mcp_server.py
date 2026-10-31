# -*- coding: utf-8 -*-
"""
Personal Agent Glycemic Load Macro Balancer FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentGlycemicMacroBalancer

mcp = FastMCP("genpark-personal-agent-glycemic-load-macro-balancer-skill")
balancer = PersonalAgentGlycemicMacroBalancer()

@mcp.tool()
def calculate_meal_glycemic_load_and_buffering(ingredients_json: str) -> str:
    """
    Calculates composite Glycemic Load and protein/fat buffering index for a meal.
    """
    ingredients = json.loads(ingredients_json)
    res = balancer.calculate_meal_glycemic_load_and_buffering(ingredients)
    return json.dumps(res, indent=2)

@mcp.tool()
def predict_postprandial_cognitive_stability(
    meal_gl: float,
    protein_g: float,
    fat_g: float,
    carbs_g: float
) -> str:
    """
    Predicts post-prandial blood sugar crash probability and cognitive stamina hours.
    """
    res = balancer.predict_postprandial_cognitive_stability(meal_gl, protein_g, fat_g, carbs_g)
    return json.dumps(res, indent=2)

@mcp.tool()
def recommend_macronutrient_stabilizer(
    target_carb_intake_g: float,
    desired_stability: str = "HIGH_FOCUS"
) -> str:
    """
    Calculates recommended protein and fat buffers to neutralize glycemic spikes.
    """
    res = balancer.recommend_macronutrient_stabilizer(target_carb_intake_g, desired_stability)
    return json.dumps(res, indent=2)

def main():
    print("Testing Glycemic Macro Balancer FastMCP Server:")
    print(predict_postprandial_cognitive_stability(22.0, 25.0, 15.0, 45.0))

if __name__ == "__main__":
    main()
