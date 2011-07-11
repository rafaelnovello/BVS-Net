from django.http import HttpResponse

from reports import RelatorioListagem
from geraldo.generators import PDFGenerator
from models import Instance

def testReport(request):
    resp = HttpResponse(mimetype='application/pdf')
    
    instances = Instance.objects.order_by('name', 'id')
    rel = RelatorioListagem(queryset=instances)
    rel.generate_by(PDFGenerator, filename=resp)
    
    return resp
    
    
