# Dean'z Elite OS ECS Service Identity & Access Boundary v1

## Purpose

This document defines the first bounded identity and access contract for the
`task-planner-foundation` ECS service path.

It exists to answer these questions before any live AWS deployment work:

- which runtime identities will exist?
- what should each identity be allowed to do?
- what must remain out of source?
- what future deployment trust model is acceptable?

This document does not:

- create IAM roles
- create trust policies
- create secrets
- deploy anything
- add GitHub deployment automation
- change the Flask application contract

## Scope

This contract applies to the current foundation service and its planned ECS
runtime shape:

- [app.py](./app.py)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json)
- [aws/ecs-service-parameters.template.json](./aws/ecs-service-parameters.template.json)

## Identity Classes

The first ECS service path should recognize three identity classes only.

### 1. ECS Execution Role

Purpose:

- support ECS/Fargate runtime startup
- allow image retrieval from ECR
- allow container log delivery to CloudWatch

Allowed boundary:

- pull image for this service from its scoped ECR repository
- publish container logs to the scoped CloudWatch log group

Not allowed:

- mutate ECS services
- read application data broadly
- administer IAM
- administer Secrets Manager broadly
- act as a deployment operator

### 2. ECS Task Role

Purpose:

- represent the running application container identity

Current posture:

- minimum-access role
- no additional AWS API access required for the current Flask foundation app

Future allowed direction only if later required and explicitly documented:

- read service-scoped configuration from AWS Systems Manager Parameter Store
- read service-scoped secrets from AWS Secrets Manager

Not allowed:

- wildcard AWS access
- ECR administration
- ECS service mutation
- IAM mutation
- cross-service data access without explicit review

### 3. Future GitHub OIDC Deployment Role

Purpose:

- later allow GitHub Actions to deploy without long-lived AWS secrets

Current posture:

- planning only
- no trust relationship created yet
- no workflow assumes this role yet

Future bounded direction:

- push image to the service ECR repository
- register new task definition revisions
- update the ECS service to a new task definition

Not allowed:

- broad account administration
- wildcard IAM management
- organization-wide infrastructure control
- storing long-lived AWS keys in GitHub secrets as a shortcut

## Identity Boundary Rules

### Separation Of Duties

- execution role starts tasks and emits logs
- task role represents application runtime only
- deployment role performs future CI/CD deployment actions only

These roles must not collapse into one broad admin identity.

### Service Scoping

Any future access must stay scoped to this service path:

- `task-planner-foundation`
- its ECR repository
- its CloudWatch log group
- its ECS task definition family
- its ECS service

### Source Boundary

Source may contain:

- role names
- role purpose
- allowed capability descriptions
- placeholder ARNs in templates

Source must not contain:

- real access keys
- real secrets
- committed trust tokens
- wide-open IAM policies

## Current Minimum-Access Posture

For the current foundation state, the minimum acceptable identity posture is:

- execution role:
  - ECR image pull for this service only
  - CloudWatch log write for this service only
- task role:
  - no extra AWS permissions by default
- GitHub OIDC deployment role:
  - deferred until a later mission

That keeps the current service boring and explicit.

## Canonical Planning Artifact

The non-secret role boundary inventory is captured in:

- [aws/ecs-identity-access-boundary.template.json](./aws/ecs-identity-access-boundary.template.json)

That file is a planning artifact only.

It is not an IAM policy.
It is not a deployable trust document.

## Drift And Block Rules

The first live ECS service should be blocked if any of these conditions occur:

- one role is granted broad `*` access without explicit justification
- task role gains permissions unrelated to the foundation service
- execution role is used as a deployment role
- deployment workflow relies on long-lived AWS keys in source or GitHub secrets
- role scopes are undocumented relative to the service boundary

## Portability Rules

- IAM design must remain understandable without AWS-specific application code
- application code must not assume direct AWS API access unless later justified
- the service must remain runnable locally without any AWS identity dependency

## Governance Rules

- identity changes must be documented before use
- task-role widening must remain separate from application-code changes
- future deployment-role trust must be reviewed before automation is added
- identity boundaries must stay service-scoped, not account-wide

## Explicit Non-Goals

This contract does not:

- create IAM roles
- create OIDC trust
- add GitHub deploy jobs
- add Secrets Manager entries
- add runtime secrets to task definitions
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [aws/ecs-service-parameters.template.json](./aws/ecs-service-parameters.template.json)
- [aws/ecs-identity-access-boundary.template.json](./aws/ecs-identity-access-boundary.template.json)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json)

## Follow-On Contract

This identity boundary now pairs with the future deployment-trust boundary:

- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json)

The next non-deploying AWS step after that should be:

- `Public Runtime Verification & Release Gate Contract v1`

## Warning

Do not start live AWS deployment from this contract alone.

This is still a bounded planning artifact for a foundation service.
