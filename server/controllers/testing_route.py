from server import app


@app.route('/api')
def hello_docker():
    return 'Soon we will see it from the docker!'
