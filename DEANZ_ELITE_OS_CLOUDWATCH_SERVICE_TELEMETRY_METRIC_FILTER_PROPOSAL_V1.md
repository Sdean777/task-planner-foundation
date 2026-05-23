# Dean'z Elite OS CloudWatch Service Telemetry Metric Filter Proposal v1

## Purpose

This document records the bounded proposal for the first CloudWatch
metric-filter layer over the existing `service_telemetry_snapshot` event in
`task-planner-foundation`.

It exists to answer these questions:

- what is the minimum non-duplicative metric-filter shape?
- how should the repo convert the current structured-log baseline into a first
  CloudWatch metric without widening runtime or workflow authority?
- how do we avoid semantic collision with Atlas and other sovereign OS
  telemetry surfaces?
- what is the next exact bounded mission after this proposal?

This mission does not:

- change `app.py`
- change either workflow file
- create a CloudWatch metric filter
- create a CloudWatch alarm
- mutate AWS runtime state

## Scope

This proposal applies to:

- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_BASELINE_REVIEW_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_BASELINE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_PATCH_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_PATCH_V1.md)
- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_SOURCE_PUBLICATION_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_SOURCE_PUBLICATION_V1.md)
- [aws/cloudwatch-service-telemetry-metric-filter-proposal.template.json](./aws/cloudwatch-service-telemetry-metric-filter-proposal.template.json)

It governs only the minimum first CloudWatch metric-filter shape for the
foundation service telemetry event already present in the live log stream.

## Proposal Objective

The objective of this mission was to define the smallest future CloudWatch
mutation that would make this statement true without overreaching:

- the structured service-telemetry event is now queryable as a deterministic
  CloudWatch metric

The baseline review already proved:

- the service is steady on `task-planner-foundation:3`
- the `service_telemetry_snapshot` event is present in the live log stream
- no metric filters exist yet
- no service alarms exist yet

So the missing layer is not more runtime code. It is one explicit
metric-filter transform over the event that already exists.

## Proposed Minimum Shape

The first metric-filter layer should stay narrow:

1. preserve the current `app.py` event shape exactly
2. preserve the current log group
3. add one CloudWatch metric filter only
4. count only `service_telemetry_snapshot` occurrences
5. defer alarms, dashboards, subscriptions, and retention changes

In plain terms:

- do not modify runtime emission again
- do not introduce a second log event family
- do not introduce Atlas or sovereign OS identifiers into this service layer
- only add one deterministic count metric over the existing event

## Proposed Metric Filter Shape

The first metric filter should be bounded to:

- log group:
  - `/deanz-elite/task-planner-foundation`
- filter pattern:
  - `{ $.eventType = "service_telemetry_snapshot" }`
- metric namespace:
  - `DeanzElite/Foundation`
- metric name:
  - `ServiceTelemetrySnapshotCount`
- metric value:
  - `1`

This is enough to turn the structured event into a simple metric signal without
creating a broader observability system.

## Anti-Collision Boundary

This proposal must remain explicitly separate from Atlas and sovereign OS
telemetry semantics.

That means the first metric filter must not:

- use `atlas` in the metric namespace
- use `runtimeTelemetry`, `atlasService`, `confidenceTelemetry`,
  `authorizationTelemetry`, `operatorSessionTelemetry`,
  `remoteRuntimeTelemetry`, `distributedCoordinationTelemetry`,
  `sandboxGovernanceTelemetry`, `promotionGovernanceTelemetry`,
  `failoverGovernanceTelemetry`, or `scopedMemoryTelemetry` as metric names
- claim Brain, Atlas, validator, memory, or governance authority
- imply that this foundation service is a sovereign OS telemetry surface

The proposal is intentionally foundation-scoped:

- service domain = `task-planner-foundation`
- metric domain = `DeanzElite/Foundation`
- event source = `/telemetry`

That keeps the CloudWatch metric layer operationally useful without creating an
Atlas namespace collision.

## Why This Proposal Is Minimal And Correct

This proposal uses the smallest possible new surface:

- the event already exists
- the log path already exists
- the service contract is already stable
- the log group is already live

So the first metric-filter layer does not need:

- new event fields
- runtime code changes
- log subscription filters
- alarms
- dashboards
- traces
- cross-repo namespace merging

Those can remain future missions if needed.

## Explicitly Out Of Scope

The following remain out of scope for the first metric-filter mutation:

- any `app.py` change
- any workflow change
- CloudWatch alarms
- CloudWatch dashboards
- CloudWatch subscriptions
- retention-policy mutation
- Atlas namespace reuse
- sovereign OS telemetry consolidation

This proposal is about one foundation-local metric-filter layer only.

## Proposal Conclusion

The correct proposal verdict is:

- `ready_for_controlled_patch_review`

Meaning:

- the baseline review is complete
- the minimum first metric-filter shape is defined
- the next step should inspect the exact future CloudWatch mutation boundary
  before any live metric-filter creation is allowed

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

- [aws/cloudwatch-service-telemetry-metric-filter-proposal.template.json](./aws/cloudwatch-service-telemetry-metric-filter-proposal.template.json)

That file records the exact proposed metric-filter shape, the anti-collision
boundary, deferred items, and the next bounded mission.

## Recommended Next Mission

The next bounded step after this proposal should be:

- `CloudWatch Service Telemetry Metric Filter Controlled Patch Review v1`

That mission should inspect the exact future CloudWatch metric-filter mutation
boundary before any live AWS metric-filter creation is allowed.

## Warning

Do not jump from this proposal straight to alarms or sovereign telemetry
convergence.

The first goal is only one foundation-scoped metric filter over the existing
`service_telemetry_snapshot` event.
