# Dean'z Elite OS CloudWatch Service Telemetry Alarm Proposal v1

## Purpose

This document records the bounded proposal for the first CloudWatch alarm
layer over the foundation-scoped `ServiceTelemetrySnapshotCount` metric in
`task-planner-foundation`.

It exists to answer these questions:

- what is the minimum non-duplicative first alarm shape?
- how should the repo add an alarm boundary without widening runtime,
  workflow, or Atlas authority?
- how should the first proposal handle sparse signal cadence and missing data?
- what is the next exact bounded mission after this proposal?

This mission does not:

- change `app.py`
- change either workflow file
- create a CloudWatch alarm
- change the metric filter
- mutate AWS runtime state

## Scope

This proposal applies to:

- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_ALARM_BASELINE_REVIEW_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_ALARM_BASELINE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_PATCH_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_PATCH_V1.md)
- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_SOURCE_PUBLICATION_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_METRIC_FILTER_SOURCE_PUBLICATION_V1.md)
- [aws/cloudwatch-service-telemetry-alarm-proposal.template.json](./aws/cloudwatch-service-telemetry-alarm-proposal.template.json)

It governs only the minimum first CloudWatch alarm shape for the existing
foundation-scoped metric already visible in CloudWatch.

## Proposal Objective

The objective of this mission was to define the smallest future CloudWatch
mutation that would make this statement true without overreaching:

- the foundation telemetry metric now has an explicit alarm object boundary

The baseline review already proved:

- the service is steady on `task-planner-foundation:3`
- the foundation metric is visible in `DeanzElite/Foundation`
- no alarm layer exists yet
- the datapoint history is present but sparse

So the missing layer is not more runtime code and not another metric. It is
one explicit, low-risk alarm shape over the metric that already exists.

## Proposed Minimum Shape

The first alarm layer should stay narrow:

1. preserve the current `app.py` event shape exactly
2. preserve the current metric filter exactly
3. add one CloudWatch metric alarm only
4. keep the alarm foundation-scoped and non-Atlas
5. keep the alarm non-paging and missing-data aware
6. defer SNS actions, composite alarms, dashboards, and workflow wiring

In plain terms:

- do not modify runtime emission again
- do not introduce a second metric family
- do not introduce Atlas or sovereign OS identifiers into this service layer
- only define one bounded review-oriented alarm object over the existing
  foundation metric

## Proposed Alarm Shape

The first alarm should be bounded to:

- alarm name:
  - `task-planner-foundation-service-telemetry-snapshot-low-activity`
- namespace:
  - `DeanzElite/Foundation`
- metric name:
  - `ServiceTelemetrySnapshotCount`
- statistic:
  - `Sum`
- period:
  - `86400`
- evaluation periods:
  - `1`
- datapoints to alarm:
  - `1`
- threshold:
  - `1`
- comparison operator:
  - `LessThanThreshold`
- treat missing data:
  - `missing`
- actions enabled:
  - `false`

This keeps the first alarm object explicit while also acknowledging that the
signal cadence is still low-volume and not yet suitable for paging or automated
action.

## Sparse-Signal Safety Posture

The baseline review made one important fact explicit:

- the metric currently has only a sparse datapoint history

So the first alarm proposal must stay conservative:

- use `treatMissingData = missing`
- disable alarm actions
- defer SNS topics, ECS actions, scaling actions, and rollback actions
- treat the first alarm as visibility and review posture only

This prevents the repo from pretending it already has a mature periodic signal
when it does not.

## Anti-Collision Boundary

This proposal must remain explicitly separate from Atlas and sovereign OS
telemetry semantics.

That means the first alarm must not:

- use `atlas` in the alarm name
- use `brain`, `validator`, `memory`, or `governance` in the alarm name
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
- alarm domain = `task-planner-foundation-*`

That keeps the first alarm operationally useful without creating an Atlas
namespace collision.

## Why This Proposal Is Minimal And Correct

This proposal uses the smallest possible new surface:

- the structured event already exists
- the metric filter already exists
- the metric already exists
- the service contract is already stable

So the first alarm layer does not need:

- new runtime code
- new log events
- new metrics
- SNS actions
- composite alarms
- dashboards
- workflow changes
- cross-repo namespace merging

Those can remain future missions if needed.

## Explicitly Out Of Scope

The following remain out of scope for the first alarm mutation:

- any `app.py` change
- any workflow change
- any metric-filter change
- SNS topics or alarm actions
- composite alarms
- CloudWatch dashboards
- CloudWatch subscriptions
- retention-policy mutation
- Atlas namespace reuse
- sovereign OS telemetry consolidation

This proposal is about one foundation-local, non-paging alarm shape only.

## Proposal Conclusion

The correct proposal verdict is:

- `ready_for_controlled_patch_review`

Meaning:

- the alarm baseline review is complete
- the minimum first alarm shape is defined
- the next step should inspect the exact future CloudWatch alarm mutation
  boundary before any live alarm creation is allowed

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

- [aws/cloudwatch-service-telemetry-alarm-proposal.template.json](./aws/cloudwatch-service-telemetry-alarm-proposal.template.json)

That file records the exact proposed alarm shape, the sparse-signal safety
posture, the anti-collision boundary, deferred items, and the next bounded
mission.

## Recommended Next Mission

The next bounded step after this proposal should be:

- `CloudWatch Service Telemetry Alarm Controlled Patch Review v1`

That mission should inspect the exact future CloudWatch alarm mutation
boundary before any live AWS alarm creation is allowed.

## Warning

Do not jump from this proposal straight into live alarm creation.

The first goal is only one foundation-scoped, missing-data-aware,
actions-disabled alarm shape over the existing foundation metric.
