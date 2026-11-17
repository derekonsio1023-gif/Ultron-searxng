
FROM docker.io/caddy:2-alpine AS caddy_builder

FROM docker.io/searxng/searxng:latest

USER root

COPY --from=caddy_builder /usr/bin/caddy /usr/bin/caddy

COPY searx/settings.yml /etc/searxng/settings.yml
COPY searx/templates /usr/local/searxng/searx/templates
COPY searx/static /usr/local/searxng/searx/static

# Instalar una versión fija de Granian
RUN pip install --no-cache-dir granian==2.8.8

# Configurar Caddy
RUN mkdir -p /etc/caddy && printf ':{$PORT:10000} {\n    header {\n        Access-Control-Allow-Origin *\n        Access-Control-Allow-Methods "GET, POST, OPTIONS"\n        Access-Control-Allow-Headers *\n    }\n    @options {\n        method OPTIONS\n    }\n    respond @options 204\n    reverse_proxy 127.0.0.1:8080\n}\n' > /etc/caddy/Caddyfile

EXPOSE 10000

ENTRYPOINT ["/bin/sh", "-c", "(/usr/local/searxng/entrypoint.sh) & exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile"]
