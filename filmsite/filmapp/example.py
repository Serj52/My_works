from .models import Film, Producer


name = Film.objects.get(id = 1)
print(type(name))

