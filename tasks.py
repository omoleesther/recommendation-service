import models
from database import SessionLocal
from taskiq_redis import RedisAsyncResultBackend, ListQueueBroker
from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource

# Here's the broker that is going to execute tasks
broker = ListQueueBroker("redis://localhost:6379/0").with_result_backend(
    RedisAsyncResultBackend("redis://localhost"))


# And here's the scheduler that is used to query scheduled sources
scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


@broker.task(
    schedule=[
        {"cron": "0 17 * * *"}
    ]
)
async def fetch_product():
    db = SessionLocal()
    product = db.query(models.Product).all()
    db.close()
    print(f"Fetched {len(product)} products")
