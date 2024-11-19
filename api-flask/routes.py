from sqlalchemy.orm import joinedload
from flask import request, jsonify
from app import app, db
from models import Fakultas

# Route GET fakultas
@app.route('/api/fakultas', methods=['GET'])
def get_fakultas():
    fakultas = Fakultas.query.all()
    output = []
    for data in fakultas:
        output.append({'id': data.id,
        'nama': data.nama})
    return jsonify(output) 

# Route Post fakultas
@app.route('/api/fakultas', methods=['POST'])
def add_fakultas():
    data = request.get_json()
    if 'nama' not in data:
        return jsonify({'message': 'Nama Fakultas Diperlukan'}),400
    fakultas = Fakultas(nama=data['nama'])
    db.session.add(fakultas)
    db.session.commit()
    return jsonify({'message': 'Fakultas Berhasil ditambahkan'}), 201