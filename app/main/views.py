from flask import request, render_template, redirect, url_for
from app import app, db
from app.main import forms
from app.models import EquipmentRepair, Department, EquipmentFault, EquipmentType, EquipmentBrand, RepairCompany
from app.main.forms import RepairRegistrationForm, RepairConfirmForm, RepairReturnForm, EquipmentReturnForm, BaseDataSetForm, OneKeyReturnForm

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/repair/repairs_registration', methods=['GET', 'POST'])
def repairs_registration():
    form = RepairRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pass
    return render_template('repairs_registration.html', form=form, modal_id="modal_registration", modal_title="报修登记窗"
                           , delete_title="删除数据确认提示窗", delete_info="确定要【删除】所勾选的记录？")


@app.route('/repair/repairs_confirmed', methods=['GET', 'POST'])
def repairs_confirmed():
    form = RepairConfirmForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pass
    return render_template('repairs_confirmed.html', form=form, modal_id="modal_confirmed", modal_title="维修确认窗"
                           , delete_title="取消确认记录确认提示窗", delete_info="确定要【取消确认】所勾选的记录？")


@app.route('/repair/repairs_return', methods=['GET', 'POST'])
def repairs_return():
    form = OneKeyReturnForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pass
    return render_template('repairs_return.html', form=form, modal_id="modal_return", modal_title="设备归还确认窗")


@app.route('/repair/new', methods=['GET', 'POST'])
def create_repair():
    form = forms.RepairRegistrationForm()
    if form.validate_on_submit():
        pass
    return render_template('repair_edit.html', form=form)


@app.route('/repair/repair_return', methods=['GET', 'POST'])
def repair_return():
    form = forms.RepairReturnForm()
    if form.validate_on_submit():
        pass
    return render_template('repair_return.html', form=form)


@app.route('/repair/equipment_return', methods=['GET', 'POST'])
def equipment_return():
    form = forms.RepairReturnForm()
    if form.validate_on_submit():
        pass
    return render_template('equipment_return.html', form=form)


@app.route('/repair/departments', methods=['GET', 'POST'])
def show_departments():
    form = BaseDataSetForm()
    return render_template('department.html', form=form, modal_id="modal_database", modal_title="科室信息维护窗")


@app.route('/repair/equipment_brands', methods=['GET', 'POST'])
def show_equipment_brands():
    form = BaseDataSetForm()
    return render_template('equipment_brand.html', form=form, modal_id="modal_database", modal_title="设备品牌维护窗")


@app.route('/repair/equipment_types', methods=['GET', 'POST'])
def show_equipment_types():
    form = BaseDataSetForm()
    return render_template('equipment_type.html', form=form, modal_id="modal_database", modal_title="设备类型维护窗")


@app.route('/repair/equipment_faults', methods=['GET', 'POST'])
def show_equipment_faults():
    form = BaseDataSetForm()
    return render_template('equipment_fault.html', form=form, modal_id="modal_database", modal_title="设备故障维护窗")


@app.route('/repair/repair_companys', methods=['GET', 'POST'])
def show_repair_companys():
    form = BaseDataSetForm()
    return render_template('repair_company.html', form=form, modal_id="modal_database", modal_title="维修公司维护窗")

@app.route('/repair/equipment_repairs/workload', methods=['GET', 'POST'])
def show_repair_workload():
    return render_template('repair_workload_statistical.html')


@app.route('/repair/equipment_repairs/fault', methods=['GET', 'POST'])
def show_repair_fault():
    return render_template('repair_fault_statistical.html')