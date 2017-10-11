![python](https://mtzfactory.github.io/logos/png/python.png)
![flask](https://mtzfactory.github.io/logos/png/flask.png)

## Proxy token 

Webservice realizado en Python y Flask para que actue como proxy, recuperando un token, entre un servicio de autenticación de un tercero y nuestra _web-app_.

Por que usar este webservice? En algun caso, p.e con _JQuery_, podemos diseñar una pequeña _web-app_ que requiera datos de un tercero mediante una API, y esta a su vez requiera de un proceso de autenticación previo a la consulta a dicha API.

En este ejemplo utilizamos la API de Spotify, [para ello necesitamos el _Client Id_ y _Client Secret_][developer] que nos devuelve al registrar nuestra _web-app_, si hacemos una consulta a nuestro webservice, este nos devolverá algo similar a lo siguiente, con el token devuelto por Spotify:

```json
{
client: "x7.2x3.9x.71",
token: "BQC5wFTNXURxLYSbKSxtNOuIbJelKrVqTqO1os-OY5FhaF00Bfvn9DSAmcwQXv8fpKUBn1mPRItXjSa43VXrZA"
}
```

[developer]: https://developer.spotify.com/my-applications/#!/applications