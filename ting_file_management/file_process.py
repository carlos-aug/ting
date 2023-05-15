import os
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_name = os.path.basename(path_file)
    if file_name in instance.items:
        print(f"{file_name} já foi processado anteriormente.")
        return

    lines = txt_importer(path_file)
    if not lines:
        print(f"{path_file} não pode ser processado.")
        return

    file_dict = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(file_name)
    print(file_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
