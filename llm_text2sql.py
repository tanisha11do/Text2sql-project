

llm = pipeline("text2text-generation", model="google/flan-t5-small")

SCHEMA = """
Tables:
inventory(item_id, item_name, quantity, unit)
suppliers(supplier_id, supplier_name, city)
orders(order_id, item_id, supplier_id, order_date, quantity)
"""

def text_to_sql(user_query: str) -> str:
    prompt = f"""
You are an expert SQL assistant.

Generate a MySQL SELECT query using ONLY these tables:
{SCHEMA}

Rules:
- MySQL syntax
- Only SELECT queries
- Correct joins
- No assumptions beyond schema

Question:
{user_query}
"""
    response = llm(prompt, max_length=200)
    return response[0]["generated_text"]
