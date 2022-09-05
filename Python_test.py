from flask import Flask, request


# Function for sorting in ascending order
def sort_asc(array):
    print(array)
    array.sort()
    print(array)
    return array

def sort_des(array):
    array.sort(reverse=True)
    return array


app = Flask(__name__)
@app.route('/sorting/launch', methods=['POST'])
def launch():
    arr= None
    method = None
    data = request.get_json()
    print(data)
    arr = data["array"]
    print(arr)
    method = data["method"]
    if method == "Ascending":
        sortArray = sort_asc(arr)
        result = {"Status" : "Done", "Sorted Array": sortArray}
    elif method == "Decending":
        sortArray = sort_des(arr)
        result = {"Status" : "Done", "Sorted Array": sortArray}
    else:
        result = {"Status": "Failed", "Feedback": "Please provide correct method"}
    print(result)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3006)