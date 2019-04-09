from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment


# Create
def posting_new(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting.id)
    else:
        return render(request, 'board_ad/posting_new.html')


# Read
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings,
    })


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'board_ad/detail.html', {
        'posting': posting,
    })


# Update
def posting_edit(request, posting_id):
    if request.method == 'POST':
        posting = Posting.objects.get(id=posting_id)
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting.id)
    else:
        posting = Posting.objects.get(id=posting_id)
        return render(request, 'board_ad/posting_edit.html', {
            'posting': posting,
        })


# Delete
def posting_delete(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')
