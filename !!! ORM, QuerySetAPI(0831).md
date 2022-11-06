
## ORM
파이썬 코드를 sql로 변환하여 DB에 접근할 수 있게 해준다
- migrations
- DatabaseAPI

## DatabaseAPI
```python
Model.manager.QuerysetAPI()
Article.objects.all()
```
- Model --> 해당 DB Table 접근
- manager  --> 파이썬 클레스에 추가되는 객체, 메서드 제공
- Queryset --> Model.manager로 받은 Table
- QuerysetAPI --> Querset조작(메서드,연산자

## QuerysetAPI

[Model.object]로 [Table]을 가져온 뒤
[Table]에서 어떤 레코드를 가져올지 정한다

```python
Article.objects.all()

<QuerySet [<Article: Article object (1)>,
		  [<Article: Article object (2)>,
		  [<Article: Article object (3)>]
>
```

```python
Article.objects.get(pk=1)

<Article: Article object (1)>
```

```python
Article.objects.filter('title'= '홀수')

<QuerySet [<Article: Article object (1)>,
		  [<Article: Article object (3)>,
		  [<Article: Article object (5)>]
>
```


```python
Article.objects.filter('cotent__contain'= 'k')
# 해당 필드에 k문자가 있는 애들 추출
# [Article.object] |.querysetAPI
#      [Table]     |.querysetAPI

<QuerySet [<Article: Article object (a)>,
		  [<Article: Article object (b)>,
		  [<Article: Article object (c)>]
>
```
[Queryset을 좀 더 명시적으로 보고싶을때]
```python
# models.py
def __str__(self):
	return self.contain

# shell
Article.objects.filter('cotent__contain'= 'k')
<QuerySet [<Article: "k'content_a">,
		  [<Article: "k'content_b">,
		  [<Article: "k'content_c">]
>
```

