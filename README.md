# scrapy_com_django_e_vueJS

Requisitos

python3
node

Pequenas instruções;

0.0 - Navegue até a pasta raiz do projeto (scrapy_com_django_e_vueJS)

Caso tenha instalado python3.8.10
1.0 - Ative o ambiente virtual – Na pasta raiz  (scrapy_com_django_e_vueJS) rode o comando
	source venv/bin/activate

Caso tenha instalado outra versão de python3
1.0 - Na pasta raiz (scrapy_com_django_e_vueJS) rode o comando
	pip install -r requirements.txt

2.0 –  Rode as migrations;
	python manage.py makemigrations
	python manage.py migrate

3.0 – Para extrair os dados do site (https://quotes.toscrape.com/). Ainda na pasta raiz rode o comando;
	python manage.py extrair_dados

4.0 – Ative o servidor python;
	python manage.py runserver

5.0 – Ative o servidor node. Navegue até a pasta front_end e rode os comandos;
	npm install
	npm run serve

