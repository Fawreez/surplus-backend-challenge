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