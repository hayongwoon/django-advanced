from django.db.models import QuerySet

from tabom.models import Article


def get_an_article(article_id: int) -> Article:
    article = Article.objects.filter(id=article_id).get()
    return article


def get_article_list(offset: int, limit: int) -> QuerySet[Article]:
    return Article.objects.order_by("-id")[offset : offset + limit]
    # id 내림차순 : 21 20 19...0 -> 슬라이싱[0:10]
    # -> 0번째 21, 1번째 20 2번째 19...
