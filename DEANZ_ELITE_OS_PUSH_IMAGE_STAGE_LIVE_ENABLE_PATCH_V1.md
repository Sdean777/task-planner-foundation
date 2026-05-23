# Dean'z Elite OS Push Image Stage Live-Enable Patch v1

## Purpose

This document records the first bounded live-enable patch applied to the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions after the refreshed live-enable controlled
patch review:

- what exact first-job hunk was changed?
- what critical lines remained preserved?
- what bounded live behavior is now present in source?
- why do later jobs remain disabled and out of scope?

This document does not:

- enable `ecs-rollout-placeholder`
- enable `public-verification-placeholder`
- widen workflow-level permissions
- change the Flask application contract

## Scope

This live-enable patch applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the patched first-job live-enable hunk.

## Patch Objective

This patch exists to turn the first job into a bounded manual image-publication
path while preserving the rest of the deployment workflow as disabled.

The applied patch must remain:

- `live_enable_patch_applied`
- `live_enable_patch_first_job_only`
- `live_enable_patch_later_jobs_still_disabled`

## Applied Patch Footprint

The applied patch remains limited to the `push-image-placeholder` job.

The patch changed only:

- comments directly above `push-image-placeholder`
- the `if:` gate for that job
- a job-local `permissions` block for that job only
- job-local step ordering and step bodies inside that job

The patch did not change:

- workflow-level `permissions: contents: read`
- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- workflow trigger shape
- workflow service scope

## Preserved Required Lines

The patch preserved these critical workflow lines:

1. `push-image-placeholder`
2. `needs: activation-gate-summary`
3. workflow-level `permissions: contents: read`
4. manual-only `workflow_dispatch`
5. disabled `ecs-rollout-placeholder`
6. disabled `public-verification-placeholder`

## Added Bounded Live Behavior

The patch adds only the reviewed first-job behavior:

- a bounded `if:` gate requiring:
  - `refs/heads/main`
  - `target_environment == production`
  - `image_tag` shaped as `sha-<git-sha>` and not the literal placeholder
  - explicit non-secret AWS account and region variables
- a job-local `permissions` block:
  - `contents: read`
  - `id-token: write`
- a checkout step for local build context
- repo-scoped GitHub OIDC authentication using
  `aws-actions/configure-aws-credentials@v4`
- bounded ECR login via `aws ecr get-login-password` to
  `docker login --password-stdin`
- bounded Docker build for the foundation image
- immutable SHA tag push first
- optional `main` convenience mirror push second

These additions remain first-job-only and keep rollout truth subordinate to the
immutable SHA tag.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- any change to workflow-level permissions
- any change to `ecs-rollout-placeholder`
- any change to `public-verification-placeholder`
- any ECS rollout command
- any public runtime verification command
- any static AWS credential
- any `app.py` change

## Outcome

The result of this patch is intentionally narrow:

- the first job is now live-capable under bounded manual conditions
- workflow-level permissions remain unchanged
- later jobs are still disabled
- rollout identity still depends on immutable `sha-<git-sha>` truth
- release-gate and rollout doctrine remain downstream requirements

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/push-image-stage-live-enable-patch.template.json`](./.github/push-image-stage-live-enable-patch.template.json)

That file records the activation guard, added first-job behavior, preserved
lines, and still-forbidden actions for this patch.

## Source Boundary

Source may contain:

- the bounded first-job `if:` gate
- the bounded first-job `permissions` block
- the reviewed first-job auth, login, build, and push steps
- preserved-line summary

Source must not contain:

- later-job enablement
- workflow-level permission widening
- static AWS credentials
- application-code changes

## Governance Rules

- the live-enable patch must remain downstream of the refreshed controlled
  patch review
- later jobs must remain disabled
- immutable image identity must remain authoritative
- release-gate and rollout posture remain downstream checks, not bundled into
  this patch
- application code must remain untouched

## Explicit Non-Goals

This patch does not:

- enable ECS rollout
- enable public verification
- create AWS credentials
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md)
- [`.github/push-image-stage-live-enable-patch.template.json`](./.github/push-image-stage-live-enable-patch.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `First Bounded ECR Image Publication Run v1`

That mission should execute the now-bounded first-job path only after the
required repository variables and manual approvals are in place.

## Warning

Do not treat this patch as permission to widen deployment authority.

It only enables the first job under bounded manual conditions while preserving
later-job disablement and downstream rollout/release discipline.
