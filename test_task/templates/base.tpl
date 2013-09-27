<DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>{% block title %}{% endblock %}</title>
  </head>
<body>
  <div class="menu">
    <a href="{% url 'index' %}">Главная</a> |
    <a href="{% url 'list' %}">Все ссылки</a>
  </div>
  <div class="content">
    {% block content %}{% endblock %}
  </div>
</body>
</html>