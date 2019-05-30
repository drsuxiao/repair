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
            modal = EquipmentRepair()
            modal.repair_date = form.repair_date.data
            modal.repair_registrant = form.repair_registrant.data
            modal.dept_code = form.dept_code.data
            modal.brand_code = form.brand_code.data
            modal.type_code = form.type_code.data
            modal.equipment_code = form.equipment_code.data
            modal.fault_code = form.fault_code.data
            modal.com_code = form.com_code.data
            modal.repair_status = 0
            db.session.add(modal)
            db.session.commit()
            form = RepairRegistrationForm()
    return render_template('repairs_registration.html', form=form, modal_id="modal_registration", modal_title="报修登记窗")


@app.route('/repair/repairs_confirmed', methods=['GET', 'POST'])
def repairs_confirmed():
    form = RepairConfirmForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pass
    return render_template('repairs_confirmed.html', form=form, modal_id="modal_confirmed", modal_title="维修确认窗")


@app.route('/repair/repairs_return', methods=['GET', 'POST'])
def repairs_return():
    form = OneKeyReturnForm()
    if request.method == 'POST':
        #if form.validate_on_submit():
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
    return render_template('department.html', form=form, modal_id="modal_database", modal_title="科室信息管理")


@app.route('/repair/equipment_brands', methods=['GET', 'POST'])
def show_equipment_brands():
    form = BaseDataSetForm()
    return render_template('equipment_brand.html', form=form, modal_id="modal_database", modal_title="设备品牌管理")


@app.route('/repair/equipment_types', methods=['GET', 'POST'])
def show_equipment_types():
    form = BaseDataSetForm()
    return render_template('equipment_type.html', form=form, modal_id="modal_database", modal_title="设备类型管理")


@app.route('/repair/equipment_faults', methods=['GET', 'POST'])
def show_equipment_faults():
    form = BaseDataSetForm()
    return render_template('equipment_fault.html', form=form, modal_id="modal_database", modal_title="设备故障管理")


@app.route('/repair/repair_companys', methods=['GET', 'POST'])
def show_repair_companys():
    form = BaseDataSetForm()
    return render_template('repair_company.html', form=form, modal_id="modal_database", modal_title="维修公司管理")

