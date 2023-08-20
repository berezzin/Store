up:
	kubectl create secret generic app-secrets --from-env-file=.env
	kubectl apply -f .\kubernetes\app-k8s.yaml
	kubectl apply -f .\kubernetes\postgres-k8s.yaml
	kubectl apply -f .\kubernetes\ingress-k8s.yaml
down:
	kubectl delete -f .\kubernetes\app-k8s.yaml
	kubectl delete -f .\kubernetes\postgres-k8s.yaml
	kubectl delete -f .\kubernetes\ingress-k8s.yaml
	kubectl delete secret app-secrets
