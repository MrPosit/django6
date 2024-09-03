from django.shortcuts import render
from .models import Team, Player, Item

def home(request):
    teams = Team.objects.all()
    context = {
        'team': teams
    }
    return render(request, 'home.html', context)

titles = ['Заголовок 1', 'Заголовок 2', 'Заголовок 3', 'Заголовок 4']

i = Item(titles='Заголовок 1')
i.save()

for title in titles[1:]:
    i2 = Item(titles=title)
    i2.save()

items = Item.objects.all()
for item in items:
    try:
        item.titles = f"{item.titles}.id={item.id}"
        item.save(update_fields=['titles'])
    except Item.DoesNotExist:
        print(f"Item with id={item.id} does not exist.")

for item in items:
    if item.id % 2 != 0:
        try:
            item.delete()
        except Item.DoesNotExist:
            print(f"Item with id={item.id} does not exist.")