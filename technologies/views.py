from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def azure_index(request):
    return HttpResponse("Hello, world. Azure openai is one of the industry leading llm model.")


def claude_index(request):
    return HttpResponse("Hello, world. Claude Sonnet is one of the industry leading llm model.")