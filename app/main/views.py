from flask import request, render_template

from app import app
from app.main import forms
from app.models import EquipmentRepair, Department, EquipmentFault, EquipmentType, EquipmentBrand, RepairCompany


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/repair/repairs_registration', methods=['GET', 'POST'])
def repairs_registration():
    data = EquipmentRepair.query.all()
    return render_template('repairs_registration.html', data=data)


@app.route('/repair/repairs_confirmed', methods=['GET', 'POST'])
def repairs_confirmed():
    data = EquipmentRepair.query.all()
    return render_template('repairs_confirmed.html', data=data)


@app.route('/repair/repairs_return', methods=['GET', 'POST'])
def repairs_return():
    data = EquipmentRepair.query.all()
    return render_template('repairs_return.html', data=data)


@app.route('/repair/new', methods=['GET', 'POST'])
def create_repair():
    form = forms.EquipmentRepairForm()
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


@app.route('/repair/depts', methods=['GET', 'POST'])
@app.route('/repair/brands', methods=['GET', 'POST'])
@app.route('/repair/types', methods=['GET', 'POST'])
@app.route('/repair/faults', methods=['GET', 'POST'])
@app.route('/repair/companys', methods=['GET', 'POST'])
def get_basedatas():
    if request.url.find('depts') != -1:
        model = Department
        title = '科室管理'
    elif request.url.find('brands') != -1:
        model = EquipmentBrand
        title = '品牌管理'
    elif request.url.find('types') != -1:
        model = EquipmentType
        title = '类型管理'
    elif request.url.find('faults') != -1:
        model = EquipmentFault
        title = '故障管理'
    elif request.url.find('companys') != -1:
        model = RepairCompany
        title = '维修公司管理'
    data = model.query.all()
    return render_template('basedata_main.html', data=data, title=title)


@app.route('/repair/dept_edit', methods=['GET', 'POST'])
@app.route('/repair/brand_edit', methods=['GET', 'POST'])
@app.route('/repair/type_edit', methods=['GET', 'POST'])
@app.route('/repair/fault_edit', methods=['GET', 'POST'])
@app.route('/repair/company_edit', methods=['GET', 'POST'])
def basedata_edit():
    form = forms.BaseDataSetForm()
    if form.validate_on_submit():
        pass
    return render_template('basedata_edit.html', form=form)
