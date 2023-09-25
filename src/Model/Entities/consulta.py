from src.Model.database import db

class Consulta(db.Model):
    ##* Atributos da tabela "consulta"
    __tablename__ = 'consulta'
    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __data_consulta = db.Column(db.Date, nullable=False)
    __descricao_consulta = db.Column(db.Text)
    __diagnostico = db.Column(db.Text)
    __medico_cpf = db.Column(db.Integer, db.ForeignKey('medico.cpf'))
    __paciente_cpf = db.Column(db.Integer, db.ForeignKey('paciente.cpf'))
    
    def __init__(self, data_consulta, descricao_consulta, diagnostico, medico_id, paciente_id):
    ## Metodo de inicializacao da classe
        self.__data_consulta = data_consulta
        self.__descricao_consulta = descricao_consulta
        self.__diagnostico = diagnostico
        self.__medico_id = medico_id
        self.__paciente_id = paciente_id
        
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
        db.session.delete(self)
        db.session.commit()
    
    def alterar_consulta(self, data_consulta=False, descricao_consulta=False, diagnostico=False, medico_id=False, paciente_id=False):
        ## Metodo para alterar consulta
        try:
            if data_consulta:
                self.__data_consulta = data_consulta
            if descricao_consulta:
                self.__descricao_consulta = descricao_consulta
            if diagnostico:
                self.__diagnostico = diagnostico
            if medico_id:
                self.__medico_id = medico_id
            if paciente_id:
                self.__paciente_id = paciente_id
            db.session.commit()
            return 'Consulta alterada com sucesso', 200

        except:
            return 'Erro ao alterar consulta', 400
    
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
        except:
            return 'Erro ao buscar consulta', 400
    
    @staticmethod
    def buscar_consultas(medico_id=False, paciente_id=False, data_consulta=False):
        ## Metodo para buscar consultas
        '''
        Busca consultas no banco de dados
        '''
        if medico_id:
            if data_consulta:
                return Consulta.query.filter_by(__medico_id=medico_id, __data_consulta=data_consulta)
            return Consulta.query.filter_by(__medico_id=medico_id)
        elif paciente_id:
            if data_consulta:
                return Consulta.query.filter_by(__paciente_id=paciente_id, __data_consulta=data_consulta)
            return Consulta.query.filter_by(__paciente_id=paciente_id)
        else:
            return 'Erro ao buscar consultas', 400
    
    @staticmethod
    def adicionar_consulta(data_consulta, descricao_consulta, diagnostico, medico_id, paciente_id):
        ## Metodo para adicionar consulta
        '''
        Adiciona uma nova consulta ao banco de dados
        
        Arguments:
            data_consulta {date} -- Data da consulta
            descricao_consulta {str} -- Descrição da consulta
            diagnostico {str} -- Diagnóstico da consulta
            medico_id {int} -- CPF do médico
            paciente_id {int} -- CPF do paciente
            
        Returns:
            Consulta -- Objeto da consulta
            ou
            str -- Mensagem de erro
        '''
        try:
            nova_consulta = Consulta(data_consulta, descricao_consulta, diagnostico, medico_id, paciente_id)
            db.session.add(nova_consulta)
            db.session.commit()
            return 'Consulta adicionada com sucesso', 200
        except:
            return 'Erro ao adicionar consulta', 400
    