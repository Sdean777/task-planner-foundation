# Dean'z Elite OS First Bounded ECR Image Publication Run v1

## Purpose

This document records the first bounded live publication of the
`task-planner-foundation` container image into Amazon ECR.

It exists to answer these questions:

- what exact source commit was published?
- what repository and tags were used?
- how was immutable SHA truth preserved despite a dirty local worktree?
- what AWS mutations occurred?
- what remained out of scope after publication?

This run does not:

- change `app.py`
- enable ECS rollout
- enable public verification
- widen the later disabled workflow jobs

## Scope

This run applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`aws/first-bounded-ecr-image-publication-run.record.json`](./aws/first-bounded-ecr-image-publication-run.record.json)

It governs only the first bounded image-publication outcome.

## Run Objective

The objective of this run was to publish the foundation image under bounded
conditions while preserving the constitutional rules already established in the
repo:

- immutable `sha-<git-sha>` tag truth stays authoritative
- `main` is only a convenience mirror
- later deployment stages remain disabled
- application code remains unchanged

## Source Of Truth

The publication source was:

- repo: `Sdean777/task-planner-foundation`
- branch: `main`
- commit: `dfc958a333b792f82c3feaaa4f543d323450938f`
- commit message:
  `Establish AWS foundation runtime contracts and verification bridge`

The live worktree was not used as the build context because it already contained
additional uncommitted planning files. To preserve immutable commit truth, the
image was built from a clean `git archive HEAD` export.

## AWS Publication Boundary

The bounded AWS publication target was:

- account: `329601960228`
- region: `us-east-1`
- repository: `task-planner-foundation`
- repository URI:
  `329601960228.dkr.ecr.us-east-1.amazonaws.com/task-planner-foundation`

The repository did not exist at the start of the run, so it was created as a
bounded prerequisite before image publication.

## Executed Outcome

The completed outcome was:

- repository created
- clean `HEAD` export built for `linux/amd64`
- immutable image tag published:
  `sha-dfc958a333b792f82c3feaaa4f543d323450938f`
- convenience mirror published:
  `main`
- both tags resolved to the same digest:
  `sha256:415e9ef181999eab1333dcf77016368d6e276ae1cf0a2e19dd5d781732a544fa`

The final successful publication path used `docker buildx build --push` against
the clean exported source tree after the initial direct `docker push` path
stalled during manifest finalization.

## Verification

The run was verified through:

1. AWS caller identity confirmation for the executing user
2. Docker builder and local image inspection
3. `docker buildx imagetools inspect` resolving both published tags
4. `aws ecr describe-images` confirming:
   - image digest
   - both tags
   - pushed timestamp
   - active registry status

Registry-confirmed outcome:

- image digest:
  `sha256:415e9ef181999eab1333dcf77016368d6e276ae1cf0a2e19dd5d781732a544fa`
- tags:
  - `sha-dfc958a333b792f82c3feaaa4f543d323450938f`
  - `main`
- pushed at: `2026-05-22T17:42:00.835000-05:00`
- media type: `application/vnd.oci.image.manifest.v1+json`
- image status: `ACTIVE`

## Preserved Boundaries

This run preserved the required boundaries:

- `app.py` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- `.github/workflows/deploy-foundation-skeleton.yml` still keeps:
  - `ecs-rollout-placeholder` disabled
  - `public-verification-placeholder` disabled
- rollout and public verification remain downstream missions

## Explicit Non-Goals

This run did not:

- register an ECS task definition
- update an ECS service
- execute public runtime verification
- widen the deployment workflow beyond the first bounded publication path

## Canonical Execution Record

The non-secret execution record for this run is:

- [`aws/first-bounded-ecr-image-publication-run.record.json`](./aws/first-bounded-ecr-image-publication-run.record.json)

That file records the commit, registry target, tags, digest, verification
status, and next bounded mission.

## Recommended Next Mission

The next bounded step after this run should be:

- `ECS Rollout Stage Candidate Review v1`

That mission should inspect only the still-disabled `ecs-rollout-placeholder`
job, confirm the newly published immutable image can serve as rollout input, and
keep ECS service mutation blocked until the second-stage rollout chain is
reviewed.

## Warning

Do not treat successful image publication as permission to skip rollout review.

Image publication is now complete, but ECS rollout and public verification
remain separate bounded stages.
