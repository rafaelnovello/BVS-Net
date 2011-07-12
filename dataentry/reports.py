# -*- coding: utf-8 -*-
from geraldo import Report, ReportBand, ObjectValue, ReportBand, landscape,SystemField, BAND_WIDTH, Label

from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A5
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from datetime import datetime

class RelatorioListagem(Report):
    title = 'Listagem de Instancias BVS'
    print_if_empty = True
    page_size = landscape(A5)

    class band_detail(ReportBand):
        height = 0.5*cm
        elements=(
                ObjectValue(attribute_name='id', left=0.5*cm),
                ObjectValue(attribute_name='name', left=4*cm),
                ObjectValue(attribute_name='status', left=8*cm),
                ObjectValue(attribute_name='portal_type', left=12*cm),
                ObjectValue(attribute_name='responsible', left=16*cm),
                    #get_value=lambda instance: instance.data_lancamento.strftime('%d/%m/%Y')),
                )
    
    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                Label(text="ID", top=0.8*cm, left=0.5*cm),
                Label(text=u"Instância", top=0.8*cm, left=4*cm),
                Label(text=u"Status", top=0.8*cm, left=8*cm),
                Label(text=u"Tipo de Portal", top=0.8*cm, left=12*cm),
                Label(text=u"Responsável", top=0.8*cm, left=16*cm),
                SystemField(expression=u'Página %(page_number)d de %(page_count)d', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
        ]
        borders = {'bottom': True}

    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
                Label(text='Geraldo Reports', top=0.1*cm),
                SystemField(expression=u'Impresso em: %s' % datetime.today(), top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}
