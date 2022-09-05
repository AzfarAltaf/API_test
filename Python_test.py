from flask import Flask, request
import time
import mysql.connector as database

# Connecting to the database
connection = database.connect(
        user='root',
        password='password',
        host=192.168.1.28,
        database=flask_database)
cursor = connection.cursor()

# Function for Writing database
def write_data_sorting(ip,data,result,status,oper,time):
    stmt_insert = "INSERT INTO Sorting ("+ip+","+data+","+result+","+status+","+oper+","+time+")"
    cursor.execute(stmt_insert)
    print("Logs Updated Successfully")



# Function for sorting in ascending order
def sort_asc(array):
    array.sort()
    return array
# Function for sorting in descending order
def sort_des(array):
    array.sort(reverse=True)
    return array

app = Flask(__name__)
@app.route('/sorting', methods=['POST'])
def launch():
    arr= None
    method = None
    ipAddr = request.remote_add
    data = request.get_json()
    req_time = time.time()
    print(data)
    arr = data["array"]
    print(arr)
    method = data["method"]
    if method == "Ascending":
        sortArray = sort_asc(arr)
        stat = "DONE"
    elif method == "Decending":
        sortArray = sort_des(arr)
        stat = "DONE"
    else:
        sortArray = 'Please provide the correct operation'
        stat = "FAILED"
    result = {"Status" : stat, "Sorted Array": sortArray}
    write_data_sorting(ipAddr,str(arr),str(sortArray),stat,method,req_time)
    print(result)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3006)
