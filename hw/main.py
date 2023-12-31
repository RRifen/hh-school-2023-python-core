from wine import Wine
from beer import Beer
from market import Market
from datetime import date
"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""


def main():
    wines = [
        Wine('good wine',    date(2020, 1, 12)),
        Wine('bad wine',     date(2020, 2, 12)),
        Wine('just wine',    date(2020, 1, 11)),
        Wine('another wine', date(2020, 1, 12)),
        Wine(None, None)
    ]
    beers = [
        Beer('good beer',    date(2021, 1, 12)),
        Beer('bad beer',     date(2019, 2, 12)),
        Beer('just beer',    date(2021, 1, 11)),
        Beer('another beer', date(2020, 2, 13)),
        Beer(None, None)
    ]
    market = Market(wines, beers)

    print('Получить список всех напитков (вина и пива) отсортированный по наименованию:')
    print(*market.get_drinks_sorted_by_title(), sep='\n', end='\n\n')

    print('Проверить наличие напитка в магазине (за время О(1))')
    print(market.has_drink_with_title('good beer'))  # True
    print(market.has_drink_with_title('just wine'))  # True
    print(market.has_drink_with_title('another bad beer'))  # False
    print(market.has_drink_with_title(None), end='\n\n')  # True

    print('Получить список напитков (вина и пива) в указанном диапазоне даты производства:')
    print(*market.get_drinks_by_production_date(
        date(2020, 2, 1),
        date(2021, 1, 1)
    ), sep='\n', end='\n')
    print(*market.get_drinks_by_production_date(
        None,
        date(2021, 1, 1)
    ), sep='\n', end='\n')
    print(*market.get_drinks_by_production_date(
        date(2020, 2, 1),
        None
    ), sep='\n', end='\n')
    print(*market.get_drinks_by_production_date(
        None,
        None
    ), sep='\n', end='\n')


if __name__ == '__main__':
    main()
