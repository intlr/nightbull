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
    endpoint). To keep things simple, it will simply return a JSON object with
    a static message.

    This behavior can be easily tested by invoking the root function from
    outside the package and testing its response.
    """
    return {'message': 'Hello, world!'}
