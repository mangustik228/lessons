from jinja2 import Template

link = '''
This is link <a href="#"> LINK </a>
'''


template = Template("{{ link | e }}")
msg = template.render(link=link)
print(msg)

template = Template(link)
print(template.render())
