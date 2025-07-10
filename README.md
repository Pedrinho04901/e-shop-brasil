# Projeto E-Shop Brasil - Advanced Databases and Big Data
# 🛒 Projeto E-Shop Brasil - Advanced Databases and Big Data

## 📘 Introdução

A **E-Shop Brasil** é uma das maiores plataformas de comércio eletrônico do país. Com o crescimento exponencial de clientes e pedidos, surgiram desafios relacionados à **gestão de dados**, **personalização da experiência do usuário** e **otimização da logística**.

Este projeto foi desenvolvido no contexto da disciplina **Advanced Databases and Big Data**, utilizando tecnologias modernas como **MongoDB**, **Streamlit**, **Plotly**, **Docker** e **Faker**, para simular um ambiente real de análise e gestão de dados.

---

## 🎯 Objetivos

- ✅ Garantir a **segurança e privacidade** dos dados dos clientes.
- ✅ Personalizar a **experiência de navegação e compra** com base no comportamento do usuário.
- ✅ Melhorar a **eficiência da entrega e controle de estoques** em tempo real.
- ✅ Aplicar conceitos de **NoSQL, Big Data e visualização interativa** de forma prática.
- ✅ Utilizar soluções **escaláveis e sustentáveis** com tecnologias open-source e ambientes conteinerizados.

---

## 🗂️ Estrutura do Projeto

```bash
e-shop-brasil-projeto/
├── app.py                # Aplicação Streamlit com operações em MongoDB
├── docker-compose.yml    # Inicialização do container MongoDB com persistência de dados
├── README.md             # Documentação completa do projeto
└── exemplos/             # Imagens, gráficos e prints de funcionalidades (opcional)
🚀 Tecnologias Utilizadas
Tecnologia	Papel no Projeto
MongoDB	Banco de dados NoSQL para armazenar produtos e pedidos
Streamlit	Interface web interativa para inserção, manipulação e visualização
Plotly	Geração de gráficos dinâmicos e interativos
Faker	Geração de dados falsos realistas para testes
Docker	Isolamento e padronização do ambiente (MongoDB)

🧪 Funcionalidades da Aplicação
📥 Inserção de Produtos no banco via formulário.

✏️ Edição e exclusão de dados diretamente pela interface.

🧪 Geração de dados falsos para testes (produtos e pedidos).

📊 Visualização interativa:

Gráfico de evolução de pedidos por dia.

Comparativo de vendas por produto.

Alerta visual para produtos com estoque baixo.

🔎 Consultas dinâmicas em tempo real via interface gráfica.

🧰 Como Executar o Projeto
🔧 Pré-requisitos
Python 3.8+

Docker + Docker Compose

Streamlit: instale com pip install streamlit

[Faker, Pymongo, Plotly]: instale com:
pip install pymongo faker plotly
🐳 Subindo o MongoDB com Docker
No terminal, na raiz do projeto:
docker-compose up -d
Isso irá:

Baixar a imagem oficial do MongoDB

Criar o container mongo_e_shop

Disponibilizar a porta 27017 localmente

### ● Comandos necessários para configurar e executar o ambiente:

1. **Subir a infraestrutura com Docker Compose**

```bash
docker-compose up -d
```

Isso irá:
- Baixar a imagem oficial do MongoDB
- Criar o container `mongo_e_shop`
- Disponibilizar a porta `27017` localmente

Verifique se está rodando com:

```bash
docker ps
```

2. **Executar a aplicação Streamlit (`app.py`)**

Com o terminal aberto na pasta do projeto:

```bash
streamlit run app.py
```

Depois, abra seu navegador em: [http://localhost:8501](http://localhost:8501)

📸 Exemplos de Uso
Imagens demonstrando o funcionamento da aplicação. Estão disponíveis na pasta exemplos/:

Funcionalidade	Print
Inserir produto	
Editar produto	
Gerar pedidos	
Gráfico: evolução de pedidos	
Gráfico: vendas por produto		

📌 Observações
O MongoDB armazena os dados em duas coleções: estoque e pedidos.

A aplicação simula pedidos com timestamps e quantidade variável.

O alerta de estoque aparece automaticamente para produtos com menos de 10 unidades.

O projeto pode ser facilmente estendido para dashboards com ferramentas como Power BI, Metabase ou Grafana.

👨‍🎓 Conclusão
Este projeto aplica de forma prática os conceitos centrais da disciplina:

Modelagem de dados NoSQL com MongoDB

Manipulação e visualização em tempo real com Streamlit

Geração e análise de Big Data com ferramentas escaláveis

Automação de ambiente com Docker

📚 Trabalho referente à disciplina: Advanced Databases and Big Data
🎓 Aluno: Pedro Fortunato
🏫 Instituição: Unifecaf
