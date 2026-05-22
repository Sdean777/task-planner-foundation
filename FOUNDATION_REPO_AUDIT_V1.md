# Foundation Repo Audit v1

Audit date: `2026-05-22`

Scope of this audit:

- inspect current foundation repo state
- identify what already exists
- identify what is duplicated or at risk of duplication
- identify the next non-duplicative AWS step

This audit adds only this file. No implementation surfaces were changed as part
of the audit itself.

## Current Repo Inventory

### Runtime

- [app.py](./app.py)
  - minimal Flask foundation service
  - endpoints present:
    - `/`
    - `/health`
    - `/status`
    - `/tasks`
    - `/memory`
    - `/agent`
    - `/telemetry`
    - `/validate`
    - `/orchestrate`
- [requirements.txt](./requirements.txt)
  - single runtime dependency: `Flask==3.1.3`

### Container and Platform Files

- [docker/Dockerfile](./docker/Dockerfile)
  - UBI Python base image
  - `EXPOSE 8081`
  - `FLASK_PORT=8081`
  - runs `python ./app.py`
- [deploy.yaml](./deploy.yaml)
  - OpenShift/Kubernetes deployment and service
  - port contract on `8081`
- [devfile.yaml](./devfile.yaml)
  - devfile build/deploy path
  - points to the same Dockerfile and deployment manifest
- [.dockerignore](./.dockerignore)
  - present
  - excludes `.git`, `.github`, `.venv`, caches, and local noise
- [.gitignore](./.gitignore)
  - ignores `.odo/*` metadata and `.venv/`

### Documentation

- [README.md](./README.md)
  - foundation purpose
  - endpoint list
  - OpenShift learning summary
  - AWS target architecture
  - local run instructions
  - container build verification section
  - foundation status checklist
- [DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md](./DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md)
  - AWS foundation doctrine
  - architecture, governance, validator, telemetry, agent direction
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
  - future workflow plan
  - marks non-deploying container verification as the current active bridge step

### GitHub Workflows

- [`.github/workflows/ci.yaml`](./.github/workflows/ci.yaml)
  - Python lint/test workflow
- [`.github/workflows/validate-with-registry.yaml`](./.github/workflows/validate-with-registry.yaml)
  - devfile registry validation path
- [`.github/workflows/container-build-verify.yml`](./.github/workflows/container-build-verify.yml)
  - non-deploying container build verification
  - local image build only
  - local smoke tests only
  - no push to registry
  - no AWS secrets

### Working Tree State

Current repo state includes existing uncommitted foundation changes:

- modified:
  - `.gitignore`
  - `README.md`
- untracked:
  - `.dockerignore`
  - `.github/workflows/container-build-verify.yml`
  - `DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md`
  - `GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md`

Those are pre-existing relative to this audit mission.

## Already Completed Work

### 1. Existing AWS Planning

Already present:

- AWS target architecture in `README.md`
- AWS foundation doctrine in `DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md`
- future GitHub/ECR/ECS plan in `GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md`

Conclusion:
- broad AWS planning already exists
- another generic AWS vision doc would be duplicative

### 2. Existing Container Workflow

Already present:

- `container-build-verify.yml`

What it already does:

- builds from `docker/Dockerfile`
- tags locally as `task-planner-foundation:test`
- runs the container locally in CI
- checks `/health`, `/validate`, and `/orchestrate`
- removes the test container
- pushes nowhere

Conclusion:
- a second “pre-AWS container verify” workflow would be duplicative

### 3. Existing Validator / Telemetry / Orchestration Coverage

Already present:

- endpoint behavior in `app.py`
- endpoint inventory in `README.md`
- validator philosophy and telemetry philosophy in `DEANZ_ELITE_OS_AWS_FOUNDATION_V1.md`

Conclusion:
- separate standalone docs for validator, telemetry, or orchestration would be duplicative at this stage

### 4. Endpoint Stability

`app.py` is unchanged in the current diff inspection.

Conclusion:
- the Flask foundation contract remains intact

## Duplicate Risk Areas

### 1. README vs AWS Foundation Doc

These two files currently overlap on:

- project purpose
- AWS target architecture
- OpenShift-to-AWS transition framing
- governance language

