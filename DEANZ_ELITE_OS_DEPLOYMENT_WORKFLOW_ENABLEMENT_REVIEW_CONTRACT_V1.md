# Dean'z Elite OS Deployment Workflow Enablement Review Contract v1

## Purpose

This document defines the first bounded review contract for gradual enablement
of the disabled jobs inside the `task-planner-foundation` deployment workflow
skeleton.

It exists to answer these questions before any job is turned on:

- which disabled job may be reviewed first?
- what evidence must already exist before that job is even reviewable?
- how does enablement remain one stage at a time?
- what is still forbidden during review?

This document does not:

- enable any workflow job
- add AWS credentials
- create AWS trust
- change the Flask application contract

## Scope

This contract applies to:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only review posture for future job enablement.

## Review Objective

The enablement review exists to decide whether a disabled job remains:

- `enablement_blocked`
- `enablement_review_required`
- `single_job_enablement_candidate_allowed`

This is a review contract, not a job-enable action.

## Candidate Jobs

The current skeleton contains three disabled deployment-bearing jobs:

- `push-image-placeholder`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`

These jobs must not be enabled all at once.

## Enablement Order

The first review order must remain sequential:

1. `push-image-placeholder`
2. `ecs-rollout-placeholder`
3. `public-verification-placeholder`

No later stage may be reviewed for enablement ahead of an earlier stage unless a
separate doctrine mission explicitly changes the order.

## Job-Specific Review Evidence

### 1. `push-image-placeholder`

Before this job may become a candidate for enablement, the following must
already exist:

- GitHub OIDC deployment trust contract
- ECR image promotion contract
- deployment workflow activation gate
- protected deployment environment and approval contract
- clean secrets posture

This is the narrowest first job because it still stops short of changing live
runtime state.

### 2. `ecs-rollout-placeholder`

Before this job may become a candidate for enablement, the following must
already exist:

- all `push-image-placeholder` evidence
- ECS runtime contract
- ECS service runbook
- ECS parameter/environment contract
- ECS identity/access boundary
- explicit rollback-to-previous-revision posture

### 3. `public-verification-placeholder`

Before this job may become a candidate for enablement, the following must
already exist:

- all `ecs-rollout-placeholder` evidence
- public runtime verification and release-gate contract
- clear blocking and rollback outcomes for the new revision

## Single-Job Rule

Only one disabled job may be treated as an enablement candidate in a single
future mission.

That means:

- no combined `push-image + ecs-rollout` enablement
- no combined `ecs-rollout + public verification` enablement
- no all-at-once activation

The first enabled stage, if it ever happens, must remain narrow enough to
observe and reverse.

## Review Outcomes

### 1. `enablement_blocked`

Required when:

- prerequisite contracts are missing
- secrets posture is unsafe
- protected environment posture is missing
- the candidate job would widen authority too early

### 2. `enablement_review_required`

Allowed when:

- prerequisites mostly exist
- evidence needs operator review
- the job is still not ready to be enabled

### 3. `single_job_enablement_candidate_allowed`

Allowed when:

- all review evidence for one specific job exists
- activation gate and protected environment boundary are satisfied
- the candidate remains service-scoped and reversible

This outcome still does not enable the job. It only allows a later mission to
propose enabling that single job.

## Still-Forbidden Actions

Even after `single_job_enablement_candidate_allowed`, the following remain
forbidden in this mission:

- enabling more than one disabled job
- bundling application changes with job enablement
- adding AWS credentials or secrets
- bypassing protected environment review
- bypassing rollback and release-gate posture

## Canonical Planning Artifact

The non-secret planning artifact for this contract is:

- [`.github/deployment-workflow-enablement-review.template.json`](./.github/deployment-workflow-enablement-review.template.json)

That file is a planning artifact only.

It is not an approval system and not a workflow control plane.

## Source Boundary

Source may contain:

- candidate job names
- review order
- evidence categories
- blocked/reviewable/candidate outcomes

Source must not contain:

- live approval tokens
- production credentials
- hidden enablement flags

## Governance Rules

- enablement review must remain downstream of the activation gate
- enablement review must remain downstream of the protected environment contract
- one-job enablement must remain narrower than deployment execution
- later-stage jobs must remain blocked until earlier-stage review is satisfied

## Explicit Non-Goals

This contract does not:

- enable any workflow job
- create live approvals
- create AWS trust
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [`.github/deployment-workflow-enablement-review.template.json`](./.github/deployment-workflow-enablement-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/push-image-stage-candidate-review.template.json`](./.github/push-image-stage-candidate-review.template.json)

## Follow-On Review

This enablement review now pairs with the first single-job candidate review:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [`.github/push-image-stage-candidate-review.template.json`](./.github/push-image-stage-candidate-review.template.json)

The next non-deploying AWS step after that should be:

- `Push Image Stage Enablement Proposal v1`

## Warning

Do not treat this contract as permission to enable jobs.

It only defines the review boundary for gradual enablement.
