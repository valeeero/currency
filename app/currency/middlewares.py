import time


from currency import model_choises as mch
from currency.models import ResponseLog


class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()

        ResponseLog.objects.create(
            path=request.path,
            response_time=(end - start) * 1_000,
            status_code=response.status_code,
            request_method=mch.METHODS
        )

        print(f'Took time {end - start} seconds') # noqa
        return response
