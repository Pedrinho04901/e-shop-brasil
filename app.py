import streamlit as st
from pymongo import MongoClient
from faker import Faker
import plotly.express as px
import pandas as pd
from bson.objectid import ObjectId

# Configuração MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['e_shop']
colecao_estoque = db['estoque']
colecao_pedidos = db['pedidos']

# Produtos iniciais
produtos_iniciais = [
    {"nome": "Smartphone XYZ", "quantidade": 50, "preco": 1999.90},
    {"nome": "Notebook ABC", "quantidade": 30, "preco": 3499.00},
    {"nome": "Fone Bluetooth", "quantidade": 100, "preco": 299.99},
    {"nome": "Camiseta Casual", "quantidade": 150, "preco": 59.90},
    {"nome": "Relógio Digital", "quantidade": 80, "preco": 499.90}
]

def popula_estoque_inicial():
    if colecao_estoque.count_documents({}) == 0:
        colecao_estoque.insert_many(produtos_iniciais)

popula_estoque_inicial()

fake = Faker()
st.title("Projeto E-Shop Brasil - Gestão de Estoque e Pedidos")

# Flags para atualizar
if 'update_estoque' not in st.session_state:
    st.session_state.update_estoque = False
if 'update_pedidos' not in st.session_state:
    st.session_state.update_pedidos = False

# --- FUNÇÕES ---

def listar_produtos():
    produtos = list(colecao_estoque.find())
    if not produtos:
        st.info("Nenhum produto cadastrado ainda.")
        return pd.DataFrame()
    else:
        df = pd.DataFrame(produtos)
        df = df.drop(columns=['_id'])
        df.insert(0, 'ID', range(1, len(df) + 1))
        st.dataframe(df)
        return df

def inserir_produto(nome, qtd, preco):
    colecao_estoque.insert_one({"nome": nome, "quantidade": qtd, "preco": preco})
    st.session_state.update_estoque = True

def editar_produto(id_, nome, qtd, preco):
    colecao_estoque.update_one({"_id": ObjectId(id_)}, {"$set": {"nome": nome, "quantidade": qtd, "preco": preco}})
    st.session_state.update_estoque = True

def excluir_produto(id_):
    colecao_estoque.delete_one({"_id": ObjectId(id_)})
    st.session_state.update_estoque = True

def gerar_produtos_falsos(n=5):
    for _ in range(n):
        inserir_produto(fake.word().capitalize(), fake.random_int(1, 100), round(fake.random_number(digits=4)/100,2))
    st.success("Produtos falsos gerados com sucesso!")

def listar_pedidos():
    pedidos = list(colecao_pedidos.find())
    if not pedidos:
        st.info("Nenhum pedido cadastrado ainda.")
        return pd.DataFrame()
    else:
        df = pd.DataFrame(pedidos)
        df = df.drop(columns=['_id'])
        df.insert(0, 'ID', range(1, len(df) + 1))
        st.dataframe(df)
        return df

def gerar_pedidos_falsos(n=10):
    produtos = list(colecao_estoque.find())
    if not produtos:
        st.warning("Crie produtos primeiro para gerar pedidos.")
        return
    for _ in range(n):
        produto = fake.random.choice(produtos)
        colecao_pedidos.insert_one({
            "produto": produto["nome"],
            "quantidade": fake.random_int(1, max(1, produto["quantidade"])),
            "timestamp": fake.date_time_this_year()
        })
    st.session_state.update_pedidos = True
    st.success("Pedidos falsos gerados com sucesso!")

# --- SEÇÕES ---

st.header("Inserir Produto no Estoque")
with st.form("form_inserir_produto"):
    nome = st.text_input("Nome do Produto")
    qtd = st.number_input("Quantidade", min_value=0, step=1)
    preco = st.number_input("Preço (R$)", min_value=0.0, step=0.01, format="%.2f")
    enviar = st.form_submit_button("Adicionar Produto")
if enviar:
    if nome.strip() == "":
        st.error("Nome do produto não pode ser vazio.")
    else:
        inserir_produto(nome, qtd, preco)
        st.success(f"Produto '{nome}' inserido com sucesso!")

# Atualizar visualização
if st.session_state.update_estoque:
    df_estoque = listar_produtos()
    st.session_state.update_estoque = False
else:
    df_estoque = listar_produtos()

if st.button("Gerar Produtos Falsos para Teste"):
    gerar_produtos_falsos()

# Editar / Excluir Produto
st.subheader("Editar ou Excluir Produto")
if not df_estoque.empty:
    ids = [str(p['_id']) for p in colecao_estoque.find()]
    nomes = [p['nome'] for p in colecao_estoque.find()]
    produto_selecionado = st.selectbox("Selecione um produto", nomes)
    index = nomes.index(produto_selecionado)
    id_sel = ids[index]
    atual = colecao_estoque.find_one({"_id": ObjectId(id_sel)})

    with st.form("form_editar"):
        nome_edit = st.text_input("Nome", value=atual["nome"])
        qtd_edit = st.number_input("Quantidade", value=int(atual["quantidade"]), min_value=0)
        preco_edit = st.number_input("Preço (R$)", value=float(atual["preco"]), min_value=0.0, format="%.2f")
        botao_editar = st.form_submit_button("Editar Produto")
        botao_excluir = st.form_submit_button("Excluir Produto")

    if botao_editar:
        editar_produto(id_sel, nome_edit, qtd_edit, preco_edit)
        st.success("Produto editado com sucesso!")

    if botao_excluir:
        excluir_produto(id_sel)
        st.success("Produto excluído com sucesso!")

# Pedidos
st.header("Pedidos")
if st.button("Gerar Pedidos Falsos para Teste"):
    gerar_pedidos_falsos()

if st.session_state.update_pedidos:
    df_pedidos = listar_pedidos()
    st.session_state.update_pedidos = False
else:
    df_pedidos = listar_pedidos()

# --- VISUALIZAÇÕES ---

st.header("Visualizações")

if not df_pedidos.empty:
    df_pedidos["timestamp"] = pd.to_datetime(df_pedidos["timestamp"])
    df_pedidos = df_pedidos.sort_values("timestamp")

    pedidos_por_data = df_pedidos.groupby(df_pedidos["timestamp"].dt.date)["quantidade"].sum().rename("Total Vendido")
    fig1 = px.line(pedidos_por_data, title="Evolução Temporal de Pedidos (Quantidade Total Vendida por Dia)")
    st.plotly_chart(fig1)

    compras_por_produto = df_pedidos.groupby("produto")["quantidade"].sum().reset_index(name="Total Vendido")
    fig2 = px.bar(compras_por_produto, x="produto", y="Total Vendido", title="Quantidade Total Vendida por Produto")
    st.plotly_chart(fig2)

if not df_estoque.empty:
    baixo_estoque = df_estoque[df_estoque["quantidade"] < 10]
    if not baixo_estoque.empty:
        st.warning("Produtos com estoque baixo (<10 unidades):")
        st.dataframe(baixo_estoque)
    else:
        st.success("Nenhum produto com estoque baixo!")
