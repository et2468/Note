## 사용자, Django서버 요청과 응답
- 사용자 URL 요청
- [URL 내부 (요청경로, 요청method, 쿠키,세션, Form데이터 등)]
- URL내부 요청경로 -> Djanog urls.py
- [URL내부 모든 데이터 ]-> view.py , [함수의 request인자]


## Django Form
- 템플릿에서 form tag 생성
- form action, method, {% url %} 속성
	- data-set, class, id, 등
- [input name="네임값"], [input작성값]이  [key : value]로 [URL요청]에 담긴다
- request인자 내부 (URL요청 내부) ![[Django request 내부.png]]
	- requset
	- type(request)
	- request.GET
	- request.GET.get('message')