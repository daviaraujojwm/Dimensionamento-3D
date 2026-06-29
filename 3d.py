import streamlit as st
import pandas as pd
from io import BytesIO
import plotly.graph_objects as go
import math
import base64
import streamlit.components.v1 as components


# 🔥 PRIMEIRA COISA
st.set_page_config(
    page_title="Cubagem de Veículos JWM - 3D",
    layout="wide",
    initial_sidebar_state="expanded"
)
components.html("""
<script>
const doc = window.parent.document;

doc.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
}, true);

doc.addEventListener('keydown', function(e) {

    if (
        e.key === 'F12' ||
        (e.ctrlKey && e.shiftKey && e.key.toLowerCase() === 'i') ||
        (e.ctrlKey && e.shiftKey && e.key.toLowerCase() === 'j') ||
        (e.ctrlKey && e.key.toLowerCase() === 'u')
    ) {
        e.preventDefault();
        return false;
    }

}, true);
</script>
""", height=0)

def carregar_imagem_base64(caminho):
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode()

login_bg = carregar_imagem_base64("telalogin.png")



USUARIOS = {
    "admin": "1234",
    "jwm": "jwm123"
}

if "logado" not in st.session_state:
    st.session_state.logado = False


if not st.session_state.logado:

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{login_bg}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .main .block-container,
    .block-container {{
        max-width: 560px !important;
        width: 560px !important;
        margin: 30px auto 0 auto !important;
        padding: 42px 38px 36px 38px !important;

        border-radius: 34px !important;
        background: rgba(255,255,255,0.075) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;

        border: 1px solid rgba(255,255,255,0.55) !important;

        box-shadow:
            0 0 18px rgba(255,255,255,0.95),
            0 0 48px rgba(255,255,255,0.45),
            0 0 90px rgba(255,255,255,0.22),
            inset 0 0 26px rgba(255,255,255,0.10) !important;
    }}

    .login-title {{
        font-size: 42px;
        font-weight: 900;
        color: white;
        text-align: center;
        margin-bottom: 12px;
    }}

    .login-sub {{
        text-align: center;
        color: rgba(255,255,255,0.92);
        font-size: 18px;
        margin-bottom: 18px;
        line-height: 1.45;
    }}

    label {{
        color: white !important;
        font-weight: 600 !important;
    }}

.stTextInput {{
    width: 100% !important;
    margin-bottom: 10px !important;
}}

div[data-testid="stTextInputRootElement"] {{
    height: 58px !important;
    border-radius: 14px !important;
    background: #2a2a38 !important;
    border: 1px solid rgba(255,255,255,.35) !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    overflow: hidden !important;
}}
div[data-testid="stTextInputRootElement"]:focus-within {{

    border: 1px solid #444 !important;

    box-shadow: none !important;

    outline: none !important;
}}

.stTextInput > div > div,
.stTextInput > div > div:hover,
.stTextInput > div > div:focus-within {{

    background: #2f313d !important;

    border: 1px solid #444 !important;

    box-shadow: none !important;

    outline: none !important;

    transform: none !important;
}}

.stTextInput input {{
    height: 58px !important;
    background: transparent !important;
    border: none !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    padding-left: 22px !important;
    box-shadow: none !important;
    outline: none !important;
}}

.stTextInput input:hover,
.stTextInput input:focus {{
    box-shadow: none !important;
    border: none !important;
}}

.stTextInput input::placeholder {{
    color: rgba(255,255,255,.65) !important;
}}

.stTextInput input::placeholder {{
    color: rgba(255,255,255,.75) !important;
}}

    @keyframes buttonGlowPulse {{

        0% {{
            box-shadow:
                0 0 15px rgba(240,18,78,.60),
                0 0 35px rgba(240,18,78,.35),
                0 0 70px rgba(42,0,136,.25);
        }}

        50% {{
            box-shadow:
                0 0 25px rgba(240,18,78,1),
                0 0 60px rgba(240,18,78,.75),
                0 0 120px rgba(42,0,136,.60);
        }}

        100% {{
            box-shadow:
                0 0 15px rgba(240,18,78,.60),
                0 0 35px rgba(240,18,78,.35),
                0 0 70px rgba(42,0,136,.25);
        }}
    }}
div[data-testid="stButton"] {{

    width: 100% !important;

    margin-top: 12px !important;

    display: flex !important;

    justify-content: center !important;
}}

div[data-testid="stButton"] button {{

    width: 62% !important;

    height: 62px !important;

    border-radius: 18px !important;

    border: 2px solid rgba(255,255,255,.65) !important;

    background: linear-gradient(
        90deg,
        #F0124E 0%,
        #C0007A 50%,
        #2A0088 100%
    ) !important;

    color: white !important;

    font-size: 26px !important;

    font-weight: 800 !important;

    box-shadow:
        0 0 18px rgba(255,255,255,.35),
        0 0 35px rgba(240,18,78,.55),
        0 0 70px rgba(42,0,136,.45) !important;

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        filter .25s ease !important;
}}

div[data-testid="stButton"] button:hover {{

    transform: translateY(-4px) scale(1.05);

    filter: brightness(1.18);

    box-shadow:
        0 0 25px rgba(255,255,255,.60),
        0 0 60px rgba(240,18,78,.90),
        0 0 120px rgba(42,0,136,.80) !important;
}}

