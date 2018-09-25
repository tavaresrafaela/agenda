from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Comment
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
from datetime import datetime, timedelta
from .forms import EventForm, CommentForm

ITEMS_PER_PAGE = 5



def split_date(string_date):
    """Transforma a data YYYY-MM-DD em uma tupla de três valores para utilizar na visão de eventos em determinado dia."""
    for value in string_date.split('-'):
        yield int(value)



# Create your views here.
def index(request):
    """Exibe a página principal da aplicação"""
    context= {
        'hider_new_button': True,
        'priorities': Event.priorities_list,
        'today': localdate(),
    }
    return render(request, 'index.html', context)




"""Exibe todos os eventos em uma única página,recebe o número da página a ser visualizada via GET."""
def all(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Event.objects.all(), ITEMS_PER_PAGE)
    total = paginator.count

    try:
        events = paginator.page(page)
    except InvalidPage:
        events = paginator.page(1)

    context = {
        'events': events,
        'total': total,
        'prioties':Event.priorities_list,
        'today':localdate(),
    }
    return render(request, 'events.html',context)



"""visualização dos eventos de um determinado dia, recebe a data em formato ano/mes/dia como parâmetro"""
def day(request, year:int, month:int, day:int):
    day = datetime(year,month,day)
    events = Event.objects.filter(date='{%Y-%m-%d}'.format(day)).oder_by('-priority','event')
    context = {
        'today':localdate(),
        'day':day,
        'events': events,
        'next': day + timedelta(days=1),
        'previous': day - timedelta(days=1),
        'priorities': Event.priorities_list
    }
    return render(request,'day.html', context)


def delete(request, id: int):
    """apaga um evento específico,se o evento não existir resultará um erro 404, se algo errado ocorrer retornará a página de erro."""
    event = get_object_or_404(Event, id=id)
    (year, month, day) = tuple(
        split_date('{:%Y-%m-%d}'.format(event.date)))
    if event.delete():
        return redirect('agenda-events-day', year=year , month=month, day=day)
    else:
        return server_error(request, 'ops_500.html')


def edit(request):
    """Edita o conteúdo de um evento, recebendo os dados enviados pelo formulário,
     validando e populando em um evento já existente."""
    form = EventForm(request.POST)
    if form.is_valid():
        event = get_object_or_404(Event, id=request.POST['id'])
        event.date = form.cleaned_data['date']
        event.event = form.cleaned_data['event']
        event.priority = form.cleaned_data['priority']
        event.save()
        (year, month, day) = tuple(
            split_date('{:%Y-%m-%d}'.format(event.date)))
        return redirect('agenda-events-day', year=year, month=month, day=day)
    else:
        return bad_request(request,None, 'ops_400.html')


def new(request):
    """Recebe os dados de um novo evento via POST, faz a validação dos dados
    e aí insere na base de dados."""
    form = EventForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        # Uso a data enviada pelo formulário para o redirecionamento.
        (year, month, day) = tuple(
            split_date(request.POST['date']))
        return redirect('agenda-events-day', year=year, month=month, day=day)
    else:
        return bad_request(request,None, 'ops_400.html')


def show(request, id:int):
    """Visualizaçao de um determinado evento e de seus comentários, recebe
    o 'id' do evnto. Caso seja acessado via POST insere um novo comentário."""
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('sgenda-events-show', id=id)
        context = {
            'event': event,
            'comments': Comment.objects.filter(event=id).order_by('-commented'),
            'hide_new_button': Event.priorities_list,
            'today': localdate(),
        }
        return render(request, 'show.html', context)