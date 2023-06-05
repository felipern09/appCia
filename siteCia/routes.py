from siteCia import app, database, cadastro  # , bcrypt
from siteCia import Usuario, Post, Comentario, Curtida, Unidade, SolicitacaoFerias, Substituicoes
from siteCia import FormLogin, CadastrarAutonomo, CadastrarEstagiario, CadastrarFuncionario, TipoColaborador, \
    FormCriarPost, FormAlterarSenha, FormAlterarEmail, FormAlterarUser, FormAlterarInsta, FormAlterarLinkedin, \
    FormAlterarTt, AlterarFoto, FormCriarComent, Substituir, MsgPrivada, DataFerias, MontarGrade, CadastrarUsuario, \
    CadastrarLote, HorariosLote
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from datetime import datetime
from PIL import Image
from siteCia import Calcular
from siteCia import contatos_colab as contatos
from flask_mobility import Mobility


Mobility(app)


def salvar_imagempost(imagemp):
    codigop = secrets.token_hex(8)
    nomep, extensaop = os.path.splitext(imagemp.filename)
    nome_arqp = nomep + codigop + extensaop
    caminho_completop = os.path.join(app.root_path, 'static/fotos_post', nome_arqp)
    tamanhop = (550, 550)
    imagem_reduzidap = Image.open(imagemp)
    imagem_reduzidap.thumbnail(tamanhop)
    imagem_reduzidap.save(caminho_completop)
    return nome_arqp


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    posts = Post.query.order_by(Post.id.desc()).all()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    curt = Curtida.query.filter_by(id_post_curt=Post.id).filter_by(id_quem_curtiu=current_user.id).all()
    id_autor = ''
    formpost = FormCriarPost()
    foto_autor = ''
    foto = ''
    comentario = ''
    foto_coment=''
    for post in posts:
        formpost = FormCriarPost()
        comentario = post.comentario
        foto_coment = Comentario.query.filter_by(id_post=post.id).all()
        foto_autor = url_for('static', filename=f'/fotos_perfil/{post.autor.foto_perfil}')
        foto = url_for('static', filename=f'/fotos_post/{post.foto_post}')
        id_autor = post.autor.id
        curt = Curtida.query.filter_by(id_post_curt=post.id).filter_by(id_quem_curtiu=current_user.id).all()
        if 'botao_submit_post' in request.form:
            if formpost.imagem.data is None:
                foto = ''
            else:
                foto = salvar_imagempost(formpost.imagem.data)
            post = Post(corpo=formpost.corpo.data, foto_post=foto, autor=current_user)
            database.session.add(post)
            database.session.commit()
            return redirect(url_for('home'))
    if 'botao_submit_post' in request.form:
        if formpost.imagem.data:
            foto = salvar_imagempost(formpost.imagem.data)
        post = Post(corpo=formpost.corpo.data, foto_post=foto, autor=current_user)
        database.session.add(post)
        database.session.commit()
        return redirect(url_for('home'))
    if 'True' in request.get_data(as_text=True):
        data = request.get_json()
        post_id = data['post_id']
        curtida = Curtida(id_post_curt=post_id, id_quem_curtiu=current_user.id)
        database.session.add(curtida)
        database.session.commit()
        return redirect(url_for('home'))
    if 'False' in request.get_data(as_text=True):
        data = request.get_json()
        post_id = data['post_id']
        curtida = Curtida.query.filter_by(id_post_curt=post_id).filter_by(id_quem_curtiu=current_user.id).first()
        database.session.delete(curtida)
        database.session.commit()
        return redirect(url_for('home'))

    return render_template('home.html', foto_perfil=foto_perfil, formpost=formpost,
                           posts=posts, foto_autor=foto_autor, foto_post=foto, id_autor=id_autor, comentario=comentario,
                           foto_coment=foto_coment, curt=curt, dispositivo=dispositivo)


