EVENTS_ORDER = "-start_date"
MAX_LENGTH_DEFAULT = 255
MAX_LENGTH = 5000
MAX_LIST_LENGTH = 15
NEWS_ORDER = "-pub_date"
PAGE = "page"
PK = 1
RELATED_NAME_MAP = {
    "News": "news",
    "Events": "event",
    "Disciplines": "discipline",
}


class MediaValidatorCfg:
    """
    Настройки для валидации ссылок
    на изображения и видео.
    """
    IMAGE = "image"
    VIDEO = "video"
    TEXT = "text"
    CONTENT_TYPE = "content-type"
    URL_ERR_MSG = "Укажите корректный URL-адрес"
    URL_ERR_IMG = "URL-адрес не указывает на изображение"
    URL_ERR_VID = "URL-адрес не указывает на видео"
    ACCESS_ERR_MSG = "Не удалось получить доступ к ссылке. "
    YT_REGEX = (r"(https?://)?(www\.)?"
                r"(youtube|youtu|youtube-nocookie)\.(com|be)/"
                r"(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})")


class NewsCfg:
    """
    Настройки для модели News.
    """

    NEWS = "News"
    NEWS_NAME_VERBOSE_NAME = "Название новости"
    NEWS_NAME_HELP_MSG = "Введите название новости"
    NEWS_IMG_URLS_RELATED_NAME = "images"
    NEWS_IMG_URLS_VERBOSE_NAME = "Добавьте ссылки на изображения"
    NEWS_IMG_URLS_HELP_MSG = "Добавьте ссылки на изображения"
    NEWS_PUB_DATE_VERBOSE_NAME = "Дата публикации новости"
    NEWS_DESCRIPTION_VERBOSE_NAME = "Содержание новости"
    NEWS_DESCRIPTION_HELP_MSG = (
        f"Напишите текст новости до {MAX_LENGTH} символов"
    )
    NEWS_META_ORDERING_FIELD = "-" + "pub_date"
    NEWS_META_VERBOSE_NAME = "Новость"
    NEWS_META_VERBOSE_NAME_PLURAL = "Новости"


class NewsImageURLCfg:
    NEWS_IMAGE_URL = "NewsImageURL"
    NEWS_IMG_URL_FOREIGN_RELATED_NAME = "news"
    NEWS_IMG_URL_FOREIGN_VERBOSE_NAME = "Новость"
    NEWS_IMG_URL_VERBOSE_NAME = "Ссылка на изображение для новости"
    NEWS_IMG_URL_HELP_MSG = "Укажите URL-адрес изображения о новости"
    NEWS_IMG_URL_META_VERBOSE_NAME = "Ссылка на новость"
    NEWS_IMG_URL_META_VERBOSE_NAME_PLURAL = "Ссылки на новости"


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
    EVENTS_START_DATE_VERBOSE_NAME = "Дата проведения события"
    EVENTS_START_DATE_HELP_MSG = "Выберите дату проведения события"
    EVENTS_PLACE_VERBOSE_NAME = "Место события"
    EVENTS_PLACE_HELP_MSG = "Введите название места события"
    EVENTS_RULES_VERBOSE_NAME = "Правила проведения события"
    EVENTS_RULES_HELP_MSG = "Напишите правила проведения события"
    EVENTS_DEADLINE_REG_VERBOSE_NAME = "Дата окончания регистрации на событие"
    EVENTS_DEADLINE_REG_HELP_MSG = (
        "Выберите дату окончания регистрации на событие"
    )
    EVENTS_DISCIPLINE_FOREIGN_KEY = "disciplines.Disciplines"
    EVENTS_DISCIPLINE_RELATED_NAME = "event_discipline"
    EVENTS_DISCIPLINE_VERBOSE_NAME = "Дисциплина для события"
    EVENTS_DISCIPLINE_HELP_MSG = "Выберите дисциплину для события"
    EVENTS_META_ORDERING_FIELD = "-" + "start_date"
    EVENTS_META_VERBOSE_NAME = "Событие"
    EVENTS_META_VERBOSE_NAME_PLURAL = "События"


