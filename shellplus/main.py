from IPython import embed

from shellplus import banner_map, import_map


def start_ipython():
    # 1) import
    # for from_, import_ in import_map.items():
    #     globals().update({from_:import_})
    globals().update(**import_map)

    # 2) print
    banner = '■■■■■■■■■■■■ Shellplus for Everyone ■■■■■■■■■■■■\n'
    # 일반 모듈
    for stem, target_list in banner_map.items():
        if stem == 'instance':
            continue
        banner += f"from {stem} import {', '.join(target_list)}\n"
    banner += '\n'

    # instancing
    instance_string_list = banner_map.get('instance', [])
    banner += '\n'.join(instance_string_list)

    banner += '\n'

    embed(colors='neutral', banner2=banner)
