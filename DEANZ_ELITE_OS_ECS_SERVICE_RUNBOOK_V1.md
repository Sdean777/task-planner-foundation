# Dean'z Elite OS ECS Service Runbook v1

## Purpose

This document is the first operator-facing ECS service runbook for the
`task-planner-foundation` service.

It translates the runtime contract into a bounded manual runbook for the next
AWS planning layer.

It does not:

- deploy anything
- add credentials
- add GitHub deployment automation
- change the Flask runtime contract

## Runbook Scope

This runbook exists to define the manual service-level steps and checks that
must be understood before any live AWS deployment work begins.

It covers:

- the AWS resources that will later be required
- the exact runtime assumptions that must not drift
- the manual verification sequence for a future ECS/Fargate service
- the stop conditions and rollback posture for the first runtime cut

It does not authorize execution.

## Foundation Preconditions

Before any ECS service work is attempted, the following foundation artifacts
must already be treated as source of truth:

- [README.md](./README.md)
- [DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md](./DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)
- [BACKUP_CHECKPOINT_V1.md](./BACKUP_CHECKPOINT_V1.md)

The service contract must remain unchanged:

- app entrypoint: `python ./app.py`
- container port: `8081`
- container env: `FLASK_PORT=8081`
- canonical health path: `/health`
- validation path: `/validate`
- orchestration path: `/orchestrate`

## Required AWS Resource Map

The first ECS runtime should plan for these resource classes:

### 1. Container Registry

- Amazon ECR repository
- recommended name: `task-planner-foundation`
- image tags must include a commit-SHA form

### 2. Compute Runtime

- Amazon ECS cluster
- Fargate task launch type
- one ECS service for this foundation app
- desired count: `1` for first proof

### 3. Networking

- one VPC with appropriate private/public subnet choice
- security groups scoped to ALB -> ECS service traffic
- `awsvpc` networking for tasks

### 4. Public Routing

- Application Load Balancer first
- one target group bound to port `8081`
- health checks pointed to `/health`

### 5. Logging

- CloudWatch Logs group
- recommended group: `/deanz-elite/task-planner-foundation`

## Manual Input Checklist

These inputs must be defined outside source before any live run begins:

- AWS account ID
- AWS region
- ECR repository URI
- ECS cluster name
- ECS service name
- task definition family and revision strategy
- VPC and subnet IDs
- security group IDs
- ALB ARN
- target group ARN
- execution role ARN
- task role ARN

No secrets or long-lived credentials belong in this repository.

## ECS Service Runtime Shape

The first service run should preserve the smallest possible runtime:

- launch type: `FARGATE`
- desired count: `1`
- task CPU: `256`
- task memory: `512`
- one container only
- container port: `8081`
- no sidecars
- no secrets required
- no background workers

This remains a foundation service, not a scaled OS runtime.

## ALB Health and Routing Rules

The future service must preserve the current endpoint intent:

- `/health`
  - infrastructure health and target-group health check
- `/status`
  - lightweight service state
- `/telemetry`
  - application telemetry surface
- `/validate`
  - deeper operational validation
- `/orchestrate`
  - orchestration-readiness surface

ALB contract:

- target group port: `8081`
- protocol: `HTTP`
- health check path: `/health`
- matcher: `200`
- no redirect assumptions
- no auth layer inserted yet

## Manual Verification Sequence

When a future live ECS service exists, verification should happen in this
order:

1. Confirm ECS service is stable.
2. Confirm task reaches `RUNNING`.
3. Confirm target group reports healthy targets.
4. Confirm CloudWatch logs are receiving container output.
5. Confirm:
   - `GET /health`
   - `GET /status`
   - `GET /validate`
   - `GET /orchestrate`
6. Confirm the service still reports the expected foundation identity.
7. Confirm no unexpected secrets or config injection occurred.

The first runtime proof should fail closed if `/health` or `/validate` breaks.

## Rollback and Stop Conditions

The first ECS cut must remain reversible.

Stop conditions:

- health check fails repeatedly
- target group never becomes healthy
- container exits repeatedly
- CloudWatch logs show startup failure
- validator path degrades
- endpoint contract drifts from the Flask foundation

Rollback posture:

- do not widen runtime during failure investigation
- revert to the previous task definition revision
- keep image tagging SHA-based for traceability
- keep investigation at the runtime layer before changing application code

## Security and Governance Rules

- do not commit AWS credentials
- prefer GitHub OIDC later over static secrets
- keep IAM permissions scoped to this service
- keep the repo portable outside AWS
- do not add OpenAI or model secrets in this phase
- do not introduce deployment automation before the runbook is understood

## Explicit Non-Goals

This runbook does not:

- create ECS resources
- create IAM roles
- push images to ECR
- define GitHub deployment automation
- switch the app to a different runtime server
- change the Flask endpoint contract

## Follow-On Contract

This runbook now pairs with:

- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [aws/ecs-service-parameters.template.json](./aws/ecs-service-parameters.template.json)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [aws/ecs-identity-access-boundary.template.json](./aws/ecs-identity-access-boundary.template.json)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)

The next non-deploying AWS step after that should be:

- `Public Runtime Verification & Release Gate Contract v1`

## Warning

Do not start live AWS deployment from this runbook alone.

This document is a bounded planning and operator-readiness layer, not a
deployment authorization.
