from flask import jsonify, abort, make_response, request
from app import app, db
from app.models import User, Department, EquipmentBrand, EquipmentType, EquipmentFault, RepairCompany, EquipmentRepair
from datetime import datetime
import json
from sqlalchemy import text
from app.main.forms import EquipmentBrand

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/repair/api/v1.0/equipment_repairs/add', methods=['POST'])
def new_equipment_repair():
    data = request.form
    data_dict = data.to_dict()
    print(data_dict)
    repair_date = data_dict.get('repair_date', datetime.now().strftime("%Y-%m-%d %H:%M"))
    dept_code = data_dict.get('dept_code')
    repair_registrant = data_dict.get('repair_registrant')
    brand_code = data_dict.get('brand_code')
    type_code = data_dict.get('type_code')
    equipment_code = data_dict.get('equipment_code')
    fault_code = data_dict.get('fault_code')
    com_code = data_dict.get('com_code')
    # repair_man = data_dict.get('repair_man')
    # repair_confirm_date = data_dict.get('repair_confirm_date')
    # repair_return_date = request.json.get('repair_return_date')
    # repair_return_man = request.json.get('repair_return_man')
    # equipment_return_date = request.json.get('equipment_return_date')
    # equipment_return_man = request.json.get('equipment_return_man')
    repair_status = 0
    if dept_code is None or equipment_code is None or brand_code is None \
            or type_code is None or fault_code is None or com_code is None:
        abort(414)  # missing arguments
    if EquipmentRepair.query.filter_by(equipment_code=equipment_code, fault_code=fault_code,
                                       com_code=com_code).first() is not None:
        abort(400)  # existing user
    row = EquipmentRepair(repair_date=repair_date, dept_code=dept_code, repair_registrant=repair_registrant,
                          brand_code=brand_code, type_code=type_code, equipment_code=equipment_code,
                          fault_code=fault_code, com_code=com_code, repair_status=repair_status)
    db.session.add(row)
    db.session.commit()
    return myreponse(row.to_json())


@app.route('/repair/api/v1.0/equipment_repairs/edit/<int:id>', methods=['POST'])
def update_equipment_repair(id):
    row = EquipmentRepair.query.filter_by(id=id).first()
    if row is None:
        abort(400)  # existing user

    data = request.form
    data_dict = data.to_dict()
    print(data_dict)
    repair_date = data_dict.get('repair_date', datetime.now())
    dept_code = data_dict.get('dept_code')
    repair_registrant = data_dict.get('repair_registrant')
    brand_code = data_dict.get('brand_code')
    type_code = data_dict.get('type_code')
    equipment_code = data_dict.get('equipment_code')
    fault_code = data_dict.get('fault_code')
    com_code = data_dict.get('com_code')
    # repair_man = request.json.get('repair_man')
    # repair_return_date = request.json.get('repair_return_date')
    # repair_return_man = request.json.get('repair_return_man')
    # equipment_return_date = request.json.get('equipment_return_date')
    # equipment_return_man = request.json.get('equipment_return_man')
    repair_status = 0
    if dept_code is None or equipment_code is None or brand_code is None \
            or type_code is None or fault_code is None or com_code is None:
        abort(414)  # missing arguments
    if EquipmentRepair.query.filter_by(equipment_code=equipment_code, fault_code=fault_code,
                                       com_code=com_code).first() is not None:
        abort(400)  # existing user
    row.repair_date = repair_date
    row.dept_code = dept_code
    row.repair_registrant = repair_registrant
    row.brand_code = brand_code
    row.type_code = type_code
    row.equipment_code = equipment_code
    row.fault_code = fault_code
    row.com_code = com_code
    # row.repair_man = repair_man
    # row.repair_status = repair_status
    # row.repair_return_date = repair_return_date
    # row.repair_return_man = repair_return_man
    # row.equipment_return_date = equipment_return_date
    # row.equipment_return_man = equipment_return_man
    db.session.commit()
    return myreponse(row.to_json())


