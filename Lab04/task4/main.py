from image import Image

def main():
    print("Демонстрація завантаження зображень за допомогою шаблону 'Стратегія'\n")

    local_image = Image("images/picture.jpg")
    print("Локальне зображення:")
    local_image.display()

    print()

    network_image = Image("https://example.com/image.png")
    print("Зображення з мережі:")
    network_image.display()


if __name__ == "__main__":
    main()
