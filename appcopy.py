
# 1 - Importar
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "Banco de dados" - Lista (Persistência de dados)
lista_tarefas = [
    "Aprender funcões DAX do Power BI",
    "Cursar programação em python para Data Science",
    "Cursar programação em R para Data Science"
]


# Rotas - senai.com/aluno
# Rota Padrão
# GET - Listar, POST - Cadastrar
@app.route("/", methods=['GET','POST'])
def index():

    # Se ele quer cadastrar:
    if request.method == 'POST':
        nova_tarefa = request.form['tarefa']

        #Adiciono a nova tarefa na lista
        lista_tarefas.append(nova_tarefa)

        #Redireciono para o index (recarrega a página)
        return redirect(url_for('index'))


    return render_template("index.html", tarefas=lista_tarefas)


if __name__ == '__main__':
    app.run(debug=True)