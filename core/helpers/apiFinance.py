import yfinance as yf
from core.models import Paper


def create_paper(paper_code):
    b3_code = paper_code.upper + '.SA'
    paper_data = yf.Ticker(b3_code)
    company_name = paper_data.info['longName']
