### show logs

```
kubectl logs -n argo $(kubectl get pods -l app=workflow-controller -n argo -o name) -f
```

### build and submit
```
# workflow
docker build . -t khanhph/storagescript
#docker push khanhph/storagescript

argo submit -n argo hellostorage.yaml


# cron workflow
argo cron create cron.yaml

```