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


class SportsCfg:
    """
    Настройки для модели Sports.
    """

    SPORTS_HELP_MSG_NAME = "Введите название вида спорта"
    SPORTS_HELP_MSG_TXT = (
        f"Напишите описание вида спорта до {MAX_LENGTH} символов"
    )
    EVENTS_HELP_MSG_IMG = "Добавьте ссылки на изображения с видами спорта"
    SPORTS_RULES_HELP_MSG_TXT = (
        f"Напишите правила вида спорта до {MAX_LENGTH} символов"
    )


class AboutCfg:
    HELP_MSG_NAME = "Введите имя участника"
    HELP_MSG_TXT = f"Укажите текст истории до {MAX_LENGTH} символов"
