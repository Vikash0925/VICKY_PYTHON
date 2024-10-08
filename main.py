from flask import Flask,render_template,request,url_for,redirect
import random 
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Oliverse*%$_12",
database="world"
)
mycursor= mydb.cursor()
# mycursor.execute(" selectcountry.Name,country.Continent,country.Population,country.LifeExpectancy,countrylanguage.language,countrylanguage.percentage from country inner join countrylanguage on country.code = countrylanguage.countrycode;")
# result = mycursor.fetchall()
#print(result)
# for rows in result :
#    print(rows )

# from MYSQLdb import _mysql
# db = _mysql.connect(host="localhost",user="root",database="world",read_default_file="~/.my.cnf")
data=[]

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")




@app.route("/submit",methods=['POST'])
def submit():
    selected_country = request.form['country']
    # query = "select country.Name,country.Continent,country.Population,country.LifeExpectancy,countrylanguage.language,countrylanguage.percentage from country inner join countrylanguage on country.code = countrylanguage.countrycode where Name = %s;"
    # mycursor.execute(query,(selected_country,))
    # result = mycursor.fetchall()
    return redirect(url_for('country',country_name=selected_country))


@app.route("/country/<country_name>")
def country(country_name):
    query = "select country.Name,country.Continent,country.Population,country.LifeExpectancy,countrylanguage.language,countrylanguage.percentage from country inner join countrylanguage on country.code = countrylanguage.countrycode where Name = %s;"
    mycursor.execute(query,(country_name,))
    result = mycursor.fetchall()
    if result ==[]:
        query="select Name,Continent,Population,LifeExpectancy from country where Name = %s"
        mycursor.execute(query,(country_name,))
        result = mycursor.fetchall()
        result_1ist=list(result[0])
        result_1ist.extend(['none',0])

        return render_template('submit.html',country_name=country_name,data=result)

    else:    
        return render_template('submit.html',country_name=country_name,data=result)

@app.route('/random')
def index():
    return "Random: {}".format(random.randint(1, 9))

if __name__ == '__main__' :
    app.run(debug=True)

