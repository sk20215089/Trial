import mysql.connector

def DataUpdate(username,usermail):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1009",
        database="chatbot"
    )
    mycursor=mydb.cursor()
    query="trial"
    message="trial"
    ins='INSERT INTO queries (Query,Username,Usermail,Answer) VALUES("{}","{}","{}","{}");'.format(query,username,usermail,message)
    mycursor.execute(ins)
    mydb.commit()
    print(mycursor._rowcount,"record inserted")

# if __name__=="__main__":
#     DataUpdate("sarthak","sk")