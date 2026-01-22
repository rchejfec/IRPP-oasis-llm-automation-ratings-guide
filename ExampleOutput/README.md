# Example Output

This folder contains sample output from running the notebook with **Gemini 2.0 Flash**.

## Files

| File | Description |
|------|-------------|
| `full_table.csv` | All 990 ratings (99 skills × 10 prompts) |
| `summary_table.csv` | Averaged ratings per skill |
| `run_metadata.json` | Model and runtime information |

## Column Definitions

### full_table.csv
- `item_name`: Skill or work activity name
- `prompt_id`: Prompt version (Version 1-10)
- `expects_explanation_flag`: 1 if explanation was requested
- `llm_raw_rating_output`: Rating (1-5)
- `llm_explanation_output`: LLM explanation (if any)
- **Processing time**: ~4 minutes (async mode)
- **Date**: January 2026

## Sample Results

### Most Automatable Skills (Avg Rating ≥ 4)
- Calculating (4.2)
- Getting Information (4.2)
- Analyzing Data or Information (4.0)
- Clerical Activities (4.0)

### Least Automatable Skills (Avg Rating ≤ 2)
- Performing General Physical Activities (1.6)
- Establishing Interpersonal Relationships (1.9)
- Assisting and Caring for Others (2.0)

## Usage

These files can be used to:
1. Understand the expected output format
2. Compare your own results against a reference
