# GitHub Actions AWS Foundation Placeholder Plan

This is the planning document for the future AWS deployment workflow for
`task-planner-foundation`.

Most of this plan is intentionally not executable yet.

The exception is the new pre-AWS container verification bridge:

- `.github/workflows/container-build-verify.yml`

That workflow is intentionally non-deploying and requires no secrets.

The next planning artifact is the explicit ECS runtime contract:

- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)

## Purpose

Document the intended workflow shape without:

- adding AWS credentials
- adding live deployment secrets
- enabling automatic production deployment
- widening the scope of this foundation repo

## Intended Workflow Shape

```text
on:
  push to main
  pull request to main
  optional manual dispatch

jobs:
  1. lint-and-validate
  2. container-build-verify
  3. push-image-to-ecr
  4. deploy-to-ecs-fargate
  5. public-runtime smoke test
```

## Planned Stages

### 1. Lint and Validate

- check out source
- set up Python
- install requirements
- run existing CI checks
- run endpoint-level validation if lightweight tests are added later

### 2. Container Build Verification

Current active bridge step.

- build from `docker/Dockerfile`
- tag locally as `task-planner-foundation:test`
- run the container locally in CI
- smoke test `/health`, `/validate`, and `/orchestrate`
- remove the test container after verification
- do not push the image anywhere
- do not require AWS credentials or deployment secrets

### 3. Push Image to ECR

- authenticate to AWS with GitHub OIDC or scoped credentials
- push image to Amazon ECR
- record image URI as a deployment artifact

### 4. Deploy to ECS/Fargate

- update ECS task definition image reference
- deploy to ECS service
- keep environment variables externalized
- keep the service stateless

### 5. Public Runtime Smoke Test

- test `/health`
- test `/validate`
- test `/orchestrate`
- fail the rollout if the foundation contract is broken

## Required Future Inputs

These are not added now, but will be required later:

- AWS account and region selection
- ECR repository name
- ECS cluster and service names
- IAM/OIDC trust configuration
- deployment environment boundaries
- rollout and rollback policy

## Security Rules

- do not commit static AWS credentials
- prefer GitHub OIDC over long-lived secrets
- keep environment configuration out of source when it becomes sensitive
- keep deployment permissions scoped to this service

## Portability Rules

- keep the app runnable locally without GitHub Actions
- keep the container runnable outside AWS
- avoid workflow logic that assumes ECS is the only future runtime forever

## Current Status

The existing live workflows remain:

- `.github/workflows/ci.yaml`
- `.github/workflows/validate-with-registry.yaml`
- `.github/workflows/container-build-verify.yml`

Current completed/active step:

- non-deploying container build verification
- ECS runtime contract planning

Still future:

- ECR image push
- ECS/Fargate deployment
- post-deploy public runtime smoke tests

This placeholder plan remains a pre-deployment design layer, not a live AWS
deploy path.
