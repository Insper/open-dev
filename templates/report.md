# Relatório de acompanhamento - {{st.name}}

Esta página lista todas as skills obtidas por {{ st.name }} e os critérios de barreira que já foram alcançados. 

#### Pontuação total: {{ xp_total }}

## Tutorial

As seguintes atividades de sala de aula foram completadas e enviadas no repositório:

<div class="skill-list-done" markdown="1">
{% for sk in sk_tutorial %} {% if sk.done %}- [X] {{ sk.name}} {% else %}- [ ] {{ sk.name}}{%  endif %}
{% endfor %}
</div>

## Código

<div class="skill-list-done" markdown="1">
{% for sk in sk_code %}
{% if sk.done %}- [X] {{ sk.name}} {% else %}- [ ] {{ sk.name}}{% endif %}
{% endfor %}
</div>


## Tradução e Documentação 

<div class="skill-list-done" markdown="1">
{% for sk in sk_docs %}
{% if sk.done %}- [X] {{ sk.name}} {% else %}- [ ] {{ sk.name}}{% endif %}
{% endfor %}
</div>


## Comunidade


<div class="skill-list-done" markdown="1">
{% for sk in sk_comm %}
{% if sk.done %}- [X] {{ sk.name}} {% else %}- [ ] {{ sk.name}}{% endif %}
{% endfor %}
</div>


