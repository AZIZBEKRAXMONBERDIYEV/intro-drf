from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def main(request: Request) -> Response:
    params = request.query_params

    name = params['name']

    return Response({
        "name": name
    })


@api_view(['GET', 'POST'])
def sum(request: Request) -> Response:
    if request.method == 'GET':
        params = request.query_params

        a = params['a']
        b = params['b']

    elif request.method == 'POST':
        data = request.data
        
        a = data['a']
        b = data['b']

    
    result = {
        "sum": int(a) + int(b)
    }
    return Response(data=result)

