from jinja2 import Template
from mimesis import Person
from random import randint

p = Person('ru')

persons = [
    {"name": p.name(), "age": p.age(), "height": p.height()} for _ in range(2)
]

html = """

{%- macro render_persons(persons) -%}
<ul>
    {%- for person in persons %}
    <li>{{ caller(person) }}
    </li>
    {%- endfor %}
</ul>
{%- endmacro -%}


{% call(person) render_persons(persons) %}
        <h3> {{ person.name }} </h3> 
        <ul>
            <li> Age: {{ person.age }} </li>
            <li> Height: {{ person.height }} </li>
        </ul>
{%- endcall -%}

"""

template = Template(html)
result = template.render(persons=persons)
print(result)
