import yfinance as yf
from core.models import Paper


class DataApiFinancePaper:
    def __init__(self, paper_code):
        self._b3_code = paper_code.upper() + '.SA'
        self._paper_data = yf.Ticker(self._b3_code)
        self._company_name = self._get_company_name()
        self._last_value = self._get_value()
        self._logo_url = self._get_logo_url()

    def _get_company_name(self):
        print(self._b3_code)
        return self._paper_data.info['longName']

    def _get_value(self):
        value = self._paper_data.history(period='1d', auto_adjust=True)['Close'][0]
        return value

    def _get_logo_url(self):
        url_image = self._paper_data.info['logo_url']

        return url_image

    def create_paper(self):

        return Paper.objects.create(
            b3_code=self._b3_code,
            company_name=self._company_name,
            last_value=self._last_value,
            logo_url=self._logo_url,
        )



