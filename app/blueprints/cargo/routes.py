from app.extensions import db
from app.blueprints.cargo.models import Mapping, Cargo_info, Cargo_list
from flask import render_template, flash, request, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from app.blueprints.cargo.forms import CreateCargoForm
from sqlalchemy import func


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def display_home():
    return render_template('layouts/home-test.html')



#Add Number
@main.route('/add_cargo_number', methods=['GET', 'POST'])
@login_required
def create_cargonumber():
    form = CreateCargoForm()
    if form.validate_on_submit():
        prefix = str(form.cargo_number.data)[0:3]
        prefix_exists = db.session.query(Mapping.query.filter(Mapping.prefix == prefix).exists()).scalar()
        if prefix_exists:
            info_exists = db.session.query(Cargo_info.query.filter(Cargo_info.cargo_number==form.cargo_number.data).exists()).scalar()
            if not info_exists: 
                cargo_number1 = Cargo_info(cargo_number=form.cargo_number.data)
                db.session.add(cargo_number1)
                db.session.commit()
            list_exists = db.session.query(Cargo_list.query.filter(Cargo_list.id==current_user.id, Cargo_list.cargo_number==form.cargo_number.data).exists()).scalar()
            if not list_exists:
                cargo_number2 = Cargo_list(current_user.id, form.cargo_number.data)
                db.session.add(cargo_number2)
                db.session.commit()
                flash('Number added successfully')
                return redirect(url_for('main.display_cargo_info'))
            else:
                flash('This number is already registered.')
        else:
            flash('The prefix ' + prefix + ' is not supported.')
    return render_template('cargo/add_cargo_number.html', form=form)




#List Number
@main.route('/cargo_number_list')
@login_required
def display_cargo_info():
    cargo_infos = Cargo_info.query.join(Cargo_list, Cargo_list.cargo_number==Cargo_info.cargo_number).filter(Cargo_list.id==current_user.id).all()
    return render_template('cargo/cargo_number_list.html', cargo_infos=cargo_infos)




#Delete Number
@main.route('/delete_number/<delete_number>', methods=['GET', 'POST'])
def delete_cargo_number(delete_number):
    delete_info = Cargo_info.query.get(delete_number)
    if request.method == 'POST':
        delete_list = Cargo_list.query.get((current_user.id, delete_number))
        db.session.delete(delete_list)
        db.session.commit()
        list_exists = db.session.query(Cargo_list.query.filter(Cargo_list.cargo_number==delete_number).exists()).scalar()
        if not list_exists:
            db.session.delete(delete_info)
            db.session.commit()
            flash('Cargo number ' + delete_number + ' has been deleted successfully. It has been deleted from cargo_info too because no one else registered this number. (This message is for test.)')
        else:
            flash('Cargo number ' + delete_number + ' has been deleted successfully. However this number remains in cargo_info because it is registered by another users. (This message is for test.)')
#        flash('cargo number delete successfully')
        return redirect(url_for('main.display_cargo_info'))
    return render_template('cargo/delete_number.html', delete_info=delete_info, delete_number=delete_info.cargo_number)





