

### Defines a generic SQL query function to execute SELECT queries
def sql_explore(q, cnn):
    """
    q : the SQL query as text
    cnn : the connection parameter
    """
    errors_list = []
    elem = []
    with cnn.cursor() as curs:
        try:   
            ### Décommenter pour nouvelle exécution
            curs.execute(q)
            elem = curs.fetchall()
            cnn.commit()
        except Exception as e:
            cnn.rollback()
            print(e)
            errors_list.append(e)
    return [elem, errors_list]        




### Defines a generic SQL query function to execute DDL queries
def sql_execute(q, cnn):
    """
    q : the SQL query as text
    cnn : the connection parameter


    errors_list = []
    with cnn.cursor() as curs:
        try:   
            ### Décommenter pour nouvelle exécution
            curs.execute(q)
            cnn.commit()
        except Exception as e:            
            cnn.rollback()
            errors_list.append(e)
    return [errors_list]      
"""