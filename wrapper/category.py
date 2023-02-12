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


def modify_category(category_data):
    category_id = category_data.get("category_id")
    name = category_data.get("name")
    enable = category_data.get("enable")

    update_query = """UPDATE image SET name = %s,
                                       enable = %s
                                       WHERE
                                       id = %s"""

    arguments = (name, enable, category_id)

    response = execute_query(update_query, arguments)

    return response


def remove_category(category_id):
    response = {
        "success": True,
        "message": "Success"
    }

    # Remove category from category table
    delete_category_query = """DELETE FROM category WHERE id = %s"""
    delete_category_response = execute_query(delete_category_query, category_id)
    if not delete_category_response.get("success"):
        return delete_category_response

    # Delete data from category_product table
    delete_category_product_query = """DELETE FROM category_product WHERE category_id = %s"""
    delete_category_product_response = execute_query(delete_category_product_query, category_id)
    if not delete_category_product_response.get("success"):
        return delete_category_product_response

    return response
