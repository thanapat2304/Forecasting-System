def connect_aep_portal():
    return None
    
def execute_query_portal(query, params=None):
    connection = connect_aep_portal()
    if connection is None:
        return None
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    if query.strip().upper().startswith("SELECT"):
        result = cursor.fetchall()
    else:
        connection.commit()
        result = None
    cursor.close()
    connection.close()
    return result
    
def connect_aep_DB():
    return None