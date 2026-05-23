# Dean'z Elite OS ECS Service Parameterization & Environment Contract v1

## Purpose

This document defines the first bounded parameterization and environment
contract for the `task-planner-foundation` ECS service path.

It exists to answer one question before any live ECS service creation:

> which values are fixed by the foundation service contract, which values must
> be supplied at deployment time, and which values must never live in source?

This document does not:

- deploy anything
- add credentials
- add secrets
- change the Flask application contract
- add deployment automation

## Scope

This contract applies only to the current foundation service and its planned
AWS runtime shape:

- [app.py](./app.py)
- [docker/Dockerfile](./docker/Dockerfile)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)

It does not widen the application or authorize live runtime changes.

## Parameter Classes

All future ECS configuration values must fall into one of three classes.

### 1. Foundation Constants

These values are fixed by the service contract and should not drift between
local runtime, container runtime, and first ECS proof:

- application entrypoint: `python ./app.py`
- container name: `task-planner-foundation`
- container port: `8081`
- health check path: `/health`
- validation path: `/validate`
- orchestration path: `/orchestrate`
- non-secret env:
  - `FLASK_PORT=8081`
  - `PYTHONUNBUFFERED=1`

These belong in source because they define the runtime shape of the service
itself.

### 2. Deployment Parameters

These values are required for a real ECS service, but they are not source
truth for the application:

- AWS account ID
- AWS region
- ECR repository URI
- ECS cluster name
- ECS service name
- ECS task definition family
- desired count
- VPC ID
- subnet IDs
- security group IDs
- ALB ARN
- target group ARN
- execution role ARN
- task role ARN
- CloudWatch log group name
- public base URL

These must be externalized from app code and managed as environment-specific
runtime inputs.

### 3. Sensitive Values

These values are not required yet, but if they appear later they must stay out
of the repository:

- API credentials
- AWS access keys
- private tokens
- database URLs with secrets
- model or OpenAI keys
- webhook secrets

Future sensitive values should be sourced from AWS-native secret systems such
as:

- AWS Secrets Manager
- AWS Systems Manager Parameter Store

Not:

- committed `.env` files
- inline GitHub workflow literals
- task definition JSON committed with real secrets

## Current Approved Environment Boundary

The first ECS service should allow only these application-level environment
variables:

| Variable | Value | Class | Status |
| --- | --- | --- | --- |
| `FLASK_PORT` | `8081` | foundation constant | approved |
| `PYTHONUNBUFFERED` | `1` | runtime hygiene | approved |

Nothing else is approved at this stage.

That means:

- no environment-specific app behavior flags yet
- no hidden feature toggles
- no secret placeholders inside the task definition for now

## Canonical Deployment Parameter Inventory

The non-secret service parameter inventory is captured in:

- [aws/ecs-service-parameters.template.json](./aws/ecs-service-parameters.template.json)

That file is a planning artifact only. It is not a live deploy manifest.

Its purpose is to keep the future ECS service parameter boundary explicit and
portable.

## Source-Of-Truth Mapping

### Values That Stay In Source

- app entrypoint
- container port
- endpoint contract
- non-secret baseline environment
- task family naming intent
- log group naming convention

### Values That Stay External To Source

- account-specific ARNs
- region selection
- VPC/subnet/security group identifiers
- actual deployment URLs
- cluster/service names if they vary by environment
- future secret values

### Values That Must Be Resolved Before Live ECS Work

- `awsRegion`
- `awsAccountId`
- `ecrRepositoryUri`
- `ecsClusterName`
- `ecsServiceName`
- `executionRoleArn`
- `taskRoleArn`
- `subnetIds`
- `securityGroupIds`
- `targetGroupArn`

## Environment Drift Rules

The first ECS cut should be blocked if any of these conditions occur:

- container port differs from `8081`
- health check path differs from `/health`
- `FLASK_PORT` differs from `8081`
- undocumented new environment variables are introduced
- secret literals appear in source-controlled templates
- account- or region-specific values are hard-coded into application code

This service should remain boring and explicit.

## Portability Rules

- the service must still run locally with `python app.py`
- the container must still run without AWS-specific logic in the application
- ECS-specific values must remain replaceable if the runtime later moves
- no committed parameter file should become a de facto secret store

## Governance Rules

- deployment parameters must be reviewable as plain configuration inputs
- app code changes must remain separate from AWS runtime parameter changes
- parameter additions must be documented before they are used
- deployment automation may reference these parameter names later, but must not
  widen them silently

## Explicit Non-Goals

This contract does not:

- create an ECS service
- create IAM roles
- create Secrets Manager entries
- create GitHub Actions deployment jobs
- add `.env` files with live values
- switch the app to a production WSGI server

## Paired Artifacts

- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)
- [aws/ecs-service-parameters.template.json](./aws/ecs-service-parameters.template.json)

## Follow-On Contract

This contract now pairs with:

- [aws/ecs-identity-access-boundary.template.json](./aws/ecs-identity-access-boundary.template.json)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)

The next non-deploying AWS step after that should be:

- `Public Runtime Verification & Release Gate Contract v1`

## Warning

Do not start live AWS deployment from this contract alone.

This is still a bounded planning artifact for a foundation service.
