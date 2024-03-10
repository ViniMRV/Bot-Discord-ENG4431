from flask import Flask, redirect,request,jsonify, render_template, flash, session, url_for
import uuid
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import secrets

load_dotenv()

mongo_url = os.getenv("MONGO_URL")

app = Flask(__name__)
app.secret_key = "chavebraba"
client = MongoClient(mongo_url)

db = client.db_name
registro_logs = db.logs
registro_usuarios = db.usuarios

tokens = {}

try:
  client.admin.command("ping")
  print("conexão com o banco realizada")
except Exception as e:
  print("erro: " + str(e))

@app.route('/logs')
def list_all():
  try:
    logs = list(registro_logs.find({}))
    return jsonify(logs), 200
  except Exception as e:
    return {"error": str(e)}, 400

@app.route('/logs', methods=["POST"])
def create_log():
  body = request.json
  body["_id"] = str(uuid.uuid4().hex)

  try:
    registro_logs.insert_one(body)
    return jsonify(body), 201
  except Exception as e:
    return {"error": str(e)}, 400

@app.route('/logs/<id>')
def read_log(id):
  try:
    body = registro_logs.find_one({"_id": id})
    if body:
      return jsonify(body), 200
    else:
      return {"error": "Log não encontrado"}, 404
  except Exception as e:
    return {"error": str(e)}, 400

@app.route('/logs/<id>', methods=["PUT"])
def update_log(id):
  try:
    body = request.json
    body["_id"] = id
    registro_logs.replace_one({"_id": id}, body)
    return {"message": "Log atualizada com sucesso"}, 200
  except Exception as e:
    return {"error": str(e)}, 400

@app.route('/logs/<id>', methods=["DELETE"])
def delete_log(id):
  try:
    registro_logs.delete_one({"_id": id})
    return {"message": "Log deletado com sucesso"}, 404
  except Exception as e:
    return {"error": str(e)}, 400

@app.route('/cadastro',methods = ["GET","POST"])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		existing_user = registro_usuarios.find_one({'username': username})
		if existing_user:
			flash('O nome de usuário já está em uso. Escolha outro.', 'danger')
		else:
			new_user = {'username': username, 'password': password}
			registro_usuarios.insert_one(new_user)
			flash('Registro bem-sucedido! ', 'success')
			return render_template("pos.html",message = "Cadastro bem sucedido")
	return render_template('register.html')

@app.route('/login', methods=["POST"])
def login():
  if request.method == 'POST':
      dados = request.json
      username = dados["username"]
      password = dados["password"]
      user = registro_usuarios.find_one({'username': username, 'password': password})
      
      if user:
        session['username'] = username
        return {"username":username,"password":password},200
          
      else:
        return {"message":'Credenciais inválidas. Tente novamente.'},400
  
  return render_template('login.html')


    
  
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)

