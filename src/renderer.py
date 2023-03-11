"""
Функции для формирования выходной информации.
"""

from decimal import ROUND_HALF_UP, Decimal

from collectors.models import LocationInfoDTO


class Renderer:
    """
    Генерация результата преобразования прочитанных данных.
    """

    def __init__(self, location_info: LocationInfoDTO) -> None:
        """
        Конструктор.

        :param location_info: Данные о географическом месте.
        """

        self.location_info = location_info

    async def render(self) -> tuple[str, ...]:
        """
        Форматирование прочитанных данных.

        :return: Результат форматированияё
        """

        values = (
            ["--------Информация о стране/городе", f"-----------------------------"],
            ["Страна", f"{self.location_info.location.name}"],
            ["Площадь страны", f"{self.location_info.location.area}"],
            ["Столица", f"{self.location_info.location.capital}"],
            ["Широта", f"{self.location_info.location.latitude}°"],
            ["Долгота", f"{self.location_info.location.longitude}°"],
            ["Регион", f"{self.location_info.location.subregion}"],
            ["Время", f"{self.location_info.weather.dt.strftime(f'%H:%M')}"],
            ["Часовой пояс", f"{self.location_info.weather.timezone}"],
            ["Языки", f"{await self._format_languages()}"],
            ["Население страны", f"{await self._format_population()} чел."],
            ["Курсы валют", f"{await self._format_currency_rates()}"],
            ["----------------------------Погода", f"----------------------------"],
            ["О погоде", f"{self.location_info.weather.description}"],
            ["Температура", f"{self.location_info.weather.temp} °C"],
            ["Скорость ветра", f"{self.location_info.weather.wind_speed}"],
            ["Видимость",f"{self.location_info.weather.visibility}м"],
            ["Облачность", f"{self.location_info.weather.clouds}"],
            ["Давление", f"{self.location_info.weather.pressure} мм рт. ст."],
            ["Влажность", f"{self.location_info.weather.humidity}%"],
            ["---------------------------Новости", f"----------------------------"],

        )

        length = len(self.location_info.news.articles)
        if length > 5:
            length = 3
        for i in range(length):
            values = (
                *values,
                [
                    f"{i+1}",
                    f"{self.location_info.news.articles.pop().author} - {self.location_info.news.articles.pop().title}",
                ],
            )

        return values

    async def _format_languages(self) -> str:
        """
        Форматирование информации о языках.

        :return:
        """

        return ", ".join(
            f"{item.name} ({item.native_name})"
            for item in self.location_info.location.languages
        )

    async def _format_population(self) -> str:
        """
        Форматирование информации о населении.

        :return:
        """

        # pylint: disable=C0209
        return "{:,}".format(self.location_info.location.population).replace(",", ".")

    async def _format_currency_rates(self) -> str:
        """
        Форматирование информации о курсах валют.

        :return:
        """

        return ", ".join(
            f"{currency} = {Decimal(rates).quantize(exp=Decimal('.01'), rounding=ROUND_HALF_UP)} руб."
            for currency, rates in self.location_info.currency_rates.items()
        )
