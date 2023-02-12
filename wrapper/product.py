from wrapper.db import *
from wrapper.image import *
from wrapper.category import *
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


def get_product(product_id):
    response = {
        "success": True,
        "message": "Success"
    }
    
    # Get product info from db
    product = get_product_from_db(product_id)
    if not product:
        response["success"] = False
        response["message"] = f"product with the porduct id {product_id} not found"
        return response

    # Get product categories from db
    categories = get_product_categories_from_db(product_id)

    # Get product images from db
    images = get_product_images_from_db(product)

    response["data"] = {
            "product": product,
            "categories": categories,
            "images": images
        }

    return response


def modify_product(product_data):
    product_id = product_data.get("product_id")
    name = product_data.get("name")
    description = product_data.get("description")
    enable = product_data.get("enable")

    update_query = """UPDATE product SET name = %s,
                                         description = %s,
                                         enable = %s
                                         WHERE
                                         id = %s"""
    arguments = (name, description, enable, product_id)

    update_response = execute_query(update_query, arguments)

    return update_response


def remove_product(product_id):
    response = {
        "success": True,
        "message": "Success"
    }

    # Delete data from product table
    delete_product_query = """DELETE FROM product WHERE id = %s"""
    delete_product_response = execute_query(delete_product_query, product_id)
    if not delete_product_response.get("success"):
        return delete_product_response

    # Delete data from category_product table
    delete_category_product_query = """DELETE FROM category_product WHERE product_id = %s"""
    delete_category_product_response = execute_query(delete_category_product_query, product_id)
    if not delete_category_product_response.get("success"):
        return delete_category_product_response

    # Delete data from product_image table
    delete_product_image_query = """DELETE FROM product_image WHERE product_id = %s"""
    delete_product_image_response = execute_query(delete_product_image_query, product_id)
    if not delete_product_image_response.get("success"):
        return delete_product_image_response

    return response


def add_product_to_db(product_data):
    name = product_data.get("name")
    description = product_data.get("description")
    enable = product_data.get("enable")

    insert_query = """INSERT INTO product (name, description, enable) VALUES(%s, %s, %s);"""
    arguments = (name, description, enable)
    insert_response = execute_query(insert_query, arguments)
    print(insert_response)
    return insert_response


def get_product_from_db(product_id):
    select_query = """SELECT * FROM product WHERE id = %s"""
    product = fetch_query(select_query, product_id, get="one")

    return product


def get_product_categories_from_db(product_id):
    categories = []

    select_query = """SELECT * FROM category_product WHERE product_id = %s"""
    category_ids = fetch_query(select_query, product_id)

    if not category_ids:
        return categories

    for category_id in category_ids:
        category = get_category_from_db(category_id=category_id.get("category_id"))
        categories.append(category)

    return categories


def get_product_images_from_db(product_id):
    images = []

    select_query = """SELECT * FROM product_image WHERE product_id = %s"""
    image_ids = fetch_query(select_query, product_id)

    if not image_ids:
        return images

    for image_id in image_ids:
        image = get_image_from_db(image_id.get("image_id"))
        images.append(image)

    return images
