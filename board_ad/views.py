from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Posting, Comment

# Posting
# Create
@require_http_methods(['GET, POST'])
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
@require_http_methods(['GET'])
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings,
    })


@require_http_methods(['GET'])
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = Comment.objects.filter(posting_id__exact=posting_id)
    return render(request, 'board_ad/detail.html', {
        'posting': posting,
        'comments': comments,
    })


# Update
@require_http_methods(['GET, POST'])
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
@require_http_methods(['POST'])
def posting_delete(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')


# Comment
# Create
@require_http_methods(['POST'])
def comment_new(request, posting_id):
    comment = Comment()
    comment.posting_id = posting_id
    comment.content = request.POST.get('comment')
    comment.save()
    return redirect('board_ad:posting_detail', posting_id)


# Delete
def comment_delete(request, posting_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('board_ad:posting_detail', posting_id)
