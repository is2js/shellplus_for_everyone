# shellplus_for_everyone

![img_1.png](images/01.png)


## Usage
1. IPython 패키지가 없다면 설치합니다.
    ```shell
    pip install ipython
    ```
   
2. 프로젝트 폴더에 shellplus폴더를 생성하고, shellplus폴더 속 모듈들을 복사합니다.
    ![img_1.png](images/02.png)

3. 프로젝트 폴더에 shell.py를 생성한 뒤, 모듈들을 import하여 아래와 같이 사용합니다.
    - 경로는 `/`나 `\`를 사용하여 프로젝트 폴더부터 시작합니다.
    - `import_xxx()` 모듈들을 사용 후 ->  `start_ipython()`을 호출하여 실행합니다. 
    ```python
    from shellplus import start_ipython, import_target, import_folder
    
    # 1) 내 파일 속 python 객체 import
    import_target('/main.py', 'app')
    #   from main import app
    
    # 2) 내 파일 속 python 객체 import시 특별한 조건이 필요할 때
    # 2-1) Sqlalchemy 의 Base객체를 상속받은 모든 테이블 class들을 import
    import_target('/database.py', 'Base', with_table=True)
    #   from database import Base, SessionLocal
    #   from models import Film, Employee, Department
    
    # 2-2) class import로서, 인스터싱을 추가로 하는 경우, 인스턴스의 명칭을 같이 입력
    import_target('/database.py', 'SessionLocal', instance_name='session')
    #   session = SessionLocal()
    
    # 2-3) 프로젝트 경로가 아닌, 하위경로의 모듈 전체를 import하는 경우
    #   import_target('schemas/picstagrams.py', 'PostSchema')
    #   import_target('schemas/abc/picstagrams.py', 'TagCreateReq')
    
    # 2-4) 여러 python객체를 import하는 경우 list로 입력
    #   import_target('schemas/picstagrams.py', ['TagCreateReq', 'PostSchema'])
    import_target('schemas\picstagrams.py', '*')
    
    
    # 3) 폴더를 지정하여 *.py의 모든 모듈들을 import하기
    import_folder('schemas')
    #   from schemas.picstagrams import *
    #   from schemas.tracks import *
    #   from schemas.utils import *
    
    
    # 4) 설치된 패키지 from -> .으로 연결된 상대경로 / import -> * or 'select' or ['select', 'or_']
    import_target('sqlalchemy', ['select', 'or_'], is_package=True)
    #   from sqlalchemy import select, or_
    
    
    start_ipython()

    ```
   

4. 터미널에서 shell.py를 실행하여 IPython의 장점(자동완성, 히스토리, 색상, 도움말)을 활용하여 테스트 합니다.
    ```shell
    python .\shell.py
    ```
    ```ipython
    Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.18.1 -- An enhanced Interactive Python. Type '?' for help.
    
    ■■■■■■■■■■■■ Shellplus for FastAPI ■■■■■■■■■■■■
    from main import app
    from database import Base, SessionLocal
    from models import Film, Employee, Department
    from schemas.picstagrams import *
    from sqlalchemy import select, or_
    
    session = SessionLocal()
    In [1]: TagCreateReq.parse_obj({'value':'[asdf'})
    Out[1]: TagCreateReq(name='[asdf')
    
    In [2]: TagCreateReq.parse_obj({'value':'[asdf'})
    Out[2]: TagCreateReq(name='[asdf')
    
    In [3]: exit
    
    ```