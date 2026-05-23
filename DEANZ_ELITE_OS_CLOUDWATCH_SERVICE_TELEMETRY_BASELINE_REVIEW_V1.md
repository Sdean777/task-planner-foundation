# Dean'z Elite OS CloudWatch Service Telemetry Baseline Review v1

## Purpose

This document records the bounded review of the current CloudWatch telemetry
baseline for the `task-planner-foundation` service after the hosted public
runtime smoke workflow path was proven end to end.

It exists to answer these questions:

- what CloudWatch telemetry baseline already exists?
- what is the difference between current CloudWatch logging and explicit
  service-level telemetry connection?
- does the current runtime emit structured service telemetry into CloudWatch?
- what is the next correct non-duplicative telemetry mission?

This mission does not:

- change `app.py`
- change either workflow file
- add CloudWatch alarms, filters, or subscriptions
- mutate AWS runtime state

## Scope

This telemetry-baseline review applies to:

- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_SUCCESS_SOURCE_PUBLICATION_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_SUCCESS_SOURCE_PUBLICATION_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [`aws/cloudwatch-service-telemetry-baseline-review.record.json`](./aws/cloudwatch-service-telemetry-baseline-review.record.json)

It governs only the bounded review of the current CloudWatch service telemetry
baseline.

## Review Objective

The objective of this mission was to determine whether the open checklist item

- `CloudWatch-backed deployment telemetry connected`

should now be considered complete.

That required separating two different truths:

1. CloudWatch log visibility already exists
2. explicit service-level telemetry connection may still be missing

## Live Baseline Findings

The review found that CloudWatch logging is real and live:

- ECS service:
  `task-planner-foundation`
- active task definition:
  `task-planner-foundation:2`
- launch type:
  `FARGATE`
- task-definition log driver:
  `awslogs`
- log group:
  `/deanz-elite/task-planner-foundation`
- log stream prefix:
  `ecs`

The ECS service is currently steady:

- desired count:
  `1`
- running count:
  `1`
- pending count:
  `0`
- rollout state:
  `COMPLETED`

## CloudWatch Log Baseline Confirmed

The live CloudWatch baseline is present:

- log group exists:
  `/deanz-elite/task-planner-foundation`
- recent log streams exist for current and prior tasks
- the latest stream is active and ingesting events
- request logs for `/health` and `/telemetry` are visible in CloudWatch

So the repo can truthfully say:

- container stdout is reaching CloudWatch
- runtime access evidence is visible in CloudWatch

## What Is Still Missing

The review also found that CloudWatch-backed service telemetry is not yet
explicitly connected as a governed baseline.

Current gaps:

- CloudWatch metric filters:
  none
- CloudWatch subscription filters:
  none
- CloudWatch alarms with service prefix:
  none
- explicit retention policy on the service log group:
  not set in the live log-group response
- explicit service-telemetry event channel:
  not present

The sampled CloudWatch events are plain Flask request logs such as:

- `GET /health`
- `GET /telemetry`

That proves access logging, but not an explicit telemetry pipeline.

## App-Level Telemetry Versus CloudWatch Telemetry

The application still exposes `/telemetry` as an app-level operational
endpoint.

That endpoint currently reports:

- service identity
- runtime classification
- infrastructure classification
- phase
- endpoint inventory
- task count
- agent status

But the service does not currently emit that telemetry payload as structured
CloudWatch telemetry data. CloudWatch only sees the request/access log for the
endpoint call, not the telemetry object itself.

That is the remaining gap.

## Review Conclusion

The correct baseline verdict is:

- `cloudwatch_logging_present_service_telemetry_not_yet_connected`

Meaning:

- CloudWatch logging baseline: present
- CloudWatch service telemetry baseline: incomplete

So the README checklist should remain:

- `CloudWatch-backed deployment telemetry connected`
  -> unchecked

That is still the honest source-truth state after this review.

## Preserved Boundaries

This mission preserved the required boundaries:

- `app.py` stayed unchanged
- `.github/workflows/public-runtime-smoke.yml` stayed unchanged
- `.github/workflows/deploy-foundation-skeleton.yml` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- no AWS mutation happened in this mission

## Canonical Execution Record

The non-secret execution record for this review is:

- [`aws/cloudwatch-service-telemetry-baseline-review.record.json`](./aws/cloudwatch-service-telemetry-baseline-review.record.json)

That file records the live ECS/log findings, the missing telemetry-layer
findings, and the next bounded mission.

## Recommended Next Mission

The next bounded step after this review should be:

- `CloudWatch Service Telemetry Baseline Proposal v1`

That mission should define the smallest explicit source-truth shape for
CloudWatch-backed service telemetry without jumping straight into alarms,
dashboards, or broad observability expansion.

## Warning

Do not mark CloudWatch-backed deployment telemetry as complete just because
logs exist.

CloudWatch log visibility and explicit service-telemetry connection are not the
same thing.
