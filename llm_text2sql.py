from langchain_core.prompts import PromptTemplate
from llm import llm

TEXT2SQL_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""
You are an expert MySQL data analyst.

Database tables:
- inventory
- suppliers
- orders
- practitioners
- patient_assignments

Database schema:

inventory(
  inventory_id INT PRIMARY KEY,
  item_code VARCHAR,
  item_name VARCHAR,
  category VARCHAR,
  quantity_available INT,
  unit VARCHAR,
  reorder_level INT,
  max_stock_level INT,
  expiry_date DATE,
  storage_location VARCHAR
)

suppliers(
  supplier_id INT PRIMARY KEY,
  supplier_name VARCHAR,
  city VARCHAR,
  rating DECIMAL,
  active_status BOOLEAN
)

orders(
  order_id INT PRIMARY KEY,
  inventory_id INT,
  supplier_id INT,
  order_date DATE,
  ordered_quantity INT,
  received_quantity INT,
  order_status VARCHAR,
  total_cost DECIMAL
)

practitioners(
  practitioner_id INT PRIMARY KEY,
  full_name VARCHAR,
  specialization VARCHAR,
  availability_status VARCHAR
)

patient_assignments(
  assignment_id INT PRIMARY KEY,
  practitioner_id INT,
  patient_name VARCHAR,
  appointment_type VARCHAR,
  duration_minutes INT,
  assignment_date DATE
)

IMPORTANT:
- Use ONLY the column names given above
- Do NOT invent columns like item_id
- Generate ONLY a SELECT query
- Use proper JOINs when needed
- Do NOT explain anything
- No markdown
- Return only SQL

User question:
{question}
"""
)

def text_to_sql(question: str) -> str:
    prompt = TEXT2SQL_PROMPT.format(question=question)
    response = llm.invoke(prompt)
    return response.content.strip()
