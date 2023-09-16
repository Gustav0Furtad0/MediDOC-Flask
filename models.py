from database import db

class Doctor(db.Model):
    __tablename__ = 'doctor'
    cpf = db.Column(db.String(14), nullable=False, unique=True, primary_key=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    crm = db.Column(db.String(20), nullable=False, unique=True)
    data_inscricao_crm = db.Column(db.Date, nullable=False)

    consultas = db.relationship('Consultation', backref='medico')
    
    def __init__(self, nome_completo, crm, cpf, data_inscricao_crm):
        self.nome_completo = nome_completo
        self.crm = crm
        self.cpf = cpf
        self.data_inscricao_crm = data_inscricao_crm

class Patient(db.Model):
    __tablename__ = 'patient'
    cpf = db.Column(db.String(14), nullable=False, unique=True, primary_key=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)

    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(255))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(50))
    cep = db.Column(db.String(10))

    telefone = db.Column(db.String(20))
    email = db.Column(db.String(255))

    consultas = db.relationship('Consultation', backref='paciente')
    
    def __init__(self, nome_completo, cpf, data_nascimento, sexo, numero, complemento, cidade, estado, cep, telefone, email):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.email = email

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)

    consultacoes = db.relationship('Consultation', secondary='consultation_categories', back_populates='categorias')
    
    def __init__(self, nome):
        self.nome = nome
    
    consultation_categories = db.Table('consultation_categories',
    db.Column('consultation_id', db.Integer, db.ForeignKey('consultation.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Consultation(db.Model):
    __tablename__ = 'consultation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_consulta = db.Column(db.Date, nullable=False)
    descricao_consulta = db.Column(db.Text)
    prescricao = db.Column(db.Text)
    diagnostico = db.Column(db.Text)
    medico_id = db.Column(db.Integer, db.ForeignKey('doctor.cpf'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('patient.cpf'))

    categorias = db.relationship('Category', secondary='consultation_categories', back_populates='consultacoes')