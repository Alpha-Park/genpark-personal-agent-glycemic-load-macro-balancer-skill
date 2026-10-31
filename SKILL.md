---
name: genpark-personal-agent-glycemic-load-macro-balancer-skill
description: Personal Agent Glycemic Load Macro Balancer. Computes meal glycemic load, evaluates protein and fat digestive buffering, and predicts post-prandial cognitive focus stability vs brain-fog crash probabilities.
license: MIT
version: 1.0.0
tools:
  - calculate_meal_glycemic_load_and_buffering
  - predict_postprandial_cognitive_stability
  - recommend_macronutrient_stabilizer
---

# Personal Agent Glycemic Load Macro Balancer

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent metabolic health and mental stamina advisor. Your objective is to prevent afternoon brain fog, post-prandial energy crashes, and reactive hypoglycemia by modeling glycemic loads and macronutrient gastric damping.

## When to Activate This Skill
- When an agent or user reviews meal plans, nutritional choices, or dining decisions.
- When forecasting mental clarity windows and scheduling deep cognitive tasks after meals.
- When calculating protein/fat counterweights to neutralize high-carbohydrate meals.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentGlycemicMacroBalancer

balancer = PersonalAgentGlycemicMacroBalancer()
res = balancer.predict_postprandial_cognitive_stability(meal_gl=12.0, protein_g=30.0, fat_g=15.0, carbs_g=40.0)
print("Stable Focus Hours:", res["estimated_stable_focus_hours"])
```

### Option 2: FastMCP Tool Calling
- `calculate_meal_glycemic_load_and_buffering(ingredients_json)`
- `predict_postprandial_cognitive_stability(meal_gl, protein_g, fat_g, carbs_g)`
- `recommend_macronutrient_stabilizer(target_carb_intake_g, desired_stability="HIGH_FOCUS")`

## Core Mathematical Principles
1. **Weighted Glycemic Load**: $GL = \sum rac{GI_i 	imes 	ext{Carbs}_i}{100}$.
2. **Gastric Buffering Damping**: Lipids and proteins delay gastric emptying, attenuating peak glucose excursion: $GL_{	ext{eff}} = GL \cdot (1 - 0.22 \ln(1 + B))$.
