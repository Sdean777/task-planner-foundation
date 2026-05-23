# Dean'z Elite OS Task Planner Foundation

This repository is the first foundation service pattern for Dean'z Elite OS.
It is intentionally small: a Flask service with health, validation, telemetry,
memory, task, and orchestration endpoints that proves the operational basics
before intelligence is added.

The service is currently shaped by OpenShift learnings and is now being
prepared for AWS-native container deployment without losing portability.

## Project Purpose

This repo exists to preserve the base service discipline required for a larger
OS runtime:

- source-controlled service ownership
- container build lifecycle
- deployment manifest discipline
- health and status inspection
- validator-first runtime checks
- telemetry visibility
- orchestration surface readiness

This is foundation infrastructure, not final Dean'z Elite OS intelligence.

## Verified Endpoints

The current Flask service preserves these endpoints:

| Endpoint | Purpose |
| --- | --- |
| `/` | foundation service banner |
| `/health` | minimal health status |
| `/status` | runtime service status |
| `/tasks` | task structure placeholder |
| `/memory` | foundation system memory |
| `/agent` | foundation agent descriptor |
| `/telemetry` | service runtime telemetry |
| `/validate` | validator-first health checks |
| `/orchestrate` | ordered orchestration plan |

Verified locally on `2026-05-22`:

- `/health`
- `/status`
- `/validate`
- `/orchestrate`

## Current Foundation Behavior

- The app is a Flask service in [app.py](./app.py).
- The only runtime dependency is `Flask==3.1.3` in [requirements.txt](./requirements.txt).
- The existing container path is preserved through [docker/Dockerfile](./docker/Dockerfile).
- The existing OpenShift/devfile pattern is preserved through [deploy.yaml](./deploy.yaml) and [devfile.yaml](./devfile.yaml).

## OpenShift Learning Summary

The current repo already captures several useful OpenShift lessons:

- keep the service simple and observable before widening behavior
- keep the container contract explicit with one app entrypoint
- keep platform metadata separate from the app runtime
- expose a validator endpoint early so runtime health can be checked without guessing
- expose telemetry and orchestration endpoints early so later runtime layers have stable surfaces

Those learnings are being carried forward into the AWS foundation path instead
of being discarded.

## Docker and Portability Notes

The current container path remains intentionally compatible with the existing
OpenShift pattern:

- base image: `registry.access.redhat.com/ubi9/python-39:1-1776086485`
- container port: `8081`
- container env: `FLASK_PORT=8081`
- startup command: `python ./app.py`

Local app behavior defaults to port `8080` if `FLASK_PORT` is not set.
Containerized behavior stays on `8081`, which matches the current
`Dockerfile`, `deploy.yaml`, and `devfile.yaml`.

This keeps the repo portable:

- OpenShift/devfile flow stays intact
- Docker build remains valid
- AWS runtimes can map the container on the same port without changing endpoints

## Local Run

Create a local virtual environment and run the service:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The local server listens on `http://127.0.0.1:8080` by default.

If you want local behavior to match the container port:

```bash
FLASK_PORT=8081 python app.py
```

Test the key endpoints:

```bash
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/validate
curl http://127.0.0.1:8080/orchestrate
```

## AWS Target Architecture

The first recommended AWS path for this service is:

```text
GitHub
  -> CI validation
  -> container build
  -> ECR image
  -> ECS/Fargate service
  -> Application Load Balancer or API Gateway
  -> public API route
  -> CloudWatch logs/telemetry
  -> validator and orchestration consumers
```

Recommended first runtime choices:

- container registry: Amazon ECR
- compute: Amazon ECS with Fargate
- logs and telemetry: Amazon CloudWatch
- routing: Application Load Balancer first, API Gateway if API management becomes necessary
- build and deploy automation: GitHub Actions first, AWS CodeBuild/CodePipeline as an optional later path

EKS can remain a later option if the runtime grows beyond the simplicity that
ECS/Fargate is meant to preserve.

