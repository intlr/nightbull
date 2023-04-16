from fastapi import FastAPI

app = FastAPI()


@app.get('/', openapi_extra={
    'summary': 'Root',
    'description': 'Get root endpoint',
    'responses': {
        '200': {
            'description': 'Successful response',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'message': {'type': 'string'}
                        },
                        'example': {
                            'message': 'Hello, world!'
                        }
                    }
                }
            }
        },
    }
})
def root():
    return {'message': 'Hello, world!'}
