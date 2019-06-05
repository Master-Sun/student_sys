import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeCountMiddleware(MiddlewareMixin):
    # 进入的第一个方法
    def process_request(self, request):
        self.start_time = time.time()    # 记录进入中间件时间
        return

    # 执行视图函数
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()    # 执行视图函数前的时间
        response = func(request)
        costed = time.time() - start    # 整个视图函数的执行时间
        print('执行view方法花费时间：{:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        print(111111)
        pass

    #　模板渲染时进入的方法，可在此处对response进行操作，如设置headers
    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('一次请求的响应时间：{:.2f}s'.format(costed))
        return response