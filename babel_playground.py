from babel.support import Translations

LOCALE_PATH = 'locale'
LANGUAGE = 'en_US'

translations = Translations.load(LOCALE_PATH, [LANGUAGE])
_ = translations.gettext

print(_('hello world'))