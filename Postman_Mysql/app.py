from flask import Flask, request, render_template,redirect,url_for
from flask_mysqldb import MySQL

vj = Flask(__name__)
vj.secret_key = "Vijay@006"
vj.config["MYSQL_HOST"] = "localhost"
vj.config["MYSQL_USER"] = "root"
vj.config["MYSQL_PASSWORD"] = "Vijay@006"
vj.config["MYSQL_DB"] = "postman"

mysql = MySQL(vj)

@vj.route("/")
def geti():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM post_methods")
    data = cur.fetchall()
    cur.close()
    return render_template("table.html", data=data)

@vj.route("/post",methods=["POST"])
def posti():
    if request.method=="POST":
       data=request.get_json()
       Name=data["Name"]
       Age=data["Age"]
       RollNo=data["RollNo"]
       Mark_1=data["Mark_1"]
       Mark_2=data["Mark_2"]
       Mark_3=data["Mark_3"]
       Mark_4=data["Mark_4"]
       Mark_5=data["Mark_5"]
       cur=mysql.connection.cursor()
       cur.execute("insert into post_methods(Name,Age,RollNo,Mark_1,Mark_2,Mark_3,Mark_4,Mark_5) values(%s,%s,%s,%s,%s,%s,%s,%s)",(Name,Age,RollNo,Mark_1,Mark_2,Mark_3,Mark_4,Mark_5))
       mysql.connection.commit()
       cur.close()
    return redirect(url_for("geti"))

@vj.route("/put_api/<int:id>",methods=["PUT"])
def puti(id):
       data=request.get_json()
       Name=data["Name"]
       Age=data["Age"]
       RollNo=data["RollNo"]
       Mark_1=data["Mark_1"]
       Mark_2=data["Mark_2"]
       Mark_3=data["Mark_3"]
       Mark_4=data["Mark_4"]
       Mark_5=data["Mark_5"]
       cur=mysql.connection.cursor()
       cur.execute("update post_methods set Name=%s,Age=%s,RollNo=%s,Mark_1=%s,Mark_2=%s,Mark_3=%s,Mark_4=%s,Mark_5=%s where id=%s",(Name,Age,RollNo,Mark_1,Mark_2,Mark_3,Mark_4,Mark_5,id))
       mysql.connection.commit()
       cur.close()
       return redirect(url_for("geti"))

@vj.route("/patch_api/<int:id>",methods=["PATCH"])
def patchi(id):
       data=request.get_json()
       Name=data["Name"]
       Age=data["Age"]
       RollNo=data["RollNo"]
       Mark_1=data["Mark_1"]
       Mark_2=data["Mark_2"]
       Mark_3=data["Mark_3"]
       Mark_4=data["Mark_4"]
       Mark_5=data["Mark_5"]
       cur=mysql.connection.cursor()
       cur.execute("update post_methods set Name=%s,Age=%s,RollNo=%s,Mark_1=%s,Mark_2=%s,Mark_3=%s,Mark_4=%s,Mark_5=%s where id=%s",(Name,Age,RollNo,Mark_1,Mark_2,Mark_3,Mark_4,Mark_5,id))
       mysql.connection.commit()
       cur.close()
       return redirect(url_for("geti"))


@vj.route("/delete_api/<int:id>",methods=["DELETE"])
def deleti(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM post_methods WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("geti"))
     


if __name__ == "__main__":
    vj.run(debug=True)
