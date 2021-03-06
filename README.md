# NegraTec API [![Build Status](https://snap-ci.com/NegraTec/negratec-api/branch/master/build_image)](https://snap-ci.com/NegraTec/negratec-api/branch/master)
[Quadro das funcionalidades a serem implementadas e para adição de novas](https://waffle.io/NegraTec/negratec-api).

Documentação da API: http://docs.negratecapi.apiary.io/

API para receber as submissões do site negratec.github.io.

## Contribuição

### Pré-requisitos

- Python 3.4
- VirtualEnv (opcional)
- [Postgres 9.3](http://postgresapp.com/)
- Faça fork do projeto e realize o clone do projeto na sua máquina `git clone https://github.com/NegraTec/negratec-api.git`.

### Configuração da máquina

Primeiro rode o VirtualEnv e rode `source [pasta-criada]/bin/activate`. **(opcional)**

Para instalação das dependências `pip install -r requirements.txt`

Crie o banco de dados com o comando `createdb negratec`

### Testes

`paver test`

Antes de qualquer **pull request** execute `paver ci` na sua máquina. Este comando além dos testes, executa o flake8 que checa sintaxe e estilo.

### Executar o servidor

`paver server`
