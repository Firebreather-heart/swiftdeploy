set_ = {
    'APP_NAME' :'swiftdeploy',
    'APP_HEADER' : 'swiftdeploy',
    'APP_FOOTER':'swiftdeploy',
}

class Settings:
    pass

settings = Settings()
for key, item in set_.items():
    setattr(settings, key, item)