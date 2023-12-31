from datetime import date
from decorator import decorator_time


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.drinks = (wines or []) + (beers or [])
        self.titles = {wine.title for wine in wines} | {beer.title for beer in beers}

    @decorator_time
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.titles

    @decorator_time
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(self.drinks, key=lambda drink: drink.title or "")

    @decorator_time
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        return list(
            filter(
                lambda drink:
                    drink.production_date and
                    ((from_date or date.min) <= drink.production_date) and
                    (drink.production_date <= (to_date or date.max)),
                self.drinks)
        )
