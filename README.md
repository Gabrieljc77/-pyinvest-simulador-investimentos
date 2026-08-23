PyInvest — Simulador Comparativo de Investimentos

Simulador educacional desenvolvido em Python para comparar diferentes alternativas de investimento por meio de juros compostos, aportes mensais, tributação e análise estatística.





Sobre o projeto

O PyInvest é uma aplicação de linha de comando que permite simular e comparar a evolução de quatro modalidades de investimento:

CDB

LCI/LCA

Poupança

FII — Fundo de Investimento Imobiliário

A partir dos dados informados pelo usuário, o programa calcula o valor estimado de cada alternativa, considera aportes mensais, aplica regras simplificadas de tributação para CDB, gera cenários para FIIs e identifica qual opção apresentou o maior valor final dentro da simulação.

O projeto foi desenvolvido com foco no aprendizado de Python, lógica de programação, funções, cálculos financeiros, estruturas condicionais e uso de módulos da biblioteca padrão.

Funcionalidades

Conversão de uma taxa anual para uma taxa mensal equivalente.

Cálculo de juros compostos sobre o capital inicial.

Inclusão de aportes mensais durante o período da simulação.

Comparação entre CDB, LCI/LCA, Poupança e FII.

Aplicação de uma tabela simplificada de Imposto de Renda regressivo para CDB.

Simulação de 5 cenários aleatórios para FII, com variação de ±3% sobre o valor calculado.

Cálculo de:

média;

mediana;

desvio padrão dos cenários de FII.

Definição de uma meta financeira.

Verificação automática se a meta foi atingida.

Identificação da alternativa com o maior valor final estimado.

Geração de gráficos em barras no próprio terminal.

Formatação dos valores no padrão monetário brasileiro.

Exibição da data da simulação e de uma data estimada de resgate.

Tecnologias e bibliotecas

O projeto utiliza apenas recursos da biblioteca padrão do Python, portanto não é necessário instalar pacotes externos.

Tecnologia / módulo

Utilização

Python

Linguagem principal do projeto

math

Potenciação e cálculos de juros compostos

random

Geração das variações aleatórias dos cenários de FII

datetime

Data da simulação e estimativa da data de resgate

statistics

Média, mediana e desvio padrão dos cenários

locale

Configuração regional do ambiente

Como os cálculos funcionam

Juros compostos

O programa utiliza uma função de montante que considera:

capital inicial;

aportes mensais;

taxa de rendimento;

prazo em meses.

De forma simplificada, o cálculo segue a ideia:

Montante = Capital Inicial × (1 + taxa)^meses
         + Aporte Mensal × [((1 + taxa)^meses - 1) / taxa]

Conversão da taxa anual

A taxa anual informada para o CDI é transformada em uma taxa mensal equivalente:

Taxa mensal = (1 + taxa anual)^(1/12) - 1

Em seguida, o programa aplica o percentual do CDI informado pelo usuário para CDB e LCI/LCA.

CDB

Para o CDB, o programa:

calcula o rendimento bruto;

calcula o lucro em relação ao total aportado;

aplica uma alíquota simplificada de Imposto de Renda sobre o lucro;

apresenta o valor líquido estimado.

Tabela utilizada pelo programa:

Prazo estimado

Alíquota de IR

Até 180 dias

22,5%

De 181 a 360 dias

20%

De 361 a 720 dias

17,5%

Acima de 720 dias

15%

Para transformar o prazo em dias, o programa considera cada mês como 30 dias.

LCI/LCA

A LCI/LCA utiliza a taxa mensal equivalente do CDI multiplicada pelo percentual informado pelo usuário.

Nesta versão do projeto, não é aplicado Imposto de Renda ao resultado da LCI/LCA.

Poupança

A simulação da poupança utiliza uma taxa fixa de:

0,5% ao mês

Essa é uma simplificação adotada pelo projeto e não representa necessariamente todas as regras reais de remuneração da poupança.

FII

A rentabilidade de FII informada pelo usuário é tratada pelo programa como uma taxa mensal.

Após calcular um valor-base, o PyInvest cria cinco cenários aleatórios, cada um podendo variar entre -3% e +3%.

Com esses cinco resultados são calculados:

média;

mediana;

desvio padrão.

A média dos cenários é utilizada na comparação final com os demais investimentos.

Fluxo do programa

Entrada de dados
      ↓
Conversão das taxas
      ↓
Cálculo do CDB
      ↓
Cálculo da LCI/LCA
      ↓
Cálculo da Poupança
      ↓
Simulação dos cenários de FII
      ↓
Cálculo das estatísticas
      ↓
Comparação dos resultados
      ↓