class EventsImageURLCfg:
    EVENTS_IMAGE_URL = "EventsImageURL"
    EVENTS_IMG_URL_FOREIGN_RELATED_NAME = "event"
    EVENTS_IMG_URL_FOREIGN_VERBOSE_NAME = "Событие"
    EVENTS_IMG_URL_VERBOSE_NAME = "Ссылка на изображение события"
    EVENTS_IMG_URL_HELP_MSG = "Укажите URL-адрес изображения о событии"
    EVENTS_IMG_URL_META_VERBOSE_NAME = "Ссылка на событие"
    EVENTS_IMG_URL_META_VERBOSE_NAME_PLURAL = "Ссылки на событие"


class DisciplinesCfg:
    """
    Настройки для модели Disciplines.
    """

    DISCIPLINES = "Disciplines"
    DISCIPLINES_NAME_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINES_NAME_HELP_MSG = "Напишите название дисциплины"
    DISCIPLINES_DESCRIPTION_VERBOSE_NAME = "Описание дисциплины"
    DISCIPLINES_DESCRIPTION_HELP_MSG = (
        f"Напишите описание дисциплины до {MAX_LENGTH} символов"
    )
    DISCIPLINES_IMG_URLS_RELATED_NAME = "disciplines_images"
    DISCIPLINES_IMG_URLS_VERBOSE_NAME = "Изображения для дисциплин"
    DISCIPLINES_IMG_URLS_HELP_MSG = (
        "Добавьте ссылки на изображения с дисциплиной"
    )
    DISCIPLINES_RULES_VERBOSE_NAME = "Правила спортивной дисциплины"
    DISCIPLINES_RULES_HELP_MSG = (
        f"Напишите правила дисциплины до {MAX_LENGTH} символов"
    )
    DISCIPLINES_META_ORDERING_FIELD = "name"
    DISCIPLINES_META_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINES_META_VERBOSE_NAME_PLURAL = "Спортивные дисциплины"


class DisciplinesImageURLCfg:
    """
    Настройки для модели DisciplinesImageURL.
    """

    DISCIPLINES_IMG_URL = "DisciplinesImageURL"
    DISCIPLINES_IMG_URL_FOREIGN_RELATED_NAME = "discipline"
    DISCIPLINES_IMG_URL_FOREIGN_VERBOSE_NAME = "Спортивная дисциплина"
    DISCIPLINES_IMG_URL_VERBOSE_NAME = "Ссылка на изображение с дисциплиной"
    DISCIPLINES_IMG_URL_HELP_MSG = (
        "Укажите URL-адрес изображения со спортивной дисциплиной"
    )
    DISCIPLINES_IMG_URL_META_VERBOSE_NAME = "Ссылка на спортивную дисциплину"
    DISCIPLINES_IMG_URL_META_VERBOSE_NAME_PLURAL = (
        "Ссылки на спортивную дисциплину"
    )


class AboutCfg:
    """
    Настройки для модели About.
    """
    NAME_VERBOSE_NAME = "Название"
    DESCRIPTION_VERBOSE_NAME = "Подробное описание"
    IMAGE_URL_VERBOSE_NAME = "Ссылка на изображение"
    HELP_MSG_IMG = "Укажите URL-адрес изображения"
    HELP_MSG_NAME = "Введите имя участника"
    HELP_MSG_ROLE = "Название роли, к которой относится участник"
    HELP_MSG_BRAND = "Укажите название"
    MAX_LENGTH_NAME = 50
    ABOUT_VERBOSE_NAME = "О нас"
    ABOUT_VERBOSE_NAME_PLURAL = ABOUT_VERBOSE_NAME


