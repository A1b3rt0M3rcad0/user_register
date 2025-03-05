
# User Register API

Este repositório contém uma API para registro de usuários e outras ações relacionadas, como login e alteração de nome de usuário. A API oferece endpoints para criar, editar e deletar contas de usuário, bem como consultar dados de usuários registrados.

## Pré-requisitos

Antes de rodar a aplicação, é necessário configurar algumas variáveis de ambiente essenciais. Estas variáveis de ambiente permitem que a aplicação se conecte corretamente ao banco de dados MySQL e que a autenticação de segurança funcione conforme esperado.

### Variáveis de Ambiente

1. **MYSQL_STRING_CONNECTION**  
   Esta variável contém a string de conexão do MySQL. Ela é usada para conectar a aplicação ao banco de dados.

   Exemplo:
   ```bash
   MYSQL_STRING_CONNECTION= Sua string de conexão
   ```

2. **AUTH_SECRET_KEY**  
   Esta chave é utilizada para assinar e verificar tokens JWT. Ela deve ser mantida em segredo para garantir a segurança da aplicação.

   Exemplo:
   ```bash
   AUTH_SECRET_KEY= Sua chave secreta
   ```

3. **AUTH_ALGORITM**  
   Esta variável define o algoritmo usado para assinar e verificar os tokens JWT. O algoritmo recomendado para segurança é o **HS256**.

   Exemplo:
   ```bash
   AUTH_ALGORITM=HS256
   ```

4. **HOST**  
   Esta variável define o host de desenvolvimento, por padrão deixe 0.0.0.0.

   Exemplo:
   ```bash
   HOST=0.0.0.0
   ```

5. **PORT**  
   Esta variável define a porta de sua aplicação de desenvolvimento, por padrão deixe 5000.

   Exemplo:
   ```bash
   PORT=5000
   ```

### Recomendação sobre o algoritmo de autenticação (AUTH_ALGORITM)

É **fortemente recomendado** que você utilize o algoritmo **HS256** para garantir que a autenticação da API seja segura e funcional. Caso decida utilizar um algoritmo diferente, será necessário ajustar o código da aplicação para suportar o novo algoritmo de criptografia.

Se você optar por usar um algoritmo diferente, altere a implementação de validação do token no código, especificamente na parte que lida com a criação e verificação dos tokens JWT.

## Como rodar a aplicação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/A1b3rt0M3rcad0/user_register.git
   cd user-register
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scriptsctivate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**

   - Crie um arquivo `.env` na raiz do projeto ou configure as variáveis diretamente no seu sistema.

     Exemplo de `.env`:

     ```bash
     MYSQL_STRING_CONNECTION= Adicione aqui sua string de conexão
     AUTH_SECRET_KEY= Adicione Aqui sua chave secreta
     AUTH_ALGORITM= HS256
     ```

5. **Rodando a aplicação de desenvolvimento:**

   Após configurar as variáveis de ambiente, você pode rodar a aplicação com o seguinte comando:

   ```bash
   python run_dev.py
   ```

   A aplicação estará rodando no endereço `http://localhost:5000`.

6. **Rodando a aplicação com gunicorn: (Pode ter problemas no Windown)**

   Após configurar as váriaveis de ambiente, você pode rodar a aplicação com o seguinte comando:

   ```bash
   gunicorn -b 0.0.0.0:5000 run.app
   ```

## Endpoints da API

A API oferece os seguintes endpoints para interagir com usuários:

- **POST /user/register**  
  Registra um novo usuário.
  
- **POST /user/login**  
  Realiza o login de um usuário e retorna um token JWT.

- **POST /user/change_username**  
  Permite que o usuário altere o seu nome de usuário.

- **POST /user/delete_user**  
  Deleta a conta de um usuário.

- **POST /user/find_user**  
  Encontra um usuário pelo seu nome de usuário.

- **API COMPLETA: /api/docs**
  Enconta a documentação da api

## Testes

Recomendamos que, ao configurar o projeto e iniciar os testes, você verifique se tudo está funcionando corretamente. Caso algum teste de autenticação falhe, é possível que um dos tokens de teste tenha expirado. Nesses casos, basta gerar um novo token, substituir o antigo e executar os testes novamente para garantir que o sistema esteja funcionando corretamente.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.