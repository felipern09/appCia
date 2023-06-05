from siteCia import app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField,BooleanField, DateField, IntegerField,SelectField, \
    TextAreaField, widgets, SelectMultipleField, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from siteCia import Usuario

# Cadastros:
# 	fazer logica de salvar excel com dados dos forms - ok
# 		ver forma do site salvar isso para eu fazer download
# 		procurar hospedagem e funcionalidades de hospedagem


class FormAlterarUser(FlaskForm):
    novousername = StringField('Escreva o novo username', validators=[DataRequired(), Length(min=4, max=15)])
    botao_submit_username = SubmitField('Alterar username')


class FormAlterarEmail(FlaskForm):
    novoemail = StringField('Escreva o novo e-mail', validators=[DataRequired(), Email(), EqualTo('confirma_email', message='E-mail deve ser igual a confirmação de e-amil!')])
    confirma_email = StringField('Confirme o novo e-mail', validators=[DataRequired(), Email()])
    botao_submit_nemail = SubmitField('Alterar')

    def validate_novoemail(self, novoemail):
        usuario = Usuario.query.filter_by(email=novoemail.data).first()
        if usuario:
            raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail.')


class FormAlterarSenha(FlaskForm):
    senha = PasswordField('Escreva a senha atual', validators=[DataRequired()])
    novasenha = PasswordField('Escreva a nova senha', validators=[DataRequired(), Length(min=6, max=15), EqualTo('confirma_senha', message='Nova senha deve ser igual a confirmação de nova senha!')])
    confirma_senha = PasswordField('Confirme a nova senha', validators=[DataRequired()])
    botao_submit_senha = SubmitField('Alterar')


class FormAlterarTt(FlaskForm):
    novott = StringField('Escreva seu usuário do Twitter (sem o @).', validators=[DataRequired()])
    botao_submit_tt = SubmitField('Salvar')


class FormAlterarInsta(FlaskForm):
    novoinsta = StringField('Escreva somente seu usuário do Instagram (sem o @).', validators=[DataRequired()])
    botao_submit_insta = SubmitField('Salvar')


class FormAlterarLinkedin(FlaskForm):
    novolinkedin = StringField('Cole o link do seu Linkedin', validators=[DataRequired()])
    botao_submit_linkedin = SubmitField('Salvar')


class AlterarFoto(FlaskForm):
    novafoto = FileField('Escolha a nova foto de perfil', validators=[FileAllowed(['jpg', 'png'])])
    botao_submitfoto = SubmitField('Salvar')


class FormCriarPost(FlaskForm):
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    imagem = FileField('Escolha a imagem do post', validators=[FileAllowed(['jpg', 'png'])])
    botao_submit_post = SubmitField('Postar!')


class MsgPrivada(FlaskForm):
    corpo = TextAreaField('Escreva sua mensagem', validators=[DataRequired()])
    botao_submit_msg = SubmitField('Enviar!')


