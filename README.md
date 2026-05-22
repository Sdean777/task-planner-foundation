# Dean'z Elite OS Task Planner Foundation

This repository is the first foundation service pattern for Dean'z Elite OS.
It is intentionally small: a Flask service with health, validation, telemetry,
memory, task, and orchestration endpoints that proves the operational basics
before intelligence is added.

The service is currently shaped by OpenShift learnings and is now being
prepared for AWS-native container deployment without losing portability.

## Project Purpose

This repo exists to preserve the base service discipline required for a larger
OS runtime:

- source-controlled service ownership
- container build lifecycle
- deployment manifest discipline
- health and status inspection
- validator-first runtime checks
- telemetry visibility
- orchestration surface readiness

This is foundation infrastructure, not final Dean'z Elite OS intelligence.

## Verified Endpoints

The current Flask service preserves these endpoints:

| Endpoint | Purpose |
| --- | --- |
| `/` | foundation service banner |
| `/health` | minimal health status |
| `/status` | runtime service status |
| `/tasks` | task structure placeholder |
| `/memory` | foundation system memory |
| `/agent` | foundation agent descriptor |
| `/telemetry` | service runtime telemetry |
| `/validate` | validator-first health checks |
| `/orchestrate` | ordered orchestration plan |

Verified locally on `2026-05-22`:

- `/health`
- `/status`
- `/validate`
- `/orchestrate`

## Current Foundation Behavior

- The app is a Flask service in [app.py](./app.py).
- The only runtime dependency is `Flask==3.1.3` in [requirements.txt](./requirements.txt).
- The existing container path is preserved through [docker/Dockerfile](./docker/Dockerfile).
- The existing OpenShift/devfile pattern is preserved through [deploy.yaml](./deploy.yaml) and [devfile.yaml](./devfile.yaml).

## OpenShift Learning Summary

The current repo already captures several useful OpenShift lessons:

- keep the service simple and observable before widening behavior
- keep the container contract explicit with one app entrypoint
- keep platform metadata separate from the app runtime
- expose a validator endpoint early so runtime health can be checked without guessing
- expose telemetry and orchestration endpoints early so later runtime layers have stable surfaces

Those learnings are being carried forward into the AWS foundation path instead
of being discarded.

## Docker and Portability Notes

The current container path remains intentionally compatible with the existing
OpenShift pattern:

- base image: `registry.access.redhat.com/ubi9/python-39:1-1776086485`
- container port: `8081`
- container env: `FLASK_PORT=8081`
- startup command: `python ./app.py`

Local app behavior defaults to port `8080` if `FLASK_PORT` is not set.
Containerized behavior stays on `8081`, which matches the current
`Dockerfile`, `deploy.yaml`, and `devfile.yaml`.

This keeps the repo portable:

- OpenShift/devfile flow stays intact
- Docker build remains valid
- AWS runtimes can map the container on the same port without changing endpoints

## Local Run

Create a local virtual environment and run the service:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The local server listens on `http://127.0.0.1:8080` by default.

If you want local behavior to match the container port:

```bash
FLASK_PORT=8081 python app.py
```

Test the key endpoints:

```bash
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/validate
curl http://127.0.0.1:8080/orchestrate
```

## AWS Target Architecture

The first recommended AWS path for this service is:

```text
GitHub
  -> CI validation
  -> container build
  -> ECR image
  -> ECS/Fargate service
  -> Application Load Balancer or API Gateway
  -> public API route
  -> CloudWatch logs/telemetry
  -> validator and orchestration consumers
```

Recommended first runtime choices:

- container registry: Amazon ECR
- compute: Amazon ECS with Fargate
- logs and telemetry: Amazon CloudWatch
- routing: Application Load Balancer first, API Gateway if API management becomes necessary
- build and deploy automation: GitHub Actions first, AWS CodeBuild/CodePipeline as an optional later path

EKS can remain a later option if the runtime grows beyond the simplicity that
ECS/Fargate is meant to preserve.

The precise non-deploying runtime contract is documented in
[DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md),
with the paired task skeleton in
[aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json).

## Migration Notes

What changes now:

- documentation is being rewritten around Dean'z Elite OS foundation service intent
- AWS mapping is being made explicit
- GitHub-to-container-to-ECR-to-ECS workflow structure is being documented
- container build hygiene is being improved without breaking OpenShift compatibility

What does not change now:

- Flask endpoints stay the same
- no OpenAI integration is added
- no autonomous agent behavior is added
- no AWS credentials are introduced
- no live deployment automation is introduced

## GitHub Actions Placeholder Plan

The future AWS workflow is documented only, not activated yet.

See:

- [DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md](./DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)

The current live workflows remain:

- [`.github/workflows/ci.yaml`](./.github/workflows/ci.yaml)
- [`.github/workflows/validate-with-registry.yaml`](./.github/workflows/validate-with-registry.yaml)
- [`.github/workflows/container-build-verify.yml`](./.github/workflows/container-build-verify.yml)

## Container Build Verification

The new `container-build-verify.yml` workflow is the safe bridge between
OpenShift learning and future AWS deployment.

What it does:

- builds the container locally from `docker/Dockerfile`
- tags it locally as `task-planner-foundation:test`
- runs the container locally in GitHub Actions
- smoke tests `/health`, `/validate`, and `/orchestrate`
- removes the test container after verification

What it does not do:

- does not require secrets
- does not push to ECR
- does not deploy to ECS or EKS
- does not widen the Flask app scope

This is deliberate. Before AWS deployment, the repo must prove container
portability cleanly.

For local developer use, Docker verification also requires a running Docker
daemon.

## Foundation Status Checklist

- [x] Source ownership complete
- [x] OpenShift deployment pattern present and documented
- [x] API endpoints preserved
- [x] Validator endpoint passing locally
- [x] Orchestrator endpoint ready locally
- [x] AWS migration planning started
- [x] Container build verification workflow added
- [x] ECS runtime contract planning added
- [ ] Container image published to ECR
- [ ] ECS/Fargate runtime created
- [ ] Public AWS routing enabled
- [ ] CloudWatch-backed deployment telemetry connected

## Next Phase Instructions

The next phase should stay disciplined:

1. Keep this service as a stable base runtime.
2. Use the ECS runtime contract as the source of truth before any AWS deployment work.
3. Containerize and publish through ECR.
4. Stand up ECS/Fargate as the first AWS runtime target.
5. Route logs and service telemetry into CloudWatch.
6. Add build/deploy automation only after the image and runtime contracts are stable.
7. Add stronger validator and orchestration behavior before adding model-driven intelligence.

Do not turn this repo into a large AI app yet. Keep it as the first clean
foundation service pattern for Dean'z Elite OS.
