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
    ...


def file_metadata(instance, position):
    ...
