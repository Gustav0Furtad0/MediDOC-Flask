from src.Model.database import db
from flask_sqlalchemy import SQLAlchemyError

class Consulta(db.Model):
    ##* Atributos da tabela "consulta"
    __tablename__ = 'consulta'
    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __data_consulta = db.Column(db.Date, nullable=False)
    __descricao_consulta = db.Column(db.Text)
    __diagnostico = db.Column(db.Text)
    __medico_cpf = db.Column(db.Integer, db.ForeignKey('medico.cpf'))
    __paciente_cpf = db.Column(db.Integer, db.ForeignKey('paciente.cpf'))
    
    def __init__(self, data_consulta, descricao_consulta, diagnostico, medico_cpf, paciente_cpf):
    ## Metodo de inicializacao da classe
        self.__data_consulta = data_consulta
        self.__descricao_consulta = descricao_consulta
        self.__diagnostico = diagnostico
        self.__medico_cpf = medico_cpf
        self.__paciente_cpf = paciente_cpf
        
    def to_dict(self):
        ## Metodo para retornar os dados da consulta em um dicionario
        '''
        Retorna um dicionário com os dados da consulta
        Returns:
            dict -- Dicionário com os dados da consulta
            {
                'id': int,
                'data_consulta': date,
                'descricao_consulta': str,
                'diagnostico': str,
                'medico_cpf': int,
                'paciente_cpf': int
            }
        '''
        return {
            'id': self.__id,
            'data_consulta': self.__data_consulta,
            'descricao_consulta': self.__descricao_consulta,
            'diagnostico': self.__diagnostico,
            'medico_cpf': self.__medico_cpf,
            'paciente_cpf': self.__paciente_cpf
        }
    
    def deletar_consulta(self):
        ## Metodo para deletar consulta
        '''
        Deleta a consulta do banco de dados
        '''
        try:
            db.session.begin()
            db.session.delete(self)
            db.session.commit()
            
        except SQLAlchemyError:
            db.session.rollback()
            return False, 'Erro ao deletar consulta'
            
    def alterar_consulta(self, data_consulta=False, descricao_consulta=False, diagnostico=False, medico_cpf=False, paciente_cpf=False):
        ## Metodo para alterar consulta
        '''
        Altera os dados da consulta
        
        Arguments:
            data_consulta {date} -- Data da consulta (default: {False})
            descricao_consulta {str} -- Descrição da consulta (default: {False})
            diagnostico {str} -- Diagnóstico da consulta (default: {False})
            medico_cpf {int} -- CPF do médico (default: {False})
            paciente_cpf {int} -- CPF do paciente (default: {False})
            
        Returns:
            bool -- True se a consulta foi alterada com sucesso
            str -- Mensagem de erro
        '''
        try:
            db.session.begin()
            if data_consulta:
                self.__data_consulta = data_consulta
            if descricao_consulta:
                self.__descricao_consulta = descricao_consulta
            if diagnostico:
                self.__diagnostico = diagnostico
            if medico_cpf:
                self.__medico_cpf = medico_cpf
            if paciente_cpf:
                self.__paciente_cpf = paciente_cpf
            db.session.commit()
            return True, 'Consulta alterada com sucesso!'

        except SQLAlchemyError:
            db.session.rollback()
            return False, 'Erro ao alterar consulta'
    
    ##* Metodos estaticos
    @staticmethod
    def buscar_consulta(id):
        ## Metodo para buscar consulta
        '''
        Busca uma consulta no banco de dados
        
        Arguments:
            id {int} -- ID da consulta
            
        Returns:
            Consulta -- Objeto da consulta
            ou
            str -- Mensagem de erro
        '''
        try:
            if id:
                return Consulta.query.filter_by(__id=id).first()
        except SQLAlchemyError:
            return False, 'Erro ao buscar consulta'
    
    @staticmethod
    def buscar_consultas(medico_cpf=False, paciente_cpf=False, data_consulta=False):
        ## Metodo para buscar consultas
        '''
        Busca consultas no banco de dados
        Arguments:
            data_consulta {date} -- Data da consulta
            descricao_consulta {str} -- Descrição da consulta
            diagnostico {str} -- Diagnóstico da consulta
            medico_cpf {int} -- CPF do médico
            paciente_cpf {int} -- CPF do paciente
        ''' 
        try:
            if medico_cpf:
                if data_consulta:
                    return Consulta.query.filter_by(__medico_cpf=medico_cpf, __data_consulta=data_consulta)
                return Consulta.query.filter_by(__medico_cp=medico_cpf)
            elif paciente_cpf:
                if data_consulta:
                    return Consulta.query.filter_by(__paciente_cpf=paciente_cpf, __data_consulta=data_consulta)
                return Consulta.query.filter_by(__paciente_cpf=paciente_cpf)
        except SQLAlchemyError:
            return False, 'Erro ao buscar consultas'
        
    @staticmethod
    def adicionar_consulta(data_consulta, descricao_consulta, diagnostico, medico_cpf, paciente_cpf):
        ## Metodo para adicionar consulta
        '''
        Adiciona uma nova consulta ao banco de dados
        
        Arguments:
            data_consulta {date} -- Data da consulta
            descricao_consulta {str} -- Descrição da consulta
            diagnostico {str} -- Diagnóstico da consulta
            medico_cpf {int} -- CPF do médico
            paciente_cpf {int} -- CPF do paciente
            
        Returns:
            Consulta -- Objeto da consulta
            ou
            str -- Mensagem de erro
        '''
        try:
            db.session.begin()
            nova_consulta = Consulta(data_consulta, descricao_consulta, diagnostico, medico_cpf, paciente_cpf)
            db.session.add(nova_consulta)
            db.session.commit()
            return True, 'Consulta adicionada com sucesso!'
        except SQLAlchemyError:
            db.session.rollback()
            return False, 'Erro ao adicionar consulta'
        
    