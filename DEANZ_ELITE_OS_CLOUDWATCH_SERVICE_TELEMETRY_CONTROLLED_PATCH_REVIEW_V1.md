# Dean'z Elite OS CloudWatch Service Telemetry Controlled Patch Review v1

## Purpose

This document records the bounded controlled-patch review for the first
explicit CloudWatch-backed service telemetry connection in
`task-planner-foundation`.

It exists to answer these questions:

- what exact `app.py` diff is in scope?
- what exact `app.py` diff is out of scope?
- how should structured service telemetry be emitted without changing the HTTP
  contract?
- what is the next exact bounded mission after this review?

This mission does not:

- change `app.py`
- change either workflow file
- add CloudWatch alarms, dashboards, filters, or subscriptions
- mutate AWS runtime state

## Scope

This controlled review applies to:

- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_BASELINE_REVIEW_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_BASELINE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_BASELINE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_CLOUDWATCH_SERVICE_TELEMETRY_BASELINE_PROPOSAL_V1.md)
- [`app.py`](./app.py)
- [`aws/cloudwatch-service-telemetry-controlled-patch-review.template.json`](./aws/cloudwatch-service-telemetry-controlled-patch-review.template.json)

It governs only the exact future `app.py` diff for the first service telemetry
connection patch.

## Review Objective

The objective of this mission was to inspect the exact code-shape boundary for
the first implementation patch so the repo can move from:

- logs-only CloudWatch baseline

to:

- explicit structured service-telemetry emission over the existing
  `stdout -> awslogs -> CloudWatch Logs` path

without widening scope.

## Exact Future Diff In Scope

The future patch is allowed to do only the following in `app.py`:

1. add one import:
   - `import json`
2. add one helper function:
   - `emit_service_telemetry_snapshot(payload)`
3. build the current `/telemetry` response into a local variable
4. derive one compact telemetry event from that response
5. emit the telemetry event with:
   - `print(json.dumps(event), flush=True)`
6. return the unchanged `/telemetry` response

That is the full allowed future patch boundary.

## Exact Future Diff Out Of Scope

The future patch must not:

- change any endpoint path
- change the `/telemetry` response keys
- change the `/telemetry` response values
- emit telemetry from endpoints other than `/telemetry`
- add CloudWatch API calls
- add alarms, filters, subscriptions, dashboards, or traces
- change workflow files
- change deployment configuration

This review keeps the first patch intentionally tiny.

## Controlled Event Shape

The future helper should emit one compact event with exactly these fields:

- `eventType`
  - `service_telemetry_snapshot`
- `service`
  - `task-planner-foundation`
- `runtime`
  - from the current telemetry response
- `infrastructure`
  - from the current telemetry response
- `phase`
  - from the current telemetry response
- `status`
  - from the current telemetry response
- `taskCount`
  - from the current telemetry response
- `agentStatus`
  - from the current telemetry response
- `activeEndpointCount`
  - `len(active_endpoints)`
- `sourceEndpoint`
  - `/telemetry`

The event should remain compact and deterministic.

## Preferred Future Implementation Shape

The future patch should prefer this code shape:

1. derive `identity = runtime_identity()`
2. create `telemetry_response = {...}`
3. call `emit_service_telemetry_snapshot(telemetry_response)`
4. `return telemetry_response`

The helper should transform the response into the compact event rather than
duplicate runtime/state logic independently.

That keeps the HTTP response and the CloudWatch event anchored to the same
source truth.

## Why This Controlled Boundary Is Correct

This review keeps the first telemetry patch:

- inside one file
- inside one endpoint path
- on the existing stdout logging channel
- compatible with the current smoke workflow
- compatible with the current public release gate

It avoids skipping straight to a larger observability system before the first
structured telemetry proof exists.

## Review Conclusion

The correct controlled-review verdict is:

- `ready_for_patch`

Meaning:

- the future `app.py` diff is explicit
- the out-of-scope edges are explicit
- the next bounded mission should be the implementation patch itself

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

- [`aws/cloudwatch-service-telemetry-controlled-patch-review.template.json`](./aws/cloudwatch-service-telemetry-controlled-patch-review.template.json)

That file records the exact allowed diff, exact blocked diff, the event shape,
and the next bounded mission.

## Recommended Next Mission

The next bounded step after this review should be:

- `CloudWatch Service Telemetry Patch v1`

That mission should implement the reviewed `app.py` diff only, then verify the
service still satisfies the existing smoke and release-gate contract while
CloudWatch receives explicit structured service telemetry.

## Warning

Do not widen the first telemetry patch beyond the reviewed `app.py` boundary.

The first goal is explicit structured service telemetry in CloudWatch, not full
observability expansion.
