# Django mysql db연결

1. settings.py설정

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', // 마지막에 원하는 db이름 넣기 ex)postgresql
        'NAME': 'test',  					  // db이름
        'USER': 'root',  
        'PASSWORD': 'ssafy',
        'HOST': 'localhost',
        'PORT': '3306',  					  // port번호
        'OPTIONS': {
            'charset': 'utf8mb4',			  // MySQL에서 사용되는 문자 인코딩 방식을 설정
            								  // 4바이트 문자(이모티콘, 일부 이중바이트 문자, 특정 언어의 문자) 저장가능
            								  
        },

    }
}
```

2. models.py 작성

```python
from django.db import models
# Create your models here.


class Member(models.Model):
    nickname = models.CharField(max_length=55)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nickname
```

3. migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Teminal에서 shell로 테스트

```bash
python manage.py shell

from test.models import Member
member1 = Member.objects.create(nickname='John', email='john@example.com')
member2 = Member.objects.create(nickname='Jane', email='jane@example.com')
```

5. mysql db확인 (mysql workbench로 하거나 cmd로 하거나)









