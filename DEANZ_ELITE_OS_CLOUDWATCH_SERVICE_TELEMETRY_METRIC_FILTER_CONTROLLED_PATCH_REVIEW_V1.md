# Dean'z Elite OS CloudWatch Service Telemetry Metric Filter Controlled Patch Review v1

## Purpose

This document records the bounded controlled-patch review for the first
CloudWatch metric-filter layer over the existing
`service_telemetry_snapshot` event in `task-planner-foundation`.

It exists to answer these questions:

- what exact future CloudWatch mutation is in scope?
- what exact mutation is out of scope?
- how should the first metric-filter layer stay foundation-scoped and
  non-Atlas?
- what is the next exact bounded mission after this review?

This mission does not:

- change `app.py`
- change either workflow file
- create a CloudWatch metric filter
- create a CloudWatch alarm
- mutate AWS runtime state

## Scope

This controlled review applies to:

- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_BASELINE_REVIEW_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_BASELINE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_PROPOSAL_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_PROPOSAL_V1.md)
- [aws/cloudwatch-service-telemetry-metric-filter-controlled-patch-review.template.json](./aws/cloudwatch-service-telemetry-metric-filter-controlled-patch-review.template.json)

It governs only the exact future CloudWatch mutation boundary for the first
metric-filter layer.

## Review Objective

The objective of this mission was to inspect the exact mutation boundary for
the first CloudWatch metric filter so the repo can move from:

- structured telemetry event present in CloudWatch Logs

to:

- one deterministic CloudWatch metric derived from that event

without widening into a broader observability system or colliding with Atlas
semantics.

## Exact Future Mutation In Scope

The future patch is allowed to do only the following:

1. create one metric filter on:
   - log group `/deanz-elite/task-planner-foundation`
2. use only the filter pattern:
   - `{ $.eventType = "service_telemetry_snapshot" }`
3. emit only one metric transformation:
   - namespace `DeanzElite/Foundation`
   - metric name `ServiceTelemetrySnapshotCount`
   - metric value `1`
4. record the patch doctrine and execution evidence in the repo after the live
   CloudWatch mutation succeeds

That is the full allowed future mutation boundary.

## Exact Future Mutation Out Of Scope

The future patch must not:

- modify `app.py`
- modify `.github/workflows/public-runtime-smoke.yml`
- modify `.github/workflows/deploy-foundation-skeleton.yml`
- create more than one metric filter
- create a CloudWatch alarm
- create a dashboard
- create a subscription filter
- mutate log retention
- change the log group
- change the event shape
- reuse Atlas or sovereign OS telemetry names

This review keeps the first CloudWatch metric mutation intentionally tiny.

## Controlled CloudWatch Mutation Shape

The future mutation should prefer one bounded command shape:

1. create exactly one metric filter
2. target exactly one existing service log group
3. count only `service_telemetry_snapshot`
4. keep the namespace foundation-scoped
5. defer alarms and all later observability layers

In practice, the future patch should remain equivalent to one bounded
`aws logs put-metric-filter` mutation with:

- log group name:
  - `/deanz-elite/task-planner-foundation`
- filter name:
  - `task-planner-foundation-service-telemetry-snapshot-count`
- filter pattern:
  - `{ $.eventType = "service_telemetry_snapshot" }`
- metric namespace:
  - `DeanzElite/Foundation`
- metric name:
  - `ServiceTelemetrySnapshotCount`
- metric value:
  - `1`

## Anti-Collision Boundary

The future metric-filter patch must remain explicitly separate from Atlas and
sovereign OS telemetry semantics.

That means the future patch must not:

- use `atlas` in the filter name or metric namespace
- use `runtimeTelemetry`, `atlasService`, `confidenceTelemetry`,
  `authorizationTelemetry`, `operatorSessionTelemetry`,
  `remoteRuntimeTelemetry`, `distributedCoordinationTelemetry`,
  `sandboxGovernanceTelemetry`, `promotionGovernanceTelemetry`,
  `failoverGovernanceTelemetry`, or `scopedMemoryTelemetry` as filter or
  metric names
- claim that the foundation metric is a Brain, Atlas, validator, memory, or
  governance metric

The filter must remain foundation-local:

- service = `task-planner-foundation`
- namespace = `DeanzElite/Foundation`
- event = `service_telemetry_snapshot`

## Why This Controlled Boundary Is Correct

This review keeps the first metric-filter mutation:

- outside runtime code
- outside workflow code
- inside one existing log group
- inside one deterministic filter pattern
- inside one foundation-scoped namespace
- outside Atlas and sovereign OS telemetry identifiers

It avoids skipping straight to alarms, dashboards, or cross-system telemetry
merging before the first metric proof exists.

## Review Conclusion

The correct controlled-review verdict is:

- `ready_for_patch`

Meaning:

- the future CloudWatch mutation is explicit
- the out-of-scope edges are explicit
- the next bounded mission should be the live metric-filter patch itself

## Preserved Boundaries

This mission preserved the required boundaries:

- `app.py` stayed unchanged
- `.github/workflows/public-runtime-smoke.yml` stayed unchanged
- `.github/workflows/deploy-foundation-skeleton.yml` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- no AWS mutation happened in this mission

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [aws/cloudwatch-service-telemetry-metric-filter-controlled-patch-review.template.json](./aws/cloudwatch-service-telemetry-metric-filter-controlled-patch-review.template.json)

That file records the exact allowed mutation, exact blocked mutation,
anti-collision boundary, and the next bounded mission.

## Recommended Next Mission

The next bounded step after this review should be:

- `CloudWatch Service Telemetry Metric Filter Patch v1`

That mission should create the one reviewed metric filter only, then verify
the filter exists without widening into alarms or other observability layers.

## Warning

Do not widen the first metric-filter patch beyond the reviewed CloudWatch
boundary.

The first goal is one foundation-scoped metric filter, not an Atlas merge or
a full observability stack.
