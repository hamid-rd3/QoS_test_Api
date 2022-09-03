from unittest import result
from rest_framework import serializers
from .models import QoS
import asyncio




class QoSSerializer(serializers.ModelSerializer):

    qos_parameters = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = QoS
        fields = [
            "id",
            "site_url",
            "ping_count",
            "ping_timeout",
            "ping_algorithm",
            "ddosify_count",
            "ddosify_duration",
            "ddosify_timeout",
            "async_view",
            "qos_parameters",
        ]
        # example = {
        #     'site_url': 'https://www.varzesh3.com/',
        #     'ping_count': 5,
        #     'ping_timeout': 0.2,
        #     'ping_algorithm': 'binary_search',
        #     'ddosify_count': 100,
        #     'ddosify_duration': 5,
        #     'ddosify_timeout': 1,
        #     'async_view': True
        # }

    log_keys = ["ping_resault", "selenium_resault",
                "curl_resault", "ddosify_resault"]

    def get_qos_parameters(self, obj):

        if not hasattr(obj, 'site_url'):
            return None
        if not isinstance(obj, QoS):
            return None

        if obj.async_view:

            event_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(event_loop)
            return (event_loop.run_until_complete(self.main_async(obj)))

        else:

            log_values = [obj.get_ping(), obj.get_selenium(),
                          obj.get_curl(), obj.get_ddosify()]
            log_dict = {k: v for k, v in zip(self.log_keys, log_values)}
            return log_dict

    async def main_async(self, obj):

        loop = asyncio.get_event_loop()

        log_async_values = await asyncio.gather(
            loop.run_in_executor(None, obj.get_ping),
            loop.run_in_executor(None, obj.get_selenium),
            loop.run_in_executor(None, obj.get_curl),
            loop.run_in_executor(None, obj.get_ddosify))
        results = {k: v for k, v in zip(self.log_keys, log_async_values)}

        return results