Verificação da meta
      ↓
Relatório no terminal

Requisitos

Python 3 instalado no computador.

Terminal, Prompt de Comando, PowerShell ou terminal integrado de uma IDE.

Não há dependências externas.

Como executar

1. Clone o repositório

git clone <URL-DO-SEU-REPOSITORIO>

2. Entre na pasta do projeto

cd <NOME-DO-REPOSITORIO>

3. Execute o programa

Com o nome atual do arquivo:

python "Projeto AP.py"

Em alguns sistemas, o comando pode ser:

python3 "Projeto AP.py"

Para deixar o projeto mais padronizado no GitHub, uma melhoria simples é renomear Projeto AP.py para pyinvest.py ou main.py.

Dados solicitados

Ao executar o programa, o usuário informa:

Capital Inicial (R$):
Aporte Mensal (R$):
Prazo (meses):
CDI Anual (%):
Percentual CDI no CDB (%):
Percentual CDI na LCI (%):
Rentabilidade FII (%):
Meta Financeira (R$):

Exemplo de uso

Exemplo de entrada:

Capital Inicial (R$): 1000
Aporte Mensal (R$): 200
Prazo (meses): 12
CDI Anual (%): 14.9
Percentual CDI no CDB (%): 100
Percentual CDI na LCI (%): 90
Rentabilidade FII (%): 0.8
Meta Financeira (R$): 5000

O relatório gerado apresenta uma estrutura semelhante a:

==================== PYINVEST ====================

RELATÓRIO PYINVEST
Total investido: R$ ...

CDB         : R$ ...
Gráfico     : █████████████████████

LCI/LCA     : R$ ...
Gráfico     : █████████████████████

Poupança    : R$ ...
Gráfico     : ███████████████████

FII (Média) : R$ ...
Gráfico     : ████████████████████

Estatísticas FII (Mediana): R$ ...
Desvio Padrão FII: R$ ...
Meta atingida? Sim/Não

Melhor opção: ...

Como os cenários de FII são gerados com valores aleatórios, os resultados relacionados a FII podem mudar a cada execução.

Estrutura do projeto

PyInvest/
├── Projeto AP.py
└── README.md

O arquivo Projeto AP.py concentra, nesta versão, toda a lógica do sistema.

Principais funções

Função

Responsabilidade

moeda()

Formata valores como moeda brasileira

taxa_mensal()

Converte taxa anual em taxa mensal equivalente

montante()

Calcula o montante usando juros compostos e aportes

ir_cdb()

Retorna a alíquota simplificada de IR do CDB

barra()

Cria a representação gráfica em barras no terminal

melhor_opcao()

Identifica o maior resultado entre os investimentos

gerar_relatorio()

Executa cálculos, estatísticas e exibe o relatório

main()

Coleta as entradas do usuário e inicia a simulação

Conceitos praticados

Este projeto aplica conceitos importantes de programação, como:

funções;

parâmetros e retornos;

condicionais;

operadores matemáticos;

entrada e saída de dados;

módulos da biblioteca padrão;

geração de números pseudoaleatórios;

estatística descritiva;

formatação de strings;

organização de código;

cálculos financeiros.

Limitações atuais

O PyInvest é um projeto educacional e utiliza simplificações matemáticas e financeiras.

Entre as principais limitações:

não consulta taxas financeiras em tempo real;

não considera inflação;

não considera taxas de administração, custódia, corretagem ou outros custos;

utiliza uma regra fixa de 0,5% ao mês para a poupança;

utiliza uma simulação simplificada para FIIs;

considera meses de 30 dias para a estimativa de prazo;

não contempla todas as particularidades tributárias de investimentos reais;

os resultados de FII variam entre as execuções;

entradas inválidas ou algumas taxas iguais a zero ainda podem exigir tratamento adicional.

Por isso, os resultados devem ser interpretados como simulações para fins de estudo, e não como recomendação de investimento.

Possíveis melhorias

Adicionar validação das entradas do usuário.

Tratar taxas iguais a zero.

Criar uma interface gráfica.

Permitir exportação do relatório para CSV ou PDF.

Gerar gráficos com bibliotecas de visualização.

Consultar indicadores financeiros por API.

Criar testes automatizados.

Separar o projeto em módulos.

Permitir novos tipos de investimento.

Adicionar comparação de rentabilidade real descontando inflação.

Autores

Projeto desenvolvido por:

Gabriel Jardim

Gabriel Alonso

Nicolas Gabriel

Observação

Este software foi criado para fins acadêmicos e educacionais. As simulações não substituem dados oficiais, avaliação de risco ou orientação de um profissional habilitado.
