# Enterprise Integration Patterns

This reference defines enterprise/service integration patterns to recognize when extracting training data from real-world agent frameworks.

## Issue Tracking & ITSM

### ServiceNow (IT Service Management)

**Pattern: ServiceNow Client**
```python
class ServiceNowClient:
    """Client for ServiceNow API."""

    def __init__(self, instance_url: str, username: str, password: str):
        self.base_url = f"{instance_url}/api/now"
        self.auth = HTTPBasicAuth(username, password)

    async def create_incident(self, short_description: str, description: str, priority: int = 1) -> dict:
        """Create a new incident."""
        payload = {
            "short_description": short_description,
            "description": description,
            "priority": priority,
            "impact": 2,
            "urgency": 2
        }
        # Implementation

    async def update_incident(self, incident_id: str, status: str, work_notes: str) -> dict:
        """Update an incident status and add work notes."""
        # Implementation

    async def get_user(self, sys_id: str) -> dict:
        """Get user details by sys_id."""
        # Implementation

    async def create_change_request(self, change_request: dict) -> dict:
        """Create a change request."""
        # Implementation
```

**Instruction:** "Create a ServiceNow client with methods for creating incidents, updating status, and creating change requests"

---

### Confluence (Documentation/Wiki)

**Pattern: Confluence Client**
```python
class ConfluenceClient:
    """Client for Atlassian Confluence API."""

    def __init__(self, base_url: str, token: str):
        self.base_url = f"{base_url}/wiki/api/v2"
        self.headers = {"Authorization": f"Bearer {token}"}

    async def create_page(self, space: str, title: str, content: str, parent_id: str = None) -> dict:
        """Create a new Confluence page."""
        payload = {
            "type": "page",
            "title": title,
            "space": {"key": space},
            "body": {"storage": {"value": content, "representation": "storage"}},
            "ancestors": [{"id": parent_id}] if parent_id else []
        }
        # Implementation

    async def update_page(self, page_id: str, content: str, version: int) -> dict:
        """Update a page with new content."""
        # Implementation

    async def search_pages(self, space: str, query: str) -> list[dict]:
        """Search for pages by query."""
        # Implementation

    async def attach_file(self, page_id: str, file_path: str, comment: str = None) -> dict:
        """Attach a file to a page."""
        # Implementation
```

**Instruction:** "Create a Confluence client with methods for creating pages, updating content, searching, and file attachments"

---

### Jira (Issue Tracking)

**Pattern: Jira Client**
```python
class JiraClient:
    """Client for Jira REST API."""

    def __init__(self, url: str, email: str, token: str):
        self.base_url = f"{url}/rest/api/2"
        self.auth = HTTPBasicAuth(email, token)

    async def create_issue(self, project: str, summary: str, issuetype: str, description: str = "") -> dict:
        """Create a new issue in Jira."""
        payload = {
            "fields": {
                "project": {"key": project},
                "summary": summary,
                "description": description,
                "issuetype": {"name": issuetype}
            }
        }
        # Implementation

    async def transition_issue(self, issue_key: str, transition_name: str) -> dict:
        """Transition an issue to a new status."""
        # Implementation

    async def add_comment(self, issue_key: str, comment: str) -> dict:
        """Add a comment to an issue."""
        # Implementation

    async def search_issues(self, jql: str) -> list[dict]:
        """Search issues using JQL."""
        # Implementation
```

**Instruction:** "Create a Jira client with methods for creating issues, transitioning status, adding comments, and JQL search"

---

## Monitoring & Observability

### Grafana (Dashboards/Alerting)

**Pattern: Grafana Client**
```python
class GrafanaClient:
    """Client for Grafana API."""

    def __init__(self, url: str, api_key: str):
        self.base_url = f"{url}/api"
        self.headers = {"Authorization": f"Bearer {api_key}"}

    async def create_dashboard(self, dashboard: dict) -> dict:
        """Create a new dashboard."""
        # Implementation

    async def query_datasource(self, datasource_uid: str, query: str, time_range: dict) -> list[dict]:
        """Query a datasource."""
        # Implementation

    async def create_alert(self, alert: dict) -> dict:
        """Create a new alert rule."""
        # Implementation

    async def get_dashboard(self, dashboard_uid: str) -> dict:
        """Get dashboard by UID."""
        # Implementation
```

**Instruction:** "Create a Grafana client with methods for creating dashboards, querying datasources, and managing alerts"

