from django.http import HttpResponse
from django.urls import reverse

def reverse_view(request, year):
    url = reverse('reverse', args=[year])
    
    # 생성된 URL을 포함한 응답을 반환합니다.
    return HttpResponse(f'Reversed URL: {url}')


def format_view(request, format=None):
    data = {f'message {format}': 'Hello, world!'}
    return HttpResponse(data)