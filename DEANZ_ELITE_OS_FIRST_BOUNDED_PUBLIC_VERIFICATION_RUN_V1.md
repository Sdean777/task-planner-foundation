# Dean'z Elite OS First Bounded Public Verification Run v1

## Purpose

This document records the first bounded attempt to execute the
`task-planner-foundation` public verification path after the third-job workflow
patch was applied.

It exists to answer these questions:

- does a stable non-secret `FOUNDATION_PUBLIC_BASE_URL` actually exist?
- is there a real public routing surface for the service, or only task-level
  networking?
- was a safe bounded public verification run actually possible?
- what verification work was intentionally avoided when stable routing was
  missing?

This run does not:

- change `app.py`
- modify the workflow
- invent endpoint truth from an ephemeral task IP
- treat a blocked preflight as a successful public verification run

## Scope

This run applies to:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`aws/first-bounded-public-verification-run.record.json`](./aws/first-bounded-public-verification-run.record.json)

It governs only the first bounded public-verification execution attempt.

## Run Objective

The objective of this run was to execute the now-bounded third-job public
verification path against real AWS state while preserving the established
safety rules:

- a stable non-secret base URL must exist before endpoint truth is claimed
- public verification must remain subordinate to release-gate order
- rollback posture must remain possible
- ephemeral task networking must not be mistaken for durable public routing

## ECS And Routing Preflight Findings

The bounded public-verification preflight found four critical facts:

1. the ECS baseline service is steady at `desired=1`, `running=1`, `pending=0`
2. the `task-planner-foundation` service has no load balancer attached
3. the service has no service registry attached
4. the running task has an ephemeral public ENI address, but that does not
   satisfy the requirement for a stable non-secret
   `FOUNDATION_PUBLIC_BASE_URL`

Observed AWS state:

- ECS service `task-planner-foundation` in cluster `task-planner-foundation`
  returned:
  - `loadBalancers: []`
  - `serviceRegistries: []`
  - `desiredCount: 1`
  - `runningCount: 1`
  - `pendingCount: 0`
- running task:
  `arn:aws:ecs:us-east-1:329601960228:task/task-planner-foundation/e0a3f7ccebd14d68954086ee2f4acefe`
- task ENI:
  `eni-03cba2d85c74f8852`
- task public DNS:
  `ec2-34-237-138-71.compute-1.amazonaws.com`
- task public IP:
  `34.237.138.71`

## Why The ENI Was Not Accepted As Base URL Truth

The task ENI public address was intentionally rejected as the verification
surface because:

- it is task-level and therefore ephemeral
- it is not represented as a stable repo-scoped non-secret base URL contract
- the task security group `sg-0538f40fa41c92d64` only allows inbound
  `tcp/3000` from ALB security group `sg-07fce31d4ae9be1d4`
- there is no direct internet ingress rule for the task itself
- no attached ALB or service registry currently turns that runtime into a
  durable public endpoint for the workflow

So the service is running, but there is still no authoritative
`FOUNDATION_PUBLIC_BASE_URL`.

## Execution Outcome

This run is recorded as:

- `public_verification_run_blocked_missing_stable_public_base_url`

No live public endpoint probes were executed.

Specifically:

- no `curl` verification was run
- no `/health` probe was attempted
- no `/status` probe was attempted
- no `/validate` probe was attempted
- no `/orchestrate` probe was attempted
- no `/telemetry` probe was attempted

The run stopped before probing because a stable public routing surface does not
yet exist.

## Why The Stop Was Correct

The public-verification patch intentionally assumed a stable non-secret
`FOUNDATION_PUBLIC_BASE_URL`. That condition is not yet true for
`task-planner-foundation`.

Proceeding anyway would have violated the repo's own rules:

- endpoint truth must not be invented from ephemeral runtime state
- public verification must stay subordinate to release-gate order
- rollback posture must remain explicit
- stable routing must exist before workflow verification claims runtime health

So the correct execution result is a blocked run, not a partial verification.

## Preserved Boundaries

This run preserved the required boundaries:

- `app.py` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- `push-image-placeholder` behavior remained untouched
- `ecs-rollout-placeholder` behavior remained untouched
- no public routing was mutated blindly

## Canonical Execution Record

The non-secret execution record for this run is:

- [`aws/first-bounded-public-verification-run.record.json`](./aws/first-bounded-public-verification-run.record.json)

That file records the steady ECS baseline, the missing stable routing surface,
and the next bounded mission.

## Recommended Next Mission

The next bounded step after this blocked run should be:

- `Public Routing Baseline Standup v1`

That mission should create the first explicit stable non-secret
`FOUNDATION_PUBLIC_BASE_URL` for `task-planner-foundation` under bounded
review rather than pretending public verification can proceed on task-level
networking alone.

## Warning

Do not retry public verification by guessing endpoint truth from the task ENI.

Stand up the explicit public routing baseline first, then rerun bounded public
verification against that known target.
