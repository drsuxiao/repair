from passlib.apps import custom_app_context as pwd_context
from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    usercode = db.Column(db.String(10), unique=True, index=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def to_json(self):
        """
        完成User数据模型到JSON格式化的序列化字典转换
        """
        json_user = {
            'id': self.id,
            'usercode': self.usercode,
            'username': self.username,
            'password': self.password_hash
        }
        return json_user

# 日期统一更为字符串类型保存，方便比较
class EquipmentRepair(db.Model):
    __tablename__ = 'equipment_repair'
    id = db.Column(db.Integer, primary_key=True)
    repair_date = db.Column(db.String(20), default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    # 外键，和department表对应
    dept_code = db.Column(db.String(10), db.ForeignKey('department.code'))   # 报修科室
    repair_registrant = db.Column(db.String(10))  # 报修人
    # equipment_brand = db.Column(db.String(10))  # 设备品牌
    brand_code = db.Column(db.String(10), db.ForeignKey('equipment_brand.code'))  # 设备品牌
    # equipment_type = db.Column(db.String(10))   # 设备类型
    type_code = db.Column(db.String(10), db.ForeignKey('equipment_type.code'))   # 设备类型
    equipment_code = db.Column(db.String(10))   # 设备编号
    # equipment_fault = db.Column(db.String(50))  # 设备故障
    fault_code = db.Column(db.String(10), db.ForeignKey('equipment_fault.code'))  # 设备故障
    # repair_company = db.Column(db.String(30))  # 维修公司
    com_code = db.Column(db.String(10), db.ForeignKey('repair_company.code'))  # 维修公司
    repair_man = db.Column(db.String(10))  # 维修人
    repair_confirm_date = db.Column(db.String(20))  # 维修确认日期
    repair_return_date = db.Column(db.String(20))  # 维修归还日期
    repair_return_man = db.Column(db.String(10))  # 维修归还人
    equipment_return_date = db.Column(db.String(20))  # 设备归还科室日期
    equipment_return_man = db.Column(db.String(10))  # 设备归还科室人
    repair_status = db.Column(db.Integer)  # 维修状态  修好，修不好，正常

    def to_json(self):
        """
        完成EquipmentRepair数据模型到JSON格式化的序列化字典转换
        """
        json_equipment_repair = {
            'id': self.id,
            'repair_date': self.repair_date,
            'dept_code': self.dept_code,  # 科室编码
            'repair_department': self.department.name,  # 科室名称
            'repair_registrant': self.repair_registrant,
            'brand_code': self.brand_code,
            'equipment_brand': self.equipment_brand.name,
            'type_code': self.type_code,
            'equipment_type': self.equipment_type.name,
            'equipment_code': self.equipment_code,
            'fault_code': self.fault_code,
            'equipment_fault': self.equipment_fault.name,
            'com_code': self.com_code,
            'repair_company': self.repair_company.name,
            'repair_man': self.repair_man,
            'repair_confirm_date': self.repair_confirm_date,
            'repair_return_date': self.repair_return_date,
            'repair_return_man': self.repair_return_man,
            'equipment_return_date': self.equipment_return_date,
            'equipment_return_man': self.repair_return_man,
            'repair_status': self.repair_status
        }
        return json_equipment_repair


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, index=True)
    name = db.Column(db.String(50), unique=True, index=True)
    # 一对多反馈
    repairs = db.relationship("EquipmentRepair", backref='department', lazy='dynamic')

    def to_json(self):
        """
        完成department数据模型到JSON格式化的序列化字典转换
        """
        json_department = {
            'id': self.id,
            'dept_code': self.code,
            'dept_name': self.name
        }
        return json_department


class EquipmentBrand(db.Model):
    __tablename__ = 'equipment_brand'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, index=True)
    name = db.Column(db.String(10), unique=True, index=True)
    # 一对多反馈
    repairs = db.relationship("EquipmentRepair", backref='equipment_brand', lazy='dynamic')

    def to_json(self):
        """
        完成EquipmentBrand数据模型到JSON格式化的序列化字典转换
        """
        json_brand = {
            'id': self.id,
            'brand_code': self.code,
            'brand_name': self.name
        }
        return json_brand


class EquipmentType(db.Model):
    __tablename__ = 'equipment_type'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, index=True)
    name = db.Column(db.String(10), unique=True, index=True)
    # 一对多反馈
    repairs = db.relationship("EquipmentRepair", backref='equipment_type', lazy='dynamic')

    def to_json(self):
        """
        完成EquipmentType数据模型到JSON格式化的序列化字典转换
        """
        json_type = {
            'id': self.id,
            'type_code': self.code,
            'type_name': self.name
        }
        return json_type


class EquipmentFault(db.Model):
    __tablename__ = 'equipment_fault'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, index=True)
    name = db.Column(db.String(10), unique=True, index=True)
    # 一对多反馈
    repairs = db.relationship("EquipmentRepair", backref='equipment_fault', lazy='dynamic')

    def to_json(self):
        """
        完成EquipmentFault数据模型到JSON格式化的序列化字典转换
        """
        json_fault = {
            'id': self.id,
            'fault_code': self.code,
            'fault_name': self.name
        }
        return json_fault


class RepairCompany(db.Model):
    __tablename__ = 'repair_company'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, index=True)
    name = db.Column(db.String(10), unique=True, index=True)
    # 一对多反馈
    repairs = db.relationship("EquipmentRepair", backref='repair_company', lazy='dynamic')

    def to_json(self):
        """
        完成RepairCompany数据模型到JSON格式化的序列化字典转换
        """
        json_com = {
            'id': self.id,
            'com_code': self.code,
            'com_name': self.name
        }
        return json_com




