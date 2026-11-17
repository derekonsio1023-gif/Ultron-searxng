FROM docker.io/caddy:2-alpine AS caddy_builder

FROM docker.io/searxng/searxng:latest

USER root
COPY --from=caddy_builder /usr/bin/caddy /usr/bin/caddy

# Copia tu configuración y tus plantillas/estáticos modificados del fork
COPY searx/settings.yml /etc/searxng/settings.yml
COPY searx/templates /usr/local/searxng/searx/templates
COPY searx/static /usr/local/searxng/searx/static

# Genera el Caddyfile directamente dentro del contenedor
RUN mkdir -p /etc/caddy && printf ':{$PORT:10000} {\n    header {\n        Access-Control-Allow-Origin *\n        Access-Control-Allow-Methods "GET, POST, OPTIONS"\n        Access-Control-Allow-Headers *\n    }\n    @options {\n        method OPTIONS\n    }\n    respond @options 204\n    reverse_proxy localhost:8080\n}\n' > /etc/caddy/Caddyfile

EXPOSE 10000

ENTRYPOINT ["/bin/sh", "-c", "(/usr/local/searxng/entrypoint.sh || granian --interface wsgi --host 0.0.0.0 --port 8080 searx.webapp:app) & exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile"]
