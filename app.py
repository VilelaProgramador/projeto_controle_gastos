from flask import Flask, render_template, request, redirect
import csv
import os 
from collections import defaultdict
import matplotlib.pyplot as plt

app = Flask(__name__) 
ARQUIVO = 'gastos.csv'


if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['descricao', 'valor', 'data', 'categoria', 'tipo'])

@app.route("/")
def index():
    gastos = []
    receitas = {}
    despesas = {}
    total_receitas = 0
    total_despesas = 0

    with open(ARQUIVO, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            gastos.append(row)
            valor = float(row['valor'])

            if row['tipo'].lower() == 'receita':
                receitas[row['categoria']] = receitas.get(row['categoria'], 0) + valor
                total_receitas += valor
            else:
                despesas[row['categoria']] = despesas.get(row['categoria'], 0) + valor
                total_despesas += valor

    saldo = total_receitas - total_despesas

    gerar_graficos(gastos)  
    return render_template(
        'index.html',
        gastos=gastos,
        receitas=receitas,
        despesas=despesas,
        total_receitas=total_receitas,
        total_despesas=total_despesas,
        saldo=saldo
    )

@app.route("/adicionar", methods=["POST"])
def adicionar():
    descricao = request.form["descricao"]
    valor = float(request.form["valor"])
    data = request.form["data"]
    categoria = request.form["categoria"]
    tipo = request.form["tipo"]

    with open(ARQUIVO, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([descricao, valor, data, categoria, tipo])

    return redirect("/")


def gerar_graficos(gastos):
    receitas = defaultdict(float)
    despesas = defaultdict(float)

    for g in gastos:
        valor = float(g['valor'])
        if g['tipo'].lower() == 'receita':
            receitas[g['categoria']] += valor
        else:
            despesas[g['categoria']] += valor

    if receitas:
        categorias = list(receitas.keys())
        valores = list(receitas.values())
        plt.figure(figsize=(6,6))
        plt.pie(valores, labels=categorias, autopct='%1.1f%%')
        plt.title('Receitas por Categoria')
        plt.savefig('static/receitas.png')
        plt.close()

    if despesas:
        categorias = list(despesas.keys())
        valores = list(despesas.values())
        plt.figure(figsize=(6, 6))
        plt.pie(valores, labels=categorias, autopct='%1.1f%%')
        plt.title('Despesas por Categoria')
        plt.savefig('static/despesas.png')
        plt.close()

if __name__ == '__main__':
    app.run(debug=True)