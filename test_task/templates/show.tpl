{% extends 'base.tpl' %}

{% block title %}Information{% endblock %}

{% block content %}
  <h1>{{ link.short_link }} -> {{ link.original_url }}</h1>
  <p>Дата создания: {{ link.created_at|date:"D d M Y H:i:s" }}</p>
  <p>Количество переходов: {{ link.redirect_count }}</p>
{% endblock %}