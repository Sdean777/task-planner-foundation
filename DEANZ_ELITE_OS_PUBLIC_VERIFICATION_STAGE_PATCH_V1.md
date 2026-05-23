# Dean'z Elite OS Public Verification Stage Patch v1

## Purpose

This document records the first bounded live patch applied to the
`public-verification-placeholder` job inside the
`task-planner-foundation` deployment workflow skeleton.

It exists to answer these questions after the public-verification controlled
patch review:

- what exact third-job hunk was changed?
- what critical lines remained preserved?
- what bounded live verification behavior is now present in source?
- why do push-image and rollout behavior remain unchanged and upstream?

This document does not:

- change `push-image-placeholder`
- change `ecs-rollout-placeholder`
- change the Flask application contract

## Scope

This public-verification patch applies to:

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the patched third-job public-verification hunk.

## Patch Objective

This patch exists to turn the third job into a bounded manual public-runtime
verification path while preserving upstream push-image and rollout behavior.

The applied patch must remain:

- `public_verification_stage_patch_applied`
- `public_verification_stage_patch_third_job_only`
- `public_verification_stage_patch_upstream_jobs_unchanged`

## Applied Patch Footprint

The applied patch remains limited to the `public-verification-placeholder` job.

The patch changed only:

- comments directly above `public-verification-placeholder`
- the `if:` gate for that job
- job-local step ordering and step bodies inside that job

The patch did not change:

- `push-image-placeholder`
- `ecs-rollout-placeholder`
- workflow trigger shape
- workflow service scope
- workflow-level permissions

## Preserved Required Lines

The patch preserved these critical workflow lines:

1. `public-verification-placeholder`
2. `needs: ecs-rollout-placeholder`
3. workflow-level `permissions: contents: read`
4. manual-only `workflow_dispatch`
5. `push-image-placeholder` behavior unchanged
6. `ecs-rollout-placeholder` behavior unchanged

## Added Bounded Live Behavior

The patch adds only the reviewed third-job behavior:

- a bounded `if:` gate requiring:
  - `refs/heads/main`
  - `target_environment == production`
  - `image_tag` shaped as `sha-<git-sha>` and not the literal placeholder
  - explicit non-secret `FOUNDATION_PUBLIC_BASE_URL`
- a release-gate posture step describing bounded outcomes
- derivation of a trailing-slash-safe `PUBLIC_BASE_URL`
- bounded blocking verification for:
  - `/health`
  - `/status`
  - `/validate`
  - `/orchestrate`
- bounded warning-bearing verification for `/telemetry`
- bounded outcome summary:
  - `keep_active`
  - `manual_review_required`
  - `rollback_required`

These additions remain third-job-only and keep public verification subordinate
to manual review and rollback posture.

## Prohibited Content That Remains Absent

The applied patch still does not contain:

- any change to workflow-level permissions
- any change to `push-image-placeholder`
- any change to `ecs-rollout-placeholder`
- any hardcoded production endpoint URL
- any application-code change
- any static AWS credential

## Outcome

The result of this patch is intentionally narrow:

- the third job is now live-capable under bounded manual conditions
- `push-image-placeholder` remains the upstream image publisher
- `ecs-rollout-placeholder` remains the upstream rollout path
- public verification identity now depends on non-secret
  `FOUNDATION_PUBLIC_BASE_URL` rather than committed endpoint literals
- release-gate posture remains explicit through ordered blocking and
  warning-bearing checks

## Canonical Planning Artifact

The non-secret planning artifact for this patch is:

- [`.github/public-verification-stage-patch.template.json`](./.github/public-verification-stage-patch.template.json)

That file records the activation guard, added third-job behavior, preserved
lines, and still-forbidden actions for this patch.

## Source Boundary

Source may contain:

- the bounded third-job `if:` gate
- the reviewed third-job verification steps
- the non-secret `FOUNDATION_PUBLIC_BASE_URL` boundary
- preserved-line summary

Source must not contain:

- workflow-level permission widening
- committed production endpoint URLs
- static AWS credentials
- application-code changes

## Governance Rules

- the public-verification stage patch must remain downstream of the
  public-verification controlled patch review
- push-image and rollout jobs must remain unchanged
- release-gate order must remain visible
- rollback posture and manual review outcomes must remain explicit
- application code must remain untouched

## Explicit Non-Goals

This patch does not:

- change push-image behavior
- change rollout behavior
- create AWS credentials
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/public-verification-stage-patch.template.json`](./.github/public-verification-stage-patch.template.json)

## Recommended Next Mission

The next bounded step after this patch should be:

- `First Bounded Public Verification Run v1`

That mission should execute the now-bounded third-job path only after a stable
non-secret `FOUNDATION_PUBLIC_BASE_URL` is established.

## Warning

Do not treat this patch as permission to widen runtime verification authority.

It only enables the third job under bounded manual conditions while preserving
upstream push-image and rollout behavior.