div[data-testid="stButton"] button:active {{

    transform: scale(.97);
}}

    header,
    #MainMenu,
    footer {{
        visibility: hidden;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="login-title">Dimencionamento 3D</div>
        <div class="login-sub">
            <b>Bem-vindo de volta!</b><br>
            Faça login para acessar sua conta.
        </div>
    """, unsafe_allow_html=True)

    usuario = st.text_input("Usuário", placeholder="Usuário")
    senha = st.text_input("Senha", type="password", placeholder="Senha")

    entrar = st.button("Entrar", use_container_width=True)

    st.markdown("""
        <div style="text-align:center; color:white; margin-top:24px;">
            Criado pela <b style="color:#F0124E;">JWM Soluções Logísticas</b>
        </div>
    """, unsafe_allow_html=True)

    if entrar:
        if usuario in USUARIOS and senha == USUARIOS[usuario]:
            st.session_state.logado = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.stop()
# CSS
st.markdown("""
<style>
...
</style>
""", unsafe_allow_html=True)

MAX_CAIXAS = 300
MAX_CAIXAS_3D = 200
MAX_ITERACOES = 12000
MAX_GRID = 12000
MAX_RENDER_3D = 80
MAX_ORIENTACOES = 6


def carregar_imagem_base64(caminho):
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = carregar_imagem_base64("tela de fundo.png")

st.markdown("""
<style>
/* ============================
   FUNDO
============================ */
.header-jwm{
    position:absolute;

    top:-300px;
    left:40px;

    display:flex;
    align-items:center;
    gap:28px;

    z-index:99999;

    pointer-events:none;
}

.logo-jwm{
    width:90px;
    height:auto;
}

.titulo-jwm{
    font-size:24px;
    font-weight:800;
    color:white;
    white-space:nowrap;

    text-shadow:
        0 0 15px rgba(0,0,0,.95);
}
            /* menu superior direito */
#MainMenu {
    visibility: hidden;
}

/* DEIXA O HEADER INVISÍVEL, MAS MANTÉM O BOTÃO DO SIDEBAR */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
    min-height: 0px !important;
}

/* MANTÉM O HEADER/TOOLBAR EXISTINDO PARA O SIDEBAR FUNCIONAR */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 42px !important;
}

/* DEIXA O TOOLBAR VISÍVEL */
[data-testid="stToolbar"] {
    visibility: visible !important;
    opacity: 1 !important;
    display: flex !important;
}

/* ESCONDE APENAS OS BOTÕES DA DIREITA */
[data-testid="stToolbar"] > div:not(:first-child) {
    display: none !important;
}

/* BOTÃO DO SIDEBAR */
[data-testid="collapsedControl"] {
    visibility: visible !important;
    opacity: 1 !important;
    display: flex !important;
    position: fixed !important;
    top: 10px !important;
    left: 14px !important;
    z-index: 9999999 !important;
}

/* ESCONDE MENU PADRÃO E FOOTER */
#MainMenu,
footer {
    visibility: hidden !important;
}

/* REMOVE ESPAÇO SOBRANDO NO TOPO */
[data-testid="stAppViewContainer"] > .main {
    padding-top: 0 !important;
}

.block-container {
    margin-top: 260px !important;
}
            :root{
    --background-color:#0b0f17;
    --secondary-background-color:#141824;
    --text-color:#ffffff;
}

/* força fundo escuro */
html,
body{
    color:#ffffff !important;
}

