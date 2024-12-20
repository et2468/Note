# PyQt 기본 구성 요소

```python
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
```

1. 윈도우 

   - 모든 위젯의 가장 기초가 되는 위젯을 윈도우라고 부른다.

   - 나만의 윈도우 클래스를 만들어서 사용하기 위해,

   - PyQt가 제공하는 `QMainWindow`를 상속 받아서 `MyWindow`라는 클래스를 정의합니다.

2. 명령줄 인수: `sys.argv`
   - 프로그램을 실행할 때 명령줄에서 입력하는 추가적인 값이나 데이터

3. super()

   - `MyWindow` 클래스는 `QMainWindow` 클래스를 상속받는데, 생성자에서 부모클래스인 `QMainWindow`의 생성자를 호출해줘야 합니다.

   - `QMainWindow`의 기능을 제대로 상속받고 사용할 수 있도록 부모 클래스의 초기화 과정을 수행

