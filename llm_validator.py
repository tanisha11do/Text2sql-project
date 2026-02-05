from langchain_core.prompts import PromptTemplate
from llm import llm

# answer_validator =""" You are an intelligent, context-aware AI assistant.

# Your task is to analyze the provided CONTEXT and the USER QUERY thoroughly before generating a response.

# Instructions:
# 1. Carefully read and understand the full context. Do not ignore any relevant details.
# 2. Identify what the user is actually asking, including implicit requirements.
# 3. If the query involves data retrieval, analysis, or computation:
#    - Generate the appropriate SQL query if required
#    - Infer results logically from the context if actual execution is not possible
# 4. Present outputs in the most suitable format:
#    - Use clear tables when displaying structured data
#    - Use formatted SQL blocks when sharing queries
#    - Combine text explanations with tables when helpful
# 5. Ensure correctness, consistency, and clarity in all outputs.
# 6. If information is missing or ambiguous, make reasonable assumptions and clearly mention them.
# 7. Maintain a friendly, conversational, and professional tone — explain results simply without being verbose.
# 8. Do not hallucinate data. Base all outputs strictly on the provided context.

# Output Guidelines:
# - Start with a brief, friendly explanation of what you found or did
# - Follow with tables and/or SQL outputs as needed
# - End with a short helpful note or insight if relevant

# Inputs:
# CONTEXT:
# {context}

# USER QUERY:
# {query}

# Generate the best possible response that satisfies the user's request.
#  """


test = """
User asked:
{question}

Generated SQL:
{sql}

SQL Result:
{result}

Task:
1. Check if SQL result answers the question
2. Give the result in simple English just the names not table

Rules:
1. Be specific to use only the required fields to be retireved based on the user question

Answer clearly.
"""
VALIDATION_PROMPT = PromptTemplate(
    input_variables=["question","sql", "result"],
    template= test
)

def validate_and_explain(question:str, sql:str,  result) -> str:
    prompt = VALIDATION_PROMPT.format(
        question=question,
        sql = sql,
        result=result
    )
    response = llm.invoke(prompt)
    return response.content.strip()

