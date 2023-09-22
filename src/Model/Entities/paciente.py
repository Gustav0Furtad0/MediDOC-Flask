from src.Model.database import db

class Paciente(db.Model):
    __tablename__ = 'paciente'
    cpf = db.Column(db.String(14), nullable=False, unique=True, primary_key=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    consultas = db.relationship('Consulta', backref='paciente')
    
    def __init__(self, nome_completo, cpf, data_nascimento, sexo, telefone, email):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.telefone = telefone
        self.email = email
    
    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome_completo': self.nome_completo,
            'data_nascimento': self.data_nascimento,
            'sexo': self.sexo,
            'telefone': self.telefone,
            'email': self.email
        }
    
    def add_paciente(self):
        db.session.add(self)
        db.session.commit()
    
    def update_paciente(self):
        db.session.commit()
    
    def delete_paciente(self):
        db.session.delete(self)
        db.session.commit()
    