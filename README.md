Sistema Sorveteria

O Sistema Sorveteria é uma aplicação web completa desenvolvida em Python com o framework Django como projeto final da disciplina de Práticas de Software Web II (PSW II). O objetivo principal da aplicação é simular o gerenciamento ponta a ponta de uma sorveteria, centralizando com eficiência as informações de clientes, produtos, pedidos e pagamentos.

🛠️️ Tecnologias e Arquitetura

Para garantir robustez e segurança, a arquitetura do projeto emprega tecnologias modernas e bem consolidadas:

Backend: Python com Django Framework.

Banco de Dados: SQLite (gerenciado pelo Django ORM).

Frontend / Interface: HTML5, CSS3, JavaScript e Bootstrap (garantindo um layout responsivo e de fácil navegação em qualquer dispositivo).

Autenticação: Integração com o pacote nativo django.contrib.auth para gerenciamento seguro de sessões, controle de acessos e utilização do painel administrativo por superusuários.

🏛️ Estrutura e Modelos de Dados

A estrutura do sistema é organizada em torno de operações de CRUD completas e entidades bem definidas baseadas no diagrama do projeto:

Pessoa: Responsável por armazenar o cadastro completo dos clientes e usuários (como CPF, nome, telefone e endereço detalhado), possuindo uma relação direta de um-para-muitos com os pedidos e conectando-se também ao modelo de usuário padrão do Django.

Produto: Gerencia o catálogo de itens comercializados na sorveteria, mantendo o registro de descrições e valores atualizados.

Pedido_Produto: Atua como uma tabela intermediária essencial para resolver a relação de muitos-para-muitos entre pedidos e produtos, detalhando exatamente quais itens compõem cada compra, bem como a quantidade e o preço total correspondente.

Pagamento: Gerencia as informações financeiras de quitação, registrando a forma de pagamento escolhida e o valor total vinculado diretamente a cada pedido correspondente.

📋 Pré-requisitos

Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

Python (versão 3.10 ou superior recomendada)

Git (para clonar o repositório)

Gerenciador de pacotes pip (geralmente incluso na instalação padrão do Python)

🚀 Passo a Passo para Execução Local

1. Clonar o Repositório

Abra o terminal em seu computador e execute o comando abaixo para clonar o projeto (substitua pelo link real do seu repositório):

git clone https://github.com/seu-usuario/sistema-sorveteria.git
cd sistema-sorveteria


2. Criar e Ativar o Ambiente Virtual

É altamente recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

No Linux / macOS:

python3 -m venv venv
source venv/bin/activate


No Windows (Prompt de Comando ou PowerShell):

python -m venv venv
venv\Scripts\activate


3. Instalar as Dependências

Com o ambiente virtual ativado, instale os pacotes necessários listados no arquivo requirements.txt:

pip install -r requirements.txt


4. Executar as Migrações do Banco de Dados

O Django criará o banco de dados SQLite localmente e aplicará as tabelas correspondentes aos modelos do sistema (Pessoa, Produto, Pedido, Pedido_Produto, Pagamento):

python manage.py makemigrations
python manage.py migrate


5. Criar o Superusuário (Painel Administrativo)

Para ter acesso completo ao painel administrativo do Django e gerenciar os dados da sorveteria, crie uma conta de superusuário:

python manage.py createsuperuser


Insira os dados solicitados no terminal (Nome de usuário, E-mail e Senha).

6. Iniciar o Servidor de Desenvolvimento

Execute o servidor local do Django:

python manage.py runserver