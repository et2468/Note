1. 가장 원초적인 방법
```python
#views.py
def article = Article.object.get(pk=pk)
	context = {
		'artcle':article,
	}
	return render(request,'artcles/detail.html',context)


# artcles/detail.html
{{article.pk}}
{{article.title}}
{{article.content}}

```
