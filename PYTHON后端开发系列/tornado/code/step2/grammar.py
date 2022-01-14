from tornado.template import Template

# <1>.填充表达式，填充变量，填充变量的值到模板的双大括号中{{ 变量 }}
content = Template("<html><body><h1>{{ header }}</h1></body></html>")
content = content.generate(header="Welcome")
print(content.decode('utf-8'))
content = Template("{{ 1+1 }}").generate()
print(content.decode('utf-8'))
content = Template("{{ 'scrambled eggs'[-4:] }}").generate()
print(content.decode('utf-8'))
content = Template("{{ ','.join([str(x*x) for x in range(10)]) }}").generate()
print(content.decode('utf-8'))

# <2>.控制流语句，控制语句以{% 条件 %}包围，支持if、for、while和try
content = Template("<html><body><h1>{% if page %}{{ page }}{% end %}</h1></body></html>")
content = content.generate(page=10)
print(content.decode('utf-8'))
from tornado.escape import xhtml_escape
content = Template(xhtml_escape(
	"<html><body><h1>{% if len(entries) == 3 %}{{ entries }}{% end %}</h1>"
	) + "{{ ','.join([str(x*x) for x in range(10)]) }}</body></html>")
content = content.generate(entries=["Tom","Jac","Ros"])
print(content.decode('utf-8'))

html = """
	<html>
	    <head>
	        <title>{{ title }}</title>
	    </head>
	    <body>
	        <h1>{{ header }}</h1>
	        <ul>
	            {% for book in books %}
	                <li>{{ book }}</li>
	            {% end %}
	        </ul>
	    </body>
	</html>
"""
books=["Learning Python", "Programming Collective Intelligence", "Restful Web Services"]
content = Template(html)
content = content.generate(title="书籍列表", header="看书", books=books)
print(content.decode('utf-8'))


