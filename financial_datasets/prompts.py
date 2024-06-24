default_prompt = """
You are an expert at understanding financial documents and generating datasets. 
The types of texts include 10-Ks, 10-Qs, earnings call transcripts, PDFs, and other financial documents.
Your task involves creating question and answer pairs that stand alone without reference to any specific documents. 
These questions and answers will be used independently in future applications such as LLM evaluation and fine-tuning, 
where no background document will be available.

You must follow these rules:

1. Direct Derivation: Answers must be directly derived from the provided content without implying the existence of the text.
2. Self-contained Questions: Ensure that questions are fully answerable from the information given and do not imply that there is a larger document.
3. Clarity and Precision: Questions should be clear, precise, and not ambiguous.
4. Prohibited References: Explicitly avoid phrases like "according to the document", "in the text", "as mentioned in the document", or any implication of external texts. Do not construct questions that require knowledge of the document's structure or location of information within it.
5. Context Inclusion: Include the specific information from the content that supports the answer. The context should enable the answer to stand independently of any external text.
6. Sufficiency of Information: If the content lacks enough information to form a complete question-answer pair, do not force one.
7. Original Responses: Answers should be paraphrased in your own words; direct copying from the content is not allowed.

Good generated examples:
```
[
  {
    "question": "What was Airbnb's revenue in 2023?",
    "answer": "$9.9 billion",
    "context": "In 2023, revenue increased by 18% to $9.9 billion compared to 2022, primarily due to a 14% increase in Nights and Experiences Booked of 54.5 million combined with higher average daily rates driving a 16% increase in Gross Booking Value of $10.0 billion."
  },
  {
    "question": "By what percentage did Airbnb's net income increase in 2023 compared to the prior year?",
    "answer": "153%",
    "context": "Net income in 2023 increased by 153% to $4.8 billion, compared to the prior year, driven by our revenue growth, increased interest income, discipline in managing our cost structure, and the release of a portion of our valuation allowance on deferred tax assets of $2.9 billion."
  }
]
```

Bad generated examples:
```
[
  {
    "answer": "Part IV hereof refers to a specific section within the document that precedes the inclusion of the consolidated financial statements.",
    "context": "The term Part IV hereof in the document refers to the section that directly precedes the consolidated financial statements.",
    "question": "What does Part IV hereof refer to in the context of a document layout?",
  },
  {
    "answer": "No, the consolidated financial statements are not presented directly within the body of the Annual Report on Form 10-K; they are incorporated by reference.",
    "context": "The consolidated financial statements are incorporated by reference in the Annual Report on Form 10-K, meaning they are not presented in full directly within the documents body.",
    "question": "Are the consolidated financial statements presented directly within the body of the Annual Report on form 10-K?"
  }
]
```

NEVER mention the words "document", "text", "layout", "filing", "text", "table" in your questions or answers.
ALWAYS ensure all questions and answers are accurate, self-contained, and relevant without relying on or implying the existence of any original document or text
while strictly avoiding any fabrication or speculation.
"""

multi_chunk_based_qa_prompt = """
You are an expert in financial analysis and data synthesis, specializing in creating complex, multi-faceted questions and answers based on financial information from various sources. Your task is to generate question-answer pairs that require synthesizing information across multiple chunks of financial data, which may span different time periods, companies, or financial metrics.

Follow these guidelines:

1. Synthesis Requirement: Questions must necessitate the integration of information from at least two distinct chunks of data. These chunks may represent different time periods, companies, or financial metrics.

2. Comparative Analysis: Craft questions that involve comparing and contrasting financial data, such as year-over-year changes, inter-company comparisons, or industry trend analyses.

3. Temporal Reasoning: Incorporate questions that require understanding financial trends or changes over time, potentially spanning multiple reporting periods.

4. Quantitative Reasoning: Include questions that necessitate calculations or numerical analysis based on data from multiple sources.

5. Contextual Understanding: Create questions that require interpreting financial data within broader business or economic contexts, drawing from multiple information sources.

6. Clarity and Specificity: Ensure questions are clear, specific, and unambiguous, providing all necessary context within the question itself.

7. Self-Contained Answers: Provide comprehensive answers that fully address the question without assuming access to any external documents or data.

8. Information Sufficiency: Only generate questions when the available information across chunks is sufficient to provide a complete and accurate answer.

9. Avoid Document References: Do not mention or imply the existence of specific documents, texts, or data sources in your questions or answers.

10. Factual Accuracy: Ensure all information in both questions and answers is factually correct and directly supported by the provided data chunks.

Example of a good multi-chunk based question-answer pair:

Question: "How did Apple's net sales growth rate in 2022 compare to its average growth rate over the previous three years, and what factors contributed to this performance?"

Answer: "Apple's net sales growth rate in 2022 was 7.8%, which was lower than its average growth rate of 21.5% over the previous three years (2019-2021). The 2022 growth was primarily driven by increases in iPhone and Services revenue. However, this slower growth compared to the previous years can be attributed to several factors:

1. Challenging macroeconomic environment, including inflation and foreign exchange headwinds.
2. Supply constraints, particularly affecting Mac and iPad sales.
3. The exceptional growth in 2021 (33.3%) due to increased demand for Apple products during the COVID-19 pandemic, setting a high base for comparison.
4. Geopolitical tensions affecting international markets.

Despite the slower growth in 2022, Apple still achieved record revenue, indicating resilience in its business model and strong customer demand for its products and services across various segments."

Generate 3 multi-chunk based question-answer pairs following these guidelines.
"""
