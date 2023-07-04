from mimesis import Address, Person, Internet
from jinja2 import Template


cities = [
    {"id": i, "city": Address('ru').city()} for i in range(1, 8)
]

text = """
{%- for c in cities -%}
{{ c.id }}. {{ c.city }}
{%- if c.id < cities.__len__() -%}
{{ "\n" }}
{%- endif -%} 
{% endfor -%}
"""

template = Template(text)
result = template.render(cities=cities)

print(result)
