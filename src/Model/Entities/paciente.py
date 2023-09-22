from src.Model.database import db

class Paciente(db.Model):
    ##* Atributos da tebela "paciente"
    __tablename__ = 'paciente'
    cpf = db.Column(db.String(14), nullable=False, unique=True, primary_key=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    consultas = db.relationship('Consulta', backref='paciente')
    
    def __init__(self, nome_completo, cpf, data_nascimento, sexo, telefone, email):
    ## Metodo de inicialização da classe
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.telefone = telefone
        self.email = email
    
    def to_dict(self):
    ## Metodo para retornar os dados do paciente em um dicionario
        '''
        Retorna um dicionário com os dados do paciente
        Returns:
            dict -- Dicionário com os dados do paciente
            {
                'cpf': int,
                'nome_completo': str,
                'data_nascimento': date,
                'sexo': str,
                'telefone': str,
                'email': str
            }
        '''
        return {
            'cpf': self.cpf,
            'nome_completo': self.nome_completo,
            'data_nascimento': self.data_nascimento,
            'sexo': self.sexo,
            'telefone': self.telefone,
            'email': self.email
        }
    
    def get_consultas(self):
        ## Metodo para retornar consultas do medico
        '''
        Retorna as consultas do médico
        Returns:
            list -- Lista com as consultas do médico
        '''
        return self.__consultas
    
    def atualizar_paciente(self, nome_completo=False, data_nascimento=False, sexo=False, telefone=False, email=False):
        ## Metodo para atualizar medico
        '''
        Atualiza os dados do médico
        Keyword Arguments:
            nome_completo {str} -- Nome completo do médico (default: {False})
            data_nascimento {date} -- Data de inscrição no CRM do médico (default: {False})
            sexo {str} -- Sexo do paciente (default: {False})
            telefone {str} -- Telefone do paciente (default: {False})
            email {str} -- Email do paciente (default: {False})
        '''
        if nome_completo:
            self.nome_completo = nome_completo
        if data_nascimento:
            self.data_nascimento = data_nascimento
        if sexo:
            self.sexo = sexo
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email
        
        db.session.commit()
    
    def deletar_paciente(self):
        ## Metodo para deletar paciente
        '''
        Deleta o paciente do banco de dados
        '''
        db.session.delete(self)
        db.session.commit()
    
    ##* Metodos estaticos
    @staticmethod
    def buscar_paciente_por_cpf(cpf):
        ## Metodo para retornar paciente pelo cpf
        '''
        Retorna um paciente pelo seu CPF
        Arguments:
            cpf {int} -- CPF do paciente
        Returns:
            Paciente -- Objeto do paciente
        '''
        return Paciente.query.filter_by(cpf=cpf).first()

    @staticmethod
    def buscar_pacientes():
        ## Metodo para retornar todos os pacientes
        '''
        Retorna todos os pacientes cadastrados
        Returns:
            list -- Lista com todos os pacientes cadastrados
        '''
        return Paciente.query.all()
    
    @staticmethod
    def buscar_pacientes_por_nome(nome):
        ## Metodo para retornar pacientes pelo nome
        '''
        Retorna uma lista de pacientes pelo seu nome
        Arguments:
            nome {str} -- Nome do paciente
        Returns:
            list -- Lista com os pacientes encontrados
        '''
        return Paciente.query.filter(Paciente.nome_completo.like(f'%{nome}%')).all()
    
    @staticmethod
    def buscar_pacientes_por_data_nascimento(data_nascimento):
        ## Metodo para retornar pacientes pela data de nascimento
        '''
        Retorna uma lista de pacientes pela sua data de nascimento
        Arguments:
            data_nascimento {date} -- Data de nascimento do paciente
        Returns:
            list -- Lista com os pacientes encontrados
        '''
        return Paciente.query.filter_by(data_nascimento=data_nascimento).all()
    
    @staticmethod
    def buscar_pacientes_por_sexo(sexo):
        ## Metodo para retornar pacientes pelo sexo
        '''
        Retorna uma lista de pacientes pelo seu sexo
        Arguments:
            sexo {str} -- Sexo do paciente
        Returns:
            list -- Lista com os pacientes encontrados
        '''
        return Paciente.query.filter_by(sexo=sexo).all()
    
    @staticmethod
    def buscar_pacientes_por_telefone(telefone):
        ## Metodo para retornar pacientes pelo telefone
        '''
        Retorna uma lista de pacientes pelo seu telefone
        Arguments:
            telefone {str} -- Telefone do paciente
        Returns:
            list -- Lista com os pacientes encontrados
        '''
        return Paciente.query.filter_by(telefone=telefone).all()
    
    @staticmethod
    def add_paciente(nome_completo, cpf, data_nascimento, sexo, telefone, email):
        ## Metodo para adicionar paciente
        '''
        Adiciona um paciente ao banco de dados
        Arguments:
            nome_completo {str} -- Nome completo do paciente
            cpf {int} -- CPF do paciente
            data_nascimento {date} -- Data de nascimento do paciente
            sexo {str} -- Sexo do paciente
            telefone {str} -- Telefone do paciente
            email {str} -- Email do paciente
        '''
        try:
            paciente = Paciente.query.filter_by(cpf=cpf).first()
            if paciente:
                raise Exception('CPF já cadastrado!')
            paciente = Paciente(nome_completo, cpf, data_nascimento, sexo, telefone, email)
            
            db.session.add(paciente)
            db.session.commit()
            
            return True, 'Paciente cadastrado com sucesso!'
        except:
            return False, 'Erro ao cadastrar paciente!'
        
    
