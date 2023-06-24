from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


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

        a = int(params['a'])
        b = int(params['b'])

    elif request.method == 'POST':
        data = request.data
        
        a = data['a']
        b = data['b']

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    result = {
        "sum": a + b
    }
    return Response(data=result, status=status.HTTP_200_OK)