class FormCriarComent(FlaskForm):
    corpo = TextAreaField('Adicione um comentário', validators=[DataRequired()])
    botao_submit_coment = SubmitField('Comentar!')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[Email(), DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar-me')
    botao_submit_login = SubmitField('Entrar')


class TipoColaborador(FlaskForm):
    estagiario = BooleanField('Estagiário')
    funcionario = BooleanField('Funcionário')
    autonomo = BooleanField('Autônomo')
    botao_continue = SubmitField('Avançar')


class CadastrarFuncionario(FlaskForm):
    email = StringField('E-mail', validators=[Email(), DataRequired()])
    nome = StringField('Nome completo', validators=[DataRequired()])
    datanasc = DateField('Data de nascimento', format= '%d-%m-%Y', validators=[DataRequired()])
    genero = SelectField('Gênero', choices=('', 'Masculino', 'Feminino', 'Outro'), validators=[DataRequired()])
    est_civ = SelectField('Estado Civil', choices=('', '1 - Solteiro(a)', '2 - Casado(a)', '3 - Divorciado(a)', '4 - Viuvo(a)', '7 - Separado(a)'), validators=[DataRequired()])
    raca = SelectField('Raça', choices=('', '1 - Indígena', '2 - Branca', '4 - Preta', '6 - Amarela', '8 - Parda', '9 - Não informar'), validators=[DataRequired()])
    pcd = SelectField('É Pessoa com Deficiência?', choices=('', '1 - Sim', '2 - Não'), validators=[DataRequired()])
    aposent = SelectField('É aposentado por idade?', choices=('', '1 - Sim', '2 - Não'), validators=[DataRequired()])
    instru = SelectField('Grau de instrução', choices=('','01 - Analfabeto','02 - Até o 4º ano completo do Ensino Fundamental','03 - 5º ano do Ensino Fundamental Completo','04 - Do 6º ao 9º ano do Ensino Fundamental completo','05 - Ensino Fundamental completo','06 - Ensino Médio incompleto','07 - Ensino Médio completo','08 - Educação Superior Incompleta','09 - Educação Superior Completa','10 - Pós Graduação Completa','11 - Mestrado Completo','12 - Doutorado Completo'), validators=[DataRequired()])
    nacion = SelectField('Nacionalidade', choices=('','1 - Brasileiro nato','2 - Brasileiro Nascido no Exterior','3 - Estrangeiro','4 - Estrangeiro Naturalizado Brasileiro'), validators=[DataRequired()])
    cid_nasc = StringField('Cidade de nascimento', validators=[DataRequired()])
    est_nasc = SelectField('Estado de nascimento', choices=('','AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'), validators=[DataRequired()])
    pai = StringField('Nome do pai', validators=[DataRequired()])
    mae = StringField('Nome da mãe', validators=[DataRequired()])
    end_res = StringField('Endereço residencial', validators=[DataRequired()])
    num = IntegerField('Número', validators=[DataRequired()])
    bair = StringField('Bairro', validators=[DataRequired()])
    cep = IntegerField('CEP', validators=[DataRequired()])
    cid_end = StringField('Cidade', validators=[DataRequired()])
    uf_end = SelectField('UF', choices=('','AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'), validators=[DataRequired()])
    tel = IntegerField('DDD+telefone', validators=[DataRequired()])
    cpf = IntegerField('CPF (Apenas números)', validators=[DataRequired()])
    rg = IntegerField('RG (Apenas números)', validators=[DataRequired()])
    org_rg = StringField('Orgão Emissor do RG', validators=[DataRequired()])
    pis = IntegerField('PIS (Apenas números)', validators=[DataRequired()])
    tit = IntegerField('Título de eleitor (Apenas números)', validators=[DataRequired()])
    zona = IntegerField('Zona Eleitoral (Apenas números)', validators=[DataRequired()])
    sec = IntegerField('Seção Eleitoral (Apenas números)', validators=[DataRequired()])
    ctps = IntegerField('CTPS (Apenas números)', validators=[DataRequired()])
    serie = IntegerField('Série CTPS (Apenas números)', validators=[DataRequired()])
    uf_ctps = SelectField('UF CTPS', choices=('','AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'), validators=[DataRequired()])
    emis_ctps = DateField('Data de emissão CTPS', format= '%d-%m-%Y', validators=[DataRequired()])
    depart = SelectField('Departamento', choices=('','Unidade Park Sul - qualquer departamento','Kids','Musculação','Esportes e Lutas','Crossfit','Ginástica','Gestantes','Recepção','Financeiro','TI','RH','Marketing','Manutenção'), validators=[DataRequired()])
    cargo = SelectField('Cargo', choices=('','OAF Crossfit','OAF Dança','OAF Esportes Adulto','OAF Gestantes','OAF Ginástica','OAF Hidro','OAF Kids','OAF Lutas Adulto','OAF Musculação','OAF Natação','OAF Yoga','Aprendiz','Auxiliar Financeiro','Auxiliar TI','Auxiliar RH','Manutencista','Massagista','Monitora Kids','Recepcionista','Vendedora'), validators=[DataRequired()])
    horario = StringField('Horário de trabalho', validators=[DataRequired()])
    botao_submit_cadastroF = SubmitField('Enviar')


class CadastrarEstagiario(FlaskForm):
    email = StringField('E-mail', validators=[Email(), DataRequired()])
    nome = StringField('Nome completo', validators=[DataRequired()])
    datanasc = DateField('Data de nascimento', format= '%d-%m-%Y', validators=[DataRequired()])
    rg = IntegerField('RG (Apenas números)', validators=[DataRequired()])
    cpf = IntegerField('CPF (Apenas números)', validators=[DataRequired()])
    pai = StringField('Nome do pai', validators=[DataRequired()])
    mae = StringField('Nome da mãe', validators=[DataRequired()])
    genero = SelectField('Gênero', choices=('', 'Masculino', 'Feminino', 'Outro'), validators=[DataRequired()])
    est_civ = SelectField('Estado Civil', choices=('', '1 - Solteiro(a)', '2 - Casado(a)', '3 - Divorciado(a)', '4 - Viuvo(a)', '7 - Separado(a)'), validators=[DataRequired()])
    end_res = StringField('Endereço residencial', validators=[DataRequired()])
    num = IntegerField('Número', validators=[DataRequired()])
    bair = StringField('Bairro', validators=[DataRequired()])
    cep = IntegerField('CEP', validators=[DataRequired()])
    tel = IntegerField('DDD+telefone', validators=[DataRequired()])
    semest = IntegerField('Semestre', validators=[DataRequired()])
    turno = SelectField('Turno', choices=('','Matutino', 'Vespertino', 'Noturno'), validators=[DataRequired()])
    concl = IntegerField('Provável ano de conclusão do curso:', validators=[DataRequired()])
    facul = StringField('Faculdade', validators=[DataRequired()])
    depart = SelectField('Departamento', choices=('','Unidade Park Sul - qualquer departamento','Kids','Musculação','Esportes e Lutas','Crossfit','Ginástica','Gestantes','Recepção','Financeiro','TI','RH','Marketing','Manutenção'), validators=[DataRequired()])
    horario = StringField('Horário de trabalho', validators=[DataRequired()])
    botao_submit_cadastroE = SubmitField('Enviar')


class CadastrarAutonomo(FlaskForm):
    email = StringField('E-mail', validators=[Email(), DataRequired()])
    nome = StringField('Nome completo', validators=[DataRequired()])
    datanasc = DateField('Data de nascimento', format= '%d-%m-%Y', validators=[DataRequired()])
    genero = SelectField('Gênero', choices=('', 'Masculino', 'Feminino', 'Outro'), validators=[DataRequired()])
    instru = SelectField('Grau de instrução', choices=('','01 - Analfabeto','02 - Até o 4º ano completo do Ensino Fundamental','03 - 5º ano do Ensino Fundamental Completo','04 - Do 6º ao 9º ano do Ensino Fundamental completo','05 - Ensino Fundamental completo','06 - Ensino Médio incompleto','07 - Ensino Médio completo','08 - Educação Superior Incompleta','09 - Educação Superior Completa','10 - Pós Graduação Completa','11 - Mestrado Completo','12 - Doutorado Completo'), validators=[DataRequired()])
    cid_nasc = StringField('Cidade de nascimento', validators=[DataRequired()])
    est_nasc = SelectField('Estado de nascimento', choices=('','AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'), validators=[DataRequired()])
    end_res = StringField('Endereço residencial', validators=[DataRequired()])
    num = IntegerField('Número', validators=[DataRequired()])
    bair = StringField('Bairro', validators=[DataRequired()])
    cep = IntegerField('CEP', validators=[DataRequired()])
    cid_end = StringField('Cidade', validators=[DataRequired()])
    uf_end = SelectField('UF', choices=('','AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'), validators=[DataRequired()])
    tel = IntegerField('DDD+telefone', validators=[DataRequired()])
    cpf = IntegerField('CPF (Apenas números)', validators=[DataRequired()])
    rg = IntegerField('RG (Apenas números)', validators=[DataRequired()])
    emis_rg = DateField('Data de emissão RG', format= '%d-%m-%Y', validators=[DataRequired()])
    pis = IntegerField('PIS (Apenas números)', validators=[DataRequired()])
    aula = StringField('Aula a ser ministrada', validators=[DataRequired()])
    valorhr = StringField('Valor Combinado por hr-aula', validators=[DataRequired()])
    banco = StringField('Banco a ser creditado o pagamento', validators=[DataRequired()])
    agencia = StringField('Agência', validators=[DataRequired()])
    conta = StringField('Conta', validators=[DataRequired()])
    tipo_conta = SelectField('Tipo de conta', choices=('','Corrente','Poupança','Salário'), validators=[DataRequired()])
    botao_submit_cadastroA = SubmitField('Enviar')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class Substituir(FlaskForm):
    with app.app_context():
        substituto = SelectField('Prof. Substituto', choices=([usuario.nome for usuario in Usuario.query.order_by(Usuario.nome).all()]), validators=[DataRequired()])
        dt_inicio = DateField('Data de início da substituição', format='%d-%m-%Y', validators=[DataRequired()])
        dt_fim = DateField('Data fim da substituição', format='%d-%m-%Y', validators=[DataRequired()])
        depto = SelectField('Departamento', choices=('Crossfit', 'Esportes Adulto', 'Ginástica', 'Kids', 'Muculação', 'PK Sul'), validators=[DataRequired()])
        seg = MultiCheckboxField('Segunda', choices='S')
        ter = MultiCheckboxField('Terça', choices='T')
        qua = MultiCheckboxField('Quarta', choices='Q')
        qui = MultiCheckboxField('Quinta', choices='Q')
        sex = MultiCheckboxField('Sexta', choices='S')
        botao_enviar = SubmitField('Enviar')


class DataFerias(FlaskForm):
    inicio1 = DateField('Início das Férias', format='%d/%m/%Y', validators=[DataRequired()])
    fim1 = DateField('Início das Férias', format='%d/%m/%Y', validators=[DataRequired()])
    inicio2 = DateField('Início das Férias', format='%d/%m/%Y', validators=[DataRequired()])
    fim2 = DateField('Início das Férias', format='%d/%m/%Y', validators=[DataRequired()])
    inicio3 = DateField('Início das Férias', format='%d/%m/%Y', validators=[DataRequired()])
    fim3 = DateField('Início das Férias', format='%d/%m/%Y', validators=[DataRequired()])
    botao_enviarferias = SubmitField('Enviar solicitação de férias')


class MontarGrade(FlaskForm):
    with app.app_context():
        professor = SelectField('Professor', choices=([usuario.nome for usuario in Usuario.query.order_by(Usuario.nome).all()]), validators=[DataRequired()])
        depto = SelectField('Departamento', choices=('Crossfit', 'Esportes Adulto', 'Ginástica', 'Kids', 'Muculação', 'PK Sul'), validators=[DataRequired()])
        deseg = TimeField('De', format='%HH:%MM')
        ateseg = TimeField('Até', format='%HH:%MM')
        deter = TimeField('De', format='%HH:%MM')
        ateter = TimeField('Até', format='%HH:%MM')
        dequa = TimeField('De', format='%HH:%MM')
        atequa = TimeField('Até', format='%HH:%MM')
        dequi = TimeField('De', format='%HH:%MM')
        atequi = TimeField('Até', format='%HH:%MM')
        desex = TimeField('De', format='%HH:%MM')
        atesex = TimeField('Até', format='%HH:%MM')
        botao_enviar = SubmitField('Adicionar')


class CadastrarUsuario(FlaskForm):
    email = StringField('E-mail', validators=[Email(), DataRequired()])
    nome = StringField('Nome completo', validators=[DataRequired()])
    depart = SelectField('Departamento', choices=('','Unidade Park Sul - qualquer departamento','Kids','Musculação','Esportes e Lutas','Crossfit','Ginástica','Gestantes','Recepção','Financeiro','TI','RH','Marketing','Manutenção'), validators=[DataRequired()])
    cargo = SelectField('Cargo', choices=('','OAF Crossfit','OAF Dança','OAF Esportes Adulto','OAF Gestantes','OAF Ginástica','OAF Hidro','OAF Kids','OAF Lutas Adulto','OAF Musculação','OAF Natação','OAF Yoga','Aprendiz','Auxiliar Financeiro','Auxiliar TI','Auxiliar RH','Manutencista','Massagista','Monitora Kids','Recepcionista','Vendedora'), validators=[DataRequired()])
    remuneracao = StringField('Hr-aula/Salário', validators=[DataRequired()])
    whatsapp = StringField('Whatsapp', validators=[DataRequired()])
    admissao = DateField('Data de admissão', format='%d/%m/%Y', validators=[DataRequired()])
    botao_submit_cadastrousu = SubmitField('Enviar cadastro')


class CadastrarLote(FlaskForm):
    arquivo = FileField('Escolha o arquivo "xlsx".', validators=[FileAllowed(['xlsx'])])
    botao_submit_arq = SubmitField('Enviar arquivo')




class HorariosLote(FlaskForm):
    arquivo = FileField('Escolha o arquivo "xlsx".', validators=[FileAllowed(['xlsx'])])
    botao_submit_horarios = SubmitField('Enviar arquivo')
