from flask import Blueprint

import controllers


product = Blueprint("product", __name__)


@product.route('/product', methods=['POST'])
def add_product_route():
    return controllers.add_product()

@product.route('/product', methods=['GET'])
def get_products_route():
    return controllers.get_all_products()

@product.route('/product/<uuid:product_id>', methods=['GET'])
def get_product_by_id_route(product_id):
    return controllers.get_product_by_id(product_id)

@product.route('/products/active', methods=['GET'])
def get_active_products_route():
    return controllers.get_active_products()

@product.route('/product/company/<uuid:company_id>', methods=['GET'])
def get_products_by_company_route(company_id):
    return controllers.get_products_by_company(company_id)

@product.route('/product/<uuid:product_id>', methods=['PUT'])
def update_product_by_id_route(product_id):
    return controllers.update_product_by_id(product_id)

@product.route('/product/<uuid:product_id>', methods=['DELETE'])
def delete_product_by_id_route(product_id):
    return controllers.delete_product_by_id(product_id)



