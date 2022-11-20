import pytest
from neurolab_conda.youtube import get_time_info
from neurolab_conda.custom_exception import InvalidURLException

good_URL_data = [
    ("https://youtu.be/roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", 42),
]

URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
    ("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s")
]



@pytest.mark.parametrize("url,response",good_URL_data)
def test_get_time_info(url,response):
    assert get_time_info(url)==response


@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)