import pytest

from ixigo.pages.FlightSearchPage import FlightSearchPage
from ixigo.utilities.ExcelReader import get_flight_search_data


@pytest.mark.smoke
@pytest.mark.parametrize(
    "from_city,to_city,departure_date",
    get_flight_search_data()
)
def test_flight_search(setup, from_city, to_city, departure_date):

    flight_page = FlightSearchPage(setup)

    flight_page.search_flight(
        from_city,
        to_city,
        departure_date
    )

    assert flight_page.is_search_results_displayed(), \
        "Flight search results page was not displayed"