The precise non-deploying runtime contract is documented in
[DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md),
with the paired task skeleton in
[aws/ecs-task-definition.template.json](./aws/ecs-task-definition.template.json).
The next operator-facing planning layer is the ECS service runbook in
[DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md).
The next parameter boundary is documented in
[DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md),
with the paired parameter template in
[aws/ecs-service-parameters.template.json](./aws/ecs-service-parameters.template.json).
The identity and access boundary is documented in
[DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md),
with the paired planning template in
[aws/ecs-identity-access-boundary.template.json](./aws/ecs-identity-access-boundary.template.json).
The future GitHub deployment-trust posture is documented in
[DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md),
with the paired trust template in
[aws/github-oidc-deployment-trust.template.json](./aws/github-oidc-deployment-trust.template.json).
The future rollout handoff is documented in
[DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md),
with the paired rollout template in
[aws/ecr-image-promotion-ecs-rollout.template.json](./aws/ecr-image-promotion-ecs-rollout.template.json).
The future public verification and release gate is documented in
[DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md),
with the paired gate template in
[aws/public-runtime-verification-release-gate.template.json](./aws/public-runtime-verification-release-gate.template.json).
The workflow introduction boundary is documented in
[DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md),
with the paired activation template in
[aws/deployment-workflow-activation-gate.template.json](./aws/deployment-workflow-activation-gate.template.json).
The first disabled deployment workflow shape is documented in
[DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md),
with the paired skeleton workflow in
[`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml).
The protected deployment environment boundary is documented in
[DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md),
with the paired environment template in
[`.github/protected-deployment-environment.template.json`](./.github/protected-deployment-environment.template.json).
The gradual job-enablement review boundary is documented in
[DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md),
with the paired review template in
[`.github/deployment-workflow-enablement-review.template.json`](./.github/deployment-workflow-enablement-review.template.json).
The first single-job candidate review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md),
with the paired candidate template in
[`.github/push-image-stage-candidate-review.template.json`](./.github/push-image-stage-candidate-review.template.json).
The first single-job enablement proposal is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md),
with the paired proposal template in
[`.github/push-image-stage-enablement-proposal.template.json`](./.github/push-image-stage-enablement-proposal.template.json).
The next single-job patch-review boundary is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md),
with the paired patch-review template in
[`.github/push-image-stage-controlled-patch-review.template.json`](./.github/push-image-stage-controlled-patch-review.template.json).
The first single-job placeholder-bound workflow patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md),
with the paired patch record in
[`.github/push-image-stage-placeholder-bound-patch.template.json`](./.github/push-image-stage-placeholder-bound-patch.template.json).
The next single-job GitHub OIDC auth-shape review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md),
with the paired auth-shape template in
[`.github/push-image-stage-github-oidc-auth-shape-review.template.json`](./.github/push-image-stage-github-oidc-auth-shape-review.template.json).
The first single-job GitHub OIDC auth-placeholder patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md),
with the paired auth-placeholder record in
[`.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json`](./.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json).
The next single-job ECR-login shape review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md),
with the paired login-shape template in
[`.github/push-image-stage-ecr-login-shape-review.template.json`](./.github/push-image-stage-ecr-login-shape-review.template.json).
The first single-job ECR-login placeholder patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md),
with the paired login-placeholder record in
[`.github/push-image-stage-ecr-login-placeholder-patch.template.json`](./.github/push-image-stage-ecr-login-placeholder-patch.template.json).
The next single-job image-push shape review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md),
with the paired push-shape template in
[`.github/push-image-stage-image-push-shape-review.template.json`](./.github/push-image-stage-image-push-shape-review.template.json).
The first single-job image-push placeholder patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md),
with the paired push-placeholder record in
[`.github/push-image-stage-image-push-placeholder-patch.template.json`](./.github/push-image-stage-image-push-placeholder-patch.template.json).
The next single-job push-job permission-widening review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md),
with the paired permission-review template in
[`.github/push-image-stage-push-job-permission-widening-review.template.json`](./.github/push-image-stage-push-job-permission-widening-review.template.json).
The first single-job push-job permission placeholder patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md),
with the paired permission-placeholder record in
[`.github/push-image-stage-push-job-permission-placeholder-patch.template.json`](./.github/push-image-stage-push-job-permission-placeholder-patch.template.json).
The next single-job OIDC auth-action invocation review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md),
with the paired invocation-review template in
[`.github/push-image-stage-oidc-auth-action-invocation-review.template.json`](./.github/push-image-stage-oidc-auth-action-invocation-review.template.json).
The first single-job OIDC auth-action placeholder patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md),
with the paired auth-action placeholder record in
[`.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json`](./.github/push-image-stage-oidc-auth-action-placeholder-patch.template.json).
The next single-job ECR-login command invocation review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md),
with the paired invocation-review template in
[`.github/push-image-stage-ecr-login-command-invocation-review.template.json`](./.github/push-image-stage-ecr-login-command-invocation-review.template.json).
The first single-job ECR-login command placeholder patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md),
with the paired command-placeholder record in
[`.github/push-image-stage-ecr-login-command-placeholder-patch.template.json`](./.github/push-image-stage-ecr-login-command-placeholder-patch.template.json).
The refreshed single-job live-enable candidate review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md),
with the paired review template in
[`.github/push-image-stage-live-enable-candidate-review.template.json`](./.github/push-image-stage-live-enable-candidate-review.template.json).
The refreshed single-job live-enable proposal is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md),
with the paired proposal template in
[`.github/push-image-stage-live-enable-proposal.template.json`](./.github/push-image-stage-live-enable-proposal.template.json).
The refreshed single-job live-enable controlled patch review is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md),
with the paired review template in
[`.github/push-image-stage-live-enable-controlled-patch-review.template.json`](./.github/push-image-stage-live-enable-controlled-patch-review.template.json).
The refreshed single-job live-enable patch is documented in
[DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md),
with the paired patch template in
[`.github/push-image-stage-live-enable-patch.template.json`](./.github/push-image-stage-live-enable-patch.template.json).

## Migration Notes

What changes now:

- documentation is being rewritten around Dean'z Elite OS foundation service intent
- AWS mapping is being made explicit
- GitHub-to-container-to-ECR-to-ECS workflow structure is being documented
- container build hygiene is being improved without breaking OpenShift compatibility

What does not change now:

- Flask endpoints stay the same
- no OpenAI integration is added
- no autonomous agent behavior is added
- no AWS credentials are introduced
- no live deployment automation is introduced

## GitHub Actions Placeholder Plan

The future AWS workflow is documented only, not activated yet.

See:

- [DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md](./DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_SHAPE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_IMAGE_PUSH_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_WIDENING_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_INVOCATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_INVOCATION_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PATCH_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)

The current live workflows remain:

- [`.github/workflows/ci.yaml`](./.github/workflows/ci.yaml)
- [`.github/workflows/validate-with-registry.yaml`](./.github/workflows/validate-with-registry.yaml)
- [`.github/workflows/container-build-verify.yml`](./.github/workflows/container-build-verify.yml)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml) with bounded push-image, ECS rollout, and public verification paths
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml) as a separate read-only smoke workflow

## Container Build Verification

The new `container-build-verify.yml` workflow is the safe bridge between
OpenShift learning and future AWS deployment.

What it does:

- builds the container locally from `docker/Dockerfile`
- tags it locally as `task-planner-foundation:test`
- runs the container locally in GitHub Actions
- smoke tests `/health`, `/validate`, and `/orchestrate`
- removes the test container after verification

What it does not do:

- does not require secrets
- does not push to ECR
- does not deploy to ECS or EKS
- does not widen the Flask app scope

This is deliberate. Before AWS deployment, the repo must prove container
portability cleanly.

For local developer use, Docker verification also requires a running Docker
daemon.

## Foundation Status Checklist

- [x] Source ownership complete
- [x] OpenShift deployment pattern present and documented
- [x] API endpoints preserved
- [x] Validator endpoint passing locally
- [x] Orchestrator endpoint ready locally
- [x] AWS migration planning started
- [x] Container build verification workflow added
- [x] ECS runtime contract planning added
- [x] ECS service runbook layer added
- [x] ECS parameterization and environment contract added
- [x] ECS identity and access boundary added
- [x] GitHub OIDC deployment trust contract added
- [x] ECR image promotion and ECS rollout contract added
- [x] Public runtime verification and release gate contract added
- [x] Deployment workflow activation gate added
- [x] Deployment workflow skeleton added in disabled form
- [x] Protected deployment environment and approval contract added
- [x] Deployment workflow enablement review contract added
- [x] Push-image stage candidate review added
- [x] Push-image stage enablement proposal added
- [x] Push-image stage controlled patch review added
- [x] Push-image stage placeholder-bound patch applied
- [x] Push-image stage GitHub OIDC auth-shape review added
- [x] Push-image stage GitHub OIDC auth-placeholder patch applied
- [x] Push-image stage ECR-login shape review added
- [x] Push-image stage ECR-login placeholder patch applied
- [x] Push-image stage image-push shape review added
- [x] Push-image stage image-push placeholder patch applied
- [x] Push-image stage push-job permission-widening review added
- [x] Push-image stage push-job permission placeholder patch applied
- [x] Push-image stage OIDC auth-action invocation review added
- [x] Push-image stage OIDC auth-action placeholder patch applied
- [x] Push-image stage ECR-login command invocation review added
- [x] Push-image stage ECR-login command placeholder patch applied
- [x] Push-image stage live-enable candidate review added
- [x] Push-image stage live-enable proposal added
- [x] Push-image stage live-enable controlled patch review added
- [x] Push-image stage live-enable patch applied
- [x] Container image published to ECR
- [x] ECS/Fargate runtime created
- [x] Public AWS routing enabled
- [ ] CloudWatch-backed deployment telemetry connected

## Next Phase Instructions

The next phase should stay disciplined:

1. Keep this service as a stable base runtime.
2. Use the ECS runtime contract as the source of truth before any AWS deployment work.
3. Use the ECS service runbook to define the manual AWS resource and verification path before any live runtime work.
4. Use the ECS parameterization contract to keep service names, ports, roles, URLs, and non-secret environment values explicit and externalized.
5. Use the identity and access boundary to keep execution role, task role, and future OIDC deployment role scope narrow and reviewable.
6. Use the GitHub OIDC trust contract to keep repository, branch, audience, and future deploy-role trust boundaries explicit before any workflow is allowed to assume AWS identity.
7. Use the rollout contract to keep immutable image tags, task-definition revision handoff, and rollback posture explicit before any release workflow exists.
8. Use the public runtime verification and release gate contract to define how a new revision is accepted, flagged for review, or rolled back.
9. Use the deployment workflow activation gate to ensure a real deploy workflow is still blocked until planning, rollback, trust, and approval preconditions are explicit.
10. Use the disabled workflow skeleton to keep future stage order visible without enabling push or deploy behavior yet.
11. Use the protected deployment environment contract to keep environment name, branch restrictions, reviewer posture, and still-disabled actions explicit before any job enablement is considered.
12. Use the enablement review contract to keep job enablement gradual, one-stage-at-a-time, and evidence-bound.
13. Use the push-image candidate review to assess only the first disabled job without enabling it or advancing later stages.
14. Use the push-image enablement proposal to define the exact minimal diff shape for only the first job while keeping the workflow disabled.
15. Use the push-image controlled patch review to inspect the exact first-job workflow hunk before any workflow mutation is attempted.
16. Use the placeholder-bound patch as the only allowed first-job workflow mutation while the job remains disabled.
17. Use the GitHub OIDC auth-shape review to define the exact future first-job auth posture before any auth or registry commands are introduced.
18. Use the GitHub OIDC auth-placeholder patch only to record the future first-job auth hunk while the job stays disabled and workflow permissions remain unchanged.
19. Use the ECR-login shape review to define the exact future first-job registry-login posture before any registry command is introduced.
20. Use the ECR-login placeholder patch only to record the future first-job registry-login hunk while the job stays disabled and workflow permissions remain unchanged.
21. Use the image-push shape review to define the exact future first-job image-publication posture before any push command is introduced.
22. Use the image-push placeholder patch only to record the future first-job image-publication hunk while the job stays disabled and workflow permissions remain unchanged.
23. Use the push-job permission-widening review to define the exact future job-local permission posture before any permissions change is introduced.
24. Use the push-job permission placeholder patch only to record the future first-job permission hunk while the job stays disabled and workflow-level permissions remain unchanged.
25. Use the OIDC auth-action invocation review to define the exact future action-invocation posture before any auth action reference is introduced.
26. Use the OIDC auth-action placeholder patch only to record the future first-job auth-action hunk while the job stays disabled and workflow-level permissions remain unchanged.
27. Use the ECR-login command invocation review to define the exact future registry-login command posture before any login-command reference is introduced.
28. Use the ECR-login command placeholder patch only to record the future first-job registry-login command hunk while the job stays disabled and workflow permissions remain unchanged.
29. Use the refreshed live-enable candidate review to determine whether the complete first-job placeholder chain is stable before any future enablement proposal reopens live behavior.
30. Use the refreshed live-enable proposal to define the exact first-job-only diff shape before any controlled patch review is allowed.
31. Use the refreshed live-enable controlled patch review to inspect the exact first-job diff before any live-enable patch is allowed.
32. Use the refreshed live-enable patch to keep first-job auth, login, and image publication bounded to manual main-branch production dispatch with immutable SHA tag truth.
33. Complete the first bounded ECR image publication run from a clean `HEAD` export so immutable `sha-<git-sha>` truth is preserved even when the local worktree contains later planning files.
34. Use the ECS rollout stage candidate review to inspect the still-disabled `ecs-rollout-placeholder` job after bounded image publication and before any task-definition or service mutation is allowed.
35. Use the ECS rollout stage enablement proposal to define the exact second-job-only diff shape while `public-verification-placeholder` remains blocked and rollout commands stay proposal-bound.
36. Use the ECS rollout stage controlled patch review to inspect the exact second-job diff while immutable SHA rollout truth, rollback posture, and release-gate posture remain explicit.
37. Use the ECS rollout stage patch to keep second-job task-definition registration and service update bounded to manual main-branch production dispatch while `public-verification-placeholder` remains disabled.
38. Treat the first bounded ECS rollout run as blocked if the task-definition family or ECS service baseline does not already exist; do not invent baseline state during rollout.
39. Use ECS service baseline standup to create the first explicit cluster, task family, log group, and service target before public verification is reviewed.
40. Use the public verification stage candidate review to inspect the still-disabled `public-verification-placeholder` job only after bounded image publication and ECS baseline standup both exist.
41. Use the public verification stage enablement proposal to define the exact third-job-only diff shape while live public checks remain proposal-bound.
42. Use the public verification stage controlled patch review to inspect the exact third-job diff while release-gate order, rollback posture, and manual review outcomes remain explicit.
43. Use the public verification stage patch to keep third-job runtime verification bounded to manual main-branch production dispatch while push-image and rollout jobs remain unchanged.
44. Treat the first bounded public verification run as blocked if a stable non-secret `FOUNDATION_PUBLIC_BASE_URL` is not yet established; do not invent endpoint truth during verification.
45. Use public routing baseline standup to create the first stable non-secret `FOUNDATION_PUBLIC_BASE_URL` before retrying bounded public verification.
46. Use public routing baseline standup to establish the bounded ALB listener, target group, and stable non-secret base URL before retrying public verification.
47. Use the second bounded public verification run to execute the third-job verification path against the stable base URL rather than task-level networking.
48. Complete telemetry runtime identity alignment so `/telemetry` reflects the live AWS ALB + ECS Fargate runtime instead of stale legacy wording.
49. Use post-deploy public runtime smoke tests to prove repeatable ALB-backed stability after the first clean `keep_active` release-gate result.
50. Use public runtime smoke automation review to lock the future smoke-automation layer to a separate read-only boundary rather than a deployment controller.
51. Use public runtime smoke automation proposal to define the exact future automation shape before any workflow patch is considered.
52. Use public runtime smoke automation controlled patch review to inspect the exact future smoke-workflow diff before any workflow file is created.
53. Use public runtime smoke automation patch to create one separate read-only smoke workflow file only after the controlled review is complete.
54. Use the first bounded public runtime smoke automation run to prove the new workflow reproduces the already-accepted smoke evidence without drift.
55. Use GitHub-hosted public runtime smoke workflow dispatch review to decide whether the now-proven read-only workflow is ready for repository-backed hosted execution.
56. Use GitHub-hosted public runtime smoke workflow dispatch proposal to define the exact repository-backed hosted execution boundary before any real GitHub-hosted run is attempted.
57. Use GitHub-hosted public runtime smoke workflow dispatch controlled run review to inspect the exact repository-backed hosted-run boundary before any real GitHub-hosted dispatch is attempted.
58. Use the first bounded GitHub-hosted public runtime smoke workflow dispatch run to prove one repository-backed hosted dispatch reproduces the already-accepted smoke evidence without drift.
59. If that hosted run is blocked because the smoke workflow exists only as local source state, use `GitHub-Hosted Public Runtime Smoke Workflow Source Publication v1` to establish a clean tracked and pushed source checkpoint before retrying.
60. Use the second bounded GitHub-hosted public runtime smoke workflow dispatch run to retry one repository-backed hosted dispatch against the now-published workflow source.
61. If that hosted run is blocked because `FOUNDATION_PUBLIC_BASE_URL` is missing in GitHub repository variables, use `GitHub-Hosted Public Runtime Smoke Workflow Variable Baseline v1` to establish the non-secret repository-variable boundary before retrying.
62. Use the GitHub-hosted public runtime smoke workflow variable baseline to establish `FOUNDATION_PUBLIC_BASE_URL` as an explicit repository-backed non-secret input before retrying the hosted smoke workflow.
63. Use the third bounded GitHub-hosted public runtime smoke workflow dispatch run to prove one real repository-backed hosted dispatch completes successfully against the published workflow and repository-variable baseline.
64. If that hosted run succeeds while the new run evidence still exists only in local source state, use `GitHub-Hosted Public Runtime Smoke Success Source Publication v1` to publish the successful hosted-dispatch evidence as tracked repository source.
65. Use the GitHub-hosted public runtime smoke success source publication checkpoint to converge local hosted-smoke doctrine and execution evidence back into tracked repository source.
66. Use `CloudWatch Service Telemetry Baseline Review v1` to inspect the remaining gap between CloudWatch log visibility and explicit service-level telemetry connection.
67. Add build/deploy automation only after the image, runtime, runbook, parameter, identity, trust, rollout, release-gate, activation-gate, skeleton, environment, enablement-review, push-image candidate-review, push-image proposal, push-image controlled patch review, push-image placeholder-bound patch, push-image GitHub OIDC auth-shape review, push-image GitHub OIDC auth-placeholder patch, push-image ECR-login shape review, push-image ECR-login placeholder patch, push-image image-push shape review, push-image image-push placeholder patch, push-image push-job permission-widening review, push-image push-job permission placeholder patch, push-image OIDC auth-action invocation review, push-image OIDC auth-action placeholder patch, push-image ECR-login command invocation review, push-image ECR-login command placeholder patch, push-image live-enable candidate review, push-image live-enable proposal, push-image live-enable controlled patch review, push-image live-enable patch, first bounded ECR image publication run, ECS rollout stage candidate review, ECS rollout stage enablement proposal, ECS rollout stage controlled patch review, ECS rollout stage patch, first bounded ECS rollout run, ECS service baseline standup, public verification stage candidate review, public verification stage enablement proposal, public verification stage controlled patch review, public verification stage patch, first bounded public verification run, public routing baseline standup, second bounded public verification run, telemetry runtime identity alignment, post-deploy public runtime smoke tests, public runtime smoke automation review, public runtime smoke automation proposal, public runtime smoke automation controlled patch review, public runtime smoke automation patch, first bounded public runtime smoke automation run, GitHub-hosted public runtime smoke workflow dispatch review, GitHub-hosted public runtime smoke workflow dispatch proposal, GitHub-hosted public runtime smoke workflow dispatch controlled run review, GitHub-hosted public runtime smoke workflow source publication, the first bounded GitHub-hosted public runtime smoke workflow dispatch run, the second bounded GitHub-hosted public runtime smoke workflow dispatch run, the GitHub-hosted public runtime smoke workflow variable baseline, the third bounded GitHub-hosted public runtime smoke workflow dispatch run, and the GitHub-hosted public runtime smoke success source publication checkpoint are stable.
68. Add stronger validator and orchestration behavior before adding model-driven intelligence.

Do not turn this repo into a large AI app yet. Keep it as the first clean
foundation service pattern for Dean'z Elite OS.
