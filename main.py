from controllers.menu import MenuManager
from views.menu import MenuViews


def main():
    MenuViews.app_title()
    MenuManager().main_menu_start()


if __name__ == "__main__":
    main()
