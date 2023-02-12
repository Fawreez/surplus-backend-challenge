from wrapper.db import *

def get_category_from_db(category_id=None, category_name=None):
    if category_id:
        select_query = """SELECT * FROM category WHERE id = %s"""
        category = fetch_query(select_query, category_id, get="one")
        return category
    elif category_name:
        select_query = """SELECT * FROM category WHERE name = %s"""
        category = fetch_query(select_query, category_name, get="one")
        return category
    else:
        return None


def add_category_to_db(category_name):
    enable = True
    category_name = category_name.lower()

    insert_query = """INSERT INTO category (name, enable) VALUES (%s, %s)"""
    response = execute_query(insert_query, (category_name, enable))

    return response

