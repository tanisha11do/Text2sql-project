from langchain_core.prompts import PromptTemplate
from llm import llm

VALIDATION_PROMPT = PromptTemplate(
    input_variables=["question", "sql", "result"],
    template="""
User asked:
{question}

Generated SQL:
{sql}

SQL Result:
{result}

Task:
1. Check if SQL result answers the question
2. Give the result in simple English

Rules:
2. Do not give suggested fix
3. Be specific to use only the required fields to be retireved based on the user question

Answer clearly.
"""
)

def validate_and_explain(question, sql, result):
    prompt = VALIDATION_PROMPT.format(
        question=question,
        sql=sql,
        result=result
    )
    response = llm.invoke(prompt)
    return response.content.strip()

