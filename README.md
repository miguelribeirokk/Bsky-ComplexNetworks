# 📊 Do Campo para a Rede ⚽📡  
## A Dinâmica dos Torcedores da Série A do Brasileirão 2024 no Bluesky

Este repositório contém o artigo, scripts e dados (quando públicos) relacionados à pesquisa acadêmica que explora o comportamento das torcidas dos times da **Série A do Campeonato Brasileiro de 2024** na rede social emergente **Bluesky**.

> Autores: Miguel A. R. e Silva e Mateus H. V. Figueiredo  
> Afiliação: Instituto de Ciências Exatas e Tecnológicas (ICET) – UFV Florestal  
> Contato: `miguel.a.silva@ufv.br`, `mateus.h.figueiredo@ufv.br`

---

## 📝 Resumo

Com o **banimento temporário do Twitter/X no Brasil**, diversas comunidades migraram para o **Bluesky**. Aproveitando essa movimentação, este estudo investigou:

- Os perfis oficiais e não oficiais dos **20 clubes da Série A**;
- As redes de seguidores de cada time;
- A sobreposição entre torcidas, utilizando **grafos complexos**.

Modelamos e analisamos o comportamento das torcidas usando métricas como:

- Coeficiente de Clusterização  
- Centralidade (PageRank)  
- Conectividade e distância média  
- Sobreposição de seguidores entre clubes rivais

---

## 🔍 O que tem neste repositório?

```bash
├── 📁 src
│   ├── 📁 api_methods        # Métodos de autenticação e coleta via AT Protocol
│   ├── 📁 archives           # Dumps históricos e coletas brutas
│   ├── 📁 db                 # Armazenamento local (.json, .csv, etc)
│   ├── 📁 model              # Lógica e algoritmos para modelagem de rede
│   ├── 📁 notebooks          # Jupyter notebooks para exploração e visualização
│   ├── 📁 results            # Resultados finais
│   └── 📄 dbtest.py          # Script de teste de conexão com o banco
│
├── 📄 Bsky_TP.pdf            # Artigo científico completo
├── 📄 requirements.txt       # Dependências do projeto
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **AT Protocol / Bluesky API**
- `pandas`, `networkx`, `matplotlib`, `json`, `csv`
- Jupyter Notebooks para análise interativa

---

## 📌 Reproduzindo o Projeto

1. Clone o repositório  
2. Crie um ambiente virtual  
3. Instale as dependências com: 
```bash
pip install -r requirements.txt
```
4. Execute os notebooks na pasta `notebooks/` para reproduzir as análises e visualizações

---

## 🧾 Citação

Se este projeto for útil para sua pesquisa ou trabalho, por favor cite:

```bibtex
@misc{silva2024bluesky,
  title={Do Campo para a Rede: A Dinâmica dos Torcedores dos Times da Série A do Brasileirão 2024 no Bluesky},
  author={Silva, Miguel A. R. and Figueiredo, Mateus H. V.},
  year={2024},
  howpublished={GitHub repository: https://github.com/miguelribeirokk/Atari-2600-mods}
}
```

## 📌 Observações

- Os dados respeitam os termos de uso da plataforma Bluesky.
- Este repositório é acadêmico e não possui vínculo com os clubes citados.



## ✉️ Contato

- Miguel A. R. e Silva — @miguelribeirokk — miguel.a.silva@ufv.br
- Mateus H. V. Figueiredo — mateus.h.figueiredo@ufv.br

