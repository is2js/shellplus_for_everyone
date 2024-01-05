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
    ```python
    # shell.py
    from shellplus import start_ipython, import_target, import_folder
    
    # 1) 내 파일 속 python 객체 import
    import_target('/main.py', 'app')
    import_target('/database.py', 'Base', with_table=True)
    import_target('/database.py', 'SessionLocal', instance_name='session')
    import_target('schemas\picstagrams.py', '*')
    
    import_target('sqlalchemy', ['select', 'or_'], is_package=True)
    
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