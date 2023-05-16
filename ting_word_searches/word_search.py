from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    result = []
    for file_info in instance.items:
        filename = txt_importer(file_info)
        occurrences = []

        for i, line in enumerate(filename):
            if word.lower() in line.lower():
                occurrences.append({"linha": i + 1})
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_info,
                    "ocorrencias": occurrences,
                }
            )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
