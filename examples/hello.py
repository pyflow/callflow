from callflow import CallFlow

app = CallFlow()

@app.route('/')
async def hello(request):
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)