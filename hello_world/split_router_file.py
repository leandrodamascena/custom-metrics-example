from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools import Metrics, Tracer

router = Router()
tracer = Tracer()
metrics = Metrics(namespace="powertools")

@router.get("/hello")
@tracer.capture_method
def get_hello():
    metrics.add_metric(name="Hello", unit=MetricUnit.Count, value=1)
    return {"msg": "hello"}

@router.get("/world")
@tracer.capture_method
def get_hello():
    metrics.add_metric(name="World", unit=MetricUnit.Count, value=1)
    return {"msg": "world"}
