from babel.support import Translations

LOCALE_PATH = 'locale'
LANGUAGE = 'zh_Hans'

translations = Translations.load(LOCALE_PATH, [LANGUAGE])
_ = translations.gettext

print(_('hello world'))