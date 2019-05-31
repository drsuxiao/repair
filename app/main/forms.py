from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length
from app.models import Department, EquipmentBrand, EquipmentType, EquipmentFault, RepairCompany, User, EquipmentRepair
'''
'BooleanField', 'DecimalField', 'DateField', 'DateTimeField', 'FieldList',
'FloatField', 'FormField', 'IntegerField', 'RadioField', 'SelectField',
'SelectMultipleField', 'StringField', 'TimeField',
'''


class RepairRegistrationForm(FlaskForm):
    """
        创建/编辑设备报修登记表单
        """
    # SelectField 这里务必注意coerce选项的添加，否则提交时，下拉表单中的内容无法通过validate_on_submit的 验证
    # Text Field类型，文本输入框，必须输入是"年-月-日"格式的日期
    repair_priority = SelectField('优先级', validators=[DataRequired()], coerce=str,
                                  render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 优先级
    repair_date = StringField('报修日期', validators=[DataRequired()],
                              render_kw={'class': "form-control input-sm", "style": "width: 200px"})
    dept_code = SelectField('报修科室', validators=[DataRequired()], coerce=str,
                            render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 报修科室
    repair_registrant = StringField('报修人', validators=[DataRequired()],
                                    render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 报修人
    brand_code = SelectField('设备品牌', validators=[DataRequired()], coerce=str,
                             render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备品牌
    type_code = SelectField('设备类型', validators=[DataRequired()], coerce=str,
                            render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备类型
    equipment_code = StringField('设备编号', validators=[Length(min=8, max=10), DataRequired()],
                                 render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 设备编号
    fault_code = SelectField('设备故障', validators=[DataRequired()], coerce=str,
                             render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备故障
    com_code = SelectField('维修公司', validators=[DataRequired()], coerce=str,
                           render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 维修公司
    repair_remarks = StringField('备注', render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 备注
    # 在构造化Form实例时指定selectField的choices内容,
    def __init__(self, *args, **kwargs):
        super(RepairRegistrationForm, self).__init__(*args, **kwargs)
        self.dept_code.choices = [(dept.code, dept.name) for dept in Department.query.order_by(Department.code).all()]
        self.brand_code.choices = [(brand.code, brand.name) for brand in
                                   EquipmentBrand.query.order_by(EquipmentBrand.code).all()]
        self.type_code.choices = [(type.code, type.name) for type in
                                  EquipmentType.query.order_by(EquipmentType.code).all()]
        self.fault_code.choices = [(fault.code, fault.name) for fault in
                                   EquipmentFault.query.order_by(EquipmentFault.code).all()]
        self.com_code.choices = [(com.code, com.name) for com in RepairCompany.query.order_by(RepairCompany.code).all()]
        self.repair_priority.choices = [('0', '一般'), ('1', '比较急'), ('2', '非常急'), ('3', '特急')]


class RepairConfirmForm(FlaskForm):
    """
    创建/编辑维修确认表单
    """
    # SelectField 这里务必注意coerce选项的添加，否则提交时，下拉表单中的内容无法通过validate_on_submit的 验证
    # Text Field类型，文本输入框，必须输入是"年-月-日"格式的日期
    dept_code = SelectField('报修科室', validators=[DataRequired()], coerce=str,
                            render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 报修科室
    brand_code = SelectField('设备品牌', validators=[DataRequired()], coerce=str,
                             render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备品牌
    type_code = SelectField('设备类型', validators=[DataRequired()], coerce=str,
                            render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备类型
    equipment_code = StringField('设备编号', validators=[Length(min=8, max=10), DataRequired()],
                                 render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 设备编号
    fault_code = SelectField('设备故障', validators=[DataRequired()], coerce=str,
                             render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备故障
    repair_confirm_date = StringField('维修确认日期',validators=[DataRequired()],
                              render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 维修确认日期
    com_code = SelectField('维修公司', validators=[DataRequired()], coerce=str,
                           render_kw={'class': "selectpicker form-control input-sm", "style": "width: 200px",
                                      "title": "请选择"})  # 维修公司
    repair_man = StringField('维修人', validators=[DataRequired()],
                             render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 维修人
    repair_remarks = StringField('备注', render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 备注

    # 在构造化Form实例时指定selectField的choices内容,
    def __init__(self, *args, **kwargs):
        super(RepairConfirmForm, self).__init__(*args, **kwargs)
        self.dept_code.choices = [(dept.code, dept.name) for dept in Department.query.order_by(Department.code).all()]
        self.brand_code.choices = [(brand.code, brand.name) for brand in EquipmentBrand.query.order_by(EquipmentBrand.code).all()]
        self.type_code.choices = [(type.code, type.name) for type in EquipmentType.query.order_by(EquipmentType.code).all()]
        self.fault_code.choices = [(fault.code, fault.name) for fault in EquipmentFault.query.order_by(EquipmentFault.code).all()]
        self.com_code.choices = [(com.code, com.name) for com in RepairCompany.query.order_by(RepairCompany.code).all()]


class OneKeyReturnForm(FlaskForm):
    repair_return_date = StringField('维修归还日期', validators=[DataRequired()],
                                     render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 维修归还日期
    repair_return_man = StringField('维修归还人', validators=[DataRequired()],
                                    render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请输入"})  # 维修归还人
    equipment_return_date = StringField('归还科室日期', validators=[DataRequired()],
                                        render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备归还科室日期
    equipment_return_man = StringField('归还科室人', validators=[DataRequired()],
                                       render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请输入"})  # 设备归还科室人
    repair_result = StringField('维修结果', validators=[DataRequired()],
                                render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 维修结果
    repair_remarks = StringField('备注', render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 备注


class EquipmentReturnForm(FlaskForm):
    """
    设备归还科室确认表单
    """
    equipment_return_date = StringField('归还科室日期', validators=[DataRequired()],
                                        render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 设备归还科室日期
    equipment_return_man = StringField('归还科室人', validators=[DataRequired()],
                                       render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请输入"})  # 设备归还科室人
    repair_result = StringField('维修结果', validators=[DataRequired()],
                                render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 维修结果



class RepairReturnForm(FlaskForm):
    """
    维修归还确认表单
    """
    repair_return_date = StringField('维修归还日期', validators=[DataRequired()],
                                     render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请选择"})  # 维修归还日期
    repair_return_man = StringField('维修归还人', validators=[DataRequired()],
                                    render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请输入"})  # 维修归还人
    repair_remarks = StringField('备注', validators=[DataRequired()],
                                 render_kw={'class': "form-control input-sm", "style": "width: 200px"})  # 备注


class BaseDataSetForm(FlaskForm):
    code = StringField('编码', validators=[DataRequired(), Length(min=3, max=10)],
                       render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请输入"})
    name = StringField('名称', validators=[DataRequired()],
                       render_kw={'class': "form-control input-sm", "style": "width: 200px", "title": "请输入"})


