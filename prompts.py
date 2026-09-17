"""Prompt templates for AI-assisted git operations."""


def branch_name(diff):
    return f"""\
Role: Git branch name generator.

Rules:
- Format: <company>/<feature> or just <feature> if no company is identifiable
- Extract company from file paths or namespaces in the diff (e.g. bestdk, nordicfeel, postnord)
- Feature part: kebab-case, lowercase, 2-4 words max
- No prefixes like "feature/" — only company/ or bare name
- Examples: bestdk/scanning-changes, nordicfeel/supplier-mail, disable-send-button

Diff:
{diff}

Output: branch name only, nothing else."""


def commit_message(diff, previous_commits):
    return f"""\
Role: Git commit message generator.

Rules:
- Max 50 characters
- Imperative mood, present tense (e.g. "Add", "Fix", "Remove" — not "Added", "Fixes")
- No trailing period
- Capitalize first word
- Consider ALL changes in the diff (additions, deletions, modifications, renames)
- If multiple types of changes exist, summarize the overall intent or most significant change
- Describe *what* the changes accomplish together, not individual operations
- Keep the message consistent with the theme/context of previous commits on this branch
{previous_commits}
Diff:
{diff}

Output: commit message only, nothing else."""


def pr_title(diff, commits_context):
    return f"""\
Role: GitHub pull request title generator.

Rules:
- Max 50 characters
- Imperative mood, present tense (e.g. "Add", "Fix", "Remove" — not "Added", "Fixes")
- No trailing period
- Capitalize first word
- Summarize the overall intent of all changes, not individual lines
- Use the commit messages below to understand the context and theme of the changes
{commits_context}
Diff:
{diff}

Output: PR title only, nothing else."""
