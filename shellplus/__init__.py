from collections import OrderedDict

# 하위모듈이 사용할 전역 데이터 -> 하위모듈에서 채우고 -> import한 외부 shell.py에서 globals() 등에 입력할 때 사용한다.
banner_map = OrderedDict()
import_map = dict()

from .imports import import_target, import_folder
from .main import start_ipython



