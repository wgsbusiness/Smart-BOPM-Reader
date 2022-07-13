# Smart-BOPM-Reader


Servidor Django para o projeto de catalogação dados criminais.

## Instalação

Estas são as instruções gerais para se ter o servidor rodando localmente.

### Clonagem do projeto

Usa-se os seguintes comandos para criar uma pasta para o projeto e cloná-lo.

```
$ mkdir sbr
$ cd sbr
$ git clone https://github.com/wgsbusiness/Smart-BOPM-Reader.git.
```

### Criação do ambiente virtual

Para que não haja conflitos entre as versões das bibliotecas usadas com as que já estão na máquina, usamos um ambiente virtual.

```
$ sudo apt install python3-venv
$ python3 -m venv env
```

Para ativar o ambiente virtual usamos o seguinte comando:

```
$ source env/bin/activate
```

### Instalação das bibliotecas

Com o ambiente virtual ativado, instalamos as bibliotecas de projeto com o seguinte comando:

```
$ pip3 install -r requirements.txt
```

### Iniciando o servidor django

É necessário, agora, migrar o banco de dados.

```
$ ./manage.py migrate
```

Finalmente podemos iniciar o servidor.

```
$ ./manage.py runserver
```

Ele pode ser acessado pelo URL padrão "localhost:8000" ou "127.0.0.1:8000".