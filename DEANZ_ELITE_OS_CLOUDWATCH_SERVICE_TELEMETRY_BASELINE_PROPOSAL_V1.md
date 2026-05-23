# Dean'z Elite OS CloudWatch Service Telemetry Baseline Proposal v1

## Purpose

This document records the bounded proposal for the first explicit
CloudWatch-backed service telemetry connection for the
`task-planner-foundation` service.

It exists to answer these questions:

- what is the minimum non-duplicative telemetry connection shape?
- how should the repo convert the current logs-only CloudWatch baseline into
  explicit service telemetry without widening observability scope too early?
- what should stay out of scope for the first telemetry connection patch?
- what is the next exact bounded mission after this proposal?

This mission does not:

- change `app.py`
- change either workflow file
- add CloudWatch alarms, dashboards, filters, or subscriptions
- mutate AWS runtime state

## Scope

This proposal applies to:

- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_BASELINE_REVIEW_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_BASELINE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [`app.py`](./app.py)
- [`aws/cloudwatch-service-telemetry-baseline-proposal.template.json`](./aws/cloudwatch-service-telemetry-baseline-proposal.template.json)

It governs only the minimum explicit source-truth shape for the first
CloudWatch-backed service telemetry connection.

## Proposal Objective

The objective of this mission was to define the smallest future patch that
would make this statement true without overreaching:

- `CloudWatch-backed deployment telemetry connected`

The review already proved:

- CloudWatch log delivery exists
- the ECS runtime is stable
- `/telemetry` is truthful at the application layer

So the missing piece is not more infrastructure. It is explicit service
telemetry entering the already-working CloudWatch log path.

## Proposed Minimum Shape

The first telemetry-connection patch should stay narrow:

1. preserve the existing `awslogs` driver, log group, and stream-prefix path
2. preserve the current `/telemetry` response contract
3. add one small app-level structured telemetry emission path in `app.py`
4. route that structured telemetry event to stdout so CloudWatch receives it
   through the existing ECS log configuration

In plain terms:

- do not build a second telemetry system
- use the existing stdout -> `awslogs` -> CloudWatch Logs channel
- make `/telemetry` produce an explicit structured service-telemetry event in
  addition to its current HTTP response

## Proposed Future Patch Boundary

The minimum future patch should be bounded to:

- `app.py`
- one new helper for structured telemetry emission
- one invocation from the `/telemetry` route
- no endpoint contract widening
- no workflow changes
- no AWS API mutation

The `/telemetry` HTTP response should remain compatible with the current smoke
workflow and release-gate expectations.

## Proposed Structured Event Shape

The future structured CloudWatch telemetry event should be a compact JSON
object emitted to stdout with fields derived from the existing `/telemetry`
response.

Proposed fields:

- `eventType`
  - `service_telemetry_snapshot`
- `service`
  - `task-planner-foundation`
- `runtime`
  - derived current runtime identity
- `infrastructure`
  - derived current infrastructure identity
- `phase`
  - `foundation-api`
- `status`
  - current service status
- `taskCount`
  - current task count
- `agentStatus`
  - current agent status
- `activeEndpointCount`
  - count of registered endpoints
- `sourceEndpoint`
  - `/telemetry`

This is enough to make service telemetry explicit in CloudWatch without
inventing a metrics system yet.

## Why This Proposal Is Minimal And Correct

This proposal uses the smallest possible new surface:

- the service already knows the telemetry values
- the ECS runtime already ships stdout to CloudWatch
- the smoke workflow already exercises `/telemetry`

So the first telemetry connection does not need:

- metric filters
- subscription filters
- alarms
- dashboards
- traces
- a new telemetry endpoint
- a separate telemetry sidecar

Those can remain future missions if needed.

## Explicitly Out Of Scope

The following remain out of scope for the first telemetry-connection patch:

- CloudWatch metric filters
- CloudWatch subscription filters
- CloudWatch alarms
- dashboards or widgets
- trace instrumentation
- retention-policy mutation
- workflow changes
- deploy-pipeline mutation

This proposal is about explicit service telemetry presence, not observability
expansion.

## Proposal Conclusion

The correct proposal verdict is:

- `ready_for_controlled_patch_review`

Meaning:

- the logs-only review is complete
- the minimum telemetry connection shape is defined
- the next step should inspect the exact source diff before any code change is
  made

## Preserved Boundaries

This mission preserved the required boundaries:

- `app.py` stayed unchanged
- `.github/workflows/public-runtime-smoke.yml` stayed unchanged
- `.github/workflows/deploy-foundation-skeleton.yml` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- no AWS mutation happened in this mission

## Canonical Planning Artifact

The non-secret planning artifact for this proposal is:

- [`aws/cloudwatch-service-telemetry-baseline-proposal.template.json`](./aws/cloudwatch-service-telemetry-baseline-proposal.template.json)

That file records the exact proposed event shape, patch boundary, deferred
items, and next bounded mission.

## Recommended Next Mission

The next bounded step after this proposal should be:

- `CloudWatch Service Telemetry Controlled Patch Review v1`

That mission should inspect the exact future `app.py` diff for the telemetry
helper and `/telemetry`-route emission before any implementation patch is
allowed.

## Warning

Do not jump from this proposal straight to alarms or observability sprawl.

The first goal is only to make service telemetry explicit in CloudWatch over
the existing bounded log path.
