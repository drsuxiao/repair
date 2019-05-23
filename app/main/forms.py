from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length
from app.models import Department, EquipmentBrand, EquipmentType, EquipmentFault, RepairCompany, User, EquipmentRepair
'''
'BooleanField', 'DecimalField', 'DateField', 'DateTimeField', 'FieldList',
'FloatField', 'FormField', 'IntegerField', 'RadioField', 'SelectField',
'SelectMultipleField', 'StringField', 'TimeField',
'''


class EquipmentRepairForm(FlaskForm):
    """
    创建/编辑设备报修登记表单
    """
    # SelectField 这里务必注意coerce选项的添加，否则提交时，下拉表单中的内容无法通过validate_on_submit的 验证
    # Text Field类型，文本输入框，必须输入是"年-月-日"格式的日期
    repair_date = DateField('报修日期', format='%Y-%m-%d', validators=[DataRequired()], render_kw={'type': "date"})
    dept_code = SelectField('报修科室', validators=[DataRequired()], coerce=str)  # 报修科室
    repair_registrant = StringField('报修人', validators=[DataRequired()])  # 报修人
    brand_code = SelectField('设备品牌', validators=[DataRequired()], coerce=str)  # 设备品牌
    type_code = SelectField('设备类型', validators=[DataRequired()], coerce=str)  # 设备类型
    equipment_code = StringField('设备编号', validators=[DataRequired(), Length(min=8, max=10)])   # 设备编号
    fault_code = SelectField('设备故障', validators=[DataRequired()], coerce=str)  # 设备故障
    com_code = SelectField('维修公司', validators=[DataRequired()], coerce=str)  # 维修公司
    repair_man = StringField('维修人', validators=[DataRequired()])  # 维修人
    repair_return_date = DateField('维修归还日期', format='%Y-%m-%d', render_kw={'type': "date"})  # 维修归还日期
    repair_return_man = StringField('维修归还人')  # 维修归还人
    equipment_return_date = DateField('设备归还科室日期', format='%Y-%m-%d', render_kw={'type': "date"})  # 设备归还科室日期
    equipment_return_man = StringField('设备归还科室人')  # 设备归还科室人
    # repair_status = IntegerField('维修状态')  # 维修状态
    save = SubmitField('报修')
    # cancel = SubmitField('取消')

    # 在构造化Form实例时指定selectField的choices内容,
    def __init__(self, *args, **kwargs):
        super(EquipmentRepairForm, self).__init__(*args, **kwargs)
        self.dept_code.choices = [(dept.code, dept.name) for dept in Department.query.order_by(Department.code).all()]
        self.brand_code.choices = [(brand.code, brand.name) for brand in EquipmentBrand.query.order_by(EquipmentBrand.code).all()]
        self.type_code.choices = [(type.code, type.name) for type in EquipmentType.query.order_by(EquipmentType.code).all()]
        self.fault_code.choices = [(fault.code, fault.name) for fault in EquipmentFault.query.order_by(EquipmentFault.code).all()]
        self.com_code.choices = [(com.code, com.name) for com in RepairCompany.query.order_by(RepairCompany.code).all()]


class RepairReturnForm(FlaskForm):
    """
    创建/编辑设备报修归还表单
    """
    repair_return_date = DateField('维修归还日期', format='%Y-%m-%d', render_kw={'type': "date"}, validators=[DataRequired()])  # 维修归还日期
    repair_return_man = StringField('维修归还人', validators=[DataRequired()])  # 维修归还人
    equipment_return_date = DateField('设备归还科室日期', format='%Y-%m-%d', render_kw={'type': "date"}, validators=[DataRequired()])  # 设备归还科室日期
    equipment_return_man = StringField('设备归还科室人', validators=[DataRequired()])  # 设备归还科室人
    # repair_status = IntegerField('维修状态')  # 维修状态
    save = SubmitField('归还')


class BaseDataSetForm(FlaskForm):
    code = StringField('编码', validators=[DataRequired(), Length(min=3, max=10)])
    name = StringField('名称', validators=[DataRequired()])
    save = SubmitField('保存')

