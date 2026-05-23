# Dean'z Elite OS Public Runtime Verification & Release Gate Contract v1

## Purpose

This document defines the first bounded public-runtime verification and release
gate contract for the `task-planner-foundation` AWS path.

It exists to answer these questions once a bounded revision becomes reachable
through the staged foundation chain:

- which public/runtime checks must pass after a new revision becomes reachable?
- which failures should block release or force rollback?
- which signals are informational versus release-critical?
- who decides whether a revision stays active?

This document does not:

- deploy anything
- create a release workflow
- create a monitoring system
- change the Flask application contract

## Scope

This contract applies to the current foundation rollout-planning chain:

- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)

It does not by itself widen the current bounded foundation runtime authority.

## Gate Objective

The first release gate exists to determine whether a new runtime revision:

- stays active
- requires manual review before acceptance
- must roll back to the previous known-good revision

The gate must stay deterministic and narrow for the foundation service.

## Verification Order

The first public/runtime verification order should be:

1. ECS service stability
2. target group health
3. CloudWatch log visibility
4. public/runtime endpoint verification
5. release decision

That sequence keeps infrastructure truth ahead of application-level acceptance.

## Verification Surfaces

### 1. Infrastructure Health Gate

Required:

- ECS task reaches stable running posture
- target group reports healthy target
- CloudWatch logs are present for the new revision

These are blocking conditions.

### 2. Public Health Path

Endpoint:

- `/health`

Expectation:

- HTTP `200`
- lightweight health response

This is release-blocking.

### 3. Status And Identity Path

Endpoint:

- `/status`

Expectation:

- HTTP `200`
- response still identifies the foundation service correctly

This is release-blocking because wrong identity implies the wrong runtime may
be active.

### 4. Validation Path

Endpoint:

- `/validate`

Expectation:

- HTTP `200`
- validator-first runtime checks still pass

This is release-blocking.

### 5. Orchestration Path

Endpoint:

- `/orchestrate`

Expectation:

- HTTP `200`
- ordered orchestration readiness contract still resolves

This is release-blocking.

### 6. Telemetry Path

Endpoint:

- `/telemetry`

Expectation:

- HTTP `200` if present and stable

For the first gate, `/telemetry` is warning-bearing, not release-blocking,
because CloudWatch log presence remains the primary observability requirement.

## Gate Decision Classes

The first gate should allow only three outcomes:

### 1. `keep_active`

Allowed when:

- infrastructure checks pass
- `/health` passes
- `/status` passes
- `/validate` passes
- `/orchestrate` passes

### 2. `manual_review_required`

Allowed when:

- release-blocking checks pass
- one or more warning-bearing checks degrade
- operator review is still required before calling the release fully healthy

### 3. `rollback_required`

Required when:

- any release-blocking check fails
- the new revision cannot be trusted as the active runtime

## Release-Blocking Criteria

The first gate must block or roll back if any of these occur:

- ECS service fails to stabilize
- target group health fails
- CloudWatch logs for the new revision are absent
- `/health` does not return `200`
- `/status` does not return `200`
- `/validate` does not return `200`
- `/orchestrate` does not return `200`
- the active runtime identity no longer matches the foundation service

## Warning-Bearing Criteria

The first gate may require manual review, but not immediate rollback, if:

- `/telemetry` is degraded while all release-blocking checks pass
- response shape drift appears non-critical but still needs operator inspection

These warnings must not silently pass as success.

## Rollback Decision Rule

The release gate must not invent rollback targets.

If rollback is required, the gate should reference:

- the previous known-good task-definition revision
- the previous immutable image reference

If those are not identifiable, the rollout should be considered unsafe.

## Source Boundary

Source may contain:

- verification order
- release-gate rules
- endpoint expectations
- placeholder release-gate metadata

Source must not contain:

- production endpoint URLs
- live rollout history from a real account
- automated deploy logic in this mission

## Canonical Planning Artifact

The non-secret release-gate planning artifact is:

- [aws/public-runtime-verification-release-gate.template.json](./aws/public-runtime-verification-release-gate.template.json)

That file is a planning artifact only.

It is not a live release manifest and not an automated deployment gate.

## Next Bounded Review Layer

The next bounded review layer after this contract and the ECS baseline standup
is:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/public-verification-stage-candidate-review.template.json`](./.github/public-verification-stage-candidate-review.template.json)

That layer must still remain review-only and must not enable live public smoke
tests or mutate runtime routing.

## Governance Rules

- public verification must remain downstream of rollout identity
- release acceptance must remain separate from image promotion
- rollback must stay revision-based
- warning-only signals must never be mistaken for full success

## Explicit Non-Goals

This contract does not:

- create a deploy workflow
- create a smoke-test pipeline
- update an ECS service
- create real monitoring alarms
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [aws/public-runtime-verification-release-gate.template.json](./aws/public-runtime-verification-release-gate.template.json)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [aws/deployment-workflow-activation-gate.template.json](./aws/deployment-workflow-activation-gate.template.json)

## Current Bounded Chain

This release gate now feeds the current public-verification workflow chain:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_PATCH_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_VERIFICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_VERIFICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_ROUTING_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_PUBLIC_ROUTING_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_SECOND_BOUNDED_PUBLIC_VERIFICATION_RUN_V1.md](./DEANZ_ELITE_OS_SECOND_BOUNDED_PUBLIC_VERIFICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_TELEMETRY_RUNTIME_IDENTITY_ALIGNMENT_V1.md](./DEANZ_ELITE_OS_TELEMETRY_RUNTIME_IDENTITY_ALIGNMENT_V1.md)
- [DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md](./DEANZ_ELITE_OS_POST_DEPLOY_PUBLIC_RUNTIME_SMOKE_TESTS_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PATCH_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_PROPOSAL_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_CONTROLLED_RUN_REVIEW_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_CONTROLLED_RUN_REVIEW_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_RUN_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_SOURCE_PUBLICATION_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_SOURCE_PUBLICATION_V1.md)

The next bounded step after that chain should be:

- `Second Bounded GitHub-Hosted Public Runtime Smoke Workflow Dispatch Run v1`

## Warning

Do not start live AWS deployment from this contract alone.

This is still a bounded planning artifact for a foundation service.