---

### Prometheus (Metrics)

**Pattern: Prometheus Client**
```python
class PrometheusClient:
    """Client for Prometheus API."""

    def __init__(self, url: str):
        self.base_url = f"{url}/api/v1"

    async def query(self, promql: str, time_range: tuple) -> list[dict]:
        """Query Prometheus metrics."""
        # Implementation

    async def get_series_metadata(self, match: str) -> list[dict]:
        """Get metadata for series matching the label selector."""
        # Implementation

    async def create_alert_rule(self, rule: dict) -> dict:
        """Create an alert rule."""
        # Implementation
```

**Instruction:** "Create a Prometheus client with methods for querying metrics, getting series metadata, and creating alert rules"

---

## Version Control & Code Hosting

### GitHub

**Pattern: GitHub Client**
```python
class GitHubClient:
    """Client for GitHub API."""

    async def create_pr(self, repo: str, title: str, head: str, base: str, body: str = "") -> dict:
        """Create a pull request."""
        # Implementation

    async def get_file(self, repo: str, path: str, ref: str = "main") -> str:
        """Get file content from repository."""
        # Implementation

    async def update_file(self, repo: str, path: str, content: str, message: str, branch: str = "main") -> dict:
        """Update or create a file in repository."""
        # Implementation

    async def create_issue(self, repo: str, title: str, body: str) -> dict:
        """Create an issue in a repository."""
        # Implementation

    async def add_reviewers(self, repo: str, pr_number: int, reviewers: list[str]) -> dict:
        """Add reviewers to a project card / pull request."""
        # Implementation

    async def create_release(self, repo: str, tag_name: str, name: str, body: str) -> dict:
        """Create a release."""
        # Implementation
```

**Instruction:** "Create a GitHub client with methods for PRs, files, issues, reviewers, and releases"

---

### GitLab

**Pattern: GitLab Client**
```python
class GitLabClient:
    """Client for GitLab API."""

    async def create_merge_request(self, project: int, source_branch: str, target_branch: str, title: str) -> dict:
        """Create a merge request."""
        # Implementation

    async def create_pipeline(self, project: int, ref: str) -> dict:
        """Trigger a pipeline."""
        # Implementation

    async def get_pipeline_status(self, project: int, pipeline_id: int) -> dict:
        """Get pipeline job status."""
        # Implementation
```

**Instruction:** "Create a GitLab client with methods for merge requests, pipelines, and job status"

---

## Artifact Management

### JFrog Artifactory

**Pattern: Artifactory Client**
```python
class ArtifactoryClient:
    """Client for JFrog Artifactory API."""

    def __init__(self, url: str, api_key: str):
        self.base_url = f"{url}/artifactory/api"
        self.headers = {"X-JFrog-Art-Apikey": api_key}

    async def upload_artifact(self, repo: str, artifact_path: str, file_path: str, properties: dict = None) -> dict:
        """Upload an artifact to Artifactory."""
        # Implementation with checksums

    async def download_artifact(self, repo: str, artifact_path: str) -> bytes:
        """Download an artifact from Artifactory."""
        # Implementation

    async def search_artifacts(self, repo: str, name: str) -> list[dict]:
        """Search for artifacts by name using AQL."""
        # Implementation

    async def get_build_info(self, repo: str, build_name: str, build_number: str) -> dict:
        """Get build information from Artifactory."""
        # Implementation

    async def copy_artifact(self, src_repo: str, src_path: str, dest_repo: str, dest_path: str) -> dict:
        """Copy an artifact between repositories."""
        # Implementation
```

**Instruction:** "Create an Artifactory client with upload, download, search, build info, and copy methods"

---

## CI/CD & Build Systems

### Jenkins

**Pattern: Jenkins Client**
```python
class JenkinsClient:
    """Client for Jenkins API."""

    def __init__(self, url: str, username: str, api_key: str):
        self.base_url = f"{url}"
        self.auth = HTTPBasicAuth(username, api_key)

    async def trigger_build(self, job_name: str, parameters: dict = None) -> dict:
        """Trigger a Jenkins build."""
        # Implementation

    async def get_build_status(self, job_name: str, build_number: int) -> dict:
        """Get build status."""
        # Implementation

    async def get_console_output(self, job_name: str, build_number: int) -> str:
        """Get build console output."""
        # Implementation

    async def get_job_info(self, job_name: str) -> dict:
        """Get job configuration and information."""
        # Implementation
```

