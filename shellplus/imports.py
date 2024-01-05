from __future__ import annotations

import re
from importlib import import_module
from pathlib import Path

from . import banner_map, import_map


def set_banner_map(from_path, import_value):
    if (not (value_list := banner_map.get(from_path))) or import_value not in value_list:
        banner_map.setdefault(from_path, []).append(import_value)


def import_target(
        relative_module_path, target_object_list,
        instance_name: bool | str = False,
        is_package=False,
        with_table=False
):
    if not isinstance(target_object_list, (list, tuple)):  # Sequence나 Iterable을 주면 'string'을 순회 인식해버림.
        target_object_list = [target_object_list]

    if is_package:
        from_path = relative_module_path
        imported_module = import_module(f'{from_path}')

        for target_object in target_object_list:
            if target_object == '*':
                # globals().update(
                #     {name: getattr(module_of_target, name) for name in dir(module_of_target)
                #      if not name.startswith('_')}
                # )
                import_map.update(
                    {
                        module_name: getattr(imported_module, module_name) for module_name in dir(imported_module)
                        if not module_name.startswith('_')
                    }
                )

                # banner_map.setdefault(stem, []).append(target_name)
                set_banner_map(from_path, target_object)

                break

            target = getattr(imported_module, target_object)  # TODO: create_app 팩토리라면, 거내서 생성까지
            # globals().update({target_name: target})
            import_map.update({target_object: target})
            target_object = getattr(target, '__name__', target_object)

            # banner_map.setdefault(stem, []).append(target_name)
            set_banner_map(from_path, target_object)
        return

    # 1) "/" or "\" 를 사용한 사용자 상대경로 입력 -> re.split(pattern, 대상) -> Path(*list)로 상대경로 Path 제작
    relative_module_path = relative_module_path.lstrip(r'[/|\\]')
    relative_module_path_parts = re.split(r'[/|\\]', relative_module_path)

    relative_path_of_module = Path(*relative_module_path_parts)  # .resolve() # 상대주소만 이용할거면 .resolve()를 통한 C:// 절대경로는 (X

    #  schemas\picstagrams.py
    # 참고)
    # parent_paths = [part for part in relative_path_of_module.parents
    #                 if relative_path_of_module.name not in part.parts]
    # parent_paths  >> [WindowsPath('schemas'), WindowsPath('.')]

    for target_object in target_object_list:
        if len(relative_module_path_parts) > 1:
            # print(f"depth 1개이상 >>")
            # parent_paths = [part for part in module_of_target_path.parents
            #                 if module_of_target_path.name not in part.parts]
            # print(f"parent_paths >> {parent_paths}")
            # parent_paths >> [
            # WindowsPath('C:/Users/cho_desktop/PycharmProjects/htmx/schemas'),
            # WindowsPath('C:/Users/cho_desktop/PycharmProjects/htmx'),
            # WindowsPath('C:/Users/cho_desktop/PycharmProjects'),
            # WindowsPath('C:/Users/cho_desktop'),
            # WindowsPath('C:/Users'),
            # WindowsPath('C:/')
            # ]

            # relative_path = module_of_target_path.relative_to(root_path)
            # print(f"relative_path >> {relative_path} in {__file__}")

            # relative_path >> schemas\picstagrams.py
            path_elements = '.'.join(
                list(relative_path_of_module.parts[:-1]) + [relative_path_of_module.stem])
            # print(f"path_elements  >> {path_elements}")
            # path_elements  >> schemas.picstagrams
            from_path = path_elements
        else:
            from_path = relative_path_of_module.stem

        # print(f"stem  >> {stem}")
        imported_module = import_module(f'{from_path}')

        if target_object == '*':
            # globals().update(
            #     {name: getattr(module_of_target, name) for name in dir(module_of_target)
            #      if not name.startswith('_')}
            # )
            import_map.update(
                {name: getattr(imported_module, name) for name in dir(imported_module)
                 if not name.startswith('_')}
            )
            banner_map.setdefault(from_path, []).append(target_object)
            break

        target = getattr(imported_module, target_object)
        # globals().update({target_name: target})
        import_map.update({target_object: target})

        target_object = getattr(target, '__name__', target_object)
        # banner_map.setdefault(stem, []).append(target_name)
        set_banner_map(from_path, target_object)

        if instance_name:
            # globals().update({instance_name: target()})
            import_map.update({instance_name: target()})

            from_path = 'instance'
            import_value = f'{instance_name} = {target_object}()'
            # if (not (value_list := banner_map.get(from_path))) or import_value not in value_list:
            #     banner_map.setdefault(from_path, []).append(import_value)
            set_banner_map(from_path, import_value)

        if target_object == 'Base' and with_table:
            for model_ in target.registry._class_registry.values():
                if hasattr(model_, '__tablename__'):
                    # globals()[clzz.__name__] = clzz
                    import_map.update({model_.__name__: model_})

                    from_path = model_.__module__
                    import_value = model_.__name__
                    # if (not (value_list := banner_map.get(from_path))) or import_value not in value_list:
                    #     banner_map.setdefault(from_path , []).append(import_value)
                    set_banner_map(from_path, import_value)


def import_folder(relative_folder_path):
    relative_folder_path = relative_folder_path.lstrip(r'[/|\\]')
    relative_folder_path_parts = re.split(r'[/|\\]', relative_folder_path)
    relative_path_folder = Path(*relative_folder_path_parts)  # .resolve() # 상대주소만 이용할거면 .resolve()를 통한 C:// 절대경로는 (X)

    # relative_path = folder_relative_path.relative_to(root_path)
    relative_import_module_path = '.'.join(list(relative_path_folder.parts))

    for module_path in relative_path_folder.glob('*.py'):
        module_name = module_path.stem  # xxx.py의 경로에서 .stem으로 모듈명만 추출

        # module = import_module(f'{relative_import_module_path}.{module_name}')
        imported_module = import_module(f'{relative_import_module_path}')

        for module_name in dir(imported_module):
            if module_name.startswith('_'):
                continue
            # globals().update({name: getattr(module, name)})
            import_map.update({module_name: getattr(imported_module, module_name)})

        from_path = f'{relative_import_module_path}.{module_name}'
        import_value = '*'
        # 이미 해당fromapath의 모듈list에 들어가 있는 모듈명이면 제외
        set_banner_map(from_path, import_value)
