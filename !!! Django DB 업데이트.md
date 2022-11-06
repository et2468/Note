1. 가장 원초적인 방법
```python
# views.py
def edit(request,pk):
	article = Article.objects.get(pk=pk)
	context = {
		'article':article
	}
	return render(request.'articles/edit.html',context)

# articles/edit.html
<form action="{% url %}"
	{{article.pk}} 번째 글
	제목 : {{article.title}}
	내용 : {{article.content}}
</form>


```