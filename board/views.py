from django.shortcuts import render


# Create your views here.
def new(request):
    pass


def create(request):
    pass


def all_list(request):
    pass


def detail(request, id):
    pass


def edit(request, id):
    pass


def update(request, id):
    pass


def delete(request, id):
    pass


def index(request):
    return render(request, 'board/index.html')


def greeting(request, name, role):  # Context 를 넘겨받음
    if name == 'admin':
        return render(request, 'board/greeting.html', {
            'name': 'Master_user',
            'role': 'Master',
        })

    return render(request, 'board/greeting.html', {
        'name': name.upper(),
        'role': role,
    })
