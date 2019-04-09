from django.shortcuts import render, redirect
from .models import Posting, Comment


def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings,
    })


def posting_detail(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    return render(request, 'board_ad/detail.html', {
        'posting': posting,
    })
