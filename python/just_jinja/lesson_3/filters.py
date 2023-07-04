from jinja2 import Template
from random import randint
from mimesis import Generic, Person


faker = Person('ru')

products = [
    {"model": faker.name(), "price": randint(10_000, 50_000)} for _ in range(15)
]

digitals = [1, 2, 3, 4, 5, 6, 7]

source = """
{%- for product in products -%}
    {% filter upper -%}
        {{- product.model }}
    {%- endfilter %} - {{ product.price }}
{% endfor %}
# До этого был вариант использования фильтра на всех product.model
# Тут вариант использования фильтра sum
ИТОГО: {{ products | sum(attribute="price") }}
# Тут вариант использования фильтра max
МАКСИМАЛЬНАЯ ЦЕНА: {{ products | max(attribute="price") }}
some_sum {{ digitals | sum }}
"""

template = Template(source)

message = template.render(products=products, digitals=digitals)

print(message)
