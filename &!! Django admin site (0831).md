admin site에 접속하여서 DB를 GUI방식?으로 조작할 수 있다

```git bash
python manage.py createsuperuser
```
```python
# articles/admin.py
from django contrib import admin
from .models import Article

admin.site.register(Article)

# 사이트에서 적절히 레코드 생성

```
