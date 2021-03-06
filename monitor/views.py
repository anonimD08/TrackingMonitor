from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from .models import \
    Track, TrackCourse

from pyspark import SparkContext, SparkConf
import logging

logger = logging.getLogger('cel_logging')

def upload_from_json(request):
    conf = SparkConf().setAppName('MyFirstStandaloneApp')
    sc = SparkContext(conf=conf)
    #track = json.loads(request.POST.get("json_value", None))
    logRDD = sc.textFile("/home/alex/big_data_edx/tracking.log")
    test = logRDD.first()
    print("!!!!!!!!!!!!!!!! :",test)
    logger.info(test)
    context = {
        'first_obj': test,
    }
    return render(request, 'upload_from_json.html', context)