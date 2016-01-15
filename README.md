#Eventex

[![Build Status](https://travis-ci.org/olivx/eventex.svg?branch=master)](https://travis-ci.org/olivx/eventex)
[![Code Health](https://landscape.io/github/olivx/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/olivx/eventex/master)

##Como desenvolver ?

1.  Clone o repositorio.
2.  Crie um  virtual env com python 3.5.
3.  Ative o virtual env.
3.  Instale as dependencias 
4.  Configure uma instancia com um .env 
5.  Rode os testes

```console
git clone git@github:olivx/eventex.git wttd                 
cd wttd             
python -m venv .wttd                
source .wttd/bin/activete               
pip install -r requirements-dev.txt             
cp contrib/env-simple .env              
python manage.py test                         
```

##Como realizar o deploy ?

1. Crie uma isntancia no heroku
2. Envie as configurações para heroku 
3. Defina uma secrect key para isntancia 
4. Defina DEBUG=False
4. Configure um serviço de email 
5. Envie o codigo para heroku

```console                                            
heroku create minha_instacia_heroku             
heroku config:push              
heroku config:set SECRET_KEY='python -m contrib/secret_gen.py'                  
heroku config:set DEBUG=False
#configure yot email services
git push heroku master --force
```