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
    EVENTS = "Events"
    EVENTS_NAME_VERBOSE_NAME = "Название события"
    EVENTS_NAME_HELP_MSG = "Введите название события"
    EVENTS_DESCRIPTION_VERBOSE_NAME = "Описание события"
    EVENTS_DESCRIPTION_HELP_MSG = (
        f"Напишите текст о событии до {MAX_LENGTH} символов"
    )
    EVENTS_IMG_RELATED_NAME = "events_images"
    EVENTS_IMG_URLS_VERBOSE_NAME = "Изображения для события"
    EVENTS_IMG_URLS_HELP_MSG = "Добавьте ссылки на изображения с событиями"
    EVENTS_PUB_DATE_VERBOSE_NAME = "Дата события"
    EVENTS_PUB_DATE_HELP_MSG = "Выберите дату события"
    EVENTS_PLACE_VERBOSE_NAME = "Место события"
    EVENTS_PLACE_HELP_MSG = "Введите название места события"
    EVENTS_DISCIPLINE_VERBOSE_NAME = "Дисциплина для события"
    EVENTS_DISCIPLINE_HELP_MSG = "Выберите дисциплину для события"
    EVENTS_META_VERBOSE_NAME = "Событие"
    EVENTS_META_VERBOSE_NAME_PLURAL = "События"


class EventsImageURLCfg:
    EVENTS_IMAGE_URL = "EventsImageURL"
    EVENTS_IMG_URL_FOREIGN_RELATED_NAME = "events"
    EVENTS_IMG_URL_FOREIGN_VERBOSE_NAME = "События"
    EVENTS_IMG_URL_VERBOSE_NAME = "Ссылка на изображение события"
    EVENTS_IMG_URL_HELP_MSG = "Укажите URL-адрес изображения о событии"




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
