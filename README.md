# Assessing the automatability of OaSIS skills and work activities using Large Language Models  
### *A guide to replicating Oschinski & Walia (2025) for researchers and governments using DSPy*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rchejfec/IRPP-oasis-llm-automation-ratings-guide/blob/main/IRPP_oasis_llm_automation_ratings_guide.ipynb)

By [Ricardo Chejfec](https://github.com/rchejfec)
[Institute for Research on Public Policy](https://irpp.org/) 

## Overview

This repository contains a Google Colab notebook that replicates the first part of the IRPP study [Harnessing Generative AI: Navigating the Transformative Impact on Canada's Labour Market](https://irpp.org/research-studies/harnessing-generative-ai/) by Matthias Oschinski and Ruhani Walia. The notebook uses Large Language Models (LLMs) via the DSPy framework to assess the automatability of skills and work activities from ESDC's 2023 OaSIS framework. The goal is to provide interested researchers and government officials with a practical starting point for leveraging LLMs in labor market analysis.

You can use the provided code to:
*	Run your own versions of this experiment, even comparing different models or parameters.
* Track how these ratings evolve as new AI tools emerge, and as we gain a better understanding of their capability.
* Adapt the script to prompt LLMs on a completely different topic with your own list of terms and phrasings.

## Background and Purpose 
In a recently published IRPP study, authors Matthias Oscinski and Ruhani Walia leverage OpenAI's ChatGPT to explore the automation risk of Canadian occupations given medium term advancements in generative AI.

The first part of their study involves asking two different OpenAI models to rate the automatability of 75 skills and work activities using 12 different phrasings and averaging the results. These skills and work activities come from ESDC's [OaSIS framework]( https://noc.esdc.gc.ca/Oasis/OasisWelcome) which breaks down Canadian occupations into their major elements. This mimics previous studies on the topic, which have typically surveyed experts rather than LLMs. In both cases, these ratings are used to explore the automation risk of occupations by aggregating the score of the occupation's most relevant competencies.

The following document recreates the first part of the study. The goal is to provide a starting place for interested researchers and government officials to build their own analysis. One of the biggest advantages of this approach is that, compared with alternatives, it is significantly cheaper, simpler, and more flexible to changing circumstances.

These types of exercises are often meant to inform rather than predict, serving as a starting point for further research or devising a government strategy. While it is possible that LLMs are not capable of reasoning through the implications of these questions, one can still expect LLM ratings to be similar to those of experts (and researchers find correlations, like this [study]( https://arxiv.org/abs/2303.10130) or [this ILO report](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)). This is particularly the case if we assume that those experts are likely to form a significant part of the literature, directly or indirectly, furnishing the LLM's answers. While hallucinations or errors are still a risk, and one that requires further research, there are steps that can be taken to try to minimize their impact. It is also likely that models will keep getting better, meaning these estimates could become more useful over time without the need for significant changes to the analysis itself.

Of course, the question is not just whether we can use an LLM, but whether we should. As a new methodology using emerging and sometimes unreliable tools, results should be approached with caution. At the same time, the only way to learn is to experiment. There is a lot of valuable work to be done validating and improving upon emerging methodologies such as this one. My hope is that this project encourages other researchers to experiment with this new approach to labour market analysis.

If you have not already, I recommend you read the full [study](https://irpp.org/research-studies/harnessing-generative-ai/) to understand the methodology, findings, and recommendations in detail.

## Getting Started 
Follow these steps to run the analysis:

**1. Prerequisites:** 
  * A Google account (for using Google Colab). 
  * An API key for an LLM provider (e.g., Google AI Studio for Gemma models, OpenAI, Anthropic, etc.). Some providers offer free tiers, which may have stricter rate limits or less powerful models. 

**2. Open in Google Colab:** 
  * Click the "Open In Colab" badge at the top of this README, or directly access the `IRPP-OaSIS-llm-automation-ratings-guide.ipynb` file in the repository and choose "Open in Colab." 

**3. Configure Your API Key:** 
  * The notebook is set up to use Google Colab's "Secrets" manager for API keys. 
  * Click on the **key icon** (🔑) in the left sidebar of Colab. 
  * Click "Add a new secret." * Enter the name for your secret (e.g., `GOOGLE_API_KEY` if using a Google model). 
  * Paste your API key into the "Value" field. 
  * Ensure the "Notebook access" toggle is enabled. 
  * The notebook code will then attempt to load this key. 

**4. Run the Notebook:** 
  * Execute the cells in the notebook sequentially. 
  * Be mindful of API rate limits. The notebook processes 99 skills/work activities with multiple prompt phrasings, leading to approximately 1,000 API requests. Adjust `time.sleep()` values in Step 3 of the notebook if needed for your specific model's limits. While some APIs (like OpenAI's) offer a more efficient **batch processing** feature for bulk tasks, this notebook uses the simpler, real-time request method for demonstration purposes.
  * Runtime can be significant (e.g., ~1 hour with Gemma 3 1B on Colab) and can be reduced by using fewer prompt phrasings or using batch processing.

**5. Review Results:** 
 * The notebook will generate CSV files containing the full table of ratings and a summary table. These will be saved in your Colab environment, and you can download them from the file browser, which is advisable as they will be deleted once you end the session.

## Example Output

The `ExampleOutput/` folder contains sample results from running the full pipeline with Gemini 2.0 Flash:

| File | Description |
|------|-------------|
| `full_table.csv` | All 990 individual ratings |
| `summary_table.csv` | Averaged rating per skill |
| `run_metadata.json` | Model info and runtime statistics |

## Important Considerations
* **DSPy Framework:** While the authors used the ChatGPT API directly, this notebook uses DSPy for its structured prompting capabilities (Signatures) rather than its optimization features, providing cleaner output parsing and easy model substitution. DSPy uses [LiteLLM](https://docs.litellm.ai/docs/providers) under the hood, making it straightforward to switch between providers. For more on DSPy's advanced features, see [dspy.ai](https://dspy.ai/).
* **Prompt Variations:** This notebook uses 10 prompt phrasings adapted from the original study's 12. Versions 7 and 9 from the original varied OpenAI-specific parameters (frequency/presence penalties) rather than wording, so they were omitted as DSPy abstracts provider-specific settings.
* **API Keys & Model Choice:** You are responsible for obtaining and managing your API key. Performance and rate limits vary by model. To switch models, update the `LLM_PROVIDER_MODEL_STRING` variable (e.g., `openai/gpt-4`, `anthropic/claude-3-sonnet`) and the corresponding secret name.
* **API Usage & Costs:** Be aware of the number of requests (approx. 1,000 - 3,000) and any potential costs associated with your chosen API. 

## Async Processing

For faster processing (~5x speedup), see the `AsyncProcessing/` folder. This provides a drop-in module to run API calls in parallel. Requires a paid API tier with higher rate limits.

## Acknowledgement and Disclaimer
I am grateful to Matthias Oschinski and Ruhani Walia for developing the original methodology, for their permission to replicate their study, and for their valuable comments on a draft of this guide. The views expressed here, and any errors in the accompanying notebook, are my own.

I used Gemini (2.5 Pro Preview) when learning how to use DSPy, with help developing initial portions of the guide and in editing. I take full responsibility for this notebook's content and accuracy.
