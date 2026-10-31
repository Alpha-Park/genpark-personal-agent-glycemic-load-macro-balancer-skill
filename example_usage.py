# -*- coding: utf-8 -*-
import json
from client import PersonalAgentGlycemicMacroBalancer

balancer = PersonalAgentGlycemicMacroBalancer()

print("=" * 64)
print("DEMO: Personal Glycemic Load & Macro Cognitive Balancer")
print("=" * 64)

# 1. Meal Glycemic Load with buffering
meal = [
    {"name": "Steel Cut Oats", "carbs_g": 40.0, "glycemic_index": 52.0, "protein_g": 7.0, "fat_g": 3.0},
    {"name": "Whey Protein Isolate", "carbs_g": 2.0, "glycemic_index": 15.0, "protein_g": 25.0, "fat_g": 1.0},
    {"name": "Almond Butter", "carbs_g": 4.0, "glycemic_index": 20.0, "protein_g": 5.0, "fat_g": 16.0}
]

res = balancer.calculate_meal_glycemic_load_and_buffering(meal)
print(f"\n1. Meal Glycemic Profile:")
print(f"   Raw GL: {res['raw_glycemic_load']} -> Effective Buffered GL: {res['effective_buffered_glycemic_load']}")
print(f"   Buffering Index: {res['macronutrient_buffering_index']} ({res['glycemic_category']})")

# 2. Predict crash probability
stability = balancer.predict_postprandial_cognitive_stability(
    meal_gl=res["effective_buffered_glycemic_load"],
    protein_g=res["total_protein_g"],
    fat_g=res["total_fat_g"],
    carbs_g=res["total_carbs_g"]
)
print(f"\n2. Cognitive Stability Forecast:")
print(f"   Crash Probability: {stability['postprandial_crash_probability_pct']}%")
print(f"   Stable Focus Window: {stability['estimated_stable_focus_hours']} hours ({stability['cognitive_impact_verdict']})")

# 3. Recommend macronutrient stabilizer for 50g carbs
advice = balancer.recommend_macronutrient_stabilizer(target_carb_intake_g=50.0, desired_stability="HIGH_FOCUS")
print(f"\n3. Stabilizer Buffer for 50g Carbs:")
print(f"   Add: {advice['recommended_protein_addition_g']}g Protein + {advice['recommended_healthy_fat_addition_g']}g Healthy Fat")
print(f"   Target Macro Ratio: {advice['target_macronutrient_ratio']}")
