from flask import jsonify, request
from db import db
from models.warranty import Warranties
from models.product import Products

def add_warranty():
    post_data = request.form if request.form else request.get_json()

    fields = ['product_id', 'warranty_months']
    required_fields = ['product_id', 'warranty_months']

    values = {}
    for field in fields:
        field_data = post_data.get(field)
        if field in required_fields and not field_data:
            return jsonify({"message": f"{field} is required"}), 400
        values[field] = field_data
        
    product = db.session.query(Products).filter(Products.product_id == values['product_id']).first()
    if not product:
        return jsonify({"message": "product not found"}), 404

    new_warranty = Warranties(values['product_id'], values['warranty_months'])

    try:
        db.session.add(new_warranty)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create warranty"}), 400

    warranty = {
        "warranty_id": new_warranty.warranty_id,
        "product_id": new_warranty.product_id,
        "warranty_months": new_warranty.warranty_months
    }

    return jsonify({"message": "warranty created", "result": warranty}), 201


def get_all_warranties():
    query = db.session.query(Warranties).all()

    warranties_list = []
    for warranty in query:
        warranties_list.append({
            "warranty_id": warranty.warranty_id,
            "product_id": warranty.product_id,
            "warranty_months": warranty.warranty_months
        })

    return jsonify({"message": "warranties found", "results": warranties_list}), 200


def get_warranty_by_id(warranty_id):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    warranty_dict = {
        "warranty_id": warranty.warranty_id,
        "product_id": warranty.product_id,
        "warranty_months": warranty.warranty_months
    }

    return jsonify({"message": "warranty found", "result": warranty_dict}), 200


def update_warranty_by_id(warranty_id):
    post_data = request.form if request.form else request.get_json()
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    warranty.warranty_months = post_data.get('warranty_months', warranty.warranty_months)
    warranty.product_id = post_data.get('product_id', warranty.product_id)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update warranty"}), 400

    return get_warranty_by_id(warranty_id)


def delete_warranty_by_id(warranty_id):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    try:
        db.session.delete(warranty)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete warranty"}), 400

    return jsonify({"message": "warranty deleted"}), 200
