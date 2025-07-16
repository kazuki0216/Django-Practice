# 📚 Project / Concept Learning Log

> Django Practice — Building a REST API with a Data ingestion pipeline. Also implementing Celery to learn about task queues.

---

## 📈 Daily Progress Tracker

| Date       | Task / Feature Built                 | What I Learned / Notes                         |
|------------|--------------------------------------|------------------------------------------------|
| 2025-07-14th | Created Django project and app       | `startapp`, basic URL routing                  |


---

## 🧠 Concept Memo

Use this section to write down *concepts you learned*, in your own words.  
Think of it like flashcards for yourself.

---

### 🔸 [Getting things started in Django]  
#### Django Views
**What is it?**  
A function or class that handles HTTP requests and returns a response.
In the urls, you use the `include` method within django.urls to assign an endpoint, and what functions will run when that endpoint is accessed. 

**Example Code**  
The bottom is an example of a view that when accessed will return a simple message to the client.
```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def azure_index(request):
    return HttpResponse("Hello, world. Azure openai is one of the industry leading llm model.")


def claude_index(request):
    return HttpResponse("Hello, world. Claude Sonnet is one of the industry leading llm model.")
```

The path function takes 2 parameters. 
1. The path from which the client will access this.
2. A URLConf.

If you have a URLConf in another directory's urls.py, then you can specify that like below.
```python
# technologies/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("azure", views.azure_index, name="azure_index"),
    path("claude", views.claude_index, name="claude_index"),
]
# ------------------------------------------
# urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("llm_models/latest/", include("technologies.urls")),
    path('admin/', admin.site.urls),
]
```
