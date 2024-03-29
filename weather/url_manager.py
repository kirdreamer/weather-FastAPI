class UrlManagerMixin:
    @staticmethod
    def add_arguments_to_url(url: str, arguments: dict[str, str]) -> str:
        return f'{url}?' + "&".join([f"{key}={value}" for key, value in arguments.items()])
        