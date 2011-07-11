# -*- coding: utf-8 -*-
from geraldo import Report, ReportBand, ObjectValue, ReportBand, landscape

from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A5

class RelatorioListagem(Report):
    title = 'Listagem de Instancias BVS'
    print_if_empty = True
    page_size = landscape(A5)

    class band_detail(ReportBand):
        height = 0.5*cm
        elements=(
                ObjectValue(attribute_name='name', left=0.5*cm),
                ObjectValue(attribute_name='status', left=3*cm),
                    #get_value=lambda instance: instance.data_lancamento.strftime('%d/%m/%Y')),
                )
