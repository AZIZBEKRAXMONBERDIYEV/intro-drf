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


@api_view(['GET'])
def sum(request: Request) -> Response:
    params = request.query_params

    a = params['a']
    b = params['b']

    data = {
        "sum": int(a) + int(b)
    }
    return Response(data=data)

