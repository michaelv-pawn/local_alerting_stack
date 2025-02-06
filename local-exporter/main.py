import os
import random
import time

from prometheus_client import Gauge, start_http_server

cpu_usage = Gauge("cpu_usage", "CPU Used", labelnames=["db_pod"])
mem_usage = Gauge("mem_usage", "Mem Used", labelnames=["db_pod"])


def set_values(**kwargs):
    for k, v in kwargs.values():
        k.set(v)


def set_init_values():
    print("Set Init Values")
    set_values(
        cpu=(cpu_usage.labels(db_pod="db1"), random.randint(1, 50)),
        mem=(mem_usage.labels(db_pod="db1"), random.randint(1, 50)),
    )


def set_allerting_values():
    print("Set Allerting Values")
    set_values(
        cpu=(cpu_usage.labels(db_pod="db1"), random.randint(80, 100)),
        mem=(mem_usage.labels(db_pod="db1"), random.randint(80, 100)),
    )


if __name__ == "__main__":
    start_http_server(8000)

    started = 0
    sleep_interval = int(os.environ.get("sleep_interval", 5))
    always_allert = os.environ.get("always_allert", False)

    print(sleep_interval)

    while True:
        if always_allert == "True":
            set_allerting_values()
            time.sleep(sleep_interval)
            continue
        if started % 6 == 0:
            set_init_values()
        else:
            set_allerting_values()
        time.sleep(sleep_interval)
        started += 1
