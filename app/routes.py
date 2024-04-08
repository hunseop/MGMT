from flask import render_template, request, redirect, url_for, flash
from . import db
from .forms import UploadForm
from .models import Server
from .forms import ServerForm
from flask import current_app as app
import pandas as pd

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command_menu', methods=['GET', 'POST'])
def command_menu():
    form = ServerForm()
    if form.validate_on_submit():
        server = Server(
            name=form.name.data,
            ip_address=form.ip_address.data,
            vendor=form.vendor.data,
            description=form.description.data,
            is_selected=form.is_selected.data
            )
        db.session.add(server)
        db.session.commit()
        flash('Server successfully added!', 'success')
        return redirect(url_for('command_menu'))
    servers = Server.query.all()
    return render_template('command_menu.html', form=form, servers=servers)

@app.route('/edit/<int:server_id>', methods=['GET', 'POST'])
def edit_server(server_id):
    server = Server.query.get_or_404(server_id)
    form = ServerForm(obj=server)
    if form.validate_on_submit():
        server.name = form.name.data
        server.ip_address = form.ip_address.data
        server.is_selected = form.is_selected.data
        db.session.commit()
        flash('Server successfully updated!', 'success')
        return redirect(url_for('command_menu'))
    return render_template('server_form.html', form=form)

@app.route('/delete/<int:server_id>', methods=['POST'])
def delete_server(server_id):
    server = Server.query.get_or_404(server_id)
    db.session.delete(server)
    db.session.commit()
    flash('Server successfully deleted!', 'success')
    return redirect(url_for('command_menu'))

@app.route('/search', methods=['GET'])
def search_servers():
    query = request.args.get('query', '')
    servers = Server.query.filter(
        (Server.name.contains(query)) | 
        (Server.ip_address.contains(query)) |
        (Server.vendor.contains(query)) |
        (Server.description.contains(query))
    ).all()
    return render_template('server_list.html', servers=servers)

@app.route('/send_command', methods=['POST'])
def send_command():
    server_ids = request.form.getlist('server_ids')
    command = request.form['command']
    # 여기서 실제 명령어 전송 로직을 구현해야 합니다.
    # 예시 코드에서는 명령어 전송 과정을 생략하고, 성공 메시지만 표시합니다.
    for server_id in server_ids:
        server = Server.query.get(server_id)
        print(f"Sending command '{command}' to {server.name} ({server.ip_address})")
    flash('Command successfully sent to selected servers!', 'success')
    return redirect(url_for('command_menu'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data  # 업로드된 파일 접근
        df = pd.read_excel(file, engine='openpyxl')  # pandas를 사용하여 엑셀 파일 읽기
        
        for index, row in df.iterrows():
            server = Server(
                name=row['Name'],
                ip_address=row['IP Address'],
                vendor=row['Vendor'],
                description=row['Description']
            )
            db.session.add(server)
        db.session.commit()
        
        flash('Devices successfully uploaded and added!', 'success')
        return redirect(url_for('command_menu'))
    return render_template('upload.html', form=form)

# routes.py

@app.route('/devices', methods=['GET', 'POST'])
def manage_devices():
    form = ServerForm()
    if form.validate_on_submit():
        server = Server(name=form.name.data, ip_address=form.ip_address.data, vendor=form.vendor.data, description=form.description.data)
        db.session.add(server)
        db.session.commit()
        flash('Device successfully added!', 'success')
        return redirect(url_for('manage_devices'))
    servers = Server.query.all()
    return render_template('manage_devices.html', form=form, servers=servers)
