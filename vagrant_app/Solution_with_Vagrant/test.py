from flask import Flask

app=Flask(__name__)

@app.route("/")
def test():
    return ("THIS PROJECT CREATED BY MEHMET AKİF ALTUN using VAGRANT TOOL")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run(debug=True)
    