from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import ServerForm
from models import Server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servers.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ServerForm()
    if form.validate_on_submit():
        server = Server(name=form.name.data, ip_address=form.ip_address.data, is_selected=form.is_selected.data)
        db.session.add(server)
        db.session.commit()
        flash('Server added successfully!', 'success')
        return redirect(url_for('index'))
    servers = Server.query.all()
    return render_template('index.html', form=form, servers=servers)

@app.route('/edit/<int:server_id>', methods=['GET', 'POST'])
def edit_server(server_id):
    server = Server.query.get_or_404(server_id)
    form = ServerForm(obj=server)
    if form.validate_on_submit():
        server.name = form.name.data
        server.ip_address = form.ip_address.data
        server.is_selected = form.is_selected.data
        db.session.commit()
        flash('Server updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('server_form.html', form=form)

@app.route('/delete/<int:server_id>', methods=['POST'])
def delete_server(server_id):
    server = Server.query.get_or_404(server_id)
    db.session.delete(server)
    db.session.commit()
    flash('Server deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search_servers():
    query = request.args.get('query', '')
    if query:
        servers = Server.query.filter((Server.name.contains(query)) | (Server.ip_address.contains(query))).all()
    else:
        servers = Server.query.all()
    return render_template('index.html', servers=servers)

@app.route('/send_command', methods=['POST'])
def send_command():
    server_ids = request.form.getlist('server_ids')
    command = request.form['command']
    for server_id in server_ids:
        server = Server.query.get(server_id)
        # 여기에 명령어 전송 로직 구현 (예: SSH를 통해 서버에 명령 실행)
        print(f"Sending command '{command}' to {server.name} ({server.ip_address})")
    flash('Command sent successfully to selected servers!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
