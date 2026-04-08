from django.shortcuts import render
from django.views import View
from .models import Facture

class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # On récupère les factures ici pour qu'elles soient à jour à chaque chargement
        factures = Facture.objects.select_related('client', 'save_by').all()
        context = {
            'factures': factures
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Même logique pour le POST si tu en as besoin
        factures = Facture.objects.select_related('client', 'save_by').all()
        context = {
            'factures': factures
        }
        return render(request, self.template_name, context)