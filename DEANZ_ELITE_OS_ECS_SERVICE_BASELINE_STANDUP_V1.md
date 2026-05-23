# Dean'z Elite OS ECS Service Baseline Standup v1

## Purpose

This document records the first explicit ECS baseline standup for the
`task-planner-foundation` service after the initial bounded rollout run was
correctly blocked by missing baseline state.

It exists to answer these questions:

- what AWS baseline resources were created?
- which immutable image and task definition now define the service baseline?
- what bounded compromises were used to get the first service running?
- what remains out of scope even after the baseline is steady?

This mission does not:

- change `app.py`
- enable `public-verification-placeholder`
- add deployment secrets to source
- claim that public reachability is finished

## Scope

This baseline standup applies to:

- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECS_ROLLOUT_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECS_ROLLOUT_RUN_V1.md)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [`aws/ecs-service-baseline-standup.record.json`](./aws/ecs-service-baseline-standup.record.json)

It governs only the explicit bounded baseline creation for the service.

## Baseline Objective

The objective of this mission was to replace the missing rollout target with a
real bounded ECS baseline:

- one explicit cluster
- one explicit task-definition family
- one explicit service
- one explicit immutable image input
- one explicit log group

That gives later rollout and public verification work an authoritative target
instead of a guessed target.

## AWS Resources Created

The following bounded resources were created:

- ECS cluster:
  `arn:aws:ecs:us-east-1:329601960228:cluster/task-planner-foundation`
- CloudWatch log group:
  `/deanz-elite/task-planner-foundation`
- ECS task definition:
  `arn:aws:ecs:us-east-1:329601960228:task-definition/task-planner-foundation:1`
- ECS service:
  `arn:aws:ecs:us-east-1:329601960228:service/task-planner-foundation/task-planner-foundation`

## Baseline Runtime Identity

The baseline is currently pinned to:

- image tag:
  `sha-dfc958a333b792f82c3feaaa4f543d323450938f`
- image digest:
  `sha256:2455af6b5b4a787cd8671c1f2c4410ffc76eef4b52f09fb37f1572565207d4ad`
- task family:
  `task-planner-foundation`
- first revision:
  `task-planner-foundation:1`

## Bounded Bootstrap Compromise

Dedicated service-scoped roles did not exist yet, so the baseline used the
existing ECS execution role as a bounded bootstrap identity for both:

- execution role:
  `arn:aws:iam::329601960228:role/ecsTaskExecutionRole-deanzelite`
- task role:
  `arn:aws:iam::329601960228:role/ecsTaskExecutionRole-deanzelite`

This was accepted only because:

- the current Flask foundation app does not require broad runtime AWS access
- the role is already proven in the same account
- no secrets were added to source
- the service remained internal-only and non-public in this mission

This is a bootstrap compromise, not the final identity boundary.

## Network Posture

The baseline service was created with:

- cluster: `task-planner-foundation`
- service: `task-planner-foundation`
- launch type: `FARGATE`
- desired count: `1`
- assign public IP: `ENABLED`
- subnets:
  - `subnet-04bc9dcc0fef57a46`
  - `subnet-0651dde07d6ec76d3`
- security group:
  - `sg-0538f40fa41c92d64`

No load balancer or target group was attached in this mission.

## Verified Outcome

The service reached bounded steady state:

- desired count: `1`
- running count: `1`
- pending count: `0`
- rollout state: `COMPLETED`
- running task:
  `arn:aws:ecs:us-east-1:329601960228:task/task-planner-foundation/e0a3f7ccebd14d68954086ee2f4acefe`

This confirms the baseline is now real and usable for later bounded work.

## Preserved Boundaries

This mission preserved the required boundaries:

- `app.py` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- `push-image-placeholder` behavior remained unchanged
- `public-verification-placeholder` remained disabled
- no public verification was attempted

## Canonical Execution Record

The non-secret execution record for this mission is:

- [`aws/ecs-service-baseline-standup.record.json`](./aws/ecs-service-baseline-standup.record.json)

That file records the created resources, baseline runtime identity, and next
bounded mission.

## Recommended Next Mission

The next bounded step after this baseline standup should be:

- `Public Verification Stage Candidate Review v1`

That mission should inspect only the still-disabled
`public-verification-placeholder` job now that both the image publication lane
and the ECS runtime baseline exist.

## Warning

Do not treat a steady ECS baseline as public readiness.

The service exists, but public reachability and release-gate verification
remain separate bounded stages.