@app.route('/repair/api/v1.0/equipment_repairs', methods=['GET'])
def get_equipment_repairs():
    querystr = request.args.get("querystr", '')
    offset = request.args.get("offset", '0')
    limit = request.args.get("limit", '10')
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'desc')
    sidePagination = request.args.get('sidePagination', 'client')

    wherestr = "1=1"
    if querystr:
        print(querystr)
        dict = json.loads(querystr)
        for key, value in dict.items():
            if isinstance(value, list):  # 日期字段处理
                if value[0] and value[1]:
                    wherestr = wherestr + ' and ' + key + '>=' + "'" + value[0] + "'" + ' and ' + key + '<=' + "'" + value[1] + "'"
            elif key in ['equipment_code', 'repair_registrant', 'repair_man', 'repair_return_man', 'equipment_return_man']:
                wherestr = wherestr + ' and ' + key + " like " + "'%" + value + "%'"
            else:
                wherestr = wherestr + ' and ' + key + "=" + "'" + value + "'"
    print(wherestr)

    change = {'repair_department': 'dept_code', 'equipment_brand': 'brand_code', 'equipment_type': 'type_code',
              'equipment_fault': 'fault_code', 'repair_company': 'com_code'}
    if sort in ['repair_department', 'equipment_brand', 'equipment_type', 'equipment_fault', 'repair_company']:
        orderbystr = change[sort] + " " + order
    else:
        orderbystr = sort + " " + order
    print(orderbystr)
    # 分页paginate的参数page，是第几页，而offset是记录的偏移量，需要转换
    # 表格标题排序，根据table提交的信息进行排序，否则排序无效
    if sidePagination == 'server':
        page = (int(offset) // int(limit)) + 1
        pagination = EquipmentRepair.query.filter(text(wherestr)).order_by(text(orderbystr)).paginate(page, int(limit), False)
        rows = pagination.items
        total = pagination.total
    else:
        rows = EquipmentRepair.query.filter(text(wherestr)).order_by(text(orderbystr))
        total = EquipmentRepair.query.filter(text(wherestr)).order_by(text(orderbystr)).count()
    print(total)
    #rows = EquipmentRepair.query.filter(text(wherestr)).order_by(text(orderbystr)).limit(int(limit)).offset(int(offset))
    #total = EquipmentRepair.query.filter(text(wherestr)).count()

    if not rows:
        abort(400)
    data = [row.to_json() for row in rows]
    # data = get_data_by_model(EquipmentRepair)
    return myreponse(data, total)


@app.route('/repair/api/v1.0/equipment_repairs/delete/<int:id>', methods=['POST'])
def delete_equipment_repair(id):
    row = EquipmentRepair.query.filter_by(id=id).first()
    if row is None:
        abort(404)  # existing user

    db.session.delete(row)
    db.session.commit()
    return myreponse(row.to_json())


@app.route('/repair/api/v1.0/users', methods=['GET'])
def get_users():
    return myreponse(get_data_by_model(User))


@app.route('/repair/api/v1.0/users/<user_id>', methods=['GET'])
def get_user(user_id):
    print(user_id)
    status = 200
    msg = ''
    user = User.query.filter_by(usercode=user_id).first()
    if user is None:
        abort(400)
    return myreponse(user.to_json())


@app.route('/repair/api/v1.0/users', methods=['POST'])
def new_user():
    usercode = request.json.get('usercode')
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(usercode=usercode).first() is not None:
        abort(400)  # existing user
    user = User(usercode=usercode, username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return myreponse(user.to_json())


@app.route('/repair/api/v1.0/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.filter_by(usercode=user_id).first()
    if user is None:
        abort(404)  # existing user

    usercode = request.json.get('usercode')
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    user.usercode = usercode
    user.username = username
    user.hash_password(password)
    db.session.commit()
    return myreponse(user.to_json())


def get_data_by_code(model, code):
    row = model.query.filter_by(code=code).first()
    if row is None:
        abort(400)
    return row.to_json()


def get_data_by_model(model):
    rows = model.query.all()
    # total = model.query.count()
    if not rows:
        abort(400)
    data = [row.to_json() for row in rows]
    return data


def update_data_by_code(model, code):
    row = model.query.filter_by(code=code).first()
    if row is None:
        abort(400)  # existing user

    code = request.json.get('code')
    name = request.json.get('name')
    if code is None or name is None:
        abort(414)  # missing arguments
    row.code = code
    row.name = name
    db.session.commit()
    return row.to_json()


def add_data_by_model(model):
    code = request.json.get('code')
    name = request.json.get('name')
    if code is None or name is None:
        abort(414)  # missing arguments
    if model.query.filter_by(code=code).first() is not None:
        abort(400)  # existing user
    row = model(code=code, name=name)
    db.session.add(row)
    db.session.commit()
    return row.to_json()


def delete_data_by_code(model, code):
    row = model.query.filter_by(code=code).first()
    if row is None:
        abort(400)  # existing user

    db.session.delete(row)
    db.session.commit()
    return row.to_json()


def myreponse(data='success', total=0):
    return jsonify({'status': 201, 'total': total, 'rows': data, 'msg': ''})


@app.route('/repair/api/v1.0/departments/<code>', methods=['GET'])
def get_department(code):
    return myreponse(get_data_by_code(Department, code))


@app.route('/repair/api/v1.0/departments', methods=['GET'])
def get_departments():
    return myreponse(get_data_by_model(Department))


@app.route('/repair/api/v1.0/departments/<code>', methods=['PUT'])
def update_department(code):
    return myreponse(update_data_by_code(Department, code))


@app.route('/repair/api/v1.0/departments', methods=['POST'])
def add_department():
    return myreponse(add_data_by_model(Department))


@app.route('/repair/api/v1.0/departments/<code>', methods=['DELETE'])
def delete_department(code):
    if EquipmentRepair.query.filter_by(dept_code=code).first() is not None:
        abort(400)
    return myreponse(delete_data_by_code(Department, code))


@app.route('/repair/api/v1.0/equipment_brands/<code>', methods=['GET'])
def get_equipment_brand(code):
    return myreponse(get_data_by_code(EquipmentBrand, code))


@app.route('/repair/api/v1.0/equipment_brands', methods=['GET'])
def get_equipment_brands():
    return myreponse(get_data_by_model(EquipmentBrand))


@app.route('/repair/api/v1.0/equipment_brands/<code>', methods=['PUT'])
def update_equipment_brand(code):
    return myreponse(update_data_by_code(EquipmentBrand, code))


@app.route('/repair/api/v1.0/equipment_brands', methods=['POST'])
def add_equipment_brand():
    return myreponse(add_data_by_model(EquipmentBrand))


@app.route('/repair/api/v1.0/equipment_brands/<code>', methods=['DELETE'])
def delete_equipment_brand(code):
    if EquipmentRepair.query.filter_by(brand_code=code).first() is not None:
        abort(400)
    return myreponse(delete_data_by_code(EquipmentBrand, code))


@app.route('/repair/api/v1.0/equipment_types/<code>', methods=['GET'])
def get_equipment_type(code):
    return myreponse(get_data_by_code(EquipmentType, code))


@app.route('/repair/api/v1.0/equipment_types', methods=['GET'])
def get_equipment_types():
    return myreponse(get_data_by_model(EquipmentType))


@app.route('/repair/api/v1.0/equipment_types/<code>', methods=['PUT'])
def update_equipment_type(code):
    return myreponse(update_data_by_code(EquipmentType, code))


@app.route('/repair/api/v1.0/equipment_types', methods=['POST'])
def add_equipment_type():
    return myreponse(add_data_by_model(EquipmentType))


@app.route('/repair/api/v1.0/equipment_types/<code>', methods=['DELETE'])
def delete_equipment_type(code):
    if EquipmentRepair.query.filter_by(type_code=code).first() is not None:
        abort(400)
    return myreponse(delete_data_by_code(EquipmentType, code))


@app.route('/repair/api/v1.0/equipment_faults/<code>', methods=['GET'])
def get_equipment_fault(code):
    return myreponse(get_data_by_code(EquipmentFault, code))


@app.route('/repair/api/v1.0/equipment_faults', methods=['GET'])
def get_equipment_faults():
    return myreponse(get_data_by_model(EquipmentFault))


@app.route('/repair/api/v1.0/equipment_faults/<code>', methods=['PUT'])
def update_equipment_fault(code):
    return myreponse(update_data_by_code(EquipmentFault, code))


@app.route('/repair/api/v1.0/equipment_faults', methods=['POST'])
def add_equipment_fault():
    return myreponse(add_data_by_model(EquipmentFault))


@app.route('/repair/api/v1.0/equipment_faults/<code>', methods=['DELETE'])
def delete_equipment_fault(code):
    if EquipmentRepair.query.filter_by(fault_code=code).first() is not None:
        abort(400)
    return myreponse(delete_data_by_code(EquipmentFault, code))


@app.route('/repair/api/v1.0/repair_companys/<code>', methods=['GET'])
def get_repair_company(code):
    return myreponse(get_data_by_code(RepairCompany, code))


@app.route('/repair/api/v1.0/repair_companys', methods=['GET'])
def get_repair_companys():
    return myreponse(get_data_by_model(RepairCompany))


@app.route('/repair/api/v1.0/repair_companys/<code>', methods=['PUT'])
def update_repair_company(code):
    return myreponse(update_data_by_code(RepairCompany, code))


@app.route('/repair/api/v1.0/repair_companys', methods=['POST'])
def add_repair_company():
    return myreponse(add_data_by_model(RepairCompany))


@app.route('/repair/api/v1.0/repair_companys/<code>', methods=['DELETE'])
def delete_repair_company(code):
    if EquipmentRepair.query.filter_by(com_code=code).first() is not None:
        abort(400)
    return myreponse(delete_data_by_code(RepairCompany, code))
