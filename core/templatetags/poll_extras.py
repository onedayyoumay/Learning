# -*- coding: utf-8 -*-

from django import template
import re
register = template.Library()

@register.filter
def youtube(value):
    """
    Converts http:// links to youtube into youtube-embed statements, so that
    one can provide a simple link to a youtube video and this filter will
    embed it.

    Based on the Django urlize filter.
    """
    text = value
    # Configuration for urlize() function
    LEADING_PUNCTUATION  = ['(', '<', '&lt;']
    TRAILING_PUNCTUATION = ['.', ',', ')', '>', '\n', '&gt;']
    word_split_re = re.compile(r'(\s+)')
    punctuation_re = re.compile('^(?P<lead>(?:%s)*)(?P<middle>.*?)(?P<trail>(?:%s)*)$' % \
            ('|'.join([re.escape(x) for x in LEADING_PUNCTUATION]),
            '|'.join([re.escape(x) for x in TRAILING_PUNCTUATION])))
    youtube_re = re.compile ('http://www.youtube.com/watch.v=(?P<videoid>(.+))')


    words = word_split_re.split(text)
    for i, word in enumerate(words):
        match = punctuation_re.match(word)
        if match:
            lead, middle, trail = match.groups()
            if middle.startswith('http://www.youtube.com/watch') or middle.startswith('http://youtube.com/watch'):
                video_match = youtube_re.match(middle)
                if video_match:
                    video_id = video_match.groups()[1]
                    middle = '''<br/><object width="425" height="350">
                    <param name="movie" value="http://www.youtube.com/v/%s"/>
                    <param name="wmode" value="transparent"/>
                    <embed src="http://www.youtube.com/v/%s" type="application/x-shockwave-flash" wmode="transparent" width="425" height="350"/>
                    </object><br/>''' % (video_id, video_id)

            if lead + middle + trail != word:
                words[i] = lead + middle + trail
    return ''.join(words)

@register.filter
def bbcode(value):

    bbdata = [
        (r'\[url\](.+?)\[/url\]', r'<a href="\1">\1</a>'),
        (r'\[url=(.+?)\](.+?)\[/url\]', r'<a href="\1">\2</a>'),
        (r'\[email\](.+?)\[/email\]', r'<a href="mailto:\1">\1</a>'),
        (r'\[email=(.+?)\](.+?)\[/email\]', r'<a href="mailto:\1">\2</a>'),
        (r'\[img\](.+?)\[/img\]', r'<img src="\1">'),
        (r'\[img=(.+?)\](.+?)\[/img\]', r'<img src="\1" alt="\2">'),
        (r'\[b\](.+?)\[/b\]', r'<b>\1</b>'),
        (r'\[i\](.+?)\[/i\]', r'<i>\1</i>'),
        (r'\[u\](.+?)\[/u\]', r'<u>\1</u>'),
        (r'\[quote\](.+?)\[/quote\]', r'<div style="margin-left: 1cm">\1</div>'),
        (r'\[center\](.+?)\[/center\]', r'<div align="center">\1</div>'),
        (r'\[code\](.+?)\[/code\]', r'<tt>\1</tt>'),
        (r'\[big\](.+?)\[/big\]', r'<big>\1</big>'),
        (r'\[small\](.+?)\[/small\]', r'<small>\1</small>'),
        (r'\[p\](.+?)\[/p\]', r'<p>\1</p>'),
        (r'\[br\]', r'<br/>')
        ]

    for bbset in bbdata:
        p = re.compile(bbset[0], re.DOTALL)
        value = p.sub(bbset[1], value)

    #The following two code parts handle the more complex list statements
    temp = ''
    p = re.compile(r'\[list\](.+?)\[/list\]', re.DOTALL)
    m = p.search(value)
    if m:
        items = re.split(re.escape('[*]'), m.group(1))
        for i in items[1:]:
            temp = temp + '<li>' + i + '</li>'
        value = p.sub(r'<ul>'+temp+'</ul>', value)

    temp = ''
    p = re.compile(r'\[list=(.)\](.+?)\[/list\]', re.DOTALL)
    m = p.search(value)
    if m:
        items = re.split(re.escape('[*]'), m.group(2))
        for i in items[1:]:
            temp = temp + '<li>' + i + '</li>'
        value = p.sub(r'<ol type=\1>'+temp+'</ol>', value)

    return value