**Instruction:** "Create a Jenkins client with methods to trigger builds, get status, retrieve console output, and get job info"

---

### GitHub Actions

**Pattern: GitHub Actions Client**
```python
class GitHubActionsClient:
    """Client for GitHub Actions API."""

    async def trigger_workflow(self, repo: str, workflow: str, branch: str, inputs: dict) -> dict:
        """Trigger a GitHub Actions workflow."""
        # Implementation

    async def get_workflow_run(self, repo: str, run_id: int) -> dict:
        """Get workflow run status."""
        # Implementation

    async def get_workflow_logs(self, repo: str, run_id: int) -> str:
        """Get logs from a workflow run."""
        # Implementation

    async def list_workflows(self, repo: str) -> list[dict]:
        """List all workflows in a repository."""
        # Implementation
```

**Instruction:** "Create a GitHub Actions client with methods to trigger workflows, get run status, retrieve logs, and list workflows"

---

### CircleCI

**Pattern: CircleCI Client**
```python
class CircleCIClient:
    """Client for CircleCI API."""

    async def trigger_pipeline(self, project: str, branch: str) -> dict:
        """Trigger a CircleCI pipeline."""
        # Implementation

    async def get_workflow(self, workflow_id: int) -> dict:
        """Get workflow details."""
        # Implementation

    async def get_artifacts(self, project: str, workflow_num: int) -> list[dict]:
        """Get artifacts from a workflow run."""
        # Implementation
```

---

## Cloud Providers

### AWS (S3, EC2, Lambda, etc.)

**Pattern: AWS SDK Clients**
```python
class S3Client:
    """Client for AWS S3 operations."""

    async def upload_file(self, bucket: str, key: str, file_path: str, metadata: dict = None) -> str:
        """Upload a file to S3."""
        # Implementation

    async def download_file(self, bucket: str, key: str) -> bytes:
        """Download a file from S3."""
        # Implementation

    async def list_files(self, bucket: str, prefix: str, delimiter: str = None) -> list[dict]:
        """List objects in a bucket with optional prefix filtering."""
        # Implementation

    async def get_file_url(self, bucket: str, key: str, expires_in: int = 3600) -> str:
        """Generate a presigned URL for file access."""
        # Implementation

class LambdaClient:
    """Client for AWS Lambda operations."""

    async def invoke_function(self, function_name: str, payload: dict) -> dict:
        """Invoke a Lambda function."""
        # Implementation

    async def create_function(self, function_config: dict) -> dict:
        """Create a new Lambda function."""
        # Implementation
```

**Instruction:** "Create an S3 client with upload, download, list, and presigned URL methods" / "Create a Lambda client with invoke and create methods"

---

### Azure DevOps / Azure Services

**Pattern: Azure DevOps Client**
```python
class AzureDevOpsClient:
    """Client for Azure DevOps API."""

    async def create_pull_request(self, project: str, repo: str, source: str, target: str, title: str) -> dict:
        """Create a pull request."""
        # Implementation

    async def get_build(self, project: str, build_id: int) -> dict:
        """Get build details."""
        # Implementation

    async def queue_build(self, project: str, definition_id: int, parameters: dict) -> dict:
        """Queue a new build."""
        # Implementation
```

---

### Google Cloud Platform

**Pattern: GCP Clients**
```python
class CloudStorageClient:
    """Client for Google Cloud Storage."""

    async def upload_blob(self, bucket: str, blob_name: str, file_path: str) -> str:
        """Upload a blob to GCS."""
        # Implementation

    async def download_blob(self, bucket: str, blob_name: str) -> bytes:
        """Download a blob from GCS."""
        # Implementation

    async def list_blobs(self, bucket: str, prefix: str) -> list[dict]:
        """List blobs with prefix."""
        # Implementation
```

---

## Container Registries

### Docker Hub / Private Registries

**Pattern: Docker Registry Client**
```python
class DockerRegistryClient:
    """Client for Docker registry API."""

    async def push_image(self, image: str, tag: str, username: str, password: str) -> str:
        """Push a Docker image to the registry."""
        # Implementation

    async def pull_image(self, image: str) -> bytes:
        """Pull a Docker image layer."""
        # Implementation

    async def list_tags(self, image: str) -> list[str]:
        """List all tags for an image."""
        # Implementation

    async def delete_tag(self, image: str, tag: str) -> dict:
        """Delete a tag from an image."""
        # Implementation
```

