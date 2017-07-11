from django.conf import settings
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    # owner필드를 추가, member app을 추가하고 CustomUser를 생성하고
    # 해당 User를 settings.AUTH_USER_MODEL을 참조하는 방식을 사용
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    highlighted = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=100, default='python')
    style = models.CharField(choices=STYLE_CHOICES, max_length=100, default='friendly')

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        # linenos = self.linenos and 'table' or False
        linenos = 'table' if self.linenos else False
        # options = self.title and {'title': self.title} or {}
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style,
            linenos=linenos,
            full=True,
            **options,
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
