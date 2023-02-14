import yfinance as yf
from core.models import Paper


class DataApiFinancePaper:
    def __init__(self, paper_code):
        self._b3_code = paper_code.upper+'.SA'
        self._paper_data = yf.Ticker(self._b3_code)
        self._company_name = self._get_company_name()
        self._last_value = self._get_value()

    def _get_company_name(self):
        return self._paper_data.info['longName']

    def _get_value(self):
        value = self._paper_data.history(period='1d', auto_adjust=True)['Close'][0]
        return value

    def create_paper(self, paper_code):
        b3_code = paper_code.upper + '.SA'
        paper_data = yf.Ticker(b3_code)
        company_name = paper_data.info['longName']
        last_value = self._get_value()
        return True



