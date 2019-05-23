from passlib.apps import custom_app_context as pwd_context
from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    usercode = db.Column(db.String(10), unique=True, index=True)
    username = db.Column(db.String(32), unique=True, index=True)
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


class EquipmentRepair(db.Model):
    __tablename__ = 'equipment_repair'
    id = db.Column(db.Integer, primary_key=True)
    repair_date = db.Column(db.DateTime(), default=datetime.now)
    repair_department = db.Column(db.String(30))
    repair_registrant = db.Column(db.String(10))  # 报修人
    equipment_brand = db.Column(db.String(10))  # 设备品牌
    equipment_type = db.Column(db.String(10))   # 设备类型
    equipment_code = db.Column(db.String(10))   # 设备编号
    equipment_fault = db.Column(db.String(50))  # 设备故障
    repair_company = db.Column(db.String(30))  # 维修公司
    repair_man = db.Column(db.String(10))  # 维修人
    repair_return_date = db.Column(db.DateTime())  # 维修归还日期
    repair_return_man = db.Column(db.String(10))  # 维修归还人
    equipment_return_date = db.Column(db.DateTime())  # 设备归还科室日期
    equipment_return_man = db.Column(db.String(10))  # 设备归还科室人
    repair_status = db.Column(db.Integer)  # 维修状态

    def to_json(self):
        """
        完成EquipmentRepair数据模型到JSON格式化的序列化字典转换
        """
        json_equipment_repair = {
            'id': self.id,
            'repair_date': self.repair_date,
            'repair_department': self.repair_department,
            'repair_registrant': self.repair_registrant,
            'equipment_brand': self.equipment_brand,
            'equipment_type': self.equipment_type,
            'equipment_code': self.equipment_code,
            'equipment_fault': self.equipment_fault,
            'repair_company': self.repair_company,
            'repair_man': self.repair_man,
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
    dept_code = db.Column(db.String(10), unique=True, index=True)
    dept_name = db.Column(db.String(50), unique=True, index=True)

    def to_json(self):
        """
        完成department数据模型到JSON格式化的序列化字典转换
        """
        json_department = {
            'id': self.id,
            'dept_code': self.dept_code,
            'dept_name': self.dept_name
        }
        return json_department


class EquipmentBrand(db.Model):
    __tablename__ = 'equipment_brand'
    id = db.Column(db.Integer, primary_key=True)
    brand_code = db.Column(db.String(10), unique=True, index=True)
    brand_name = db.Column(db.String(10), unique=True, index=True)

    def to_json(self):
        """
        完成EquipmentBrand数据模型到JSON格式化的序列化字典转换
        """
        json_brand = {
            'id': self.id,
            'brand_code': self.brand_code,
            'brand_name': self.brand_name
        }
        return json_brand


class EquipmentType(db.Model):
    __tablename__ = 'equipment_type'
    id = db.Column(db.Integer, primary_key=True)
    type_code = db.Column(db.String(10), unique=True, index=True)
    type_name = db.Column(db.String(10), unique=True, index=True)

    def to_json(self):
        """
        完成EquipmentType数据模型到JSON格式化的序列化字典转换
        """
        json_type = {
            'id': self.id,
            'type_code': self.type_code,
            'type_name': self.type_name
        }
        return json_type


class EquipmentFault(db.Model):
    __tablename__ = 'equipment_fault'
    id = db.Column(db.Integer, primary_key=True)
    fault_code = db.Column(db.String(10), unique=True, index=True)
    fault_name = db.Column(db.String(10), unique=True, index=True)

    def to_json(self):
        """
        完成EquipmentFault数据模型到JSON格式化的序列化字典转换
        """
        json_fault = {
            'id': self.id,
            'fault_code': self.fault_code,
            'fault_name': self.fault_name
        }
        return json_fault


class RepairCompany(db.Model):
    __tablename__ = 'repair_company'
    id = db.Column(db.Integer, primary_key=True)
    com_code = db.Column(db.String(10), unique=True, index=True)
    com_name = db.Column(db.String(10), unique=True, index=True)

    def to_json(self):
        """
        完成RepairCompany数据模型到JSON格式化的序列化字典转换
        """
        json_com = {
            'id': self.id,
            'com_code': self.com_code,
            'com_name': self.com_name
        }
        return json_com




