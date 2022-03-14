

def full_name(first, last, middle=''):
    """Отдает полное имя и фамилю пользователя"""
    if middle:
        full = first + ' ' + last + ' ' + middle
    else:
        full = first + ' ' + last
    return full.title()


# print(full_name('Yrysgul', 'Ergesh', 'Ergeshovna'))