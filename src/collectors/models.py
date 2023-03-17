"""
Описание моделей данных (DTO).
"""

from datetime import datetime
from pydantic import Field, BaseModel

class HashableBaseModel(BaseModel):
    """
    Добавление хэшируемости для моделей.
    """

    def __hash__(self) -> int:
        return hash((type(self),) + tuple(self.__dict__.values()))


class LocationDTO(HashableBaseModel):
    """
    Модель локации для получения сведений о погоде.

    .. code-block::

        LocationDTO(
            capital="Mariehamn",
            alpha2code="AX",
        )
    """

    capital: str
    alpha2code: str = Field(min_length=2, max_length=2)  # country alpha‑2 code


class CurrencyInfoDTO(HashableBaseModel):
    """
    Модель данных о валюте.

    .. code-block::

        CurrencyInfoDTO(
            code="EUR",
        )
    """

    code: str


class LanguagesInfoDTO(HashableBaseModel):
    """
    Модель данных о языке.

    .. code-block::

        LanguagesInfoDTO(
            name="Swedish",
            native_name="svenska"
        )
    """

    name: str
    native_name: str


class CountryDTO(BaseModel):
    """
    Модель данных о стране.

    .. code-block::

        CountryDTO(
            capital="Mariehamn",
            alpha2code="AX",
            alt_spellings=[
              "AX",
              "Aaland",
              "Aland",
              "Ahvenanmaa"
            ],
            currencies={
                CurrencyInfoDTO(
                    code="EUR",
                )
            },
            flag="http://assets.promptapi.com/flags/AX.svg",
            languages={
                LanguagesInfoDTO(
                    name="Swedish",
                    native_name="svenska"
                )
            },
            name="\u00c5land Islands",
            population=28875,
            subregion="Northern Europe",
            timezones=[
                "UTC+02:00",
            ],
            area=1580.0,
            latitude="60.116667°",
            longitude="19.9°"
        )
    """

    capital: str
    alpha2code: str
    alt_spellings: list[str]
    currencies: set[CurrencyInfoDTO]
    flag: str
    languages: set[LanguagesInfoDTO]
    name: str
    population: int
    subregion: str
    timezones: list[str]
    area: float | None
    latitude: float | None
    longitude: float | None

class CurrencyRatesDTO(BaseModel):
    """
    Модель данных о курсах валют.

    .. code-block::

        CurrencyRatesDTO(
            base="RUB",
            date="2022-09-14",
            rates={
                "EUR": 0.016503,
            }
        )
    """

    base: str
    date: str
    rates: dict[str, float]

class NewsAllArticlesDTO(HashableBaseModel):
    """
    Модель данных о статье
    .. code-block::
        NewsArticlesDTO(
         id="google-news",
            name="Google News,
            author="The Guardian",
            title="UK economy rebounds with 0.3% growth in January; bank shares tumble in market turmoil \u2013 business live - The Guardian"",
            description=null,
            url="link",
            publishedAt="2023-03-10T10:44:52Z",
            content="content"
        )
    """

    id: str | None
    name: str | None
    author: str | None
    title: str | None
    description: str | None
    url: str | None
    publishedAt: str | None
    content: str | None

class NewsInfoDTO(BaseModel):
    """
    Модель данных о новостях

    .. code-block::

        NewsInfoDTO(
            totalResults:38,
            articles[
                NewsSourceInfoDTO(
                    id="google-news",
                    name="Google News,
                    author="The Guardian",
                    title="UK economy rebounds with 0.3% growth in January; bank shares tumble in market turmoil \u2013 business live - The Guardian"",
                    description=null,
                    url="link",
                    publishedAt="2023-03-10T10:44:52Z",
                    content="content"
                )
            ]
        )
    """

    totalResults: int
    articles: set[NewsAllArticlesDTO]

class WeatherInfoDTO(BaseModel):
    """
    Модель данных о погоде.

    .. code-block::

        WeatherInfoDTO(
            temp=13.92,
            pressure=1023,
            humidity=54,
            wind_speed=4.63,
            description="scattered clouds",
        )
    """

    temp: float
    pressure: int
    humidity: int
    wind_speed: float
    description: str
    visibility: float
    clouds: float
    dt: datetime
    timezone: int

class LocationInfoDTO(BaseModel):
    """
    Модель данных для представления общей информации о месте.

    .. code-block::

        LocationInfoDTO(
            location=CountryDTO(
                capital="Mariehamn",
                alpha2code="AX",
                alt_spellings=[
                  "AX",
                  "Aaland",
                  "Aland",
                  "Ahvenanmaa"
                ],
                currencies={
                    CurrencyInfoDTO(
                        code="EUR",
                    )
                },
                flag="http://assets.promptapi.com/flags/AX.svg",
                languages={
                    LanguagesInfoDTO(
                        name="Swedish",
                        native_name="svenska"
                    )
                },
                name="\u00c5land Islands",
                population=28875,
                subregion="Northern Europe",
                timezones=[
                    "UTC+02:00",
                ],
            ),
            weather=WeatherInfoDTO(
                temp=13.92,
                pressure=1023,
                humidity=54,
                wind_speed=4.63,
                description="scattered clouds",
            ),
            currency_rates={
                "EUR": 0.016503,
            },
        )
    """

    location: CountryDTO
    weather: WeatherInfoDTO
    currency_rates: dict[str, float]
    news: NewsInfoDTO | None
