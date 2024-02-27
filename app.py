import pandas as pd
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def home():
  return "Olá mundo!"

@app.route("/BuscarVendas/CodigoProduto/<codigoProduto>")
def buscarDadosVendas(codigoProduto : int):
  produto = buscarVendasPorProduto(codigoProduto)
  return produto


def buscarVendasPorProduto(idProduto : int):
  tabelaDados = pd.read_csv('./Db/tabelaProdutos.csv')
  print("Tabela dados:")
  print(tabelaDados)

  print(f"IdProduto:{idProduto}")
  
  nomeProduto = tabelaDados.values[int(idProduto)][0]
  precoProduto = tabelaDados.values[int(idProduto)][1]

  response = {'NomeProduto': nomeProduto, 'Preco': precoProduto}
  return jsonify(response)

print("API startou")