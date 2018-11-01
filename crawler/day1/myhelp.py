import requests


def info(obj):
    methodList = [method for method in dir(obj)
                  if callable(getattr(obj, method))]

    print(methodList)

info(requests)