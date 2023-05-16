import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in instance.items:
        return

    lines = txt_importer(path_file)

    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(path_file)
    print(file_dict)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    path_file = instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        lines = txt_importer(path_file)

        file_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }

        print(file_dict)
    except (IndexError, UnboundLocalError):
        print("Posição inválida", file=sys.stderr)
