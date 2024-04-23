### show logs

```
kubectl logs -n argo $(kubectl get pods -l app=workflow-controller -n argo -o name) -f
```
