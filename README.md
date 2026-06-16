# Sistema: Calculadora, Caixa e Matrizes 

Este projeto consiste em um sistema interativo via terminal que reúne três funcionalidades matemáticas e financeiras essenciais: uma calculadora de operações básicas, um terminal de fluxo de caixa com cálculo automatizado de troco por cédulas/moedas e um multiplicador de matrizes 2x2.

O software foi desenvolvido como parte das atividades práticas propostas pela **Liga Acadêmica de Sistemas Inteligentes (LASI)**, servindo como ferramenta de consolidação dos fundamentos da lógica de programação.

---

## Tecnologias e Conceitos Aplicados

O projeto foi construído puramente em **Python 3**, utilizando os seguintes pilares do material complementar da liga:

* **Tipos de Dados:** Manipulação dados decimais de dupla precisão (`float`) para garantir a precisão dos cálculos financeiros e matemáticos.
* **Operadores:**
    * *Aritméticos:* Soma (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`), divisão inteira (`//`) e módulo/resto da divisão (`%`).
    * *Relacionais e Lógicos:* Comparações de igualdade (`==`), menor que (`<`), menor ou igual (`<=`), maior ou igual (`>=`) .
* **Estruturas Condicionais:** Uso de blocos `if`, `elif` e `else` para controle do fluxo de navegação do menu principal.
* **Condicionais Aninhadas:** Estruturas de decisão inseridas dentro de outras (como a validação de divisão por zero na calculadora e as verificações de valores negativos e falta de saldo no módulo de caixa).
* **Tratamento de Exceções:** Implementação de blocos `try/except` com `ValueError` para evitar o fechamento inesperado do programa caso o usuário digite letras onde são esperados números.

---
## Funcionalidades do Sistema

### 1. Quatro Operações Básicas
Uma calculadora tradicional que realiza operações de Soma, Subtração, Multiplicação e Divisão. Conta com uma condicional aninhada protetiva que impede o sistema de quebrar ao tentar realizar divisões por zero.

### 2. Fluxo de Caixa (Cálculo de Troco)
Simula o operador de um caixa comercial. O usuário insere o valor total e o valor pago. O sistema valida as entradas e calcula a menor quantidade possível de cédulas e moedas a serem entregues ao cliente como troco.
* **Notas processadas:** R$ 200, R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
* **Moedas processadas:** R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.
 Para evitar os clássicos erros de arredondamento com pontos flutuantes (`float`) nativos do Python, o sistema multiplica o valor do troco por 100 e o transforma em um número inteiro (`round`), realizando as divisões de cédulas de forma matematicamente exata.

### 3. Multiplicação de Matriz (2 x 2)
Realiza o cálculo algébrico entre duas matrizes quadradas de ordem 2 (A e B). A multiplicação segue estritamente a regra matemática: **Linha x Coluna**.

A equação executada pelo código para cada elemento resultante é:

---

## 📖 Estrutura de Código Explicada

O código funciona sob um laço de repetição infinito `while True`, o que garante que o menu reapareça toda vez que uma operação for finalizada. O encerramento controlado só ocorre ao digitar a opção `0`.
---
DESENVOLVIDO POR : QUEREN HAPUQUE S.R.M DOS REIS.
