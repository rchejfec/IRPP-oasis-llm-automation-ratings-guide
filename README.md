# Assessing the automatability of OaSIS skills and work activities using Large Language Models  
#### *A guide to replicating Oschinski & Walia (2025) for researchers and governments using DSPy*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/https://github.com/rchejfec/IRPP-oasis-llm-automation-ratings-guide/IRPP-OaSIS-llm-automation-ratings-guide.ipynb)

## Overview

This repository contains a Jupyter/Google Colab notebook that replicates the first part of the IRPP study [Harnessing Generative AI: Navigating the Transformative Impact on Canada's Labour Market](https://irpp.org/research-studies/harnessing-generative-ai/) by Matthias Oschinski and Ruhani Walia. The notebook uses Large Language Models (LLMs) via the DSPy framework to assess the automatability of skills and work activities from ESDC's 2023 OaSIS framework. The goal is to provide interested researchers and government officials with a practical starting point for leveraging LLMs in labor market analysis.

## Background and Purpose 
In a recently published IRPP study, authors Matthias Oscinski and Ruhani Walia  leverage OpenAI's ChatGPT to explore the automation risk of Canadian occupations given advancements in generative AI in the medium term.

The first part of their study involves asking two different OpenAI models to rate the automatability of 71 skills and work activities using 12 different phrasings and averaging the results. These skills and work activities come from ESDC's [OaSIS framework]( https://noc.esdc.gc.ca/Oasis/OasisWelcome) which breaks down Canadian occupations into their major elements. This mimics previous studies on the topic, which have typically surveyed experts rather than LLMs. In both cases, these ratings are used to explore the automation risk of occupations by aggregating the score of the occupation's most relevant competencies.

The following document recreates the first part of the study. The goal is to provide interested researchers and government officials a starting place on which they can build their own analysis. One of the biggest advantages of this approach is that, compared with alternatives, it is significantly cheaper, simpler, and more flexible to changing circumstances.

Ratings from LLMs don't need to be more accurate (or even as accurate) as those from experts to be useful. These types of exercises are often meant to inform rather than predict, serving as a starting point for further research or devising a government strategy. Given these tools' ability for processing semantic information and pattern recognition, coupled with the fact that they have been trained on unprecedentedly large amounts of data, they are particularly well suited for these types of tasks.

While it is possible that LLMs are not capable of reasoning through the implications of these questions, and rather act as some sort of stochastic parrot, one can still expect LLM ratings to be similar to those of experts (and [studies find correlations]( https://arxiv.org/abs/2303.10130)). Which makes sense, if we assume those experts likely form a big part of the literature, directly or indirectly, that is informing the LLM's answers. While hallucinations are still a risk, and one that requires further research, there are steps that can be taken to try to minimize their impact. Plus, it's reasonable to expect models to keep getting better, meaning these estimates could become more useful over time without the need for significant changes.

Still, there's a lot of exciting, valuable work to be done here -- like validating emerging methodologies like this one, improving upon them and developing new approaches. I hope this notebook can help showcase how easy it is to start incorporating LLMs into your research.

If you haven't already, I recommend you read the full [study](https://irpp.org/research-studies/harnessing-generative-ai/) to understand the methodology, findings, and recommendations in detail.

## Getting Started 
Follow these steps to run the analysis:

**1. Prerequisites:** 
  * A Google account (for using Google Colab). 
  * An API key for an LLM provider (e.g., Google AI Studio for Gemma models, OpenAI, Anthropic, etc.). Some providers offer free tiers, which may have stricter rate limits or less powerful models. 

**2. Open in Google Colab:** 
  * Click the "Open In Colab" badge at the top of this README, or directly access the `IRPP-OaSIS-llm-automation-ratings-guide.ipynb` file in this repository and choose "Open in Colab." 

**3. Configure Your API Key:** 
  * The notebook is set up to use Google Colab's "Secrets" manager for API keys. 
  * Click on the **key icon** (🔑) in the left sidebar of Colab. 
  * Click "Add a new secret." * Enter the name for your secret (e.g., `GOOGLE_API_KEY` if using a Google model). 
  * Paste your API key into the "Value" field. 
  * Ensure the "Notebook access" toggle is enabled. 
  * The notebook code will then attempt to load this key. 

**4. Run the Notebook:** 
  * Execute the cells in the notebook sequentially. 
  * Be mindful of API rate limits. The notebook processes 99 skills/work activities with multiple prompt phrasings, leading to approximately 1,000 API requests. Adjust `time.sleep()` values in Step 3 of the notebook if needed for your specific model's limits. 
  * Runtime can be significant (e.g., ~2 hours with Gemma 3 1B on Colab) and can be reduced by using fewer prompt phrasings.

**5. Review Results:** 
 * The notebook will generate CSV files containing the full table of ratings and a summary table. These will be saved in your Colab environment, and you can download them from the file browser, which is advisable as they will be deleted once you end the session. 

## Important Considerations
* **DSPy Framework:** This notebook uses DSPy for its flexibility in switching between LLMs and for structured prompting. This has several advantages, including the ability to compare estimates between models as well as ensure the analysis can easily be updated as new models are developed.
* **API Keys & Model Choice:** You are responsible for obtaining and managing your API key. Performance and rate limits vary by model. 
* **API Usage & Costs:** Be aware of the number of requests (approx. 1,000 - 3,000) and any potential costs associated with your chosen API. 

## Disclaimer
I used Gemini (2.5 Pro Preview) when learning how to use DSPy, with help developing initial portions of the code and in editing. I take full responsibility for this notebook's content and accuracy.
