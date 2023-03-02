import yfinance as yf
from core.models import Paper
"""Classe responsável por acessar a api do yahoo finance"""

class DataApiFinancePaper:
    def __init__(self, paper_code, company_name):
        self._b3_code = paper_code.upper() + '.SA'
        self._paper_data = yf.Ticker(self._b3_code)
        self._company_name = company_name
        self._last_value = self._get_value()

    def _get_value(self):
        value = self._paper_data.history(period='1d', auto_adjust=True)['Close'][0]
        return value

    def create_paper(self):
        """Método para criar um novo papel"""

        return Paper.objects.create(
            b3_code=self._b3_code,
            company_name=self._company_name,
            last_value=self._last_value,
        )


def update_values(paper_obj, period):
    """Método para atualizar valor do papel"""
    data_b3 = yf.Ticker(paper_obj.b3_code).history(period=period, auto_adjust=True, interval='1d')
    last_value = data_b3['Close'][-1]
    first_value = data_b3['Close'][0]
    paper_obj.last_value = last_value
    paper_obj.first_value = first_value

    paper_obj.save()
    print(f'{paper_obj} atualizado')

