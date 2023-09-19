from database import db

class Doctor(db.Model):
    __tablename__ = 'doctor'
    cpf = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    crm = db.Column(db.Integer, nullable=False, unique=True)
    data_inscricao_crm = db.Column(db.Date, nullable=False)
    
    senha = db.Column(db.String(50), nullable=False)

    consultas = db.relationship('Consultation', backref='medico')
    
    def __init__(self, nome_completo, crm, cpf, data_inscricao_crm, senha):
        self.nome_completo = nome_completo
        self.crm = crm
        self.cpf = cpf
        self.data_inscricao_crm = data_inscricao_crm
        self.senha = senha
        
    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome_completo': self.nome_completo,
            'crm': self.crm,
            'data_inscricao_crm': self.data_inscricao_crm,
        }

class Patient(db.Model):
    __tablename__ = 'patient'
    cpf = db.Column(db.String(14), nullable=False, unique=True, primary_key=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)

    telefone = db.Column(db.String(20))
    email = db.Column(db.String(255))

    consultas = db.relationship('Consultation', backref='paciente')
    
    def __init__(self, nome_completo, cpf, data_nascimento, sexo, telefone, email):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.telefone = telefone
        self.email = email

class Consultation(db.Model):
    __tablename__ = 'consultation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_consulta = db.Column(db.Date, nullable=False)
    descricao_consulta = db.Column(db.Text)
    prescricao = db.Column(db.Text)
    diagnostico = db.Column(db.Text)
    medico_id = db.Column(db.Integer, db.ForeignKey('doctor.cpf'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('patient.cpf'))