---

## Communication

### Slack

**Pattern: Slack Client**
```python
class SlackClient:
    """Client for Slack API."""

    async def send_message(self, channel: str, text: str, blocks: list = None) -> dict:
        """Send a message to a Slack channel."""
        # Implementation

    async def upload_file(self, channel: str, file_path: str, filename: str = None, title: str = None) -> dict:
        """Upload a file to a channel."""
        # Implementation

    async def get_channel_id(self, channel_name: str) -> str:
        """Get channel ID from channel name."""
        # Implementation

    async def add_reaction(self, channel: str, timestamp: str, reaction: str) -> dict:
        """Add a reaction to a message."""
        # Implementation

    async def open_modal(self, trigger_id: str, view: dict) -> dict:
        """Open a modal in Slack."""
        # Implementation
```

**Instruction:** "Create a Slack client with send_message, upload_file, get_channel_id, add_reaction, and open_modal methods"

---

### Microsoft Teams

**Pattern: Teams Client**
```python
class TeamsClient:
    """Client for Microsoft Teams API."""

    async def send_message(self, channel_id: str, content: str, attachments: list = None) -> dict:
        """Send a message to a Teams channel."""
        # Implementation

    async def create_channel(self, team_id: str, display_name: str, description: str = "") -> dict:
        """Create a new channel."""
        # Implementation

    async def get_channel_messages(self, channel_id: str) -> list[dict]:
        """Get messages from a channel."""
        # Implementation
```

---

### Email

**Pattern: Email Client (SMTP)**
```python
class EmailClient:
    """Client for sending emails via SMTP."""

    async def send_email(
        self,
        to: list[str],
        subject: str,
        body: str,
        html_body: str = None,
        attachments: list[str] = None
    ) -> dict:
        """Send an email."""
        # Implementation with attachments

    async def send_template_email(self, template_name: str, to: list[str], context: dict) -> dict:
        """Send an email using a template."""
        # Implementation
```

---

## Agentic Coding Patterns

**IMPORTANT:** Recognize patterns for agents that generate and edit code:

### File System Operations

```python
class FileSystemTool:
    """Tool for file system operations."""

    async def read_file(self, path: str) -> str:
        """Read file content."""
        # Implementation

    async def write_file(self, path: str, content: str) -> str:
        """Write content to a file."""
        # Implementation

    async def edit_file(self, path: str, old_text: str, new_text: str) -> str:
        """Replace text in a file."""
        # Implementation

    async def list_files(self, path: str, pattern: str = "*") -> list[str]:
        """List files matching a pattern."""
        # Implementation

    async def search_files(self, path: str, search_text: str) -> list[str]:
        """Search for files containing text."""
        # Implementation
```

**Instruction:** "Create a file system tool with read, write, edit, list, and search methods"

---

### Code Generation

```python
class CodeGenerator:
    """Agent for generating code."""

    async def generate_function(self, language: str, description: str, context: str = "") -> str:
        """Generate a function based on description."""
        # Implementation

    async def generate_class(self, language: str, description: str, methods: list[str]) -> str:
        """Generate a class with specified methods."""
        # Implementation

    async def generate_api_client(self, openapi_spec: dict) -> str:
        """Generate an API client from OpenAPI spec."""
        # Implementation
```

**Instruction:** "Create a code generator with methods to generate functions, classes, and API clients"

---

### Code Analysis

```python
class CodeAnalyzer:
    """Agent for analyzing code."""

    async def analyze_repo(self, repo_url: str) -> dict:
        """Analyze a repository and return summary."""
        # Implementation

    async def find_functions(self, code: str) -> list[dict]:
        """Extract function definitions from code."""
        # Implementation

    async def detect_dependencies(self, code: str) -> list[str]:
        """Detect imports and dependencies."""
        # Implementation

    async def review_code(self, code: str, language: str) -> list[dict]:
        """Review code and return suggestions."""
        # Implementation
```

**Instruction:** "Create a code analyzer with methods for repo analysis, function extraction, dependency detection, and code review"

---

### Testing Agent

