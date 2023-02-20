import json
import django
import os

"""Script para gravar vários papéis no banco  de dados"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()
from core.models import Paper
from core.helpers import DataApiFinancePaper


with open('papersB3.json','r') as file:
    text = file.read()
    data_b3 = dict(json.loads(text))
    print('Arquivo json lido com sucesso')
    for paper in data_b3.keys():

        try:
            DataApiFinancePaper(paper, data_b3[paper]).create_paper()

            print(f'Criou o papel {paper}')

        except Exception as err:
            print(f'falha ao baixar dados do papel {paper}')
            print(err)

print('Sucesso!')
