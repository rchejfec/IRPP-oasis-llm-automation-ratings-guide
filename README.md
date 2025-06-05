# Assessing the automatability of OaSIS' skills and work activities using Large Language Models  
#### *A guide to replicating Oschinski & Walia (2025) for researchers and governments using DSPy*
<br>

The IRPP recently published [Harnessing Generative AI: Navigating the Transformative Impact on Canada's Labour Market](https://irpp.org/research-studies/harnessing-generative-ai/) by Matthias Oschinki and Ruhani Walia. In it, the authors leverage OpenAI's ChatGPT to explore the likelihood of Canadian occupations to be automated given advancements in generative AI in the medium term.

The first part of their study involves asking two different OpenAI models to rate the automatibility of 71 skills and work activities using 12 different phrasings and averaging the results. These skills and work activities come from
ESDC's 2023 OaSIS framework which breaks down Canadian occupations into their major elements. This mimics previous studies on the topic, which have typically surveyed experts rather than LLMs. In both cases, these ratings are used to explore the automation risk of occupations, by aggregating the score of the occupation's most relevant elements.

The following document recreates the first part of the study. The goal is to provide interested researchers and government officials a starting place on which they can build their own analysis. One of the biggest advantages of this approach is that, compared with alternatives, it is significantly cheaper, simpler, and more flexible to changing circumstances.

Ratings from LLMs don't need to be more accurate (or even as accurate) as those from experts to be useful. These types of exercises are often meant to inform rather than predict, serving as a starting point for further research or devicing a government strategy. Given these tools' impressive ability for processing semantic information and pattern recognition, coupled with the fact that they have been trained on unprecedentally large amounts of data, they are particularly well suited for these types of tasks.

Even if you don't think that LLMs are capable of reasoning through the implications of these questions, and rather act as some sort of stochastic parrot, it would be reasonable to expect LLM ratings to be similar to those of experts (and indeed studies find considerable correlations), as those experts likely wrote the literature that is informing the LLM's answers. While hallucinations are still a risk, reports show new models do so considerably less often and there are steps that can be taken to try to minimize their impact on research. Plus, it's reasonable to expect models to keep getting better, meaning these estimates could become more useful over time without the need for significant changes.

Still, there's a lot of exciting, valuable work to be done here - from validating emerging methodologies like this one, to improving upon them and developing new approaches. I hope this notebook can help showcase how easy it is to start incorporating LLMs into your research, in transparent, verifiable, and replicable ways.

If you haven't already, I recommend you read the full paper (linked above) before you continue. There you'll find a lot more details on their methodology, as well as their findings and their recommendations.

#### A few notes

- This notebook uses DSPy - instead of the ChatGPT API - because it allows users to easily switch between LLMs with minimal code changes. DSPy is a framework for writing programs that use large language models, and with it we can write code that systematically prompts an LLM and processes its results in a structured way, without specifying the model or its provider. This has several advantages, including the ability to compare estimates between models as well as ensure the analysis can easily be updated as new models are developed.
- You'll have to pick a model and get an API key. There are a number of free versions available, though they are often subject to tighter limits or are considerably worse performing that the more advanced versions. In either case, you'll have to be mindful of the models specifications, like the number of alloted daily requests and requests per minute. In my tests, the code below will make roughly 1,100 requests in total per run (but theoreritcally up to 3,000 if there are latency issues). Request per minute will largely depend on the speed of your model and internet connection, but to be extra safe, you can modify the value of `time.sleep` in part # to match the models requirements.
- Using Gemma 3 1B, a fairly lightweight fast model with generous limits, it took Google Colab close to two hours to go through all 99 skills and work activities. Runtime can be reduced by using fewer prompt phrasings.