```python
class TestingAgent:
    """Agent for running and generating tests."""

    async def generate_test(self, code: str, language: str, framework: str) -> str:
        """Generate test code for given function."""
        # Implementation

    async def run_tests(self, project_path: str) -> dict:
        """Run tests and return results."""
        # Implementation

    async def generate_test_data(self, function_signature: str) -> str:
        """Generate test data for a function."""
        # Implementation
```

**Instruction:** "Create a testing agent with methods to generate tests, run tests, and generate test data"

---

### Documentation Agent

```python
class DocumentationAgent:
    """Agent for generating documentation."""

    async def generate_docs(self, code: str, format: str = "markdown") -> str:
        """Generate documentation from code."""
        # Implementation

    async def generate_api_docs(self, openapi_spec: dict) -> str:
        """Generate API documentation from OpenAPI spec."""
        # Implementation

    async def update_readme(self, repo_path: str, content: str) -> str:
        """Update README.md with new content."""
        # Implementation
```

**Instruction:** "Create a documentation agent with methods to generate docs, API docs, and update README files"

---

## DevOps Workflow Patterns

### Deployment Agent

```python
class DeploymentAgent:
    """Agent for managing deployments."""

    async def deploy(self, artifact_id: str, environment: str, jira_ticket: str) -> dict:
        """Deploy an artifact to an environment."""
        # 1. Get artifact from JFrog
        artifact = await self.jfrog.download_artifact("libs", artifact_id)

        # 2. Update deployment status in Jira
        await self.jira.update_status(jira_ticket, "IN_PROGRESS")

        try:
            # 3. Deploy to environment
            result = await self._deploy_artifact(artifact, environment)

            # 4. Update Jira with success
            await self.jira.update_status(jira_ticket, "DONE")
            return {"status": "success", "deployment_id": result["id"]}
        except Exception as e:
            await self.jira.update_status(jira_ticket, "FAILED")
            raise
```

**Instruction:** "Create a deployment agent that downloads artifacts from JFrog, deploys to environment, and updates Jira tickets"

### CI/CD Agent

```python
class CICDAgent:
    """Agent for managing CI/CD pipelines."""

    async def run_pipeline(self, config: dict) -> dict:
        """Run a CI/CD pipeline."""
        # 1. Trigger build
        build = await self.jenkins.build(config["job_name"])

        # 2. Wait for completion
        await self._wait_for_build(build["build_id"])

        # 3. Push artifact to JFrog
        artifact = await self._push_to_jfrog(build["artifact_path"])

        # 4. Create GitHub release
        await self.github.create_release(
            config["repo"],
            config["tag"],
            artifacts=[artifact]
        )

        # 5. Notify on Slack
        await self.slack.send_message(
            config["notification_channel"],
            f"Pipeline completed: {config['job_name']}"
        )

        return {"status": "success"}
```

**Instruction:** "Create a CI/CD agent that runs Jenkins builds, pushes artifacts to JFrog, creates GitHub releases, and sends Slack notifications"

### Incident Response Agent

```python
class IncidentResponseAgent:
    """Agent for automated incident response."""

    async def handle_incident(self, alert: dict) -> dict:
        """Handle an incoming alert."""
        # 1. Parse alert to determine severity
        severity = self._classify_alert(alert)

        # 2. Create Jira ticket
        ticket = await self.jira.create_incident(
            short_description=alert["title"],
            description=alert["description"],
            priority=severity
        )

        # 3. Post to Slack
        await self.slack.send_message(
            f"incidents-{severity}",
            f"Incident created: {ticket['key']}"
        )

        # 4. Update Grafana dashboard
        await self.grafana.annotate_dashboard(
            dashboard_id="alert-dashboard",
            note=f"Incident {ticket['key']} created"
        )

        # 5. Create ServiceNow ticket
        await self.servicenow.create_incident(
            short_description=alert["title"],
            description=alert["description"],
            urgency=severity
        )

        return {"ticket": ticket["key"], "severity": severity}

    async def resolve_incident(self, ticket_key: str, resolution: str, postmortem: str) -> dict:
        """Resolve an incident and update all systems."""
        # Update Jira
        await self.jira.update_ticket(ticket_key, "Resolved", resolution)

        # Update ServiceNow
        await self.servicenow.update_incident(ticket_key, "Resolved")

        # Update Grafana
        await self.grafana.clear_annotation(ticket_key)

        # Post resolution summary to Slack
        await self.slack.send_message(
            f"incidents-resolved",
            f"Incident {ticket_key} resolved: {resolution}"
        )

        return {"status": "resolved"}
```

