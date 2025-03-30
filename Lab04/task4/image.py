class ImageLoadingStrategy:
    def load_image(self, href: str) -> str:
        raise NotImplementedError("Метод load_image() повинен бути реалізований у підкласі.")


class FileSystemImageStrategy(ImageLoadingStrategy):
    def load_image(self, href: str) -> str:
        return f"Завантажено з файлової системи: {href}"


class NetworkImageStrategy(ImageLoadingStrategy):
    def load_image(self, href: str) -> str:
        return f"Завантажено з мережі: {href}"


class Image:
    def __init__(self, href: str):
        self.href = href
        if href.startswith("http://") or href.startswith("https://"):
            self.strategy = NetworkImageStrategy()
        else:
            self.strategy = FileSystemImageStrategy()

    def display(self):
        result = self.strategy.load_image(self.href)
        print(result)
