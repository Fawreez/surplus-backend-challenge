from wrapper.db import *

def get_image_from_db(image_id):
    select_query = """SELECT * FROM image WHERE id = %s"""
    image = fetch_query(select_query, image_id, get="one")
    return image


def add_image_to_db(image_data):
    name = image_data.get("name")
    image_file = image_data.get("image_file")
    enable = image_data.get("enable")

    insert_query = """INSERT INTO image (name, file, enable) VALUES (%s, %s, %s)"""
    arguments = (name, image_file, enable)

    response = execute_query(insert_query, arguments)

    return response


def modify_image(image_data):
    image_id = image_data.get("image_id")
    name = image_data.get("name")
    image_file = image_data.get("image_file")
    enable = image_data.get("enable")

    update_query = """UPDATE image SET name = %s,
                                       file = %s,
                                       enable = %s
                                       WHERE
                                       id = %s"""

    arguments = (name, image_file, enable, image_id)

    response = execute_query(update_query, arguments)

    return response


def remove_image(image_id):
    response = {
        "success": True,
        "message": "Success"
    }

    # Remove image from image table
    delete_image_query = """DELETE FROM image WHERE id = %s"""
    delete_image_response = execute_query(delete_image_query, image_id)
    if not delete_image_response.get("success"):
        return delete_image_response

    # Delete data from product_image table
    delete_product_image_query = """DELETE FROM product_image WHERE image_id = %s"""
    delete_product_image_response = execute_query(delete_product_image_query, image_id)
    if not delete_product_image_response.get("success"):
        return delete_product_image_response

    return response