**Instruction:** "Create an incident response agent that creates tickets in Jira and ServiceNow, posts alerts to Slack, annotates Grafana, and coordinates resolution"

### Monitoring Agent

```python
class MonitoringAgent:
    """Agent for continuous monitoring."""

    async def monitor_and_alert(self, config: dict) -> dict:
        """Monitor systems and send alerts."""
        while True:
            # Check Jenkins jobs
            for job in config["jenkins_jobs"]:
                status = await self.jenkins.get_latest_build_status(job)
                if status["result"] == "FAILURE":
                    await self.jira.create_incident(...)
                    await self.slack.send_message(...)
                    await self.grafana.annotate_alert(...)

            # Check Grafana alerts
            alerts = await self.grafana.get_alerts()
            for alert in alerts:
                if alert["state"] == "alerting":
                    await self.slack.send_message(...)
                    await self.jira.create_incident(...)

            # Check Prometheus metrics
            metrics = await self.prometheus.query(config["prometheus_queries"])
            for metric in metrics:
                if self._is_anomalous(metric):
                    await self.slack.send_message(...)
                    await self.servicenow.create_incident(...)

            await asyncio.sleep(config["check_interval"])
```

**Instruction:** "Create a monitoring agent that checks Jenkins jobs, Grafana alerts, and Prometheus metrics, and creates incidents for failures"

---

## Service-Specific Instruction Templates

| Service | Pattern Indicators | Instruction Template |
|---------|-------------------|---------------------|
| **ServiceNow** | `ServiceNowClient`, `create_incident` | "Create a ServiceNow client with methods for incidents, change requests, and user lookups" |
| **Confluence** | `ConfluenceClient`, `create_page`, `update_page` | "Create a Confluence client with methods for creating pages, updating content, and file attachments" |
| **Grafana** | `GrafanaClient`, `create_dashboard`, `query_datasource` | "Create a Grafana client with dashboard, datasource query, and alert methods" |
| **Prometheus** | `PrometheusClient`, `query`, `get_series` | "Create a Prometheus client with query, metadata, and alert methods" |
| **Jira** | `JiraClient`, `create_issue`, `transition_issue` | "Create a Jira client with issue creation, transition, comment, and JQL search methods" |
| **GitHub** | `GitHubClient`, `create_pr`, `update_file` | "Create a GitHub client with PR, file operations, and release management methods" |
| **GitLab** | `GitLabClient`, `create_merge_request`, `create_pipeline` | "Create a GitLab client with MR, pipeline, and job status methods" |
| **JFrog** | `ArtifactoryClient`, `upload_artifact`, `search_artifacts` | "Create a JFrog Artifactory client with upload, download, search, and copy methods" |
| **Jenkins** | `JenkinsClient`, `trigger_build`, `get_console` | "Create a Jenkins client with build trigger, status, console output, and job info methods" |
| **Slack** | `SlackClient`, `send_message`, `upload_file` | "Create a Slack client with messaging, file upload, and reaction methods" |
| **AWS S3** | `S3Client`, `upload_file`, `download_file` | "Create an S3 client with upload, download, list, and presigned URL methods" |
| **AWS Lambda** | `LambdaClient`, `invoke_function` | "Create a Lambda client with invoke and create function methods" |
| **Docker** | `DockerRegistryClient`, `push_image` | "Create a Docker registry client with push, pull, list tags, and delete methods" |
| **Email** | `EmailClient`, `send_email` | "Create an email client with SMTP sending and template email methods" |

---

## Agentic Coding Instruction Templates

| Pattern | Instruction Template |
|---------|---------------------|
| **File operations** | "Create a file system tool with read, write, edit, and search methods" |
| **Code generation** | "Create a code generator with methods to generate functions, classes, and API clients" |
| **Code analysis** | "Create a code analyzer with methods for repo analysis, function extraction, and dependency detection" |
| **Testing** | "Create a testing agent with methods to generate tests, run tests, and generate test data" |
| **Documentation** | "Create a documentation agent with methods to generate docs, API docs, and update README files" |
| **Code review** | "Create a code review agent that analyzes code and returns suggestions" |
| **Refactoring** | "Create a refactoring tool that renames variables, extracts functions, and applies fixes" |
| **Debugging** | "Create a debugging agent that finds and fixes bugs based on error messages" |
