# -*- coding: utf-8 -*-
"""
Personal Agent Glycemic Load Macro Balancer Client
Zero-dependency meal glycemic index/load aggregator, macronutrient fat/protein
buffering modeler, and post-prandial cognitive crash probability forecaster.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentGlycemicMacroBalancer:
    """
    Calculates glycemic load of meals, models digestive buffering from proteins and healthy fats,
    and forecasts post-prandial mental stamina and crash risks.
    """

    def calculate_meal_glycemic_load_and_buffering(
        self,
        ingredients: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates composite Glycemic Load: GL = sum(GI_i * Carbs_i / 100).
        Ingredient format: {"name": "Brown Rice", "carbs_g": 45.0, "glycemic_index": 55.0, "protein_g": 4.0, "fat_g": 1.5}
        """
        if not ingredients:
            raise ValueError("Ingredients list cannot be empty.")

        total_carbs = 0.0
        total_protein = 0.0
        total_fat = 0.0
        raw_gl = 0.0

        for item in ingredients:
            c = max(0.0, float(item.get("carbs_g", 0.0)))
            gi = max(0.0, min(100.0, float(item.get("glycemic_index", 50.0))))
            p = max(0.0, float(item.get("protein_g", 0.0)))
            f = max(0.0, float(item.get("fat_g", 0.0)))

            total_carbs += c
            total_protein += p
            total_fat += f
            raw_gl += (gi * c) / 100.0

        # Macronutrient buffering index: B = (1.2 * Protein + 0.8 * Fat) / max(1.0, Carbs)
        buffer_index = (1.2 * total_protein + 0.8 * total_fat) / max(1.0, total_carbs)

        # Effective GL attenuated by protein/fat gastric emptying delay
        damping_factor = max(0.40, min(1.0, 1.0 - 0.22 * math.log(1.0 + buffer_index)))
        effective_gl = round(raw_gl * damping_factor, 1)

        return {
            "total_carbs_g": round(total_carbs, 1),
            "total_protein_g": round(total_protein, 1),
            "total_fat_g": round(total_fat, 1),
            "raw_glycemic_load": round(raw_gl, 1),
            "macronutrient_buffering_index": round(buffer_index, 2),
            "effective_buffered_glycemic_load": effective_gl,
            "glycemic_category": "LOW_GL (Sustained)" if effective_gl <= 10.0 else ("MODERATE_GL" if effective_gl <= 19.0 else "HIGH_GL (Spike Risk)")
        }

    def predict_postprandial_cognitive_stability(
        self,
        meal_gl: float,
        protein_g: float,
        fat_g: float,
        carbs_g: float
    ) -> Dict[str, Any]:
        """
        Predicts post-prandial blood sugar crash probability and cognitive stability window.
        Crash Probability: 1 / (1 + exp(-0.18 * (Effective_GL - 18.0)))
        """
        b_index = (1.2 * max(0.0, protein_g) + 0.8 * max(0.0, fat_g)) / max(1.0, max(0.1, carbs_g))
        eff_gl = max(1.0, meal_gl * max(0.40, min(1.0, 1.0 - 0.22 * math.log(1.0 + b_index))))

        # Logistic crash probability
        z = 0.18 * (eff_gl - 18.0)
        crash_prob = round(1.0 / (1.0 + math.exp(-max(-6.0, min(6.0, z)))), 3)
        crash_prob_pct = round(crash_prob * 100.0, 1)

        # Expected stable focus hours post meal
        stable_hours = round(max(1.0, min(4.5, 4.0 - (eff_gl / 12.0) + (b_index * 0.8))), 1)

        return {
            "effective_glycemic_load": round(eff_gl, 1),
            "postprandial_crash_probability_pct": crash_prob_pct,
            "estimated_stable_focus_hours": stable_hours,
            "cognitive_impact_verdict": "OPTIMAL_FLOW_SUSTAINED" if crash_prob <= 0.25 else ("MODERATE_SLUMP_MANAGABLE" if crash_prob <= 0.60 else "SEVERE_REACTIVE_HYPOGLYCEMIA_RISK"),
            "post_meal_task_advice": "Ideal for complex strategic planning" if crash_prob <= 0.25 else "Schedule light admin or 15m walk post-meal"
        }

    def recommend_macronutrient_stabilizer(
        self,
        target_carb_intake_g: float,
        desired_stability: str = "HIGH_FOCUS"
    ) -> Dict[str, Any]:
        """
        Recommends protein and healthy fat grams needed to neutralize glycemic crash for target carbs.
        """
        carbs = max(5.0, float(target_carb_intake_g))
        target_buffer = 0.85 if desired_stability == "HIGH_FOCUS" else 0.50

        # target_buffer = (1.2 * P + 0.8 * F) / C
        # Equipartition between protein and fat caloric contribution
        recommended_protein_g = round((target_buffer * carbs * 0.60) / 1.2, 1)
        recommended_fat_g = round((target_buffer * carbs * 0.40) / 0.8, 1)

        return {
            "target_carb_intake_g": carbs,
            "desired_stability_level": desired_stability,
            "recommended_protein_addition_g": recommended_protein_g,
            "recommended_healthy_fat_addition_g": recommended_fat_g,
            "target_macronutrient_ratio": f"{carbs:.0f}g C : {recommended_protein_g:.0f}g P : {recommended_fat_g:.0f}g F"
        }
