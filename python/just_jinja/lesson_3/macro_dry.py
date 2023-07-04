from jinja2 import Template
from mimesis import Person

person = Person('ru')


html = """
{% macro input(name, value="", type="text", size=20) -%}
    <input type="{{ type }}" name="{{ name }} value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p> {{ input("username") }} </p>
<p> {{ input("email") }} </p>
<p> {{ input("password") }} </p>

"""

template = Template(html)
message = template.render()

print(message)
