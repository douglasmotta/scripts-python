#!/usr/bin/env python

from jira import JIRA

jira_url=""
jira_api_user=""
jira_api_token=""

def get_issue(issue_key):

    jira = JIRA(server=jira_url, basic_auth=(jira_api_user, jira_api_token))

    issue = jira.issue(issue_key)

    return issue


if __name__ == "__main__":

    issue_key = "KAN-1"

    issue_object = get_issue(issue_key)

    print(f"Duedate -> {issue_object.fields.duedate}")
    print(f"Summary -> {issue_object.fields.summary}")
    print(f"Labels -> {issue_object.fields.labels}")





