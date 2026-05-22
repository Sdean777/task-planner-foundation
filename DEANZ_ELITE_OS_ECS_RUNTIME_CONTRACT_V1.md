# Dean'z Elite OS ECS Runtime Contract v1

## Purpose

This document defines the first non-deploying AWS runtime contract for the
`task-planner-foundation` service.

It does not deploy anything.
It does not add credentials.
It does not widen application scope.

It turns the existing high-level AWS direction into a precise runtime contract
for:

- ECR image naming
- ECS/Fargate task shape
- ALB/API routing assumptions
- CloudWatch logging expectations
- health check mapping
- future GitHub OIDC boundaries

## Scope

This contract applies to the current Flask foundation service only:

- preserve existing endpoints
- preserve existing container portability
- preserve the current OpenShift-proven container pattern
- prepare for AWS-native runtime planning

Out of scope:

- live deployment
- ECR push automation
- ECS service creation
- AWS credentials
- OpenAI integration
- autonomous agent logic

## Current Service Contract

The current foundation service is defined by:

- [app.py](./app.py)
- [docker/Dockerfile](./docker/Dockerfile)
- [deploy.yaml](./deploy.yaml)
- [devfile.yaml](./devfile.yaml)

Current immutable runtime assumptions for this contract:

- container entrypoint remains `python ./app.py`
- container port remains `8081`
- `FLASK_PORT=8081` remains the container runtime port
- endpoints remain:
  - `/`
  - `/health`
  - `/status`
  - `/tasks`
  - `/memory`
  - `/agent`
  - `/telemetry`
  - `/validate`
  - `/orchestrate`

## ECR Image Contract

Recommended initial ECR repository name:

- `task-planner-foundation`

Recommended image tagging strategy:

- `sha-<git-sha>`
- `main`
- optional release tags later

Rules:

- do not use mutable ad hoc tags as the only deployment input
- keep a SHA-based tag available for every promoted image
- keep image naming service-specific and stable

Example image URI shape:

```text
<aws_account_id>.dkr.ecr.<aws_region>.amazonaws.com/task-planner-foundation:sha-<git-sha>
```

## ECS/Fargate Task Contract

Initial recommended task posture:

- runtime: ECS with Fargate
- network mode: `awsvpc`
- requires compatibilities: `FARGATE`
- initial desired count: `1`
- CPU: `256`
- memory: `512`

These values are intentionally conservative because this is still a foundation
service, not a scaled intelligence runtime.

## Container Definition Contract

Initial container assumptions:

- container name: `task-planner-foundation`
- image: injected by deployment process later
- essential: `true`
- port mapping: `8081/tcp`
- environment:
  - `FLASK_PORT=8081`
  - `PYTHONUNBUFFERED=1`

No secret environment variables are required at this stage.

## ALB / Routing Contract

Initial public routing recommendation:

- Application Load Balancer first
- target type compatible with ECS/Fargate task networking
- listener forwards to the foundation service target group

Health check contract:

- health check path: `/health`
- health check port: `traffic-port`
- success code: `200`
- protocol: `HTTP`
- healthy threshold: `2`
- unhealthy threshold: `3`
- timeout seconds: `5`
- interval seconds: `30`

`/health` is the canonical infrastructure health path.

`/validate` remains the deeper foundation validation path, but it should not be
the first ALB health check target.

## API Gateway Posture

API Gateway is not the first recommendation for this service.

Reason:

- the service currently exposes a simple HTTP foundation API
- ALB is the lighter first bridge for ECS/Fargate

API Gateway can remain a later option if:

- auth layers grow
- stage/version management becomes necessary
- broader API governance is introduced

## CloudWatch Logging Contract

Initial log contract:

- log driver: `awslogs`
- log group: `/deanz-elite/task-planner-foundation`
- stream prefix: `ecs`
- region: deployment region

Purpose:

- infrastructure/runtime logs belong in CloudWatch
- `/telemetry` remains application-level operational telemetry

These are complementary, not interchangeable.

## Telemetry and Validation Mapping

The service already has:

- `/telemetry`
- `/validate`
- `/orchestrate`

AWS runtime mapping should treat them as:

- `/health`
  - infrastructure health
- `/status`
  - lightweight service state
- `/telemetry`
  - app-level runtime telemetry surface
- `/validate`
  - operational validation surface
- `/orchestrate`
  - orchestration-readiness surface

The contract does not add CloudWatch metrics or traces yet. It only defines the
first logging and health-check boundary.

## IAM / OIDC Future Posture

Future deployment automation should prefer:

- GitHub Actions OIDC

Not:

- long-lived static AWS keys in GitHub secrets

This document does not create OIDC trust or IAM roles now. It only defines the
future posture:

- GitHub should assume a scoped AWS role later
- permissions must stay limited to this service path
- no credentials should be committed into source

## Unresolved Runtime Decision

The current container contract still runs:

```text
python ./app.py
```

That means the Flask development server is still the active runtime process.

For foundation proof, this is acceptable.

Before live public ECS traffic, a later mission must explicitly decide:

- keep the current server temporarily for early proof only
  or
- move to a production WSGI server such as Gunicorn

This decision is intentionally deferred. It should be made consciously, not
silently.

## Deliverables Connected To This Contract

This contract pairs with:

- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)
- [README.md](./README.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)

## Next Step After This Contract

The next non-deploying step after this contract should be:

- first GitHub Actions proof run of `container-build-verify.yml`
  or
- explicit ECS service/runtime notes derived from this contract

Not:

- direct ECR push
- direct ECS deployment
- credentials-in-repo shortcuts
