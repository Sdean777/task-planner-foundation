# Dean'z Elite OS Push Image Stage Enablement Proposal v1

## Purpose

This document defines the first bounded proposal for how the
`push-image-placeholder` job could be changed in a later mission without
advancing any later-stage deployment jobs.

It exists to answer these questions before any patch is applied:

- what is the exact minimal diff shape for the first job?
- what must remain unchanged while that job is proposed?
- what approvals and evidence must be rechecked immediately before a patch?

This document does not:

- enable the `push-image-placeholder` job
- add AWS authentication
- push an image to ECR
- change the Flask application contract

## Scope

This proposal applies only to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact proposal shape for the first disabled job.

## Proposal Objective

The proposal exists to define whether `push-image-placeholder` is:

- `proposal_blocked`
- `proposal_review_required`
- `proposal_ready_for_patch_mission`

This is still not a patch or an enablement action.

## Minimal Diff Shape

The first enablement proposal for `push-image-placeholder` must remain narrow.

Allowed proposed diff shape:

1. change only the `push-image-placeholder` job
2. keep `ecs-rollout-placeholder` disabled
3. keep `public-verification-placeholder` disabled
4. keep the workflow trigger as `workflow_dispatch` only
5. keep the workflow service-scoped to `task-planner-foundation`

Any proposal that widens beyond that is out of scope.

## Proposed Patch Boundaries

If a later patch mission is attempted, the proposal should allow only:

- revisiting the `if: ${{ false }}` gate for `push-image-placeholder`
- explicit comments describing the still-disabled nature of later jobs
- explicit environment reference to the protected environment posture, if later required
- narrow permissions review for the specific job

The proposal must not assume:

- ECS rollout changes
- public verification changes
- any application-code changes

## Commands That Must Remain Placeholder-Bound

Even in the proposed patch shape, these commands must remain placeholder-only
until a later mission explicitly authorizes them:

- AWS authentication configuration
- ECR login
- `docker push`
- any command that mutates AWS state

That means the first proposed patch may still contain only:

- comments
- echoed intent
- future command placeholders

not live state-changing commands.

## Recheck Evidence Before Any Patch Mission

Immediately before a future patch mission is allowed to start, these must be
rechecked:

- candidate review still allows `push-image-placeholder`
- protected environment posture still matches `production` / `main`
- GitHub OIDC trust boundary still matches the repo and branch posture
- immutable tag rule still requires `sha-<git-sha>`
- secrets posture is still clean
- later jobs remain disabled

## Proposal Outcomes

### 1. `proposal_blocked`

Required when:

- the proposed diff touches more than `push-image-placeholder`
- any later-stage job changes
- live AWS commands are introduced
- secrets posture is unsafe

### 2. `proposal_review_required`

Allowed when:

- the diff is narrow enough
- the job remains conceptually first in the sequence
- operator review is still required before any patch mission

### 3. `proposal_ready_for_patch_mission`

Allowed when:

- the proposed diff is limited to the first job
- later jobs remain disabled
- placeholder-bound commands are preserved
- all recheck evidence remains satisfied

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `proposal_ready_for_patch_mission`, the following remain forbidden
in this mission:

- modifying `ecs-rollout-placeholder`
- modifying `public-verification-placeholder`
- enabling any job
- adding `aws-actions/configure-aws-credentials`
- adding `docker push`
- adding any real AWS mutating command

## Canonical Planning Artifact

The non-secret planning artifact for this proposal is:

- [`.github/push-image-stage-enablement-proposal.template.json`](./.github/push-image-stage-enablement-proposal.template.json)

That file is a planning artifact only.

It is not a patch and not a workflow control plane.

## Source Boundary

Source may contain:

- proposed diff scope
- recheck evidence
- blocked/review/proposal-ready outcomes
- explicit forbidden actions

Source must not contain:

- live patch commands that mutate AWS
- credentials
- hidden enablement flags

## Governance Rules

- the proposal must remain narrower than the candidate review
- the proposal must remain narrower than actual job enablement
- later jobs must stay blocked
- application code must remain untouched

## Explicit Non-Goals

This contract does not:

- patch the workflow
- enable a job
- create AWS trust
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [`.github/push-image-stage-enablement-proposal.template.json`](./.github/push-image-stage-enablement-proposal.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/push-image-stage-controlled-patch-review.template.json`](./.github/push-image-stage-controlled-patch-review.template.json)

## Recommended Next Mission

The next bounded step after this proposal should be:

- `Push Image Stage Controlled Patch Review v1`

That mission should inspect the exact workflow diff for only the first job and
confirm that it remains placeholder-bound before any actual patch is applied.

## Warning

Do not treat this proposal as permission to patch the workflow.

It only defines the exact narrow shape a later patch mission must obey.
