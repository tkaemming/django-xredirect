from django.http import HttpResponse


class XRedirectMiddleware(object):
    def process_response(self, request, response):
        if self.should_send_xredirect(request, response):
            url = response['Location']
            response = self.get_xredirect_response(request, response, url)
            response['X-Redirect'] = url
        return response

    def should_send_xredirect(self, request, response):
        return request.is_ajax() and response.status_code in (301, 302)

    def get_xredirect_response(self, request, response, url):
        content = '<a href="%s" rel="redirect">Click to continue...</a>' % url
        response = HttpResponse(content)
        return response