/* containers */
[data-testid="stVerticalBlock"],
[data-testid="stForm"]{
    color:#ffffff !important;
}
.stApp {
    background-image: url("data:image/png;base64,""" + bg_img + """");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.05);
    z-index: 0;
    pointer-events:none;
}

/* ============================
   CONTAINER PRINCIPAL (CARD)
============================ */
.block-container {
    position: relative;
    z-index: 1;

    max-width: 95%;
    height: auto;

    margin: 300px auto 20px auto;

    padding: 20px 25px;

    background: rgba(10, 12, 18, 0.58);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);

    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.22);
    box-shadow: 0 6px 30px rgba(0,0,0,0.22);

    overflow: visible;

    animation: subirSuave 1.2s ease-out;
}

.main .block-container {
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}

/* ============================
   TEXTOS
============================ */
label {
    color: #f1f1f1 !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.6);
    font-weight: 500;
}
.stTextInput > div > div {

    background: #2f313d !important;

    border: 1px solid #444 !important;

    border-radius: 8px !important;

    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;

    box-shadow: none !important;
}

.stTextInput input {

    background: transparent !important;

    color: white !important;

    font-size: 16px !important;

    font-weight: 500 !important;

    height: 54px !important;

    box-shadow: none !important;

    border: none !important;
}

.stTextInput input:focus {

    box-shadow: none !important;

    outline: none !important;
}

/* INPUTS DE TEXTO */
.stTextInput input{

    height:54px !important;

    color:white !important;

    font-size:16px !important;

    font-weight:600 !important;

    padding-left:22px !important;

    line-height:54px !important;

    transform:translateY(-10px) !important;

    background:transparent !important;

    border:none !important;
    outline:none !important;
    box-shadow:none !important;
}

/* QUANTIDADE */
.stNumberInput input{

    height:54px !important;

    color:white !important;

    font-size:16px !important;

    font-weight:600 !important;

    line-height:54px !important;

    transform:translateY(-2px) !important;

    background:transparent !important;

    border:none !important;
    outline:none !important;
    box-shadow:none !important;
}

.stTextInput input::placeholder{

    color:rgba(255,255,255,.75) !important;

    font-size:16px !important;
    font-weight:600 !important;

    line-height:54px !important;
}

.stTextInput input::placeholder{

    color:rgba(255,255,255,.75) !important;
}

/* HOVER */

.stTextInput:hover > div > div{

    border:1px solid #444 !important;

    box-shadow:none !important;

    transform:none !important;
}

/* ============================
   ESPAÇAMENTO ENTRE ELEMENTOS
============================ */
.stTextInput, 
.stNumberInput, 
.stSelectbox {
    margin-bottom: 18px;
}

h1, h2, h3 {
    color: #ffffff;
    text-shadow: 0 2px 6px rgba(0,0,0,0.5);
    margin-top: 25px;
    margin-bottom: 15px;
}

/* ============================
   BOTÕES
============================ */
.stButton button {
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
    transition: 0.2s;
}

.stButton button:hover {
    transform: scale(1.03);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

/* ============================
   TÍTULO GRADIENTE
============================ */
.titulo-gradient {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #ff0000, #cc0000, #990000);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
@keyframes subirSuave{
    from{
        opacity:0;
        transform:translateY(80px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

html{
    scroll-behavior:smooth;
}
/* ============================
   RESPONSIVIDADE
============================ */
@media (max-width: 768px) {
    .block-container {
        padding: 20px !important;
    }
}
/* SIDEBAR GLASS */

section[data-testid="stSidebar"]{
    background: rgba(15, 18, 25, 0.55) !important;

    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);

    border-right: 1px solid rgba(255,255,255,0.08);

    box-shadow: none;
}
/* REMOVE LINHA INTERNA DOS INPUTS */

.stTextInput input,
.stTextInput input:hover,
.stTextInput input:focus,
.stTextInput input:active {

    border: none !important;
    outline: none !important;
    box-shadow: none !important;
}

/* REMOVE FOCUS DO STREAMLIT */

div[data-testid="stTextInputRootElement"],
div[data-testid="stTextInputRootElement"]:hover,
div[data-testid="stTextInputRootElement"]:focus-within {

    outline: none !important;
    box-shadow: none !important;
}

/* REMOVE LINHA INFERIOR */

div[data-testid="stTextInputRootElement"]::before,
div[data-testid="stTextInputRootElement"]::after {

    display: none !important;
    content: none !important;
}
</style>
""", unsafe_allow_html=True)


# ============================
# SESSION STATE INIT
# ============================

if "df_result" not in st.session_state or not isinstance(st.session_state.df_result, pd.DataFrame):
    st.session_state.df_result = pd.DataFrame(columns=[
        "Veículo",
        "Status",
        "Motivo",
        "Aproveitamento (%)",
        "Aproveitamento Peso (%)",
        "Score"
    ])
    
if "veiculo_simulado" not in st.session_state:
    st.session_state.veiculo_simulado = None

# ============================
# SIDEBAR
# ============================
if st.sidebar.button("🚪 Sair"):
    st.session_state.logado = False
    st.rerun()
st.sidebar.title("📘 Instruções de Uso")
st.sidebar.write(
    """
Preencha as dimensões, peso e quantidade do material.
Você pode adicionar várias cargas.

⚠️ Digite os valores em **metros**.
Use vírgula ou ponto para decimais.

### 1️⃣ Adicione a carga
Informe dimensões, peso e quantidade e clique em **➕ Adicionar carga**.

### 2️⃣ Empilhamento
📦 Ativado: permite empilhar as cargas.

📦 Desativado: considera apenas o piso do veículo.

### 3️⃣ Escolha os veículos
Selecione veículos específicos ou deixe em branco para testar toda a frota.

### 4️⃣ Calcule
Clique em **🚀 Calcular Resultado 3D**.

### 5️⃣ Resultado
O sistema exibirá:

🚛 Veículo recomendado

📦 Caixas alocadas

📊 Ocupação do veículo

⚖️ Aproveitamento de peso

📏 Espaço livre (comprimento, largura e altura)

### 💡 Critério
O sistema sempre busca o **menor veículo capaz de transportar 100% da carga**.
"""
)

# ============================
# BASE DE VEÍCULOS
# ============================
lista_veiculos = [

    {
        "nome": "FIORINO",
        "largura": 1.32,
        "comprimento": 1.82,
        "altura": 1.20,
        "peso_max": 650
    },

    {
        "nome": "VUC",
        "largura": 2.20,
        "comprimento": 4.90,
        "altura": 2.40,
        "peso_max": 8500
    },

    {
        "nome": "TOCO",
        "largura": 2.40,
        "comprimento": 6.80,
        "altura": 2.50,
        "peso_max": 16000
    },

    {
        "nome": "TRUCK",
        "largura": 2.60,
        "comprimento": 10.50,
        "altura": 2.63,
        "peso_max": 23000
    }

]

# ============================
# DATAFRAME DE VEÍCULOS (ESSENCIAL)
# ============================
@st.cache_data(show_spinner=False)
def get_veiculos():

    df = pd.DataFrame(lista_veiculos)

    df["Volume Bruto"] = (
        df["largura"]
        * df["comprimento"]
        * df["altura"]
    )

    df["Area Piso"] = (
        df["largura"]
        * df["comprimento"]
    )

    df.rename(
        columns={"nome": "Veículo"},
        inplace=True
    )

    df["fator"] = (
        df["Veículo"].apply(get_fator)
    )

    df["eficiencia"] = (
        df["Veículo"].apply(get_eficiencia)
    )

    return df
    
# ============================
# FUNÇÃO GLOBAL DE FATOR
# ============================
def get_fator(nome):

    nome = str(nome).upper()

    if "FIORINO" in nome:
        return 0.95

    elif "VUC" in nome:
        return 0.92

    elif "TOCO" in nome:
        return 0.90

    elif "TRUCK" in nome:
        return 0.88

    return 0.90


def get_eficiencia(nome):

    nome = str(nome).upper()

    if "TRUCK" in nome:
        return 0.85

    elif "TOCO" in nome:
        return 0.82

    elif "VUC" in nome:
        return 0.80

    elif "FIORINO" in nome:
        return 0.75

    return 0.80

# =====================================
# DATAFRAME GLOBAL DE VEÍCULOS
# =====================================
df_veiculos = get_veiculos()

# =====================================
# HELPER GLOBAL DE VOLUME
# =====================================
def volume_veiculo(veic):
    return (
        veic["largura"]
        * veic["comprimento"]
        * veic["altura"]
    )

# ============================
# SESSION STATE
# ============================
if "cargas" not in st.session_state:
    st.session_state.cargas = []


# HEADER SUPERIOR
st.markdown(f"""
<div class="header-jwm">
    <div class="titulo-jwm">
        Dimensionamento 3D
    </div>
</div>
""", unsafe_allow_html=True)

# PAINEL PRINCIPAL
st.markdown('<div class="main-container">', unsafe_allow_html=True)
# ============================
# INPUTS CARGA
# ============================

st.subheader("📦 Adicionar carga")

col1, col2, col3, col4, col5 = st.columns(
    [1.2, 1.2, 1.2, 1.2, 0.8],
    gap="large"
)

with col1:
    comp_txt = st.text_input(
        "Comprimento (m)",
        key="comp",
        placeholder="ex: 1,20 ou 1.20"
    )

with col2:
    larg_txt = st.text_input(
        "Largura (m)",
        key="larg",
        placeholder="ex: 0,80 ou 0.80"
    )

with col3:
    alt_txt = st.text_input(
        "Altura (m)",
        key="alt",
        placeholder="ex: 1,00"
    )

with col4:
    peso_txt = st.text_input(
        "Peso unitário (kg)",
        key="peso",
        placeholder="ex: 15,5"
    )

with col5:
    qtd = st.number_input(
        "Quantidade:",
        min_value=1,
        value=1,
        step=1,
        key="qtd"
    )

empilhavel_carga = st.toggle(
    "📦 Esta carga pode ser empilhada?",
    value=True
)



def parse_float(valor):
    try:
        if valor is None:
            return None
        valor = str(valor).strip().replace(",", ".")
        if valor == "":
            return None
        return round(float(valor), 4)
    except:
        return None

# 🔥 SÓ DEPOIS DISSO
comp = parse_float(comp_txt)
larg = parse_float(larg_txt)
alt = parse_float(alt_txt)
peso = parse_float(peso_txt)

# VALIDAÇÃO DE INPUTS

def validar_inputs(comp, larg, alt, peso, qtd=None):
    """
    Valida dimensões, peso e quantidade da carga.
    Retorna lista de erros (vazia se válido).
    """

    erros = []

    def invalido(valor):
        try:
            return valor is None or float(valor) <= 0
        except Exception:
            return True

    # Comprimento
    if invalido(comp):
        erros.append("Comprimento inválido")
    elif comp < 0.05:
        erros.append("Comprimento muito pequeno")

    # Largura
    if invalido(larg):
        erros.append("Largura inválida")
    elif larg < 0.01:
        erros.append("Largura muito pequena")

    # Altura
    if invalido(alt):
        erros.append("Altura inválida")
    elif alt < 0.01:
        erros.append("Altura muito pequena")

    # Peso
    if invalido(peso):
        erros.append("Peso inválido")

    # Quantidade
    if qtd is not None:
        try:
            if int(qtd) <= 0:
                erros.append("Quantidade inválida")
        except Exception:
            erros.append("Quantidade inválida")

    return erros
#.

col1, col2, col3, col4, col5 = st.columns(
    [1.2, 1.2, 1.2, 1.2, 0.8],
    gap="large"
)

erros = validar_inputs(comp, larg, alt, peso, qtd)

if erros and (comp_txt or larg_txt or alt_txt or peso_txt):
    st.error(" | ".join(erros))

# aviso de performance
if qtd > 1000:
    st.warning("⚠ Quantidade muito alta pode impactar a performance.")

pode_adicionar = len(erros) == 0

# ========================================
# ✅ BOTÃO DE ADICIONAR CARGA
# ========================================

if st.button("➕ Adicionar carga", disabled=not pode_adicionar):

    total_caixas = sum(
        int(c["Quantidade"])
        for c in st.session_state.cargas
    ) + int(qtd)

    if total_caixas > MAX_CAIXAS:
        st.error(f"❌ Limite máximo permitido: {MAX_CAIXAS} caixas no total.")
        st.stop()

    st.session_state.cargas.append({
        "Comprimento (m)": comp,
        "Largura (m)": larg,
        "Altura (m)": alt,
        "Peso unitário (kg)": peso,
        "Quantidade": qtd,
        "Volume total (m³)": comp * larg * alt * qtd,
        "Peso total (kg)": peso * qtd,
        "Empilhável": empilhavel_carga
    })

    st.rerun()
    
# ============================
# LISTA E EDIÇÃO DE CARGAS
# ============================

if st.session_state.cargas:

    st.subheader("📋 Cargas adicionadas (Editáveis)")

    df_cargas_edit = pd.DataFrame(st.session_state.cargas)

    df_editado = st.data_editor(
        df_cargas_edit,
        use_container_width=True,
        num_rows="dynamic",
        key="editor_cargas",
        hide_index=True
    )

    col1, col2, col3 = st.columns(3)

    # 💾 SALVAR ALTERAÇÕES
    with col1:
        if st.button("💾 Salvar alterações"):
            try:
                novas_cargas = []

                colunas_esperadas = [
                    "Comprimento (m)", "Largura (m)", "Altura (m)",
                    "Peso unitário (kg)", "Quantidade", "Empilhável"
                ]
                
                for col in colunas_esperadas:
                    if col not in df_editado.columns:
                        raise ValueError(f"Coluna obrigatória ausente: {col}")

                for _, row in df_editado.iterrows():

                    # 🔒 garante tipo numérico
                    try:
                        if pd.isna(row["Comprimento (m)"]):
                            raise ValueError("Campo vazio.")
                        comp = float(row["Comprimento (m)"])
                        larg = float(row["Largura (m)"])
                        alt = float(row["Altura (m)"])
                        peso = float(row["Peso unitário (kg)"])
                    except Exception as e:
                        raise ValueError("Valores inválidos na tabela.")
                    
                    if comp <= 0 or larg <= 0 or alt <= 0:
                        raise ValueError("Dimensões inválidas.")
                    
                    if peso <= 0:
                        raise ValueError("Peso inválido.")
                                        
                    vol_unit = comp * larg * alt
                    
                    try:
                        qtd_row = int(row["Quantidade"])
                    except Exception as e:
                        raise ValueError("Quantidade inválida.")
                                        
                    if qtd_row <= 0:
                        raise ValueError("Quantidade inválida.")
                    peso_total = peso * qtd_row
                    
                    novas_cargas.append({
                        "Comprimento (m)": comp,
                        "Largura (m)": larg,
                        "Altura (m)": alt,
                        "Peso unitário (kg)": peso,
                        "Quantidade": qtd_row,
                        "Volume total (m³)": vol_unit * qtd_row,
                        "Peso total (kg)": peso_total,
                        "Empilhável": bool(row.get("Empilhável", True))
                    })
                    
                total_editado = sum(
                    int(c["Quantidade"])
                    for c in novas_cargas
                )

                if total_editado > MAX_CAIXAS:
                    raise ValueError(
                        f"Limite máximo permitido: {MAX_CAIXAS} caixas no total."
                    )
                
                st.session_state.cargas = novas_cargas
                st.success("Alterações salvas com sucesso!")
                st.rerun()

            except Exception as e:
                st.error(f"Erro ao salvar alterações: {e}")

    # ❌ LIMPAR CARGA UNITÁRIA
    with col2:
        if len(df_editado) > 0:
            if not df_editado.empty:
            
                linha_para_excluir = st.selectbox(
                    "Selecione a carga para excluir:",
                    options=range(len(df_editado)),
                    format_func=lambda i: f"Carga {i+1}"
                )
            
                if st.button("❌ Excluir carga selecionada"):
                    del st.session_state.cargas[linha_para_excluir]
                    st.rerun()
else:
    st.info("Nenhuma carga adicionada ainda.")

# ============================
# SELEÇÃO DE VEÍCULOS
# ============================
todos_nomes = df_veiculos["Veículo"].tolist()

selecionados = st.multiselect(
    "🚛 Selecione veículos específicos (ou deixe vazio para testar todos):",
    todos_nomes
)

# ============================
# AUXILIARES
# ============================
@st.cache_data(show_spinner=False)
def expand_cargas_unitarias(cargas, limite=MAX_CAIXAS):
    """
    Expande cargas agregadas em unidades individuais.
    Retorna lista de caixas unitárias.
    """
    lista = []

    for c in cargas:
        try:
            qtd = int(c["Quantidade"])
            comp = float(c["Comprimento (m)"])
            larg = float(c["Largura (m)"])
            alt = float(c["Altura (m)"])
            peso = float(c["Peso unitário (kg)"])

            empilhavel = bool(
                c.get("Empilhável", True)
            )
        except Exception as e:
            continue

        if qtd <= 0 or min(comp, larg, alt, peso) <= 0:
            continue
        if qtd > 2000:
            qtd = 2000

        for _ in range(qtd):
            if len(lista) >= limite:
                return lista

            volume = comp * larg * alt

            if volume <= 0:
                continue
            
            densidade = peso / volume if volume > 0 else 0
            
            lista.append({
                "comp": comp,
                "larg": larg,
                "alt": alt,
                "peso": peso,
                "densidade": densidade,
                "volume": comp * larg * alt,
                "empilhavel": empilhavel
            })

    return lista

def calcular_totais_reais(cargas, empilhavel=True):

    volume = 0
    area = 0
    peso = 0

    for c in cargas:

        qtd = int(c["Quantidade"])

        comp = float(c["Comprimento (m)"])
        larg = float(c["Largura (m)"])
        alt = float(c["Altura (m)"])
        peso_unit = float(c["Peso unitário (kg)"])

        volume += comp * larg * alt * qtd
        area += comp * larg * qtd
        peso += peso_unit * qtd

    if empilhavel:
        return volume, peso
    else:
        return area, peso

GRID_SIZE = 1.0

def gerar_chave_grid(x, y, z):
    return (
        int(x // GRID_SIZE),
        int(y // GRID_SIZE),
        int(z // GRID_SIZE)
    )

def colide(nova, ocupadas):
    x, y, z, dx, dy, dz = nova
    for ox, oy, oz, odx, ody, odz in ocupadas:
        if (
            x < ox + odx and x + dx > ox and
            y < oy + ody and y + dy > oy and
            z < oz + odz and z + dz > oz
        ):
            return True
    return False


def tem_base(nova, ocupadas, suporte_min=0.7):

    x, y, z, dx, dy, dz = nova

    # chão
    if z == 0:
        return True

    area_caixa = dx * dy

    for ox, oy, oz, odx, ody, odz in ocupadas:

        # precisa estar exatamente sobre
        if abs((oz + odz) - z) > 0.001:
            continue

        overlap_x = max(
            0,
            min(x + dx, ox + odx) - max(x, ox)
        )

        overlap_y = max(
            0,
            min(y + dy, oy + ody) - max(y, oy)
        )

        area_suporte = overlap_x * overlap_y

        if area_suporte >= area_caixa * suporte_min:
            return True

    return False

def calcular_centro_massa(posicoes):
    if not posicoes:
        return 0

    soma = 0
    peso_total = 0

    for x, y, z, c, l, a in posicoes:

        centro_x = x + (c / 2)

        volume = c * l * a

        soma += centro_x * volume
        peso_total += volume

    if peso_total == 0:
        return 0

    return soma / peso_total
def simular_empilhamento_3d(
    cargas_unitarias,
    veiculo,
    qtd_total_real,
    limite_iter=MAX_ITERACOES,
    max_grid=MAX_GRID
):
    comp_veic = float(veiculo["comprimento"])
    larg_veic = float(veiculo["largura"])
    alt_veic = float(veiculo["altura"])
    peso_max = float(veiculo["peso_max"])

    estrategias = [
        "comprimento_menor",
        "largura_menor",
        "altura_menor",
        "comprimento_maior",
        "area_base_menor",
        "area_base_maior"
    ]

    melhor_posicoes = []
    melhor_peso = 0

    cargas_ordenadas = sorted(
        cargas_unitarias,
        key=lambda x: (-x["volume"], -x["peso"])
    )

    for estrategia in estrategias:

        posicoes = []
        peso_acumulado = 0

        espacos_livres = [
            (0, 0, 0, comp_veic, larg_veic, alt_veic)
        ]

        for item in cargas_ordenadas:

            if peso_acumulado + item["peso"] > peso_max:
                continue

            orientacoes = list(set([
                (item["comp"], item["larg"], item["alt"]),
                (item["comp"], item["alt"], item["larg"]),
                (item["larg"], item["comp"], item["alt"]),
                (item["larg"], item["alt"], item["comp"]),
                (item["alt"], item["comp"], item["larg"]),
                (item["alt"], item["larg"], item["comp"]),
            ]))

            orientacoes = [
                (
                    round(float(c), 4),
                    round(float(l), 4),
                    round(float(a), 4)
                )
                for c, l, a in orientacoes
                if c > 0 and l > 0 and a > 0
            ]

            if estrategia == "comprimento_menor":
                orientacoes = sorted(orientacoes, key=lambda d: (d[0], d[1], d[2]))

            elif estrategia == "largura_menor":
                orientacoes = sorted(orientacoes, key=lambda d: (d[1], d[0], d[2]))

            elif estrategia == "altura_menor":
                orientacoes = sorted(orientacoes, key=lambda d: (d[2], d[0], d[1]))

            elif estrategia == "comprimento_maior":
                orientacoes = sorted(orientacoes, key=lambda d: (-d[0], d[1], d[2]))

            elif estrategia == "area_base_menor":
                orientacoes = sorted(orientacoes, key=lambda d: (d[0] * d[1], d[2]))

            elif estrategia == "area_base_maior":
                orientacoes = sorted(orientacoes, key=lambda d: (-(d[0] * d[1]), d[2]))

            colocado = False

            espacos_livres = sorted(
                espacos_livres,
                key=lambda e: (e[2], e[1], e[0])
            )

            for idx, espaco in enumerate(espacos_livres):

                ex, ey, ez, ecomp, elarg, ealt = espaco

                for c, l, a in orientacoes:

                    if c > ecomp or l > elarg or a > ealt:
                        continue

                    if ex + c > comp_veic or ey + l > larg_veic or ez + a > alt_veic:
                        continue

                    if not item.get("empilhavel", True) and ez > 0:
                        continue

                    nova = (
                        round(ex, 4),
                        round(ey, 4),
                        round(ez, 4),
                        c,
                        l,
                        a
                    )

                    if colide(nova, posicoes):
                        continue

                    if not tem_base(nova, posicoes):
                        continue

                    posicoes.append(nova)
                    peso_acumulado += item["peso"]
                    colocado = True

                    espacos_livres.pop(idx)

                    sobra_comprimento = ecomp - c
                    sobra_largura = elarg - l
                    sobra_altura = ealt - a

                    if sobra_comprimento > 0.001:
                        espacos_livres.append((
                            ex + c,
                            ey,
                            ez,
                            sobra_comprimento,
                            elarg,
                            ealt
                        ))

                    if sobra_largura > 0.001:
                        espacos_livres.append((
                            ex,
                            ey + l,
                            ez,
                            c,
                            sobra_largura,
                            ealt
                        ))

                    if sobra_altura > 0.001:
                        espacos_livres.append((
                            ex,
                            ey,
                            ez + a,
                            c,
                            l,
                            sobra_altura
                        ))

                    espacos_livres = [
                        e for e in espacos_livres
                        if e[3] > 0.001 and e[4] > 0.001 and e[5] > 0.001
                    ]

                    if len(espacos_livres) > 1200:
                        espacos_livres = sorted(
                            espacos_livres,
                            key=lambda e: e[3] * e[4] * e[5],
                            reverse=True
                        )[:1200]

                    break

                if colocado:
                    break

        if len(posicoes) > len(melhor_posicoes):
            melhor_posicoes = posicoes
            melhor_peso = peso_acumulado

        if len(melhor_posicoes) == len(cargas_unitarias):
            break

    caixas_alocadas = len(melhor_posicoes)
    volume_usado = sum(
        c * l * a
        for _, _, _, c, l, a in melhor_posicoes
    )

    return melhor_posicoes, caixas_alocadas, volume_usado, melhor_peso

def executar_calculo(cargas, df_veiculos, selecionados, empilhavel=True):
    """
    Escolhe o menor veículo que consiga levar 100% da carga inteira.
    Sem combo.
    Sem ranking.
    Sem score.
    """

    if not cargas:
        return pd.DataFrame(), {"cenario": None}

    df_testar = (
        df_veiculos[df_veiculos["Veículo"].isin(selecionados)]
        if selecionados else df_veiculos.copy()
    )

    valor_total, peso_total = calcular_totais_reais(
        cargas,
        empilhavel=True
    )

    # ordena do menor para o maior
    df_testar = df_testar.sort_values(
        by=["Volume Bruto", "peso_max"],
        ascending=True
    ).reset_index(drop=True)

    for _, veic in df_testar.iterrows():

        nome = veic["Veículo"]

        # valida se cada carga cabe fisicamente com rotação
        carga_incompativel = False

        for carga in cargas:
            dim_carga = sorted([
                float(carga["Comprimento (m)"]),
                float(carga["Largura (m)"]),
                float(carga["Altura (m)"])
            ])

            dim_veiculo = sorted([
                veic["comprimento"],
                veic["largura"],
                veic["altura"]
            ])

            if any(c > v for c, v in zip(dim_carga, dim_veiculo)):
                carga_incompativel = True
                break

        if carga_incompativel:
            continue

        capacidade_max = (
            volume_veiculo(veic)
            * get_fator(nome)
            * get_eficiencia(nome)
        )

        peso_max = veic["peso_max"]

        print(
            nome,
            "Volume carga =", valor_total,
            "Capacidade =", capacidade_max,
            "Peso carga =", peso_total,
            "Peso max =", peso_max
        )

        peso_max = veic["peso_max"]

        if peso_total > peso_max:
            continue

        if valor_total > capacidade_max:
            continue

        qtd_total_real = sum(
            int(c["Quantidade"])
            for c in cargas
        )

        cargas_unitarias = expand_cargas_unitarias(
            cargas,
            limite=MAX_CAIXAS
        )

        posicoes_teste, caixas_alocadas, _, _ = simular_empilhamento_3d(
            cargas_unitarias,
            veic,
            qtd_total_real
        )

        if caixas_alocadas < qtd_total_real:
            continue

        aproveitamento_vol = min(100, (valor_total / capacidade_max) * 100)
        aproveitamento_peso = min(100, (peso_total / peso_max) * 100)

        return pd.DataFrame([{
            "Veículo": nome,
            "Status": "Viável",
            "Motivo": "Veículo comporta 100% da carga inteira.",
            "Aproveitamento (%)": round(aproveitamento_vol, 2),
            "Aproveitamento Peso (%)": round(aproveitamento_peso, 2),
            "Score": 100
        }]), {"cenario": "VEICULO_UNICO"}

    return pd.DataFrame([{
        "Veículo": "Nenhum",
        "Status": "Inviável",
        "Motivo": "Nenhum veículo único conseguiu levar 100% da carga.",
        "Aproveitamento (%)": 0,
        "Aproveitamento Peso (%)": 0,
        "Score": 0
    }]), {"cenario": None}

def limpar_dataframe(df):
    if df.empty:
        return df

    return df.replace(
        [float("inf"), -float("inf")],
        0
    ).fillna(0)
st.markdown("""
<script>

window.addEventListener('scroll', () => {

    const painel = document.querySelector('.block-container');

    if(!painel) return;

    const scroll = window.scrollY;

    painel.style.transform =
        `translateY(${scroll * 0.08}px)`;

});

</script>
""", unsafe_allow_html=True)
# ============================
# 🚀 CALCULAR E MOSTRAR SOMENTE 3D
# ============================

if st.button("🚀 Calcular Resultado 3D", disabled=not st.session_state.cargas):

    empilhavel = True

    with st.spinner("Calculando e gerando visualização 3D..."):

        df_result, meta = executar_calculo(
            st.session_state.cargas,
            df_veiculos,
            selecionados,
            empilhavel
        )

        st.session_state.df_result = limpar_dataframe(df_result)
        st.session_state.cenario = meta.get("cenario")

        if st.session_state.df_result.empty:
            st.error("Nenhum veículo conseguiu acomodar a carga.")
            st.stop()

        melhor_veiculo = st.session_state.df_result.iloc[0]["Veículo"]

        if melhor_veiculo == "Nenhum":

            valor_total_real = sum(
                c["Volume total (m³)"]
                for c in st.session_state.cargas
            )

            peso_total_real = sum(
                c["Peso total (kg)"]
                for c in st.session_state.cargas
            )

            sugestoes = []

            for _, veic_sug in df_veiculos.sort_values(
                by=["Volume Bruto", "peso_max"],
                ascending=True
            ).iterrows():

                nome_sug = veic_sug["Veículo"]

                capacidade_sug = (
                    volume_veiculo(veic_sug)
                    * get_fator(nome_sug)
                    * get_eficiencia(nome_sug)
                )

                if (
                    valor_total_real <= capacidade_sug
                    and peso_total_real <= veic_sug["peso_max"]
                ):

                    cargas_teste_sug = expand_cargas_unitarias(
                        st.session_state.cargas,
                        limite=MAX_CAIXAS
                    )

                    qtd_teste_sug = sum(
                        int(c["Quantidade"])
                        for c in st.session_state.cargas
                    )

                    _, caixas_sug, _, _ = simular_empilhamento_3d(
                        cargas_teste_sug,
                        veic_sug,
                        qtd_teste_sug
                    )

                    if caixas_sug == qtd_teste_sug:
                        sugestoes.append({
                            "Veículo": nome_sug,
                            "Capacidade útil (m³)": round(capacidade_sug, 2),
                            "Peso máximo (kg)": veic_sug["peso_max"]
                        })

            if sugestoes:
                sugestao = sugestoes[0]

                st.warning("⚠ Nenhum dos veículos selecionados conseguiu levar 100% da carga.")
                st.info(
                    f"Sugestão para levar 100% da carga: "
                    f"**{sugestao['Veículo']}**"
                )

                st.dataframe(
                    pd.DataFrame(sugestoes),
                    use_container_width=True
                )

            else:
                st.error("❌ Nenhum veículo da base consegue levar 100% da carga.")

            st.stop()

        if " + " in melhor_veiculo:
            st.error(
                "Nenhum veículo único conseguiu acomodar a carga."
            )
            st.stop()

        veic = df_veiculos[
            df_veiculos["Veículo"] == melhor_veiculo
        ].iloc[0]

        qtd_total_real = sum(
            int(c["Quantidade"])
            for c in st.session_state.cargas
        )

        cargas_unitarias = expand_cargas_unitarias(
            st.session_state.cargas,
            limite=MAX_CAIXAS
        )

        volume_total_veiculo = volume_veiculo(veic)

        valor_total_real = sum(
            c["Volume total (m³)"]
            for c in st.session_state.cargas
        )

        fator = get_fator(melhor_veiculo)
        eficiencia = get_eficiencia(melhor_veiculo)

        volume_ajustado = (
            volume_total_veiculo
            * eficiencia
            * fator
        )

        if valor_total_real > volume_ajustado:
            st.error("❌ O volume das caixas excede a capacidade física do veículo.")
            st.stop()

        posicoes, caixas, volume_usado, peso_usado = simular_empilhamento_3d(
            cargas_unitarias,
            veic,
            qtd_total_real
        )

        ocupacao = (
            min(100, (volume_usado / volume_ajustado) * 100)
            if volume_ajustado > 0 else 0
        )

        comprimento_usado = max(
            x + c for x, y, z, c, l, a in posicoes
        ) if posicoes else 0

        largura_usada = max(
            y + l for x, y, z, c, l, a in posicoes
        ) if posicoes else 0

        altura_usada = max(
            z + a for x, y, z, c, l, a in posicoes
        ) if posicoes else 0

        comprimento_livre = max(0, veic["comprimento"] - comprimento_usado)
        largura_livre = max(0, veic["largura"] - largura_usada)
        altura_livre = max(0, veic["altura"] - altura_usada)
        volume_livre = max(0, volume_ajustado - volume_usado)
    st.subheader("📦 Resultado 3D da Cubagem")

    st.success(f"🚛 Veículo Selecionado: {melhor_veiculo}")

    peso_percentual = (
        min(100, (peso_usado / veic["peso_max"]) * 100)
        if veic["peso_max"] > 0 else 0
    )

    st.info(
        f"""
        **Motivo da escolha:**  
        ✅ Menor veículo que acomodou 100% da carga no 3D.  
        ✅ Caixas alocadas: {caixas}/{qtd_total_real}.  
        ✅ Ocupação volumétrica: {ocupacao:.1f}%.  
        ✅ Aproveitamento de peso: {peso_percentual:.1f}%.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Caixas Alocadas", caixas)

    with col2:
        st.metric("Ocupação", f"{ocupacao:.1f}%")

    with col3:
        st.metric("Peso Utilizado", f"{peso_usado:.0f} kg")

    col4, col5, col6, col7 = st.columns(4)

    with col4:
        st.metric("Margem Comprimento", f"{comprimento_livre:.2f} m")

    with col5:
        st.metric("Margem Largura", f"{largura_livre:.2f} m")

    with col6:
        st.metric("Margem Altura", f"{altura_livre:.2f} m")

    with col7:
        st.metric("Volume Livre", f"{volume_livre:.2f} m³")

    if caixas < qtd_total_real:
        st.error("⚠ Nem todas as caixas couberam.")
    else:
        st.success("✅ Todas as caixas foram alocadas.")

    fig = go.Figure()

    cores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

    MAX_BOXES_RENDER = min(MAX_RENDER_3D, len(posicoes))

    for i, (x, y, z, c, l, a) in enumerate(posicoes[:MAX_BOXES_RENDER]):

        fig.add_trace(go.Mesh3d(
            x=[
                x, x+c, x+c, x,
                x, x+c, x+c, x
            ],
            y=[
                y, y, y+l, y+l,
                y, y, y+l, y+l
            ],
            z=[
                z, z, z, z,
                z+a, z+a, z+a, z+a
            ],
            alphahull=0,
            opacity=0.45,
            color=cores[i % len(cores)],
            flatshading=True,
            showscale=False
        ))

    fig.add_trace(go.Scatter3d(
        x=[
            0, veic["comprimento"], veic["comprimento"], 0,
            0, veic["comprimento"], veic["comprimento"], 0
        ],
        y=[
            0, 0, veic["largura"], veic["largura"],
            0, 0, veic["largura"], veic["largura"]
        ],
        z=[
            0, 0, 0, 0,
            veic["altura"], veic["altura"], veic["altura"], veic["altura"]
        ],
        mode="markers",
        marker=dict(
            size=2,
            color="gray",
            opacity=0.05
        ),
        showlegend=False
    ))

    fig.update_layout(
        title=f"Ocupação 3D: {ocupacao:.1f}%",
        scene=dict(
            aspectmode="data"
        ),
        height=700
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"responsive": True}
    )
