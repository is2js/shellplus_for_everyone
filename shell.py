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
