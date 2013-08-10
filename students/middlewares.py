from django.db import connection
from django.template import Template, Context
from django.utils.encoding import smart_unicode

class CoolMiddleware(object):
    def process_response ( self, request, response ):
        time = 0.0
        for q in connection.queries:
            time += float(q['time'])

        t = Template('''
            <p><em>Total query count:</em> {{ count }}<br/>
            <em>Total execution time:</em> {{ time }}</p>
        ''')

        response.content = smart_unicode("%s%s") % (smart_unicode(response.content), t.render(Context({'count':len(connection.queries),'time':time})))
        return response