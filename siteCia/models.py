from siteCia.init import database, login_manager
import datetime
from flask_login import UserMixin
import pytz

hr = pytz.timezone('America/Sao_Paulo')


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Unidade(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    cidade = database.Column(database.String, nullable=False)
    colaboradores = database.relationship('Usuario', backref='unid', lazy=True)
    alunos = database.Column(database.Integer, nullable=False)


class Usuario(database.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    cargo = database.Column(database.String, nullable=False)
    depart = database.Column(database.String, nullable=False)
    contrato = database.Column(database.String, nullable=False)
    remuneracao = database.Column(database.String, nullable=False)
    tipo_func = database.Column(database.String, nullable=False)
    hora_aula = database.Column(database.Float, nullable=False)
    substituicoes = database.relationship('Substituicoes', backref='solicitante', lazy=True)
    salario = database.Column(database.Float)
    admissao = database.Column(database.Date)
    insta = database.Column(database.String)
    twitter = database.Column(database.String)
    linkedin = database.Column(database.String)
    whatsapp = database.Column(database.String, default="61")
    unidade = database.Column(database.Integer, database.ForeignKey('unidade.id'), nullable=False)
    tipo_usuario = database.Column(database.String, nullable=False)
    posts = database.relationship('Post', backref='autor', lazy=True)
    comentario = database.relationship('Comentario', backref='autor', lazy=True)
    documentos = database.relationship('Documentos', backref='pessoa', lazy=True)
    atestados = database.relationship('Atestados', backref='pessoa', lazy=True)
    comprovanteir = database.relationship('ComprovantesIR', backref='pessoa', lazy=True)
    contracheques = database.relationship('Contracheques', backref='pessoa', lazy=True)
    ferias = database.relationship('Ferias', backref='pessoa', lazy=True)
    avaliacoes = database.relationship('Avaliacoes', backref='avaliado', lazy=True)
    aulas = database.relationship('Aulas', backref='pessoa', lazy=True)


class Post(database.Model):
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    foto_post = database.Column(database.String, nullable=True)
    corpo = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone(-datetime.timedelta(hours=3))))
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    postcurtido = database.relationship('Curtida', backref='post_curtido', lazy=True, viewonly=True)
    comentario = database.relationship('Comentario', backref='post', lazy=True)


class Curtida(database.Model):
    id_curt = database.Column(database.Integer, primary_key=True)
    id_post_curt = database.Column(database.Integer, database.ForeignKey('post.id'), nullable=False)
    id_quem_curtiu = database.Column(database.Integer)


class Comentario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    corpo_coment = database.Column(database.String, nullable=False)
    id_post = database.Column(database.Integer, database.ForeignKey('post.id'), nullable=False)
    autor_coment = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class Substituicoes(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_solicitante = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    nome_substituto = database.Column(database.String, nullable=False)
    data_pedido = database.Column(database.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone(-datetime.timedelta(hours=3))))
    inicio_subs = database.Column(database.DateTime, nullable=False)
    fim_subs = database.Column(database.DateTime, nullable=False)
    departamento_aula = database.Column(database.String, nullable=False)
    dias_aula = database.Column(database.String, default='Seg,Ter,Qua', nullable=False)
    autorizada = database.Column(database.String, default='False', nullable=False)
    analisada = database.Column(database.String, default='False', nullable=False)


class Avaliacoes(database.Model):
    idavaliacao = database.Column(database.Integer, primary_key=True)
    local_av = database.Column(database.String, nullable=False)
    data_av = database.Column(database.Date)
    conteudo_av = database.Column(database.String)
    nota_av = database.Column(database.Float)
    autor_av = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class Documentos(database.Model):
    __table_args__ = {'extend_existing': True}
    id_doc = database.Column(database.Integer, primary_key=True)
    fichacadastral = database.Column(database.String, nullable=True)
    contrato = database.Column(database.String, nullable=True)
    acordohrs = database.Column(database.String, nullable=True)
    codigoetica = database.Column(database.String, nullable=True)
    termoVT = database.Column(database.String, nullable=True)
    reciboCTPS = database.Column(database.String, nullable=True)
    rg = database.Column(database.String, nullable=True)
    cpf = database.Column(database.String, nullable=True)
    comprovend = database.Column(database.String, nullable=True)
    certificados = database.Column(database.String, nullable=True)
    titulo = database.Column(database.String, nullable=True)
    desempenho = database.Column(database.String, nullable=True)
    id_func = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class Atestados(database.Model):
    atestadoid = database.Column(database.Integer, primary_key=True)
    local_atest = database.Column(database.String, nullable=False)
    data_inicio = database.Column(database.Date, nullable=False)
    periodo = database.Column(database.Integer, nullable=False)
    data_retorno = database.Column(database.Date, nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class ComprovantesIR(database.Model):
    comprovIRid = database.Column(database.Integer, primary_key=True)
    local_comprov = database.Column(database.String, nullable=False)
    anobase = database.Column(database.Integer, nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class Contracheques(database.Model):
    contrachequeid = database.Column(database.Integer, primary_key=True)
    local = database.Column(database.String, nullable=False)
    mesref = database.Column(database.String, nullable=False)
    anoref = database.Column(database.String, nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class Ferias(database.Model):
    feriasid = database.Column(database.Integer, primary_key=True)
    local = database.Column(database.String, nullable=False)
    ano_ref = database.Column(database.Integer, nullable=False)
    inicio = database.Column(database.Date, nullable=False)
    fim = database.Column(database.Date, nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class SolicitacaoFerias(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    datapedido = database.Column(database.Date)
    periodos = database.Column(database.Integer, nullable=False, default=1)
    inicioperiodo1 = database.Column(database.Date)
    fimperiodo1 = database.Column(database.Date)
    inicioperiodo2 = database.Column(database.Date)
    fimperiodo2 = database.Column(database.Date)
    inicioperiodo3 = database.Column(database.Date)
    fimperiodo3 = database.Column(database.Date)
    status = database.Column(database.String, nullable=False, default='Em análise')


class Aulas(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    professor = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    departamento = database.Column(database.String, nullable=True)
    valorsemdsr = database.Column(database.String, nullable=True)
    inicioseg = database.Column(database.DateTime, nullable=True)
    fimseg = database.Column(database.DateTime, nullable=True)
    inicioter = database.Column(database.DateTime, nullable=True)
    fimter = database.Column(database.DateTime, nullable=True)
    inicioqua = database.Column(database.DateTime, nullable=True)
    fimqua = database.Column(database.DateTime, nullable=True)
    inicioqui = database.Column(database.DateTime, nullable=True)
    fimqui = database.Column(database.DateTime, nullable=True)
    iniciosex = database.Column(database.DateTime, nullable=True)
    fimsex = database.Column(database.DateTime, nullable=True)
    iniciosab = database.Column(database.DateTime, nullable=True)
    fimsab = database.Column(database.DateTime, nullable=True)
    iniciodom = database.Column(database.DateTime, nullable=True)
    fimdom = database.Column(database.DateTime, nullable=True)
    qtossab = database.Column(database.Integer, nullable=True)
    qtosdom = database.Column(database.Integer, nullable=True)
