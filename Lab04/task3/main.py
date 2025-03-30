from element import LightHTMLElement

def on_click(event_info):
    print("Обробник 'click': Користувач натиснув на елемент!")
    if event_info:
        print("Додаткова інформація:", event_info)


def on_mouseover(event_info):
    print("Обробник 'mouseover': Курсор наведено на елемент!")
    if event_info:
        print("Додаткова інформація:", event_info)


def main():
    button = LightHTMLElement("button", "Натисни мене!")
    print("Створено HTML елемент:", button)

    button.addEventListener("click", on_click)
    button.addEventListener("mouseover", on_mouseover)

    button.dispatchEvent("click", {"x": 150, "y": 300})
    button.dispatchEvent("mouseover", {"element": "button", "status": "hover"})

    button.dispatchEvent("dblclick")


if __name__ == "__main__":
    main()
