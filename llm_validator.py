

llm = pipeline("question-answering", model="google/flan-t5-small")

def validate_and_explain(user_query, sql_query, sql_result):
    result_text = "\n".join([str(row) for row in sql_result])

    prompt = f"""
User question:
{user_query}

SQL query:
{sql_query}

SQL result:
{result_text}

Tasks:
1. Verify whether SQL result answers the user question.
2. If yes, explain clearly.
3. If no, say what is missing.
"""
    response = llm(prompt, max_length=250)
    return response[0]["generated_text"]
