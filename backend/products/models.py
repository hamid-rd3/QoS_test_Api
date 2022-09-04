
from django.db import models

# selenium libraries
import os
import json
import stat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ping libraries
from urllib.parse import urlsplit
import subprocess
import time


class QoS(models.Model):

    site_url = models.CharField(max_length=120)

    ping_count = models.IntegerField(default=5)
    ping_timeout = models.DecimalField(
        max_digits=3, decimal_places=2, default=0.2)
    ping_algorithm = models.CharField(default='binary_search', max_length=13)

    ddosify_count = models.IntegerField(default=100)
    ddosify_duration = models.IntegerField(default=5)
    ddosify_timeout = models.IntegerField(default=1)

    async_view = models.BooleanField(default=True)

    def get_selenium(self):
        print("get_selenium is started :")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")

        path_parent = os. path. dirname(os. getcwd())  # backend
        path = os.path.join(os.getcwd(), 'chromedriver/stable/chromedriver')
        os.chmod(path, stat.S_IXUSR)
        web_driver_service = Service(executable_path=path)

        driver = webdriver.Chrome(
            service=web_driver_service, options=chrome_options)

        url = self.site_url
        driver.get(url)

        ''' Use Navigation Timing  API to calculate the timings  '''

        navigation_parameters = driver.execute_script(
            "return window.performance.getEntriesByType('navigation')")
        navigation_output = {key: float("%.2f" % (float(value))) if type(
            value) == float else value for key, value in navigation_parameters[0].items()}
        driver.quit()
        print("get_selenium is ended :")

        return navigation_output

    def get_curl(self):
        print("get_curl is started")
        url = self.site_url
        command = " --write-out \
            'connect %{time_connect}\nappconnect %{time_appconnect}\npretransfer %{time_pretransfer}\nredirect %{time_redirect}\nstart_transfer %{time_starttransfer}\ntotal %{time_total}'\
                --silent --show-error "
        lines = os.popen(f"curl {url}"+command).readlines()
        logdict = {
            'connect': round(float(lines[-6].split(' ')[1]), 2),
            'appconnect': round(float(lines[-5].split(' ')[1]), 2),
            'pretransfer': round(float(lines[-4].split(' ')[1]), 2),
            'redirect': round(float(lines[-3].split(' ')[1]), 2),
            'start_transfer': round(float(lines[-2].split(' ')[1]), 2),
            'total': round(float(lines[-1].split(' ')[1]), 2)
        }
        print("get_curl is ended")

        return logdict

    def get_ddosify(self):
        print("get_ddosify is started")

        url = self.site_url
        count = self.ddosify_count
        duration = self.ddosify_duration
        timeout = self.ddosify_timeout
        responce = os.popen(
            f" ddosify -t {url} -n {count} -d {duration} -p HTTPS -m GET -T {timeout} -o stdout-json")
        lines = responce.read()
        print("get_ddosify is ended")

        return json.loads(lines)

    def get_ping(self):
        print("get_ping is started")

        url = self.site_url
        count = self.ping_count
        timeout = self.ping_timeout
        algorithm = self.ping_algorithm
        test_hop = 1
        hostname = urlsplit(url).hostname
        start = time.time()
        if algorithm == 'linear_search':
            hop_limit = hop_count_linear(hostname, test_hop, timeout)
        else:
            hop_limit = hop_count_binary(hostname, timeout)
        lines = os.popen(
            f"ping  {hostname} -c {count} -t {hop_limit} -W {timeout} ").readlines()
        count = lines[-2].split(' ')[0]
        packet_loss = lines[-2].split(' ')[5]
        min_rtt = lines[-1].split(' ')[3].split('/')[0]
        mdev = lines[-1].split(' ')[3].split('/')[3]
        end = time.time()
        log_dict = {'packets-transmitted': count,
                    'packet_loss': packet_loss, "rtt": f"%.2f" % float(float(min_rtt)), "jitter": float(f"%.2f" % float(mdev)), 'hop_count': hop_limit, 'calculation_time': f"{'%.2f'%(end-start)} seconds"}

        print("get_ping is ended")

        return log_dict


# initial functions


def hop_count_linear(hostname, test_hop, timeout):
    """ With a TTL value of less than hop count, ping gives a “Time to live exceeded” message as well as a 100% packet loss in the statistics(responce.returncode is 1). This means that the hop count needs to be increased linearly towards the destination """

    while True:
        # the first goal is to find hop counts so count =1 to ping faster
        responce = subprocess.run(['ping', hostname, '-c 1', f'-t {test_hop}', f'-W {timeout}'], stdout=subprocess.DEVNULL,
                                  stderr=subprocess.STDOUT)
        if responce.returncode == 1:
            test_hop += 1
            continue
        break
    return test_hop


def hop_count_binary(hostname, timeout):
    """ If ttl is less than hop count , responce.returncode gives 1 and it must minus step and on the other hand If ttl is more than hop count responce.returncode gives 0 and i must plus step to get nearer to the answer 
    """
    max_root = 32
    step = int(max_root/4)
    hop_limit = int(max_root/2)
    for i in range(1, 5):
        responce = subprocess.run(
            ['ping', hostname, '-c 1', f'-t {hop_limit}', f'-W {timeout}'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if responce.returncode:
            if i == 4:
                hop_limit += 1
            hop_limit += step
        else:
            hop_limit -= step
        step = int(step/2)
    return hop_limit
# Create your models here.
