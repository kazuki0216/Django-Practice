from django.http import HttpResponse

def cafe_menu(request):
    return HttpResponse("Hello world")


def order(request):
    return HttpResponse(
        "Hello, world. Claude Sonnet is one of the industry leading llm model."
    )
