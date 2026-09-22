# Sorveteria
O Sistema Sorveteria é uma aplicação web completa desenvolvida em Python com o framework Django como projeto final da disciplina de Práticas de Software Web II (PSW II). O objetivo principal da aplicação é simular o gerenciamento ponta a ponta de uma sorveteria, centralizando com eficiência as informações de clientes, produtos, pedidos e pagamentos.

Para garantir robustez e segurança, a arquitetura do projeto emprega tecnologias modernas e bem consolidadas. O backend é construído em Python e o banco de dados SQLite gerenciado pelo Django ORM. Para o design e experiência do usuário, a interface combina HTML5, CSS3, JavaScript e Bootstrap, garantindo um layout responsivo e de fácil navegação em qualquer dispositivo. Além disso, o sistema conta com a integração do pacote nativo django.contrib.auth, permitindo o gerenciamento seguro de sessões, controle de acessos e a utilização do painel administrativo por um superusuário.

A estrutura do sistema é organizada em torno de cinco operações de CRUD principais e entidades bem definidas baseadas no diagrama do projeto:
Pessoa: Responsável por armazenar o cadastro completo dos clientes e usuários (como CPF, nome, telefone e endereço detalhado), possuindo uma relação direta de um-para-muitos com os pedidos e conectando-se também ao modelo de usuário padrão do Django. 

 Produto: Gerencia o catálogo de itens comercializados na sorveteria, mantendo o registro de descrições e valores atualizados.     
 
 Pedido_Produto: Atua como uma tabela intermediária essencial para resolver a relação de muitos-para-muitos entre pedidos e produtos, detalhando exatamente quais itens compõem cada compra, bem como a quantidade e o preço total correspondente. 
 
Pagamento: Gerencia as informações financeiras de quitação, registrando a forma de pagamento escolhida e o valor total vinculado diretamente a cada pedido correspondente.  .