from rest_framework.response import Response


class CustomResponseMixin(object):
    @staticmethod
    def get_base_response_data(data):
        return data or {}

    def cursor_response(self, status, data=None, cursor=None):
        response_data = self.get_base_response_data(data)
        response_data['cursor'] = cursor
        return Response(status=status, data=response_data)

    def response(self, status, data=None):
        response_data = self.get_base_response_data(data)
        return Response(status=status, data=response_data)
