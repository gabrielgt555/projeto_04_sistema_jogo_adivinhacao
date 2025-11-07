# 🎮 Sistema de Jogo de Adivinhação

Projeto do **Módulo 1** do MBA em Inteligência Artificial da Unifor.

O objetivo é implementar um jogo simples de adivinhação em Python, praticando:
- uso de funções (`def`)
- estruturas de repetição (`while`, `for`)
- condicionais (`if`, `elif`, `else`)
- manipulação de números aleatórios (`random.randint`)

---

## 🕹️ Como o jogo funciona

1. O jogador escolhe um **usuário** já cadastrado no código.
2. O sistema sorteia um **número secreto** entre 1 e 100.
3. O jogador tem até **10 tentativas** para adivinhar o número.
4. A cada tentativa o sistema:
   - valida se a entrada é um número inteiro
   - informa se o chute foi **maior** ou **menor** que o número secreto
5. Se acertar, o jogo calcula uma **pontuação** baseada no número de tentativas.
6. Se não acertar dentro do limite de tentativas, a pontuação é 0.

A pontuação é calculada assim:


pontos = PONTUACAO_BASE - (tentativas - 1) * PENALIDADE_POR_TENTATIVA

===============================================

- **🧱 Estrutura do projeto**

projeto_04_sistema_jogo_adivinhacao/
├── jogo_adivinhacao.py   # Código principal do jogo
├── README.md             # Este arquivo com instruções
├── .gitignore            # Arquivos/pastas ignorados pelo Git
└── venv/                 # Ambiente virtual Python (não vai para o GitHub)

===============================================

- **🐍 Como executar**

1. Clonar o repositório
   - git clone https://github.com/gabrielgt555/projeto_04_sistema_jogo_adivinhacao.git
   - cd projeto_04_sistema_jogo_adivinhacao

2. Criar e ativar o ambiente virtual
   - python -m venv venv
   - .\venv\Scripts\Activate.ps1

3. Executar o jogo
   - python jogo_adivinhacao.py

===============================================

- **📊 Exemplo de funcionamento**

🎲 Jogo iniciado para Enzo (@vetin)!
Tente adivinhar o número entre 1 e 100.

Tentativa 1: 19
📉 Seu chute foi menor que o número secreto.

Tentativa 2: 42
📈 Seu chute foi maior que o número secreto.

Tentativa 3: 37
✅ Parabéns, Enzo! Você acertou o número secreto!
Pontuação final: 80 pontos

===============================================

- **👤 Autor**

Nome: Gabriel Teixeira

GitHub: @gabrielgt555

Curso: MBA em Inteligência Artificial - Unifor

```text