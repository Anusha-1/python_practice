#pip install flask 

from flask import Flask

app=Flask(__name__) #web server(http server: locolhost:5000)

@app.route('/')
@app.route('/home')  #@app.route('/home/{id}')
def home():
    #db logic , connect to any other is or etc 
    return "<h1>Welcome to Bank of America</h1>"

@app.route('/about')
def about():
    return "<h2>Bank of America started  in 1998</h2>"

if __name__=='__main__':
    app.run(debug=True)  #(debug=True,port=2000)

#python app.py
