#!/bin/bash

docker build . -t khanhph/storagescript
docker push khanhph/storagescript

argo submit -n argo --watch hellostorage.yaml