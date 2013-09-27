{% extends 'base.tpl' %}

{% block title %}Index{% endblock %}

{% block content %}
  <form action="." method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Convert">
  </form>

  <h1>Популярные ссылки:</h1>
  <ul>
    {% for link in links %}
      <li>
        <a href="{% url 'show' link.short_link %}">{{ link.short_link }}</a> -
        <a href="{% url 'test_task.views.go_to' link.short_link %}" target="_blank">
          {{ link.original_url|truncatechars:"40" }}
        </a>
        - [{{ link.redirect_count }}]
        - {{ link.created_at|date:"D d M Y H:i:s" }}
      </li>
    {% empty %}
      <li>
        <h2>Пусто</h2>
      </li>
    {% endfor %}
  </ul>
{% endblock %}