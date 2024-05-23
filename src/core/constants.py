MAX_LENGTH_DEFAULT = 255
MAX_LENGTH = 5000


class NewsCfg:
    """
    Настройки для модели News.
    """

    HELP_MSG_NAME = "Введите название новости"
    HELP_MSG_TXT = f"Напишите текст новости до {MAX_LENGTH} символов"
    HELP_MSG_IMG = "Добавьте ссылки на изображения"


class EventsCfg:
    """
    Настройки для модели Events.
    """

    EVENTS_HELP_MSG_NAME = "Введите название события"
    EVENTS_HELP_MSG_TXT = (
        f"Напишите текст о событии до {MAX_LENGTH} символов"
    )
    EVENTS_HELP_MSG_IMG = "Добавьте ссылки на изображения с событиями"


class DisciplinesCfg:
    """
    Настройки для модели Disciplines.
    """

    DISCIPLINES = "Disciplines"
    DISCIPLINE_NAME_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINE_NAME_HELP_MSG = "Напишите название дисциплины"
    DISCIPLINE_DESCRIPTION_VERBOSE_NAME = "Описание дисциплины"
    DISCIPLINE_DESCRIPTION_HELP_MSG = (
        f"Напишите описание дисциплины до {MAX_LENGTH} символов"
    )
    DISCIPLINE_IMG_URLS_RELATED_NAME = "disciplines_images"
    DISCIPLINE_IMG_URLS_VERBOSE_NAME = "Изображения для дисциплин"
    DISCIPLINE_IMG_URLS_HELP_MSG = (
        "Добавьте ссылки на изображения с дисциплиной"
    )
    DISCIPLINE_RULES_VERBOSE_NAME = "Правила спортивных дисциплин"
    DISCIPLINE_RULES_HELP_MSG = (
        f"Напишите правила дисциплины до {MAX_LENGTH} символов"
    )
    DISCIPLINE_META_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINE_META_VERBOSE_NAME_PLURAL = "Спортивные дисциплины"


class DisciplinesImageURLCfg:
    """
    Настройки для модели DisciplinesImageURL.
    """

    DISCIPLINES_IMG_URL = "DisciplinesImageURL"
    DISCIPLINES_IMG_URL_FOREIGN_RELATED_NAME = "discipline"
    DISCIPLINES_IMG_URL_FOREIGN_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINES_IMG_URL_VERBOSE_NAME = "Ссылка на изображение с дисциплиной"
    DISCIPLINES_IMG_URL_HELP_MSG = (
        "Укажите URL-адрес изображения с видом спорта"
    )


class AboutCfg:
    HELP_MSG_NAME = "Введите имя участника"
    HELP_MSG_TXT = f"Укажите текст истории до {MAX_LENGTH} символов"
