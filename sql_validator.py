FORBIDDEN = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE"]

def validate_sql(sql: str):
    sql_upper = sql.upper()
    for word in FORBIDDEN:
        if word in sql_upper:
            raise ValueError("Unsafe SQL detected")
    if not sql_upper.strip().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed")
    return True