class CustomUserCfg:
    """
    Настройки для модели CustomUser.
    """

    REQUIRED_FIELDS = ("phone_number", )
    USERNAME_FIELD = "email"
    USER_ROLE = "UserRole"
    FIRST_NAME_VERBOSE_NAME = "Имя"
    LAST_NAME_VERBOSE_NAME = "Фамилия"
    PHONE_NUMBER_VERBOSE_NAME = "Номер телефона"
    EMAIL_VERBOSE_NAME = "email"
    ROLE_VERBOSE_NAME = "Роль"
    ROLE_RELATED_NAME = "users"
    IS_ACTIVE_VERBOSE_NAME = "Аккаунт активен"
    IS_STAFF_VERBOSE_NAME = "Является персоналом"
    HELP_MSG_FIRST = "Введите имя"
    HELP_MSG_LAST = "Введите фамилию"
    HELP_MSG_PHONE = "Введите номер телефона в формате +7999 999 99 99"
    HELP_MSG_ROLE = "Название роли, к которой относится пользователь"
    MAX_LENGTH_NAME = 50
    CUSTOM_USER_VERBOSE_NAME = "user"
    CUSTOM_USER_VERBOSE_NAME_PLURAL = "users"


class UserRoleCfg:
    """
    Настройки для модели UserRole.
    """

    NAME_ROLE_DEFAULT = "Участник"
    NAME_ROLE_VERBOSE_NAME = "Название роли"
    IS_ACTIVE_VERBOSE_NAME = "Роль активна"
    USER_ROLE_VERBOSE_NAME = "Роль"
    USER_ROLE_VERBOSE_NAME_PLURAL = "Роли"


class CustomUserManagerCfg:
    """
    Настройки для модели CustomUserManager.
    """
    ERR_MSG_EMAIL = "The Email field must be set"
    ERR_MSG_SUPERUSER = "Superuser must have is_superuser=True."
    IS_SUPERUSER = "is_superuser"
    IS_STAFF = "is_staff"


class BannerVideoCfg:
    """
    Настройки для модели BannerVideo.
    """
    VIDEO_URL_VERBOSE_NAME = "Ссылка на видео"
    HELP_MSG_VIDEO = "Укажите URL-адрес видео"
    BANNER_VIDEO_VERBOSE_NAME = "Промо видео"
    BANNER_VIDEO_VERBOSE_NAME_PLURAL = "Промо видео"


class OurMemberCfg:
    """
    Настройки для модели OurMember.
    """
    ROLE_MODEL = "MemberRole"
    ROLE_RELATED_NAME = "members"
    ROLE_VERBOSE_NAME = "Роль"
    IMAGE_URL_VERBOSE_NAME = "Ссылка на изображение"
    IMAGE_URL_HELP_TEXT = "Укажите URL-адрес изображения"
    NAME_VERBOSE_NAME = "Имя"
    TEXT_VERBOSE_NAME = "История участника"
    TEXT_HELP_MSG = f"Укажите текст истории до {MAX_LENGTH} символов"
    OUR_MEMBERS_VERBOSE_NAME = "Наш участник"
    OUR_MEMBERS_VERBOSE_NAME_PLURAL = "Наши участники"


class MemberRoleCfg:
    """
    Настройки для модели MemberRole.
    """
    NAME_VERBOSE_NAME = "Название роли"
    NAME_DEFAULT = "Общественный деятель"
    IS_ACTIVE_VERBOSE_NAME = "Роль активна",
    MEMBER_ROLE_VERBOSE_NAME = "Роль участника"
    MEMBER_ROLE_VERBOSE_NAME_PLURAL = "Роли участников"


class PartnerLogoCfg:
    """
    Настройки для модели PartnerLogo.
    """
    NAME_VERBOSE_NAME = "Название"
    PARTNER_HELP_MSG = "Введите название партнера"
    IMAGE_URL_VERBOSE_NAME = "Ссылка на изображение"
    PARTNER_LOGO_VERBOSE_NAME = "Логотип партнера"
    PARTNER_LOGO_VERBOSE_NAME_PLURAL = "Логотипы партнеров"


class BrandBookCfg:
    """
    Настройки для модели BrandBook.
    """
    ORDERING = ("-pub_date",)
    NAME_VERBOSE_NAME = "Название"
    UPLOAD_TO = "brandbook"
    FILE_VERBOSE_NAME = "Файл брендбука"
    PUB_DATE_VERBOSE_NAME = "Дата"
    IS_ACTIVE_VERBOSE_NAME = "Брендбук активен"
    BRANDBOOK_VERBOSE_NAME = "Брендбук"
    BRANDBOOK_VERBOSE_NAME_PLURAL = "Брендбуки"
