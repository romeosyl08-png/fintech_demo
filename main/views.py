from django.shortcuts import render
from .forms import ContactForm
from .brvm_data import BRVM_ACTIONS

def index(request):
    form = ContactForm()
    context = {'form': form, 'actions': BRVM_ACTIONS}
    
    if request.method == 'POST':
        
        # Si c'est le simulateur
        if 'simuler' in request.POST:
            symbole = request.POST.get('action_choisie')
            montant = int(request.POST.get('montant', 0))
            
            # Trouver l'action choisie
            action = next((a for a in BRVM_ACTIONS if a['symbole'] == symbole), None)
            
            if action and montant > 0:
                nb_actions = montant // action['prix']
                # Gain estimé basé sur la variation
                gain = int(montant * (action['variation'] / 100))
                
                context['simulation'] = {
                    'nom': action['nom'],
                    'montant': montant,
                    'nb_actions': nb_actions,
                    'gain': gain
                }
        
        # Si c'est le formulaire de contact
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                context['success'] = True
                context['form'] = ContactForm()
    
    return render(request, 'main/index.html', context)
