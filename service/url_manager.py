class UrlManagerMixin:
    def addArgumentsToUrl(self, url: str, arguments: dict[str, str]) -> str:
        return f'{url}?' + "&".join([f"{key}={value}" for key, value in arguments.items()])
        