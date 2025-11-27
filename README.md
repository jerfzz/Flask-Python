# 🧩 Flask - Lista de Tarefas

Projeto desenvolvido durante o **curso de Programação em Python**, com o objetivo de aprender os fundamentos do framework **Flask** e a criação de aplicações web dinâmicas.

A aplicação consiste em uma **lista de tarefas simples (To-Do List)**, onde o usuário pode adicionar e visualizar suas tarefas em uma interface web.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3**
- 🌶️ **Flask** — Framework web minimalista
- 🧱 **HTML5 / CSS3** — Estrutura e estilo da página
- 🧩 **Jinja2** — Template engine integrada ao Flask

---

## 💡 Funcionalidades

- Adicionar novas tarefas via formulário;
- Exibir todas as tarefas cadastradas;
- (Opcionalmente) remover tarefas, se implementado posteriormente;
- Interface simples e responsiva, com foco em usabilidade.

---

## 📂 Estrutura do Projeto

```

Flask-Python/
├── app.py               # Arquivo principal do Flask
├── templates/
│   └── index.html       # Página HTML com a interface da lista de tarefas
├── static/              # (opcional) Pasta para CSS e JS, se necessário
└── README.md

````

---

## 🧭 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/jerfzz/Flask-Python.git
cd Flask-Python
````

### 2️⃣ Criar e ativar um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```

### 3️⃣ Instalar as dependências

```bash
pip install flask
```

### 4️⃣ Executar o servidor Flask

```bash
python app.py
```

### 5️⃣ Acessar no navegador

Abra o endereço:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥️ Exemplo da Interface

A página inicial apresenta um campo de entrada para novas tarefas e uma lista com as tarefas atuais:

```html
<form method="POST">
    <label>Nova Tarefa:</label>
    <input type="text" name="tarefa" required>
    <button type="submit">Adicionar</button>
</form>

<ul>
    {% for tarefa in tarefas %}
        <li>{{ tarefa }}</li>
    {% endfor %}
</ul>
```

---

## 📘 Aprendizados

Durante o desenvolvimento deste projeto, foram estudados:

* Estrutura básica de uma aplicação Flask;
* Criação de rotas (`@app.route`);
* Utilização de métodos HTTP (`GET` e `POST`);
* Renderização de templates com variáveis (`render_template`);
* Manipulação de listas no backend.

---

## 🧑‍💻 Autor

**Jerferson (jerfzz)**
🔗 [GitHub](https://github.com/jerfzz)

---

## 🪪 Licença

Este projeto é de livre uso para fins educacionais e de aprendizado.
Sinta-se à vontade para clonar, modificar e aprimorar. 🚀

```
