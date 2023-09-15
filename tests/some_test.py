import requests
from configure import TESTED_URL
from src.enums.global_enums import GLOBAL_ERORR_MASSEGE


def test_getting_post():
    resposne = requests.get(url=TESTED_URL,timeout=10)
    datares = resposne.json()

    assert resposne.status_code == 200, GLOBAL_ERORR_MASSEGE.WRONG_COdE.value
    assert len(datares) == 2, GLOBAL_ERORR_MASSEGE.WRONG_ENUM_CONT.value


if __name__ == '__main__':
    test_getting_post()