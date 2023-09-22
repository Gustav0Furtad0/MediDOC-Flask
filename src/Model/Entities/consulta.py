from src.Model.database import db

class Consulta(db.Model):
    __tablename__ = 'consulta'
    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __data_consulta = db.Column(db.Date, nullable=False)
    __descricao_consulta = db.Column(db.Text)
    __diagnostico = db.Column(db.Text)
    __medico_id = db.Column(db.Integer, db.ForeignKey('medico.cpf'))
    __paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.cpf'))
    
    def __init__(self, data_consulta, descricao_consulta, diagnostico, medico_id, paciente_id):
        self.__data_consulta = data_consulta
        self.__descricao_consulta = descricao_consulta
        self.__diagnostico = diagnostico
        self.__medico_id = medico_id
        self.__paciente_id = paciente_id
        
    def to_dict(self):
        return {
            'id': self.__id,
            'data_consulta': self.__data_consulta,
            'descricao_consulta': self.__descricao_consulta,
            'diagnostico': self.__diagnostico,
            'medico_id': self.__medico_id,
            'paciente_id': self.__paciente_id
        }
    
    def add_consulta(self):
        db.session.add(self)
        db.session.commit()
    
    def update_consulta(self):
        db.session.commit()
    
    def delete_consulta(self):
        db.session.delete(self)
        db.session.commit()
    