<p align="center">
  <h1 align="center">☸️ Istio Circuit Breaker (Airtel)</h1>
  <p align="center">
    <strong>Kubernetes + Istio demo of circuit breaking, retries, timeouts and mTLS against a Flask app that fails on demand.</strong>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Kubernetes-manifests-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes">
    <img src="https://img.shields.io/badge/Istio-service_mesh-466bb0?style=for-the-badge&logo=istio&logoColor=white" alt="Istio">
    <img src="https://img.shields.io/badge/Fortio-load_test-a1a1a1?style=for-the-badge" alt="Fortio">
    <img src="https://img.shields.io/github/last-commit/pratiks360/istio-circuit-breaker-airtel?style=for-the-badge&label=Last+Commit" alt="Last Commit">
  </p>
</p>

---

## ✨ What Is This?

A small Flask service exposes endpoints that return success, `500`, `503`, `504` or a delayed response on request. Paired Istio manifests apply resilience policies in front of it, and Fortio generates the load that makes them trip. Created for an IBM toolchain.

## 🔌 Test Endpoints

| Path | Behaviour |
|---|---|
| `/circuit` | Health — `App is UP!!` |
| `/circuit/good` | `200 OK` |
| `/circuit/internal` | `500` internal server error |
| `/circuit/gateway` | `504` gateway timeout |
| `/circuit/service` | `503` service unavailable |
| `/circuit/delay?time=N` | Responds `200` after `N` seconds |

## 🗂️ Manifests

| Path | Purpose |
|---|---|
| `k8s/` | Deployment, Service, ServiceAccount |
| `Istio/gateway.yaml` | Ingress gateway |
| `Istio/CB/` | Circuit-breaker `DestinationRule` + `VirtualService` |
| `Istio/retry/` | Retry policy |
| `Istio/timeout/` | Timeout policy |
| `Istio/mTLS.yaml` | Mutual TLS |
| `Istio/fortio-deploy.yaml` | Fortio load generator |

## 🧩 Architecture

```
┌────────┐   ┌─────────┐   ┌────────────────┐   ┌─────────┐   ┌───────────┐
│ Fortio │──►│ Gateway │──►│ VirtualService │──►│ Dest.   │──►│ Flask pods│
└────────┘   └─────────┘   │ retry/timeout  │   │ Rule CB │   └───────────┘
                           └────────────────┘   └─────────┘
```

## 🚀 Deploy

**Prerequisites:** a cluster with Istio and sidecar injection enabled.

```bash
docker build -t circuit-demo .        # push to a registry your cluster can pull from
kubectl apply -f k8s/
kubectl apply -f Istio/gateway.yaml -f Istio/CB/
kubectl apply -f Istio/fortio-deploy.yaml
```

Hit `/circuit/internal` repeatedly (or run Fortio) and watch the breaker eject the pod. Swap `Istio/CB/` for `retry/` or `timeout/` to compare policies.

## 🧹 Cleanup

```bash
kubectl delete -f Istio/ -R && kubectl delete -f k8s/
```

Related: [istio-circuit-breaker](https://github.com/pratiks360/istio-circuit-breaker).

---

<p align="center">
  <sub>Built with ❤️ for resilient microservices.</sub>
</p>