This is acceptable for now, but adding a third broad AWS summary doc would be
unnecessary duplication.

### 2. README vs Placeholder Plan

These overlap on:

- workflow progression
- GitHub Actions role
- ECR/ECS future direction

Risk:
- adding another “next workflow plan” document would fragment the same story

### 3. Portability / Port Contract

The `8081` container contract appears in:

- `docker/Dockerfile`
- `deploy.yaml`
- `devfile.yaml`
- `README.md`
- `container-build-verify.yml`

Risk:
- future edits could drift if port changes are made in only one place

### 4. OpenShift vs AWS Runtime Language

There is a mild doctrine drift signal:

- the repo docs now emphasize AWS readiness
- `/telemetry` in `app.py` still reports:
  - `runtime: OpenShift`
  - `infrastructure: AWS-backed sandbox`

This is not a failure, but it is a hybrid message that should be handled
carefully in a later mission instead of patching docs repeatedly.

## Gaps Remaining

### 1. No AWS Runtime Contract Artifact Yet

Missing:

- ECR naming/tagging contract
- ECS task definition contract
- ALB/API Gateway routing contract
- CloudWatch log group naming and log stream expectations
- health check contract for AWS runtime consumers

This is the largest remaining AWS readiness gap.

### 2. No AWS Identity / OIDC Planning Artifact Yet

The placeholder plan correctly mentions GitHub OIDC, but there is no dedicated
runtime contract describing:

- future OIDC trust path
- IAM scope boundaries
- what GitHub will need later
- what must remain out of source

This is still planning debt, though it should not become a live credential step yet.

### 3. No Production Runtime Server Decision Yet

The container still runs:

- `python ./app.py`

That is acceptable for foundation proof, but a future AWS runtime contract
should explicitly decide whether the service stays on Flask’s dev server for
foundation-only use or moves to a production WSGI server before ECS deployment.

This should be handled as a runtime contract decision, not by silently changing
the app now.

### 4. Container Workflow Exists But Was Not Locally Docker-Verified Here

`container-build-verify.yml` exists and is structurally coherent.

However, in this environment:

- local Docker daemon was unavailable
- the workflow could not be proven by a local `docker build` / `docker run` execution here

That means:

- the workflow exists
- it appears valid by inspection
- it still needs its first real GitHub Actions run result

### 5. No ECS-Specific Non-Deploying Artifacts Yet

Missing:

- task definition skeleton
- service/runtime assumptions
- environment variable contract for AWS runtime
- port and health check mapping for ECS/ALB

These are the next practical AWS readiness pieces that do not duplicate current docs.

## Recommended Next Mission

Recommended next non-duplicative AWS step:

### `Dean'z Elite OS — ECS Runtime Contract Planning v1`

Objective:

- define the first non-deploying AWS runtime contract for this exact service
- do not deploy anything
- do not add AWS credentials
- do not change `app.py`

What that mission should produce:

- one AWS runtime contract document
- one ECS task definition skeleton or template
- explicit ECR image naming/tagging rules
- explicit ALB/ECS health check mapping using the existing endpoint contract
- explicit CloudWatch log naming / telemetry expectations
- explicit note that GitHub OIDC is future-only and still credential-free in source

Why this is the right next step:

- it does not duplicate existing AWS foundation docs
- it does not duplicate the current container verification workflow
- it turns broad AWS intent into a precise runtime contract
- it keeps deployment deferred while making the repo more AWS-ready

## Explicit Do Not Duplicate List

Do not add another:

- broad AWS foundation vision document
- second workflow roadmap document
- second non-deploying container verification workflow
- second endpoint inventory document
- second OpenShift learning summary document
- live ECR push workflow yet
- live ECS deploy workflow yet
- AWS secret or credential file
- OpenAI integration placeholder

Do not change yet:

- `app.py` endpoint surface
- the existing OpenShift-compatible `8081` container path
- the foundation-only scope of the repo

## Audit Conclusion

The repo is no longer missing high-level AWS direction. That now exists.

The repo is also no longer missing a safe container verification bridge. That
already exists.

The next correct AWS step is therefore not more general planning and not another
workflow. The next correct step is a precise, non-deploying AWS runtime
contract for ECR/ECS/ALB/CloudWatch so future implementation can proceed
without duplication or drift.
