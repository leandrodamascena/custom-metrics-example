from aws_lambda_powertools import Metrics, Logger, Tracer
import split_router_file


from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
import json


metrics = Metrics(namespace="powertools")
logger = Logger()
tracer = Tracer()
app = APIGatewayRestResolver()
app.include_router(split_router_file.router)


@metrics.log_metrics(capture_cold_start_metric=True)
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST, log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