@app.route('/noticias', methods=['GET', 'POST'])
@login_required
def noticias():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    posts = Post.query.filter_by(id_usuario=136).order_by(Post.id.desc()).all()
    id_autor = ''
    formpost = FormCriarPost()
    foto_autor = ''
    foto = ''
    comentario = ''
    foto_coment=''

    for post in posts:
        formpost = FormCriarPost()
        comentario = post.comentario
        foto_coment = Comentario.query.filter_by(id_post=post.id).all()
        foto_autor = url_for('static', filename=f'/fotos_perfil/{post.autor.foto_perfil}')
        foto = url_for('static', filename=f'/fotos_post/{post.foto_post}')
        id_autor = post.autor.id
        if 'botao_submit_post' in request.form:
            if formpost.imagem.data is None:
                foto = ''
            else:
                foto = salvar_imagempost(formpost.imagem.data)
            post = Post(corpo=formpost.corpo.data, foto_post=foto, autor=current_user)
            database.session.add(post)
            database.session.commit()
            return redirect(url_for('home'))
    if 'botao_submit_post' in request.form:
        if formpost.imagem.data:
            foto = salvar_imagempost(formpost.imagem.data)
        post = Post(corpo=formpost.corpo.data, foto_post=foto, autor=current_user)
        database.session.add(post)
        database.session.commit()
        return redirect(url_for('home'))

    return render_template('noticias.html', foto_perfil=foto_perfil, formpost=formpost,
                           posts=posts, foto_autor=foto_autor, foto_post=foto, id_autor=id_autor, comentario=comentario,
                           foto_coment=foto_coment, dispositivo=dispositivo)


@app.route('/home/excluirpost/<post_id>', methods=['GET', 'POST'])
@login_required
def excluirpost(post_id):
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    formpost = FormCriarPost()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    post = Post.query.get(post_id)
    foto_autor = url_for('static', filename=f'fotos_perfil/{post.autor.foto_perfil}')
    return render_template('excl_post.html', post=post, foto_perfil=foto_perfil, formpost=formpost, foto_autor=foto_autor,
                           dispositivo=dispositivo)


