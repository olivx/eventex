#Eventex

##Como desenvolver ?

1.  clone o repositorio.
2.  crie um  virtual env com python 3.5.
3.  Ative o virtual env.
3.  instale as dependencias 
4.  configure uma instacia com um .env 
5.  rode os testes

```console
git clone git@github:olivx/eventex.git wttd                 
cd wttd             
python -m venv .wttd                
source .wttd/bin/activete               
pip install -r requirements.txt             
cp contrib/env-simple .env              
python manage.py test                         
```

##Como realizar o deploy ?

1. crie uma isntacia no heroku
2. envie as configurações para heroku 
3. defina uma secrect key para isntancia 
4. defina DEBUG=False
4. configure um serviço de email 
5. envie o codigo para heroku

```console                                            
heroku create minha_instacia_heroku             
heroku config:push              
heroku config:set SECRET_KEY='python -m contrib/secret_gen.py'                  
heroku config:set DEBUG=False
#configure yot email services
git push heroku master --force
```