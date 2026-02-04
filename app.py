from db import get_connection
from llm_text2sql import text_to_sql
from sql_validator import validate_sql
from llm_validator import validate_and_explain


def query_db(user_query: str):
    # LLM #1 → SQL
    sql_query = text_to_sql(user_query)

    # Validate SQL
    validate_sql(sql_query)

    # Execute SQL
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)

    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    conn.close()

    # LLM #2 → Explanation
    explanation = validate_and_explain(
        user_query,
        sql_query,
        rows
    )

    return {
        "user_query": user_query,
        "generated_sql": sql_query,
        "columns": columns,
        "rows": rows,
        "explanation": explanation
    }


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type exit): ")
        if q.lower() == "exit":
            break

        result = query_db(q)
        print("\nSQL:", result["generated_sql"])
        print("Rows:", result["rows"])
        print("\nExplanation:", result["explanation"])
