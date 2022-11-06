```python
from django.views.decorators.http
@require_http_methods
@require_POST
@require_safe
# 일치하지않으면 405 Method Not Allowed
```