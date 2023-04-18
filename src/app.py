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
    """
    The root function describes the behavior for the root endpoint (main
    endpoint). To keep things simple, it only returns a JSON object with a
    static message.
    """

    return {'message': 'Hello, world!'}
