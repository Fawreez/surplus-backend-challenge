from wrapper.db import *
import uuid


def add_product(product_data):
    category_name = product_data.get("category")

    default_response = {
        "success": True,
        "message": "Success"
    }

    # Get category_id
    category = get_category_from_db(category_name=category_name)
    if category:
        category_id = category.get("id")
    else:
        category_id = add_category_to_db(category_name).get("last_id")

    # Insert product data into product table in db
    product_response = add_product_to_db(product_data)
    if not product_response.get("success"):
        return product_response
    product_id = product_response.get("last_id")

    # Insert product and category id to category_product table
    category_product_query = """INSERT INTO category_product (product_id, category_id) VALUES (%s, %s)"""
    arguments = (product_id, category_id)
    category_product_response = execute_query(category_product_query, arguments)
    if not category_product_response.get("success"):
        return category_product_response

    return default_response


def add_product_to_db(product_data):
    name = product_data.get("name")
    description = product_data.get("description")
    enable = product_data.get("enable")

    insert_query = """INSERT INTO product (name, description, enable) VALUES(%s, %s, %s);"""
    arguments = (name, description, enable)
    insert_response = execute_query(insert_query, arguments)
    print(insert_response)
    return insert_response



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