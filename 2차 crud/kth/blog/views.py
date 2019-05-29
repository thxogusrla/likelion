from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def main(request): # request만 들어오면 실행되는 함수. request외엔 더이상의 정보는 필요x
    articles = Article.objects.all()
    return render(request, "blog/main.html", {"articles": articles})

def new(request):
    if request.method == "POST": # request의 방식이 post인지 / 입력된 내용을 처리해줌.
        form = ArticleForm(request.POST)  # 입력받은 것들이 post로 인해 저장된다.
        #POST 방식으로로 들어온 데이터를 form 이라는 변수에 저장해줌.
        if form.is_valid():  # 유효한지 검사함.
            article = form.save(commit=False)  # commit=false 저장을 늦게 진행하겠다.
            article.title = form.cleaned_data["title"] #
            article.content = form.cleaned_data["content"]
            article.published_at = timezone.now() # ArticleForm에 published_at 입력해 주지 않기 때문
            article.save()
            return redirect("blog:main")

    else: # 빈페이지를 띄어주는 기능
        form = ArticleForm() # 빈 객체 form
        return render(request, "blog/new.html", {'form': form})
        # new.html에 form을 보내라.
        
def detail(request, article_id): # 몇번 객체의 블로그를 가져오고 싶은지 article_id 로 알 수 있음.
    article = get_object_or_404(Article, pk=article_id) # 특정 번호의 객체를 담을 수 있는 방법.
                                                        # Article 클래스에서 몇번(pk)를 가져올건지.
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid(): # 입력 사항에 오류가 있는지 체크. 오류가 없으면 실행.
            comment = form.save(commit=False)

            comment.article = article 
            comment.content = form.cleaned_data["content"]
            comment.save()
            return redirect("blog:detail", article_id)

    else: # 빈페이지를 출력 해주는 역할.
        form = CommentForm()
        return render(request, "blog/detail.html", {"article": article, "form": form}) 
        # 위에 article = get_....(Article, pk=article_id)가 있기 때문에 해당 
        # 번호의 객체를 출력해준다.

def edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id) 
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article) 
        # 수정대상을 instance=article로 article이 수정대상이라는 것을 알려준다.
        if form.is_valid():
            article = form.save(commit=False)  # commit=false 저장을 늦게 진행하겠다.
            article.title = form.cleaned_data["title"] #cleaned_data로 title을 사전형 변수로 나타낸다.
            article.content = form.cleaned_data["content"] 
            # 수정을 해줘야 하기 때문에 title과 content를
            article.published_at = timezone.now()
            article.save()
            return redirect("blog:detail", article_id)
    else: # 
        form = ArticleForm()
        return render(request, "blog/new.html", {'form': form})

def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("blog:main")


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id) #comment_id 번째 객체 수정.
    comment.delete()
    return redirect("blog:detail", comment.article_id)


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id) # 
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content = form.cleaned_data["content"]
            comment.save()
            return redirect("blog:detail", comment.article.id)
    else:
        form = CommentForm(instance=comment)
        return render(request, "blog/new.html", {"form": form})