@app.route('/home/excluirpost/<post_id>/terminate', methods=['GET', 'POST'])
def terminate(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor or current_user.tipo_usuario == 'master' or current_user.tipo_usuario == 'presidente'\
            or current_user.tipo_usuario == 'diretor':
        database.session.delete(post)
        database.session.commit()
        return redirect(url_for('home'))


@app.route('/gentevideos', methods=['GET', 'POST'])
@login_required
def videos():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('gentevideos.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/gentetextos', methods=['GET', 'POST'])
@login_required
def textos():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    posts = Post.query.filter_by(id_usuario=137).order_by(Post.id.desc()).all()
    id_autor = ''
    formpost = FormCriarPost()
    foto_autor = ''
    foto = ''
    comentario = ''
    foto_coment = ''

    for post in posts:
        formpost = FormCriarPost()
        comentario = post.comentario
        foto_coment = Comentario.query.filter_by(id_post=post.id).all()
        foto_autor = url_for('static', filename=f'/fotos_perfil/{post.autor.foto_perfil}')
        foto = url_for('static', filename=f'/fotos_post/{post.foto_post}')
        id_autor = post.autor.id
        if 'botao_submit_post' in request.form:
            if formpost.imagem.data is None:
                foto = ''
            else:
                foto = salvar_imagempost(formpost.imagem.data)
            post = Post(corpo=formpost.corpo.data, foto_post=foto, autor=current_user)
            database.session.add(post)
            database.session.commit()
            return redirect(url_for('home'))
    if 'botao_submit_post' in request.form:
        if formpost.imagem.data:
            foto = salvar_imagempost(formpost.imagem.data)
        post = Post(corpo=formpost.corpo.data, foto_post=foto, autor=current_user)
        database.session.add(post)
        database.session.commit()
        return redirect(url_for('home'))

    return render_template('gentetextos.html', foto_perfil=foto_perfil, formpost=formpost,
                           posts=posts, foto_autor=foto_autor, foto_post=foto, id_autor=id_autor, comentario=comentario,
                           foto_coment=foto_coment, dispositivo=dispositivo)


@app.route('/documentos', methods=['GET', 'POST'])
@login_required
def documentos():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('documentos.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/docpessoal', methods=['GET', 'POST'])
@login_required
def docpess():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('docpessoal.html', foto_perfil=foto_perfil,dispositivo=dispositivo)


@app.route('/atestados', methods=['GET', 'POST'])
@login_required
def atest():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('atestados.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/ir', methods=['GET', 'POST'])
@login_required
def comprov_ir():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('ir.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/folha', methods=['GET', 'POST'])
@login_required
def pagamentos():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('folha.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/previa', methods=['GET', 'POST'])
@login_required
def previa():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuario = Calcular(current_user)
    if current_user.remuneracao == 'Horista':
        usuario.hosrista()
        dias = usuario.dias
        dias_st = usuario.dias_st
        horas = usuario.horas
        hoje = usuario.data
        diasemana = usuario.semana
        somahoras = usuario.soma_carga
        salario = usuario.salario
        salariof = 'R$ {:,.2f}'.format(salario).replace(',','_').replace('.',',').replace('_','.')
        sal = 'R$ {:,.2f}'.format(salario-salario*0.075, 2).replace(',','_').replace('.',',').replace('_','.')
    else:
        usuario.mensalista()
        dias = usuario.dias
        dias_st = usuario.dias_st
        horas = usuario.horas
        hoje = usuario.data
        diasemana = usuario.semana
        somahoras = usuario.soma_carga
        salario = usuario.salario
        salariof = 'R$ {:,.2f}'.format(salario).replace(',','_').replace('.',',').replace('_','.')
        sal = 'R$ {:,.2f}'.format(salario-salario*0.075, 2).replace(',','_').replace('.',',').replace('_','.')

    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('previa.html', foto_perfil=foto_perfil, dias=dias, dias_st=dias_st, horas=horas, somahoras=somahoras,
                           salariof=salariof, sal=sal, hoje=hoje, diasemana=diasemana, dispositivo=dispositivo)


@app.route('/ferias', methods=['GET', 'POST'])
@login_required
def ferias():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    formferias = DataFerias()
    inicio_min = appCia.calculo_ferias.inicio_min1
    inicio_format = appCia.calculo_ferias.inicio_format
    fim_max = appCia.calculo_ferias.fim_max
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')

    return render_template('ferias.html', foto_perfil=foto_perfil, inicio_min=inicio_min, inicio_format=inicio_format,
                           fim_max=fim_max, formferias=formferias, dispositivo=dispositivo)


@app.route('/feriasrecibos', methods=['GET', 'POST'])
@login_required
def rec_ferias():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    pedidos = SolicitacaoFerias.query.all()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('recibosferias.html', foto_perfil=foto_perfil, pedidos=pedidos, dispositivo=dispositivo)


@app.route('/desempenho', methods=['GET', 'POST'])
@login_required
def desempenho():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuario = Usuario.query.get(current_user.id)
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('avdesemp.html', foto_perfil=foto_perfil, usuario=usuario, dispositivo=dispositivo)


@app.route('/grade', methods=['GET', 'POST'])
@login_required
def grade():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuario = Usuario.query.get(current_user.id)
    form_grade = MontarGrade()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('grade.html', foto_perfil=foto_perfil, usuario=usuario, form_grade=form_grade, dispositivo=dispositivo)


@app.route('/gradedeptos', methods=['GET', 'POST'])
@login_required
def gradedeptos():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuarios = Usuario.query.all()
    usuario = Usuario.query.get(current_user.id)
    deptos = []
    for usuario in usuarios:
        if usuario.depart not in deptos:
            deptos.append(usuario.depart)
    deptos.remove('Corporativo')
    deptos.remove('Recepção')
    deptos.remove('Administrativo')
    deptos.remove('Park Sul')
    deptos.remove('Child Care')
    deptos.remove('Manutenção')
    dpto = sorted(deptos)

    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('gradedeptos.html', foto_perfil=foto_perfil, usuario=usuario, deptos=deptos, dispositivo=dispositivo)


@app.route('/avaliacdesemp', methods=['GET', 'POST'])
@login_required
def aval_desempenho():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('avaliacao.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/avaliactecn', methods=['GET', 'POST'])
@login_required
def aval_tecn():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('avaliacaotecn.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/', methods=['GET', 'POST'])
def login():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        # senha_cript = bcrypt.generate_password_hash(usuario.senha)
        if usuario and usuario.senha == form_login.senha.data:
            login_user(usuario, remember=form_login.lembrar_dados.data)
            return redirect(url_for('home'))
        # elif usuario and bcrypt.check_password_hash(senha_cript, form_login.senha.data):
        #     login_user(usuario, remember=form_login.lembrar_dados.data)
        #     return redirect(url_for('home'))
        else:
            flash(f'Falha no login. E-mail ou usuário incorretos.', 'alert-danger')

    return render_template('login.html', form_login=form_login, dispositivo=dispositivo)


@app.route('/tipocolab', methods=['GET', 'POST'])
def tipo():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_tipo = TipoColaborador()
    return render_template('tipocolaborador.html', form_tipo=form_tipo, dispositivo=dispositivo)


@app.route('/cadastroest', methods=['GET', 'POST'])
def cadastroest():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_est = CadastrarEstagiario()
    if 'botao_submit_cadastroE' in request.form:
        cadastro.estagiario()
        return redirect(url_for('login')), flash('Cadastro enviado com sucesso!', 'alert-success')
    return render_template('cadastroest.html', form_est=form_est, dispositivo=dispositivo)


@app.route('/cadastrofun', methods=['GET', 'POST'])
def cadastrofunc():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_func = CadastrarFuncionario()
    if 'botao_submit_cadastroF' in request.form:
        cadastro.funcionario()
        return redirect(url_for('login')), flash('Cadastro enviado com sucesso!', 'alert-success')
    return render_template('cadastro.html', form_func=form_func, dispositivo=dispositivo)


@app.route('/cadastroaut', methods=['GET', 'POST'])
def cadastroaut():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_aut = CadastrarAutonomo()
    if 'botao_submit_cadastroA' in request.form:
        cadastro.autonomo()
        return redirect(url_for('login')), flash('Cadastro enviado com sucesso!', 'alert-success')
    return render_template('cadastroaut.html', form_aut=form_aut, dispositivo=dispositivo)


@app.route('/vt', methods=['GET', 'POST'])
@login_required
def vt():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('vt.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/adiant', methods=['GET', 'POST'])
@login_required
def adiant():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('adiant.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


def salvar_imagemperf(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arq = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arq)
    tamanho = (240, 240)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return nome_arq


@app.route('/perfiledit', methods=['GET', 'POST'])
@login_required
def editarperf():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_foto = AlterarFoto()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    if 'botao_submitfoto' in request.form:
        nome_imagem = salvar_imagemperf(form_foto.novafoto.data)
        current_user.foto_perfil = nome_imagem
        database.session.commit()
        return redirect(url_for('editarPerf'))
    return render_template('editarPerfil.html', foto_perfil=foto_perfil, form_foto=form_foto, dispositivo=dispositivo)


@app.route('/perfil/user', methods=['GET', 'POST'])
@login_required
def editaruser():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_foto = AlterarFoto()
    form_user = FormAlterarUser()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('editaruser.html', foto_perfil=foto_perfil, form_user=form_user, form_foto=form_foto, dispositivo=dispositivo)


@app.route('/perfil/senha', methods=['GET', 'POST'])
@login_required
def editarsenha():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_foto = AlterarFoto()
    form_senha = FormAlterarSenha()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    if form_senha.validate_on_submit() and 'botao_submit_senha' in request.form:
        current_user.senha = form_senha.novasenha.data
        database.session.commit()
        flash('Senha alterada com sucesso!', 'alert-success')
        return redirect(url_for('editarPerf'))
    else:
        return render_template('editarsenha.html', foto_perfil=foto_perfil, form_senha=form_senha, form_foto=form_foto, dispositivo=dispositivo)


@app.route('/perfil/email', methods=['GET', 'POST'])
@login_required
def editaremail():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_foto = AlterarFoto()
    form_email = FormAlterarEmail()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    if form_email.validate_on_submit() and 'botao_submit_nemail' in request.form:
        current_user.email = form_email.novoemail.data
        database.session.commit()
        flash(f'E-mail alterado com sucesso para {form_email.novoemail.data}!', 'alert-success')
        return redirect(url_for('editarPerf'))
    else:
        return render_template('editaremail.html', foto_perfil=foto_perfil, form_email=form_email, form_foto=form_foto, dispositivo=dispositivo)


@app.route('/perfil/linkedin', methods=['GET', 'POST'])
@login_required
def editarlinkedin():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_foto = AlterarFoto()
    form_linkedin = FormAlterarLinkedin()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')

    if form_linkedin.validate_on_submit() and 'botao_submit_linkedin' in request.form:
        current_user.linkedin = form_linkedin.novolinkedin.data
        database.session.commit()
        flash(f'Linkedin alterado com sucesso para {form_linkedin.novolinkedin.data}!', 'alert-success')
        return redirect(url_for('editarPerf'))
    else:
        return render_template('editarlinkedin.html', foto_perfil=foto_perfil, dispositivo=dispositivo, form_linkedin=form_linkedin,
                               form_foto=form_foto)


@app.route('/perfil/insta', methods=['GET', 'POST'])
@login_required
def editarinsta():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_foto = AlterarFoto()
    form_insta = FormAlterarInsta()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    if form_insta.validate_on_submit() and 'botao_submit_insta' in request.form:
        current_user.insta = form_insta.novoinsta.data
        database.session.commit()
        flash(f'Instagram alterado com sucesso para {form_insta.novoinsta.data}!', 'alert-success')
        return redirect(url_for('editarPerf'))
    else:
        return render_template('editarinsta.html', foto_perfil=foto_perfil, dispositivo=dispositivo, form_insta=form_insta, form_foto=form_foto)


@app.route('/perfil/tt', methods=['GET', 'POST'])
@login_required
def editartt():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    form_foto = AlterarFoto()
    form_tt = FormAlterarTt()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    if form_tt.validate_on_submit() and 'botao_submit_tt' in request.form:
        current_user.twitter = form_tt.novott.data
        database.session.commit()
        flash(f'Instagram alterado com sucesso para {form_tt.novott.data}!', 'alert-success')
        return redirect(url_for('editarPerf'))
    else:
        return render_template('editartt.html', foto_perfil=foto_perfil, dispositivo=dispositivo, form_tt=form_tt, form_foto=form_foto)


@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    lista = Usuario.query.order_by(Usuario.nome).all()
    mensagem = Post.query.all()
    form_msg = MsgPrivada()
    for item in lista:
        nome = item.nome
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('perfil.html', foto_perfil=foto_perfil, lista=lista, dispositivo=dispositivo, nome=nome, mensagem=mensagem, form_msg=form_msg)


@app.route('/perfilof/<usuario_id>')
@login_required
def perfilof(usuario_id):
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuario = Usuario.query.get(usuario_id)
    form_msg = MsgPrivada()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('perfilof.html', foto_perfil=foto_perfil, dispositivo=dispositivo, usuario=usuario, form_msg=form_msg)


@app.route('/comentar/<post>', methods=['GET', 'POST'])
@login_required
def comentar(post):
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    formcoment = FormCriarComent()
    post = Post.query.get(post)
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    foto = url_for('static', filename=f'/fotos_post/{post.foto_post}')
    if 'botao_submit_coment' in request.form:
        coment = Comentario(corpo_coment=formcoment.corpo.data, dispositivo=dispositivo, id_post=post.id, autor_coment=current_user.id)
        database.session.add(coment)
        database.session.commit()
        return redirect(url_for('home'))
    return render_template('comentar.html', foto_perfil=foto_perfil, dispositivo=dispositivo, foto_post=foto, post=post, formcoment=formcoment)


@app.route('/colaboradores', methods=['GET', 'POST'])
@login_required
def colab():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    plan = contatos.salvar(usuarios)
    funcionarios = len(Usuario.query.filter_by(contrato='CLT').all())
    estagiarios = len(Usuario.query.filter_by(contrato='Estágio').all())
    pj = len(Usuario.query.filter_by(contrato='PJ').all())
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('colab.html', foto_perfil=foto_perfil, dispositivo=dispositivo, usuarios=usuarios, funcionarios=funcionarios,
                           estagiarios=estagiarios, pj=pj)


@app.route('/admcolab', methods=['GET', 'POST'])
@login_required
def admcolab():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    funcionarios = len(Usuario.query.filter_by(contrato='CLT').all())
    estagiarios = len(Usuario.query.filter_by(contrato='Estágio').all())
    pj = len(Usuario.query.filter_by(contrato='PJ').all())
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('admcolab.html', foto_perfil=foto_perfil, dispositivo=dispositivo, usuarios=usuarios, funcionarios=funcionarios,
                           estagiarios=estagiarios, pj=pj)


@app.route('/gestaofolha', methods=['GET', 'POST'])
@login_required
def gerirfolha():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    unidade = Unidade.query.get(current_user.unidade)
    dpto = []
    for usuario in usuarios:
        if usuario.depart not in dpto:
            dpto.append(usuario.depart)
    dpto.remove('Corporativo')
    dpto = sorted(dpto)
    numfunc = {}
    for dpt in dpto:
        qtidade = len(Usuario.query.filter_by(depart=dpt).all())
        numfunc[dpt] = qtidade
    media={'Administrativo': '5,7k', 'Child Care': '5,4K', 'Cross': '8,5k','Esportes': '12,8k', 'Ginástica':'10k',
    'Kids':'30k', 'Manutenção':'7k','Musculação':'15,5k', 'Park Sul':'17,3k', 'Recepção':' 25,8k'}
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('gerirfolha.html', foto_perfil=foto_perfil, dpto=dpto, current_user=current_user,
                           unidade=unidade, numfunc=numfunc, dispositivo=dispositivo, media=media)


@app.route('/custos', methods=['GET', 'POST'])
@login_required
def custos():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('custos.html', foto_perfil=foto_perfil, dispositivo=dispositivo)


@app.route('/substit', methods=['GET', 'POST'])
@login_required
def substituicao():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    substit = Substituir()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    if 'botao_enviar' in request.form:
        subs = Substituicoes(id_solicitante=current_user.id, nome_substituto=substit.substituto.data,
                             inicio_subs=datetime.strptime(substit.dt_inicio.raw_data[0], '%Y-%m-%d'),
                             fim_subs=datetime.strptime(substit.dt_fim.raw_data[0], '%Y-%m-%d'),
                             departamento_aula=substit.depto.data)
        database.session.add(subs)
        database.session.commit()
        return redirect(url_for('substituicao'))
    if 'True' in request.get_data(as_text=True):
        print('pedido autorizado')
        data = request.get_json()
        botao_id = int(str(data['botao_id']).replace('_ok', ''))
        pedidosubs = Substituicoes.query.get(botao_id)
        pedidosubs.analisada = 'True'
        pedidosubs.autorizada = 'True'
        database.session.add(pedidosubs)
        database.session.commit()
        return redirect(url_for('substituicao'))
    if 'False' in request.get_data(as_text=True):
        data = request.get_json()
        botao_id = int(str(data['botao_id']).replace('_ok', ''))
        pedidosubs = Substituicoes.query.get(botao_id)
        pedidosubs.analisada = 'True'
        pedidosubs.autorizada = 'False'
        database.session.add(pedidosubs)
        database.session.commit()
        return redirect(url_for('substituicao'))

    pedido = Substituicoes.query.filter_by(id_solicitante=current_user.id).all()
    solicit = Substituicoes.query.all()
    return render_template('substit.html', foto_perfil=foto_perfil, dispositivo=dispositivo, form_substit=substit, pedido=pedido, solicit=solicit)


@app.route('/inclusao', methods=['GET', 'POST'])
@login_required
def incluirusuario():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    cadastrar = CadastrarUsuario()
    lote = CadastrarLote()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('incluirusuario.html', foto_perfil=foto_perfil, dispositivo=dispositivo, form_cadastrar=cadastrar, form_lote=lote)


@app.route('/horarios', methods=['GET', 'POST'])
@login_required
def alterarhorarios():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if 'iphone' in user_agent or 'android' in user_agent:
        dispositivo = 'mobile'
    elif 'windows' in user_agent:
        dispositivo = 'desktop'
    horarioslote = HorariosLote()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('alterarhorarios.html', foto_perfil=foto_perfil, dispositivo=dispositivo, form_horarioslote=horarioslote)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    return redirect(url_for('login'))
