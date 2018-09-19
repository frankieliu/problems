import requests


#from prometheus_client.parser import text_string_to_metric_families


url = "http://localhost:9090/metrics"
metrics = requests.get(url).content
print(metrics)

#for family in text_string_to_metric_families(str(metrics)):
#    for sample in family.samples:
#        print("Name: {0} Labels: {1} Value: {2}".format(*sample))
