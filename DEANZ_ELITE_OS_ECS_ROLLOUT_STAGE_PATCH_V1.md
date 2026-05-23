# Dean'z Elite OS ECS Rollout Stage Patch v1

## Purpose

This document records the first bounded live patch applied to the
`ecs-rollout-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after the rollout-stage controlled patch
review:

- what exact second-job hunk was changed?
- what critical lines remained preserved?
- what bounded live rollout behavior is now present in source?
- why does public verification remain disabled and out of scope?

This document does not:

- enable `public-verification-placeholder`
- change `push-image-placeholder`
- change the Flask application contract

## Scope

This rollout-stage patch applies to:

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the patched second-job rollout hunk.

## Patch Objective

This patch exists to turn the second job into a bounded manual ECS rollout
path while preserving the public verification stage as disabled.

The applied patch must remain:

- `rollout_stage_patch_applied`
- `rollout_stage_patch_second_job_only`
- `rollout_stage_patch_public_verification_still_disabled`

## Applied Patch Footprint

The applied patch remains limited to the `ecs-rollout-placeholder` job.

The patch changed only:

- comments directly above `ecs-rollout-placeholder`
- the `if:` gate for that job
- a job-local `permissions` block for that job only
- job-local step ordering and step bodies inside that job

The patch did not change:

- `push-image-placeholder`
- `public-verification-placeholder`
- workflow trigger shape
- workflow service scope
- workflow-level permissions

## Preserved Required Lines

The patch preserved these critical workflow lines:

1. `ecs-rollout-placeholder`
2. `needs: push-image-placeholder`
3. workflow-level `permissions: contents: read`
4. manual-only `workflow_dispatch`
5. `public-verification-placeholder` still disabled
6. `push-image-placeholder` behavior unchanged

## Added Bounded Live Behavior

The patch adds only the reviewed second-job behavior:

- a bounded `if:` gate requiring:
  - `refs/heads/main`
  - `target_environment == production`
  - `image_tag` shaped as `sha-<git-sha>` and not the literal placeholder
  - explicit non-secret AWS account, region, cluster, and service variables
- a job-local `permissions` block:
  - `contents: read`
  - `id-token: write`
- a checkout step for local task-definition template access
- repo-scoped GitHub OIDC authentication using
  `aws-actions/configure-aws-credentials@v4`
- bounded ECR confirmation for the immutable rollout image input
- bounded rendering of the ECS task definition candidate from the committed
  template
- capture of the previous task-definition revision for rollback posture
- bounded task-definition registration
- bounded ECS service update to the newly registered revision

These additions remain second-job-only and keep public verification outside the
current patch.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- any change to workflow-level permissions
- any change to `push-image-placeholder`
- any change to `public-verification-placeholder`
- any public runtime smoke-test command
- any application-code change
- any static AWS credential

## Outcome

The result of this patch is intentionally narrow:

- the second job is now live-capable under bounded manual conditions
- `push-image-placeholder` remains unchanged as the upstream image publisher
- `public-verification-placeholder` remains disabled
- rollout identity still depends on immutable `sha-<git-sha>` image truth
- release-gate posture remains downstream

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/ecs-rollout-stage-patch.template.json`](./.github/ecs-rollout-stage-patch.template.json)

That file records the activation guard, added second-job behavior, preserved
lines, and still-forbidden actions for this patch.

## Source Boundary

Source may contain:

- the bounded second-job `if:` gate
- the bounded second-job `permissions` block
- the reviewed second-job auth, confirmation, task-definition, and service
  update steps
- preserved-line summary

Source must not contain:

- public-verification enablement
- workflow-level permission widening
- static AWS credentials
- application-code changes

## Governance Rules

- the rollout-stage patch must remain downstream of the rollout-stage
  controlled patch review
- `public-verification-placeholder` must remain disabled
- immutable image truth must remain authoritative for rollout input
- rollback posture must remain visible through the previous revision capture
- application code must remain untouched

## Explicit Non-Goals

This patch does not:

- enable public verification
- change push-image behavior
- create AWS credentials
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/ecs-rollout-stage-patch.template.json`](./.github/ecs-rollout-stage-patch.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `First Bounded ECS Rollout Run v1`

That mission should execute the now-bounded second-job path only after the
required repository variables and manual approvals are in place.

## Warning

Do not treat this patch as permission to widen deployment authority.

It only enables the second job under bounded manual conditions while
preserving push-image behavior and downstream public-verification disablement.
