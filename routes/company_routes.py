from flask import Blueprint

import controllers


company = Blueprint("company", __name__)


@company.route('/company', methods=['POST'])
def add_company_route():
    return controllers.add_company()

@company.route('/company', methods=['GET'])
def get_companies_route():
    return controllers.get_companies()

@company.route('/company/<uuid:company_id>', methods=['GET'])
def get_company_by_id_route(company_id):
    return controllers.get_company_by_id(company_id)

@company.route('/company/<uuid:company_id>', methods=['PUT'])
def update_company_by_id_route(company_id):
    return controllers.update_company_by_id(company_id)

@company.route('/company/<uuid:company_id>', methods=['DELETE'])
def delete_company_by_id_route(company_id):
    return controllers.delete_company_by_id(company_id)
