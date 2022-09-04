from drf_yasg import openapi
from .models import QoS
from .serializer import QoSSerializer
from api.serializers import RegisterSerializer

request_schema_dict = openapi.Schema(
    title=("QoS test arguments "),
    type=openapi.TYPE_OBJECT,
    properties={
        'site_url': openapi.Schema(type=openapi.TYPE_STRING, description='web site url address', example='https://www.example.com/'),
        'ping_count': openapi.Schema(type=openapi.TYPE_INTEGER, description='number of packets to transmit', example=5),
        'ping_timeout': openapi.Schema(type=openapi.TYPE_NUMBER, description='Timeout in seconds to wait for each reply', example='0.5'),
        'ping_algorithm': openapi.Schema(type=openapi.TYPE_STRING, description='{linear_search} or {binary_search} represents how to find hop counts ', example='binary_search'),
        'dosify_count': openapi.Schema(type=openapi.TYPE_INTEGER, description='total requset count ', example=100),
        'dosify_duration': openapi.Schema(type=openapi.TYPE_INTEGER, description='Test duration in seconds. ', example=5),
        'dosify_timeout': openapi.Schema(type=openapi.TYPE_INTEGER, description='Timeout per request in seconds. ', example=1),
        'async_view': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='async and threading to improve performance ', example=True),
    }
)

register_responce = openapi.Response(
    description='Registeriation result',
    schema=RegisterSerializer,
    examples={"application/json": {
        "username": "sher221Block",
        "email": "ceef@dsg.com",
        "first_name": "sherlock",
        "last_name": "holmes"
    }}
)

responce_schema_dict = openapi.Response(
    description='QoS test result',
    schema=QoSSerializer,
    examples={"application/json": {
        "id": 23,
        "site_url": "https://www.example.com/",
        "ping_count": 5,
        "ping_timeout": "0.5",
        "ping_algorithm": "binary_search",
        "ddosify_count": 100,
        "ddosify_duration": 5,
        "ddosify_timeout": 1,
        "async_view": True,
        "qos_parameters": {
                "ping_resault": {
                    "packets-transmitted": "5",
                    "packet_loss": "0%",
                    "rtt": "0.67",
                    "jitter": 0.05,
                    "hop_count": 8,
                    "calculation_time": "4.33 seconds"
                },
            "selenium_resault": {
                    "connectEnd": 27.7,
                    "connectStart": 15.2,
                    "decodedBodySize": 482213,
                    "domComplete": 1661.7,
                    "domContentLoadedEventEnd": 571.8,
                    "domContentLoadedEventStart": 571.4,
                    "domInteractive": 571.4,
                    "domainLookupEnd": 15.2,
                    "domainLookupStart": 13.9,
                    "duration": 1663.6,
                    "encodedBodySize": 65603,
                    "entryType": "navigation",
                    "fetchStart": 1.1,
                    "initiatorType": "navigation",
                    "loadEventEnd": 1663.6,
                    "loadEventStart": 1661.8,
                    "name": "https://www.varzesh3.com/",
                    "nextHopProtocol": "h2",
                    "redirectCount": 0,
                    "redirectEnd": 0,
                    "redirectStart": 0,
                    "requestStart": 28,
                    "responseEnd": 43.3,
                    "responseStart": 35.5,
                    "secureConnectionStart": 15.7,
                    "serverTiming": [],
                    "startTime": 0,
                    "transferSize": 65903,
                    "type": "navigate",
                    "unloadEventEnd": 0,
                    "unloadEventStart": 0,
                    "workerStart": 0
                    },
            "curl_resault": {
                    "connect": 0.09,
                    "appconnect": 0.19,
                    "pretransfer": 0.19,
                    "redirect": 0,
                    "start_transfer": 0.19,
                    "total": 0.2
                    },
            "ddosify_resault": {
                    "success_perc": 100,
                    "fail_perc": 0,
                    "success_count": 100,
                    "fail_count": 0,
                    "avg_duration": 0.009,
                    "steps": {
                        "1": {
                            "name": "",
                            "status_code_dist": {
                                "200": 100
                            },
                            "error_dist": {},
                            "durations": {
                                "connection": 0,
                                "dns": 0.002,
                                "request_write": 0,
                                "response_read": 0,
                                "server_processing": 0.007,
                                "tls": 0,
                                "total": 0.009
                            },
                            "success_count": 100,
                            "fail_count": 0,
                            "success_perc": 100,
                            "fail_perc": 0
                        }
                    }
                    }
        }
    }}
)
