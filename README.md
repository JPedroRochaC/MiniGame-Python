# 🎯 Adivinhe o Número (Lógica Proposicional)

Jogo de adivinhação desenvolvido em Python utilizando **lógica proposicional**.

---

## 📋 Sobre o Projeto

Este é um mini game de terminal onde o jogador deve adivinhar um número secreto.

Diferente de um jogo comum, o número é gerado com base em **regras de lógica matemática**, utilizando proposições.

Desenvolvido como parte dos estudos no curso de  
**Análise e Desenvolvimento de Sistemas — UNIFAMETRO**

---

## 🧠 Lógica do Jogo

O número secreto segue a seguinte regra lógica:

(P ∧ Q) ∧ ¬R

Onde:

- **P** → número é par  
- **Q** → número é maior ou igual a 10  
- **R** → número é múltiplo de 3  

👉 O jogador deve usar essas condições para deduzir o número correto.

---

## 🚀 Como Executar

### Pré-requisitos:
- Python 3 instalado

### Passos:

1. Clone o repositório
2. Acesse a pasta do projeto
3. Execute o arquivo:

python minigame.py

---

## 🎮 Como Jogar

1. Escolha o nível de dificuldade:

- 🟢 Fácil: 10 a 20  
- 🟡 Médio: 10 a 30  
- 🔴 Difícil: 10 a 40  

2. Leia as regras lógicas exibidas  
3. Digite seu chute dentro do intervalo  
4. O jogo informará:
   - Se o número é maior ou menor  
5. Continue até acertar  

---

## 🛠️ Tecnologias

- Python 3  
- Biblioteca padrão `random`

---

## 📁 Estrutura do Projeto

adivinha-o-numero/
- minigame.py
- README.md

---

## 📌 Funcionalidades

- Sistema de dificuldade  
- Validação de entrada do usuário  
- Uso de lógica proposicional (P, Q, R)  
- Geração de número com base em regras  
- Contador de tentativas  

---

## 👤 Autor

João Pedro Rocha  
GitHub: https://github.com/JPedroRochaC  

---