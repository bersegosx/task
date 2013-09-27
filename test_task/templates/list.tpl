{% extends 'base.tpl' %}

{% block title %}Список ссылок{% endblock %}

{% block content %}
  <h1>Список ссылок</h1>
  <ul>
  {% for link in links %}
    <li>
      {{ link.short_link }}
      <a href="{% url 'show' link.short_link %}">Просмотр</a>
      <a href="{% url 'delete' link.short_link %}">Удаление</a>
    </li>
  {% endfor %}
  </ul>

  <div class="pagination">
    <span class="step-links">
        {% if links.has_previous %}
            <a href="?page={{ links.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ links.number }} of {{ links.paginator.num_pages }}.
        </span>

        {% if links.has_next %}
            <a href="?page={{ links.next_page_number }}">next</a>
        {% endif %}
    </span>
  </div>
{% endblock %}