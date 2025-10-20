from flask import Blueprint
import controllers

warranty = Blueprint("warranty", __name__)

@warranty.route('/warranty', methods=['POST'])
def add_warranty_route():
    return controllers.add_warranty()

@warranty.route('/warranty', methods=['GET'])
def get_all_warranties_route():
    return controllers.get_all_warranties()

@warranty.route('/warranty/<uuid:warranty_id>', methods=['GET'])
def get_warranty_by_id_route(warranty_id):
    return controllers.get_warranty_by_id(warranty_id)

@warranty.route('/warranty/<uuid:warranty_id>', methods=['PUT'])
def update_warranty_by_id_route(warranty_id):
    return controllers.update_warranty_by_id(warranty_id)

@warranty.route('/warranty/<uuid:warranty_id>', methods=['DELETE'])
def delete_warranty_by_id_route(warranty_id):
    return controllers.delete_warranty_by_id(warranty_id)
