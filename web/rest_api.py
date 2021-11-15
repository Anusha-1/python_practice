from flask import Flask,jsonify
#son data if u want to return go for api like flask etc
#html , css return web applications

app=Flask(__name__)

@app.route('/',methods=['GET'])
def getDetails():
    return jsonify({'msg':'Welcome to REST api'})

if __name__=='__main__':
    app.run(debug=True)
