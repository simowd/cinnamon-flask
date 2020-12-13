# cinnamon-flask
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev
sudo apt-get install python3-dev 

. env/bin/activate
pip install -r requirements.txt

export FLASK_APP=cinnamon
export FLASK_ENV=development
flask run