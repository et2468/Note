1. 가장 원초적인 방법

```python
article = Article()
article.title = request.POST.get('title')
article.content = request.POST.get('content')
article.save()

# article = Article(title=title, content=content)
# article.save()

# Article.objects.create(title=title, content=content)
```
- [form에서 받은 데이터]가 [request]에 담김
	- input하나당 field하나
		- [input의 name],  [input의 value]가 [key:value]로 전달
	- [기타 요소]들에 의해도 [key:value]가 전달됨 
		- [datetime, @login_requied next인자 등]

2. form사용하기