from app import db

#skema model fakultas
class Fakultas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Falultas('{self.id}', '{self.nama}')"
