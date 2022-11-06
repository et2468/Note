1. 원초적인 방법
```python
def delete(request,pk)
	if request.method = 'POST':
		article = Article.objects.get(pk=pk)
		article.delete()
		return redirect('articles:index')
```