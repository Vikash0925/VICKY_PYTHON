import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Oliverse*%$_12",
database="world"
)
mycursor= mydb.cursor()
mycursor.execute("select country.Name,country.Continent,country.Population,country.LifeExpectancy,countrylanguage.language,countrylanguage.percentage from country inner join countrylanguage on country.code = countrylanguage.countrycode;")
result = mycursor.fetchall()
print(result)
for rows in result :
   print(rows )