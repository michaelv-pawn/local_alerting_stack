```
git clone https://github.com/michaelv-pawn/local_alerting_stack.git
docker-compose down -v && docker compose up --build
exporter url: http://localhost:8000/metrics
prometheus url: http://localhost:9090
alertmanager url: http://localhost:9093
```