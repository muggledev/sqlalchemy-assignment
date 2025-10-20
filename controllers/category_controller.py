from flask import request, jsonify
from db import db
from models.category import Categories


def add_category():
    post_data = request.form if request.form else request.get_json()

    fields = ['category_name']
    required_fields = ['category_name']

    values = {}
    for field in fields:
        field_data = post_data.get(field)
        if field in required_fields and not field_data:
            return jsonify({"message": f"{field} is required"}), 400
        values[field] = field_data

    new_category = Categories(values['category_name'])

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create category"}), 400

    category = {
        "category_id": new_category.category_id,
        "category_name": new_category.category_name
    }

    return jsonify({"message": "category created", "result": category}), 201


def get_all_categories():
    categories = db.session.query(Categories).all()

    results = [{
        "category_id": c.category_id,
        "category_name": c.category_name
    } for c in categories]

    return jsonify({"message": "categories found", "results": results}), 200


def get_category_by_id(category_id):
    category = db.session.query(Categories).filter_by(category_id=category_id).first()

    if not category:
        return jsonify({"message": "category not found"}), 404

    result = {
        "category_id": category.category_id,
        "category_name": category.category_name
    }

    return jsonify({"message": "category found", "result": result}), 200


def update_category_by_id(category_id):
    post_data = request.form if request.form else request.get_json()
    category = db.session.query(Categories).filter_by(category_id=category_id).first()

    if not category:
        return jsonify({"message": "category not found"}), 404

    category.category_name = post_data.get('category_name', category.category_name)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update category"}), 400

    return get_category_by_id(category_id)


def delete_category_by_id(category_id):
    category = db.session.query(Categories).filter_by(category_id=category_id).first()

    if not category:
        return jsonify({"message": "category not found"}), 404

    try:
        db.session.delete(category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete category"}), 400

    return jsonify({"message": "category deleted"}), 200
