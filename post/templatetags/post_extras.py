from django import template
import re

# register는 유효한 tag library를 만들기 위한 모듈 레벨의 인스턴스 객체이다.
register = template.Library()

@register.filter
def add_link(value):
    content = value.content # 전달된 value 객체의 content 멤버변수를 가져온다.
    tags = value.tag_set.all() # 전달된 value 객체의 tag_set 전체를 가져오는 queryset을 리턴한다.
    for tag in tags:  # tags의 각각의 인스턴를(tag)를 순회하며, content 내에서 해당 문자열을 => 링크를 포함한 문자열로 replace 한다.
        content = re.sub(r'\#'+tag.name+r'\b', '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content) # re.sub(pattern, repl, string)	string에서 pattern과 매치하는 텍스트를 repl로 치환한다
    return content  # 원하는 문자열로 치환이 완료된 content를 리턴한다.
