countries = ["Russia", "France", "Germany", "Japan", "Brazil"]
capitals = ["Moscow", "Paris", "Berlin", "Tokyo", "Brasilia"]
cords = [[55, 37], [48, 38], [52, 77], [88, 99], [35, 12]]


def test_capitals():
    assert capitals[0] == "Moscow"
    assert capitals[1] == "Paris"
    assert capitals[2] == "Berlin"
    assert capitals[3] == "Tokyo"
    assert capitals[4] == "Brasilia"


def test_countries():
    for country in countries:
        assert country[0].isupper()



