## 1. Variable
- view에서 context로 넘어온 변수를을 사용할 수 있게 해준다
	- render( , , context)
	- JsonResponse(context) (axios)
- {{ variable }}구조로 사용한다

## 2. Filter
- 변수를 필터링 할 때 사용한다
- {{ variable | filter }}구조로 사용
- 60개의 filter가 있다고함

## 3. Tags {% %}
- html Tag처럼 사용되나 내장함수처럼 여러 기능을 가진다
-  {% tag %} 구조로 사용
- 약 24개의 내장태그들이 있다고함

## 3. 기본 Tags
- {% if %} {% endif %}
- {% url %}
- {% for %} {% endfor %}
- {% extends %}
- {% block %} {% endblock %}

## 4. Comments
- 주석


