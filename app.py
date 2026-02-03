from db import get_connection
from llm_text2sql import text_to_sql
#from llm_validator import validate_and_explain
from sql_validator import validate_sql


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
    conn.close()

    # LLM #2 → Validate & explain
    #final_answer = validate_and_explain(user_query, sql_query, rows)

    return {
        "generated_sql": sql_query,
        "sql_result": rows,
        #"final_answer": final_answer
    }
